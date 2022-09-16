from django.db import models
from django.urls import reverse, reverse_lazy


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at',]


class Song(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField(blank=True)
    rating = models.IntegerField(default=0)
    audio_file = models.FileField(upload_to='songs/',blank=True,null=True)
    review = models.ForeignKey('Review', on_delete=models.PROTECT,blank=True, null=True, verbose_name='Обзор')
    paginate_by = 2

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
        ordering = ['-rating',]

    def get_absolute_url(self):
        return reverse('view_song', kwargs={"pk": self.pk})

    def add_rating(self):
        rating = self.rating + 1
        return reverse_lazy('chart')


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['pk',]


class Review(models.Model):
    text = models.TextField(max_length=300, db_index=True, verbose_name='Текст обзора')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'
        ordering = ['pk',]