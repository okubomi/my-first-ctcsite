from django import forms
import lepl.apps.rfc3696

class UserCreationForm(forms.Form):
    '''
    name = models.CharField(verbose_name='ユーザー名', max_length=255)
    profile_image = models.CharField(verbose_name='プロファイル画像', max_length=255,null=True, blank=True)
    email = models.CharField(verbose_name='メールアドレス', max_length=255, unique=True)
    password = models.CharField(verbose_name='パスワード', max_length=255)
    '''
    name = forms.CharField(label='ユーザー名', max_length=20)
    email = forms.CharField(label='メールアドレス', max_length=50,)
    password = forms.CharField(label='パスワード', max_length=20)

    '''
    emailデータを検証するメソッド 命名：clean_フィールド名
    ''' 
    def clean_email(self):   
        email = self.cleaned_data['email']
        email_validator = lepl.apps.rfc3696.Email()
        if not email_validator(email):
            raise forms.ValidationError('%s は正しいメールアドレスの形式ではありません' % email)

        return email
