# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 6:21 下午
# @Author  : Hui
# @File    : tokenMiddleware.py
import hashlib
import time


def generate_token(username):
    """
    生成token
    """
    timestamp = str(time.time())

    token = hashlib.md5(bytes(username, encoding='utf-8'))
    token.update(bytes(timestamp, encoding='utf-8'))

    return token.hexdigest()