from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class AuthorInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name='姓名')
    tags = models.CharField(max_length=20,verbose_name='分类/话题')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "作者"
        verbose_name_plural = "作者"


class ArticleInfo(models.Model):
    title = models.CharField(max_length=50,verbose_name='标题')
    image = models.ImageField(upload_to='upload',default='logoko.png')
    texts = RichTextUploadingField()
    createtime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(AuthorInfo)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"
