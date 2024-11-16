from rest_framework.pagination import PageNumberPagination


class DefaultPageNumber(PageNumberPagination):
    page_size = 10