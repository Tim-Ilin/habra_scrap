from django.contrib import admin
from .models import Article, ParserError

# Register your models here.
admin.site.register(Article)
admin.site.register(ParserError)
