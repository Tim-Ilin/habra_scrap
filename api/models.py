from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    url = models.URLField(verbose_name='Ссылка на статью', unique=True)
    body_text = models.TextField(verbose_name='Текст статьи')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления добавления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['id']


class ParserError(models.Model):
    error = models.CharField(max_length=200, verbose_name='Ошибка')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления добавления')

    def __str__(self):
        return self.error

    class Meta:
        verbose_name = 'Ошибка'
        verbose_name_plural = 'Ошибки'
