from django.db import models
from django.contrib.auth.models import User # 导入 user 的规范操作

# Create your models here.

# Django 自己创建的 base model， 我们这里必须要inherit过来
class Category(models.Model):

    # 通过 inherit， 我们可以定义各种类型，CharField，IntegerField，DateField，这些就是 databse 的 column
    name = models.CharField(max_length=255)

    # Django 用来配置 model’s object 的 class
    class Meta:
        ordering = (['name']) # input 必须要是一个list
        verbose_name = 'Category'
        verbose_name_plural = 'Categories' # 用来覆盖 Category 这个 class 本身的复数被 Django 加上额外的 s 之后的名字
 
    # 决定 Category 这个 class 里面的 object 应该用什么 string 表示
    # 让 Category 里面的 object 显示自己的名字
    def __str__(self):
        return self.name


class Item(models.Model):

    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE) # Category 是 foreign key，related_name 是关联到 item 索引的名字
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True) # 用户可以不提供 description, 或者提供 null value
    image = models.ImageField(upload_to='item_images', blank=True, null=True) # 这里的 item_images folder 会自动被 Django 创建
    price = models.FloatField()
    isSold = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True) # Django 自动记录当下 create 的时间
    createdBy = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) # 如果 User 被删除，models.CASCADE 会让相应的 item 也删除


    class Meta:
        ordering = (['price'])


    def __str__(self):
        return self.name