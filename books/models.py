from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='书籍名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论数')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_books'
        verbose_name = '图书列表'
        verbose_name_plural = verbose_name # 复数名称

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    Gender_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    hname = models.CharField(max_length=20, verbose_name='角色姓名')
    hgender = models.SmallIntegerField(choices=Gender_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='角色描述信息')
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='所属图书')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')