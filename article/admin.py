from datetime import datetime

from django.contrib import admin

from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    fields = ['label', 'slug',]
    search_fields = ['label', 'slug',]
    list_display = ['label', 'slug',]
    prepopulated_fields = {'slug': ('label',)}


class ArticleAdmin(admin.ModelAdmin):
    fields = ('author', 'category', 'title', 'slug', 'tags', 'body',
            'summary', ('state', 'published_date'), 'allow_comments')
    list_display = ('title', 'category', 'state', 'published_date', 'creation_date',)
    list_filter = ('category', 'state',)
    search_fields = ('title', 'slug',)
    date_hierarchy = 'published_date'
    prepopulated_fields = {'slug': ('title',)}
    actions = ['action_publish', 'action_mask', 'action_draft',]
    actions_on_top = True
    actions_on_bottom = True

    def _change_state(self, queryset, state):
        values = {
            'state': state,
        }
        if state == 'published':
            values['published_date'] = datetime.now()
            msgfmt = '%s article%s marked as published'
        elif state == 'draft':
            values['published_date'] = None
            msgfmt = '%s article%s marked as draft'
        else:
            msgfmt = '%s article%s marked as masked'
        count = queryset.update(**values)
        if count == 1:
            message = msgfmt % (1, '')
        else:
            message = msgfmt % (count, 's')
        return message


    def action_publish(self, request, queryset):
        msg = self._change_state(queryset, 'published')
        self.message_user(request, msg)
    action_publish.short_description = "Mark selected articles as published"

    def action_mask(self, request, queryset):
        msg = self._change_state(queryset, 'masked')
        self.message_user(request, msg)
    action_mask.short_description = "Mark selected articles as masked"

    def action_draft(self, request, queryset):
        msg = self._change_state(queryset, 'draft')
        self.message_user(request, msg)
    action_draft.short_description = "Mark selected articles as draft"

    def save_model(self, request, article, form, change):
        article.last_update = datetime.now()
        article.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
