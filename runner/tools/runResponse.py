# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 4:42 下午
# @Author  : Hui
# @File    : runResponse.py

KEY_MISS = {
    "code": "0100",
    "success": False,
    "msg": "请求数据非法"
}

REGISTER_SUCCESS = {
    "code": "0001",
    "success": True,
    "msg": "数据请求成功"
}
REGISTER_PROJECT_EXIST = {
    "code": "0101",
    "success": False,
    "msg":"项目名已存在"
}
SYSTEM_ERROR = {
    "code": "9999",
    "success": False,
    "msg": "System Error"
}