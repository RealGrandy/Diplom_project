from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import News, Category, Song


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'created_at',
              'updated_at',)
    readonly_fields = ('get_photo', 'created_at', 'updated_at')

    # Помогает выводить фотку в списке новостей
    def get_photo(self,obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width ="35">')

    get_photo.short_description = 'Фоточка'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News,NewsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Song,SongAdmin)

admin.site.site_title = 'Управление СМИ'
admin.site.site_header = 'Управление СМИ'

