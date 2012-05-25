from django.db import models
from django.contrib.auth.models import User
from django.contrib.markup.templatetags.markup import restructuredtext

class Category(models.Model):
    label = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)

    def __unicode__(self):
        return self.label

    @models.permalink
    def get_absolute_url(self):
        return ('category_slug_article_list_view', [self.slug,])

    class Meta:
        ordering=['label',]
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ArticlePublishedManager(models.Manager):
    def get_query_set(self):
        return super(ArticlePublishedManager, self).get_query_set() \
                .filter(state='published')


#TODO: add tags
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
    creation_date = models.DateTimeField('date created', auto_now_add=True)
    last_update = models.DateTimeField('updated', auto_now=True,
            auto_now_add=True)
    body = models.TextField()
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True)
    state = models.CharField(max_length=32, choices=STATES, default='draft')
    allow_comments = models.BooleanField(default=False)

    objects = models.Manager()
    published = ArticlePublishedManager()

    @property
    def content(self):
        return restructuredtext(self.body)

    @staticmethod
    def get_last_published():
        if Article.published.count():
            return Article.published.order_by('-id')[0]
        return None

    def __unicode__(self):
        return self.slug

    @models.permalink
    def get_absolute_url(self):
        return ('article_slug_view', [self.slug,])

    class Meta:
        ordering=['-published_date', '-last_update',]
        verbose_name = 'article'
        verbose_name_plural = 'articles'



