# -*- coding: utf-8 -*-
from operator import or_

from db.postgres.ext import db

# 是否为系统＋shared_id+是否为当前用户

STATUS_MAP = {
    "000": 0,  # 无权限
    "001": 1,  # 用户私有
    "010": 3,  # 用户共享
    "011": 4,  # 自有共享
    "100": 0,  # 系统私有
    "101": 1,  # 系统自己私有
    "110": 2,  # 系统开放
    "111": 4,  # 系统自己开放
}


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(64), nullable=False, default='')

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e.message)
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e.message)
            return False

    @staticmethod
    def save_list(x_list):
        try:
            db.session.add_all(x_list)
            db.session.commit()
            return True
        except Exception as e:
            print(e.message)
            return False

    # 原始sql调用
    @staticmethod
    def original_select_sql(sql):
        try:
            rows = db.session.execute(sql)
            return rows
        except Exception as e:
            print(e.message)
            return None

    @staticmethod
    def shared_status(cur_uid, shared_id, u_id):
        """
            判断文件的状态
            :param cur_uid: 当前用户ID
            :param shared_id: 文件的shared_id
            :param u_id: 文件的user_id
            :return:
            """
        return STATUS_MAP[str(int(u_id == 1)) + str(shared_id) + str(int(cur_uid == u_id))]

    @classmethod
    def shared_condition(cls, cur_uid):
        return cls.query.filter(or_(or_(cls.user_id == 1, cls.shared_id == 1), cls.user_id == cur_uid)).all()

    @classmethod
    def shared_condition_by_crop(cls, crop_id, cur_uid):
        return cls.query.filter(cls.crop_id == crop_id).filter(
            or_(or_(cls.user_id == 1, cls.shared_id == 1), cls.user_id == cur_uid)).all()
