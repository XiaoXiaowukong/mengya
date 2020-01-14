# -*- coding:utf-8 -*-
# author:xiaoxiaowukong
# datetime:2020/1/10 下午2:51
# software: PyCharm
from flask_restful import Resource, abort

from models.mode_case import CaseModel


class CaseList(Resource):
    def get(self, area_id):
        """
        案例列表
        ---
        tags:
          - 案例
        parameters:
          - name: "area_id"
            in: "path"
            description: "区域"
            required: true
            type: "string"
        responses:
          200:
            description: "查找成功"
          404:
            description: "资源不存在"
        """
        casemodel_list = CaseModel.fetch_list()
        case_lists = []
        case_list = []
        for index, case_item in enumerate(casemodel_list):
            print (index)
            case_list.append({
                "img_file": case_item.img_file,
                "title": case_item.title,
                "content": case_item.content
            })
            if index % 3 == 0 :
                if index==0 and index + 1 == case_list.__len__():
                    case_lists.append(case_list)
                else:
                    case_list = []

        case_data = {"case": case_lists}
        print(case_data)
        return case_data
