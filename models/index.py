from django.db import models

class Menu(models.Model):
    label = models.CharField(max_length=64)
    url = models.CharField(max_length=254)
    sequence = models.IntegerField()
    visible = models.BooleanField(default=False)

    def __unicode__(self):
        return self.label

    class Meta:
        ordering = ('sequence',)
        verbose_name = 'index menu'
        verbose_name_plural = 'index menus'

