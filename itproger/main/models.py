from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    tags = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    answer_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page