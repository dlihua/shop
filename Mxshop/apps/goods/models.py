from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField
# Create your models here.


# 商品分类，此处使用无限级分类
class GoodsCategory(models.Model):
    """
    商品分类
    """
    CATEGORY_TYPE = (
        (1,'一级分类'),
        (2, '二级分类'),
        (3, '三级分类')
    )
    name = models.CharField(default='',max_length=30,verbose_name='类别名称')
    code = models.CharField(default='',max_length=30,verbose_name='类别code')
    desc = models.TextField(default='',max_length=30,verbose_name='类别描述')
    category_type = models.IntegerField(choices=CATEGORY_TYPE,verbose_name='类目级别',help_text='类目级别')
    parent_category = models.ForeignKey('self',verbose_name='父类目级别',help_text='父目录',related_name='sub_cat',null=True,blank=True)
    is_tab = models.BooleanField(default=False,verbose_name='是否导航',help_text='是否导航')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        '''
        verbose_name：指定在admin管理界面中显示中文；
        verbose_name：表示单数形式的显示，verbose_name_plural表示复数形式的显示；中文的单数和复数一般不作区别。
        '''
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

# 品牌
class GoodsCategoryBrand(models.Model):
    '''
    related_name：此参数被用在一对多的关系中，比如：
                从主键查询从键信息时为   主键.从键_set.all()
                但是使用related_name = ’aaa'
                查询代码为   主键.aaa.all()
    '''
    category = models.ForeignKey(GoodsCategory,related_name='brands',null = True,blank = True,verbose_name='商品类目')
    name = models.CharField(default='',max_length=30,verbose_name='品牌名')
    desc = models.TextField(verbose_name='品牌描述',default='',max_length=200,help_text='品牌描述')
    image = models.ImageField(upload_to='brands/',max_length=200)
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

# 商品
class Goods(models.Model):
    category = models.ForeignKey(GoodsCategory,verbose_name='商品类目')
    goods_sn = models.CharField(max_length=50,default='',verbose_name='商品唯一货号')
    name = models.CharField(max_length=100,verbose_name='商品名')
    click_num = models.IntegerField(default=0,verbose_name='点击数')
    sold_num = models.IntegerField(default=0,verbose_name='商品销售量')
    fav_num = models.IntegerField(default=0,verbose_name='收藏数')
    goods_num = models.IntegerField(default=0,verbose_name='商品库存')
    market_price = models.FloatField(default=0,verbose_name='市场价格')
    shop_price = models.FloatField(default=0,verbose_name='本店价格')
    goods_drief = models.TextField(verbose_name='商品简述',max_length=500)
    goods_desc = UEditorField(verbose_name='内容',imagePath='goods/images/',width=1000,height=300,filePath='goods/files/',default='')
    ship_free = models.BooleanField(default=True,verbose_name='是否承担运费')
    goods_front_image = models.ImageField(upload_to = 'goods/images/',null = True,blank=True,verbose_name='封面图像')
    is_new = models.BooleanField(default=False,verbose_name='是否新品')
    is_hot = models.BooleanField(default=False,verbose_name='是否热销')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name











