# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 8:17 上午
# @Author  : Hui
# @File    : pagination.py.py


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