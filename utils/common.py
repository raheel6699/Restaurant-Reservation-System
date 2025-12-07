from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


def success_response(data={}, message="Success"):
    return Response(
        data={"code": status.HTTP_200_OK, "message": message, "data": data},
        content_type='application/json',
        status=status.HTTP_200_OK
    )


def error_response(errors={}, message="Error!"):
    return Response(
        data={"code": status.HTTP_400_BAD_REQUEST, "message": message, "errors": errors},
        content_type='application/json',
        status=status.HTTP_200_OK
    )


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'per_page'
    page_query_param = 'page_no'

    def get_paginated_response(self, data):
        pagination = {
                'total_count': self.page.paginator.count,
                'current_page': self.page.number,
                'per_page': self.page.paginator.per_page,
                'total_pages': self.page.paginator.num_pages,
            }
        resultset = {"dataset": data, 'pagination': pagination }
        return success_response(resultset)