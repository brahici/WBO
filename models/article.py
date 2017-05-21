from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

def published_articles(queryset):
    return queryset.filter(state='published').order_by('-published_date')


class Category(models.Model):
    label = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)

    def articles_published(self):
        return published_articles(self.article_set)

    def __str__(self):
        return self.label

    @models.permalink
    def get_absolute_url(self):
        return ('wbo:category_slug_article_list_view', [self.slug,])

    class Meta:
        ordering=['label',]
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ArticlePublishedManager(models.Manager):
    def get_queryset(self):
        return published_articles(super(
                ArticlePublishedManager, self).get_queryset())


class Article(models.Model):
    STATES = (
        ('draft', 'Draft'),
        ('masked', 'Masked'),
        ('published', 'Published'),
    )
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True, max_length=255)
    published_date = models.DateTimeField('published on', null=True,
            blank=True)
    creation_date = models.DateTimeField('date created', auto_now=True)
    last_update = models.DateTimeField('updated', auto_now=True)
    body = models.TextField()
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True)
    state = models.CharField(max_length=32, choices=STATES, default='draft')
    allow_comments = models.BooleanField(default=False)

    objects = models.Manager()
    published = ArticlePublishedManager()

    tags = TaggableManager()

    @property
    def content(self):
        return self.body

    @staticmethod
    def get_last_published():
        if Article.published.count():
            return Article.published.latest('published_date')
        return None

    def __str__(self):
        return self.slug

    @models.permalink
    def get_absolute_url(self):
        vals = {
            'year': self.published_date.strftime('%Y'),
            'month': self.published_date.strftime('%m'),
            'day': self.published_date.strftime('%d'),
            'slug': self.slug,
        }
        return ('wbo:article_ymd_slug_view', [], vals)

    class Meta:
        ordering=['-published_date', '-last_update',]
        verbose_name = 'article'
        verbose_name_plural = 'articles'
