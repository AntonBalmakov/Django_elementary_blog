import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('Название стратьи', max_length=50)
    article_text = models.TextField('Текст статьи', max_length=1000)
    pud_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):  #была ли данная статься опубликована недавно*
        return self.pud_date >= (timezone.now()-datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # Привязка комментария к статье
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.CharField("Текст комментария ", max_length=100)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
