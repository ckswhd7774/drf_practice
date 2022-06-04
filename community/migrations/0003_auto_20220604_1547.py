# Generated by Django 3.2.9 on 2022-06-04 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_post_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='writer',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=1, help_text='카테고리 입니다.', max_length=32, verbose_name='카테고리'),
            preserve_default=False,
        ),
    ]