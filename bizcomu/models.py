from django.db import models

# Create your models here.


class Department(models.Model):
    id = models.CharField(verbose_name='部門ID', max_length=3, primary_key=True)
    name = models.CharField(verbose_name='部門名', max_length=255, )
    location = models.CharField(verbose_name='場所', max_length=255, )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'

# -------------------------------------------


GENDER_CHOICES = [
    ('1', '男性'),
    ('2', '女性'),
]

BLOOD_TYPE = [
    ('1', 'A型'),
    ('2', 'B型'),
    ('3', 'C型'),
    ('4', 'AB型'),
]

class Employee(models.Model):
    id = models.CharField(verbose_name='社員ID', max_length=4, primary_key=True)
    name = models.CharField(verbose_name='氏名', max_length=255, )
    email = models.CharField(verbose_name='メールアドレス', max_length=255, unique=True)
    # 外部参照
    department = models.ForeignKey(Department, verbose_name='部門', on_delete=models.SET_NULL)
    gender = models.CharField(verbose_name='メールアドレス', max_length=1, choices=GENDER_CHOICES)
    salary = models.IntegerField(verbose_name='月収（万円）' ,null=True, blank=True)
    birthday = models.DateTimeField(verbose_name='生年月日', )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employee''

# -------------------------------------------