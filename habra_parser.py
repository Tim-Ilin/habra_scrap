import requests
from bs4 import BeautifulSoup as BS
import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'habra_scrap.settings'
application = get_wsgi_application()
from api.models import Article, ParserError

articles = []
errors = []


def parser():
    """
    Данная фунция парсит топ популярных статей с хабра за сутки.
    Складывает все в articles, в случае неправильного статус кода
    ошибка кладется в errors
    :return: void
    """
    url = 'https://habr.com/ru/top/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BS(response.text, 'html.parser')
        all_posts = soup.find_all('article', class_='post post_preview')
        for post in all_posts:
            title = post.find('h2', class_='post__title')
            body_text = post.find('div', class_='post__text')
            url = title.a['href']
            articles.append({'title': str(title.text).replace('\n', ''),
                             'url': url,
                             'body_text': str(body_text.text).strip().replace('\n', '')})
    else:
        errors.append({'error': f'Не верный статускод {response.status_code} возможно изменился url'})


if __name__ == '__main__':
    """
    Получаем все статьи, если статьи получены, то удаляем старые и сохраняем новые
    Поскольку время на реализацию ограничено, то сделано именно так.
    Если есть ошибки, то сохраняем их в базу.
    """
    parser()
    if articles:
        all_article = Article.objects.all()
        all_article.delete()
        for article_item in articles:
            article = Article(**article_item)
            article.save()

    if errors:
        for error_item in errors:
            error = ParserError(**error_item)
            error.save()
