from django.views.generic.dates import ArchiveIndexView
from .models import Article


class Archive(ArchiveIndexView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True
    template_name = 'article_archive.html'

    

