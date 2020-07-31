from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Article
from .serializers import ArticleSerializer


def detail_url(article_id):
    """Return article detail URL"""
    return reverse('article_detail', args=[article_id])


def create_article(url):
    """Create and return a sample article"""
    defaults = {
        'title': 'Sample title',
        'url': url,
        'body_text': 'Habra scrap just amazing'
    }

    return Article.objects.create(**defaults)


class ArticleModelTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_article(self):
        """Test create new article in Article model."""
        article = create_article('http://ya.ru')
        self.assertTrue(isinstance(article, Article))
        self.assertTrue(article.title, 'Sample title')

    def test_retrieve_articles(self):
        """Test retrieving a list of articles"""
        create_article('http://ya.ru')
        create_article('http://google.com')
        ALL_ARTICLE_URL = reverse('article_list')
        res = self.client.get(ALL_ARTICLE_URL)
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['results'][0], serializer.data[0])
        self.assertEqual(res.data['results'][1], serializer.data[1])

    def test_view_article_detail(self):
        """Test viewing a article detail"""
        article = create_article('http://ya.ru')
        url = detail_url(article.id)
        res = self.client.get(url)
        serializer = ArticleSerializer(article)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
