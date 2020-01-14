#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiaoxiaowukong
# datetime:2020/1/14 上午10:41
# software: PyCharm
from db.postgres.base_model import BaseModel
from db.postgres.ext import db


class CaseModel(BaseModel):
    # 案例
    __tablename__ = "case"
    img_file = db.Column(db.String, nullable=False)
    index_case = db.Column(db.SmallInteger, nullable=False)  # 公示文件地址
    title = db.Column(db.String, default="")  # 公示文件地址
    content = db.Column(db.String, default="")  # 修改时间

    @staticmethod
    def fetch_list():
        return CaseModel.query.filter().order_by(CaseModel.index_case.asc()).all()
