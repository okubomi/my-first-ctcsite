-- 新しくデータベースを作成する
CREATE DATABASE ecsite CHARACTER SET utf8;

-- データベースを選択する(切替)
USE ecsite

-- テーブルを作成する
CREATE TABLE users (
    user_id     VARCHAR(255)    PRIMARY KEY,
    password    VARCHAR(255)    NOT NULL,
    name        VARCHAR(32),
    address     VARCHAR(255)
);

# 会員
class User(models.Model):
	# 説明
	class Meta:
		# テーブル定義名
		db_table = 'users'
		
	
	# テーブル列定義
	user_id = models.CharField(verbose_name='会員ID(email)', max_length=255, unique=True)
	password = models.CharField(verbose_name='パスワード', max_length=255)
	name = models.CharField(verbose_name='氏名', max_length=32)
	address = models.CharField(verbose_name='住所', max_length=255)
	
	# 管理者サイト上での表示文字列
	def __str__(self):
		return self.name



CREATE TABLE categories (
    category_id INTEGER         PRIMARY KEY,
    name        VARCHAR(255)    NOT NULL
);


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



CREATE TABLE items (
    item_id     INTEGER         AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(128)    NOT NULL,
    manufacturer VARCHAR(32),
    category_id INTEGER         NOT NULL,
    color       VARCHAR(16),
    price       INTEGER         NOT NULL DEFAULT 0,
    stock       INTEGER         NOT NULL DEFAULT 0,
    recommended BOOLEAN         NOT NULL DEFAULT FALSE,
    FOREIGN KEY (category_id) REFERENCES categories (category_id)
);

# 商品
class Item(models.Model):
	# 説明
	class Meta:
		# テーブル定義名
		db_table = 'items'
		
	
	# テーブル列定義
	item_id = models.AutoField(verbose_name='商品ID',primary_key=True) # 自動採番
	name = models.CharField(verbose_name='商品名', max_length=128)
	manufacturer = models.CharField(
		verbose_name='メーカー名',blank=True,null=True,max_length=32
	)
	category = models.ForeignKey( # 外部参照
        Category,
        verbose_name='カテゴリ',
        on_delete=models.CASCADE,
    )
	color = models.CharField(
		verbose_name='商品の色',blank=True,null=True,max_length=16
	)
    price = models.IntegerField(verbose_name='価格',default=0)
    stock = models.IntegerField(verbose_name='在庫数',default=0)
    recommended = models.BooleanField(verbose_name='オススメ',default=False)
    
	
	# 管理者サイト上での表示文字列
	def __str__(self):
		return self.name



CREATE TABLE items_in_cart (
    user_id     VARCHAR(255),
    item_id     INTEGER,
    amount      INTEGER         NOT NULL,
    booked_date DATE            NOT NULL,
    PRIMARY KEY (user_id, item_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (item_id) REFERENCES items (item_id)
);

# カート
class Item_in_cart(models.Model):
	# 説明
	class Meta:
		# テーブル定義名
		db_table = 'items_in_cart'
		unique_together = ('user', 'item') # 複合主キー
	
	# テーブル列定義
	user = models.ForeignKey( # 外部参照
        User,
        verbose_name='会員',
        on_delete=models.CASCADE,
    )
    item = models.ForeignKey( # 外部参照
        Item,
        verbose_name='商品',
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField(verbose_name='数量')
    booked_date = models.DateField(verbose_name='登録日', auto_now_add=True)




CREATE TABLE purchases (
    purchase_id INTEGER         AUTO_INCREMENT PRIMARY KEY,
    purchased_user  VARCHAR(255)    NOT NULL,
    purchased_date  DATE            NOT NULL,
    destination VARCHAR(255),
    cancel      BOOLEAN         NOT NULL DEFAULT FALSE,
    FOREIGN KEY (purchased_user) REFERENCES users (user_id)
);


# 注文
class Purchase(models.Model):
	# 説明
	class Meta:
		# テーブル定義名
		db_table = 'purchases'
	
	# テーブル列定義
	purchase_id = models.AutoField(verbose_name='注文ID',primary_key=True) # 自動採番
	user = models.ForeignKey( # 外部参照
        User,
        verbose_name='会員',
        on_delete=models.CASCADE,
    )
    purchased_date = models.DateField(verbose_name='注文日', auto_now_add=True)
 	destination = models.CharField(
		verbose_name='配送先', blank=True, null=True, max_length=255
	)   
	cancel = models.BooleanField(verbose_name='キャンセル',default=False)



CREATE TABLE purchases_details (
    purchase_detail_id  INTEGER AUTO_INCREMENT PRIMARY KEY,
    purchase_id INTEGER         NOT NULL,
    item_id     INTEGER         NOT NULL,
    amount      INTEGER         NOT NULL,
    FOREIGN KEY (purchase_id) REFERENCES purchases (purchase_id),
    FOREIGN KEY (item_id) REFERENCES items (item_id)
);



# 注文明細
class Purchases_detail(models.Model):
	# 説明
	class Meta:
		# テーブル定義名
		db_table = 'purchases_detail'
	
	# テーブル列定義
	purchase_detail_id = models.AutoField(verbose_name='注文明細ID',primary_key=True) # 自動採番
	purchase = models.ForeignKey( # 外部参照
        Purchase,
        verbose_name='注文',
        on_delete=models.CASCADE,
    )
    item = models.ForeignKey( # 外部参照
        Item,
        verbose_name='商品',
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField(verbose_name='注文数')





CREATE TABLE administrators (
    admin_id    VARCHAR(255)    PRIMARY KEY,
    password    VARCHAR(255)    NOT NULL,
    name        VARCHAR(32)
);


# 管理者
class Administrator(models.Model):
	# 説明
	class Meta:
		# テーブル定義名
		db_table = 'administrators'
	
	# テーブル列定義
	admin_id = models.CharField(verbose_name='管理者ID', max_length=255)
	password = models.CharField(verbose_name='管理者名', max_length=255)
	name = models.CharField(verbose_name='管理者名', max_length=32)



-- テーブルにデータを追加する
INSERT INTO administrators (admin_id, password, name) VALUES ('admin', 'admin', '管理者');

INSERT INTO categories (category_id, name) VALUES (0, 'すべて');
INSERT INTO categories (category_id, name) VALUES (1, '帽子');
INSERT INTO categories (category_id, name) VALUES (2, '鞄');

INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('麦わら帽子', '日本帽子製造', 1, '黄色', 4980, 12, FALSE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('ストローハット', '(株)ストローハットジャパン', 1, '茶色', 3480, 15, TRUE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('子ども用麦わら帽子', '東京帽子店', 1, '赤色', 2980, 3, FALSE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('ストローハット PART2', '(株)ストローハットジャパン', 1, '青色', 4480,6, FALSE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('野球帽', '日本帽子製造', 1, '緑色', 2500, 17, TRUE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('ニットキャップ', '日本帽子製造', 1, '紺色', 1800, 9, FALSE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('ハンチング帽', '日本帽子製造', 1, '黄色', 1980, 20, FALSE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('ストローハット PART3', '(株)ストローハットジャパン', 1, '茶色', 5480, 2, TRUE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('ターバン', '東京帽子店', 1, '赤色', 4580, 1, FALSE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('ベレー帽', '東京帽子店', 1, '青色', 3200, 8, FALSE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('マジック用ハット', '東京帽子店', 1, '緑色', 650, 17, TRUE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('鞄A', '東京鞄店', 2, '青色', 1980, 18, TRUE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('鞄B', '東京鞄店', 2, '緑色', 4980, 15, FALSE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('鞄E', '(株)鞄', 2, '紺色', 2200, 3, FALSE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('鞄G', '日本鞄製造', 2, '黄色', 2980, 6, FALSE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('鞄H', '日本鞄製造', 2, '茶色', 780, 17, TRUE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('鞄F', '(株)鞄', 2, '赤色', 2500, 9, TRUE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('鞄C', '東京鞄店', 2, '青色', 1800, 20, TRUE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('鞄D', '東京鞄店', 2, '緑色', 1980, 2, FALSE);
INSERT INTO items (name, manufacturer,category_id, color, price, stock, recommended) VALUES ('鞄I', '日本鞄製造', 2, '茶色', 690, 1, FALSE);
