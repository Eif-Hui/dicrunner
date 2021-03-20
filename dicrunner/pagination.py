# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 10:38 下午
# @Author  : Hui
# @File    : auth.py

from rest_framework import pagination

class MyCursorPagination(pagination.CursorPagination):
    """
    Cursor 光标分页 性能高，安全
    """
    page_size = 9
    ordering = '-update_time'
    page_size_query_param = "pages"
    max_page_size = 20


class MyPageNumberPagination(pagination.PageNumberPagination):
    """
    普通分页，数据量越大性能越差
    """
    page_size = 11
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = 20


from collections import OrderedDict
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_query_param = "page"
    page_size_query_param = "perPage"

    def get_paginated_response(self, data):
        current_page = self.page.number
        total_num = self.page.paginator.count
        total_page = self.page.paginator.num_pages
        return Response(OrderedDict([
            ('currentPage', current_page),
            ('hasNext', True if self.get_next_link() else False),
            ('hasPrev', True if self.get_previous_link() else False),
            ('items', data),
            ('totalNum', total_num),
            ('totalPage', total_page),
        ]))

