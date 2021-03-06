from django.db import models
from django.utils import timezone

# Create your models here.
class Contents(models.Model):
    content = models.CharField('商品名', max_length=20)
    amount = models.IntegerField('数量', blank=True, default=0)

    def __str__(self):
        return self.content

# --------------------------------------
# カテゴリ
class Category(models.Model):
	# 説明
	class Meta:
		# テーブル定義名
		db_table = 'categories'
		
	
	# テーブル列定義
	category_id = models.AutoField(verbose_name='カテゴリID',primary_key=True)
	name = models.CharField(verbose_name='カテゴリ名', max_length=255)
	
	# 管理者サイト上での表示文字列
	def __str__(self):
		return self.name


# --------------------------------------

# 商品
class Item(models.Model):
    name = models.CharField(
        verbose_name='商品名',
        max_length=100,
    )

    price = models.IntegerField(
        verbose_name='単価',
	    blank=True, 
	    default=0,
    )

    stock_quantity = models.IntegerField(
	    '在庫数', 
	    blank=True, 
	    default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品リスト'

# --------------------------------------

 # 顧客
class Customer(models.Model):

    name = models.CharField(
        verbose_name='顧客名',
        max_length=50,
    )

    address = models.CharField(
        verbose_name='住所',
        max_length=150,
	blank=True, 
	default='',
    )

    email = models.EmailField(
        'メールアドレス',
	max_length=150,
	blank=True, 
	default='',
    )

    user_id = models.CharField(
        verbose_name='ユーザID',
        max_length=10,
    )

    password = models.CharField(
        verbose_name='パスワード',
	max_length=10,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '顧客'
        verbose_name_plural = '顧客リスト'      



# --------------------------------------

# カート
class Cart(models.Model):

    item = models.ForeignKey(
        Item,
        verbose_name='商品',
        on_delete=models.CASCADE,
    )


    customer = models.ForeignKey(
        Customer,
        verbose_name='顧客',
        on_delete=models.CASCADE,
    )

    order_quantity = models.IntegerField(
	'個数', 
	blank=True, 
	default=1,
    )

    regist_date = models.DateTimeField(
	verbose_name='登録日',
        auto_now_add=True,
    )

    def __str__(self):
        return self.customer.name

    class Meta:
        verbose_name = 'カート注文'
        verbose_name_plural = 'カート注文リスト'