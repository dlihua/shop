from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.

# 用户
class UserProfile(AbstractUser):
    '''
    继承django自带的AbstractUser
    AbstractUser：使用情景为，对django自带的User model感到满意，但想要新加几个字段
                这时要在settings.py中添加设置
                # settings.py
                # 格式为 "<django_app名>.<model名>"
                AUTH_USER_MODEL = "apps.UserPorfile"
    '''

    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6,choices=(('male','男'),('female','女')),default='female',verbose_name='性别')
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username



# 验证码
class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code

