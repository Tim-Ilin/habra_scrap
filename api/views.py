from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Article
from .serializers import ArticleSerializer
from django.conf import settings
import logging

logging.basicConfig(filename=f'{settings.LOG_PATH}/{__name__}.log',
                    datefmt='%d-%m-%Y %I:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


def create_log(request, method_name):
    """
    Эта функция получает request и method_name, затем извлекает из
    реквеста IP адрес.
    "method_name" это строка с названием класса или функции которая
    является именем view, для того что-бы в лог файле можно было понять
    из какого мета получена конкретная запись лога.
    После чего полученная информация записывается в лог.
    """
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR',
                                  request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()
    logger.info(
        f'Called from {method_name} ip_address is {ip_address if ip_address else "unknown"} user is {request.user}')


class StandardResultsSetPagination(PageNumberPagination):
    """
    Класс который задает количество страниц получаемых за один раз.
    Или проще говоря "Пагинатор"
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ArticleList(generics.ListCreateAPIView):
    """ Данный класс отдает весь список Article ограниченный классом пагинации."""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        """
        Переопределение метода get из которого получаем request
        для логирования.
        """
        create_log(request, 'ArticleList')
        return self.list(request, *args, **kwargs)


class ArticleDetail(generics.RetrieveAPIView):
    """ Данный класс отдает конкретную запись из Article."""

    def get(self, request, *args, **kwargs):
        """
        Переопределение метода get из которого получаем request
        для логирования.
        """
        create_log(request, 'ArticleDetail')
        return self.retrieve(request, *args, **kwargs)

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
