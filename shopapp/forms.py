from django import forms
from .models import Contents

class ContentsForm(forms.ModelForm):
    content = forms.CharField(max_length=20)
    amount = forms.IntegerField(required=False)

    # Metaがないとデータベースに保存されなくなる
    class Meta:
        model = Contents
        fields = ("content","amount",)

# ------------------------------------------------

# カートに追加するフォーム01
class AddCartForm01(forms.Form):
    email = forms.EmailField(label='顧客 email',required=True,)
    item_name = forms.CharField(label='商品名',max_length=100,required=True,)
    order_quantity = forms.IntegerField()

    class Meta:
        fields = ("email","item_name","order_quantity")