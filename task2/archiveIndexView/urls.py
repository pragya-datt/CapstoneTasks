from django.urls import path
from django.views.generic.dates import ArchiveIndexView
from .models import Article
from .views import Archive

urlpatterns = [
    path('archive/',
    Archive.as_view(model=Article, date_field="pub_date"),
    name="article_archive"),
]