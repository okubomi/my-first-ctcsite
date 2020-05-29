from django.shortcuts import render
from django.shortcuts import redirect
from .models import User


# Create your views here.

def index(request):
    """
    トップ画面
    """
    return render(request, 'account/index.html')


def user_create(request):
    """
    ユーザ登録
    """    
    # リクエストメソッドがgetの時(初期アクセス画面)
    if request.method == 'GET':
        return render(request, 'account/user_create.html')        
    elif request.method == 'POST': 
        # 入力・送信されたユーザデータを格納する空のUserオブジェクトを用意
        new_user = User()
        # post送信されたデータを格納
        new_user.name = request.POST['name']
        new_user.email = request.POST['email']
        new_user.password = request.POST['password']

        # user = User(request.POST) でもOK
        # DBに保存
        new_user.save()
       
        # セッションに新規登録ユーザ名をセット
        request.session['user_name'] = new_user.name

        # リダイレクト（更新ボタン対策）
        # return render(request, 'account/user_create.html', context)
        return redirect('account:user_create_complete')
        


def user_create_complete(request):
    """
    ユーザ登録完了画面
    """
    # セッションデータから登録ユーザの名前を取得
    user_name = request.session.get('user_name')

    # htmlへ渡すデータを用意
    context = {
        'user_name': user_name # キーと値
    }    
    return render(request, 'account/user_create_complete.html', context) 



def user_list(request):
    """
    ユーザ一覧
    """      
    #ユーザレコードの全検索
    user_list = User.objects.all()

    # print(user_list)

    # htmlへ渡すデータを用意
    context = {
        # キーと値
        'user_list': user_list, 
        'message': 'Sample message',
    }
    return render(request, 'account/user_list.html', context) 


def user_detail(request, pk):
    """
    ユーザ詳細
    """        
    #ユーザレコードの検索
    user = User.objects.get(pk=pk)
    #htmlへ渡すデータを用意
    context = {
        'user': user # キーと値
    }
    return render(request, 'account/user_detail.html', context) 


def user_find(request):
    if request.method == 'GET': 
        
        # 送信されたデータを取得
        search_name = request.GET['search_name']
        # あいまい検索
        user_list = User.objects.filter(name__icontains=search_name)
        #htmlへ渡すデータを用意
        context = {
            'user_list': user_list # キーと値
        }
    return render(request, 'account/user_find_result.html', context) 