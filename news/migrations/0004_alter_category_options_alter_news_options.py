# Generated by Django 4.0.4 on 2022-05-29 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_alter_news_options_alter_news_title_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
