from django.db import models


class Keyword(models.Model):
    keyword_max_len = 100

    keyword = models.CharField('keyword', max_length=keyword_max_len)
    to_location = models.ForeignKey('Location', on_delete=models.CASCADE)
