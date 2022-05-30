from operator import mod
from tkinter.tix import Balloon

from django.db import models
from django.utils.translation import gettext_lazy as _

from config.models import BaseModel
from user.models import User


class Post(BaseModel):
    title = models.CharField(verbose_name=_('제목'), max_length=32, help_text=_('제목 입니다.'))
    article = models.TextField(verbose_name=_('내용'), help_text=_('내용 입니다.'))
    music_code = models.CharField(verbose_name=_('악보 코드'), max_length=32, help_text=_('악보 코드 입니다.'))
    writer = models.ForeignKey(verbose_name=_('작성자'), to=User, on_delete=models.CASCADE, related_name='%(class)s_writers', help_text=_('작성자 입니다.'), )

    class Meta:
        db_table = 'post_tb'
        verbose_name = _('게시글')


class PostImage(BaseModel):
    image = models.ImageField(verbose_name=_('게시글 이미지'), upload_to='post/image/%Y/%m/%d', help_text=_('게시글 이미지 입니다.'))
    post = models.ForeignKey(verbose_name=_('게시글'), to=Post, null=True, blank=True, on_delete=models.CASCADE, related_name='%(class)s_posts', help_text=_('게시글 입니다.'))

    class Meta:
        db_table = 'post_image_tb'
        verbose_name = _('게시글 이미지')
