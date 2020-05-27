# Generated by Django 3.0.6 on 2020-05-25 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_quantity', models.IntegerField(blank=True, default=1, verbose_name='個数')),
                ('regist_date', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopapp.Customer', verbose_name='顧客')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopapp.Item', verbose_name='商品')),
            ],
            options={
                'verbose_name': 'カート注文',
                'verbose_name_plural': 'カート注文リスト',
            },
        ),
    ]