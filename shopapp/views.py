from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AddCartForm01
from .forms import ContentsForm
from .models import Contents
from shopapp.models import Customer
from shopapp.models import Item
from shopapp.models import Cart


# Create your views here.

def index(request):
    return HttpResponse("Hello Django! よろしく。")


def form(request):
    # return HttpResponse("入力フォームです。")
    # >>> Blog.objects.values()
    #[{'id': 1, 'name': 'Beatles Blog', 'tagline': 'All the latest Beatles news.'}],
    contents_records = Contents.objects.values()
    form = ContentsForm(request.POST)
    if request.method == 'POST':
     
        if form.is_valid():
            form.save()
            return redirect("form")
        else:
            return redirect("form")
    else:
        form = ContentsForm()
    return render(request, 'shopapp/form.html', {'form': form, 'model': contents_records})


# カートに追加する画面を表示する
def addcartform(request):
    form = AddCartForm01()
    return render(request, 'shopapp/addCartForm01.html', {'form': form})


# カートの中身を表示する
def lookcart(request):
    # form = AddCartForm01(request.POST)
    #値の取得はrequest.POST['フォームのID']
    email_input = request.POST['email']
    item_name_input = request.POST['item_name']
    order_quantity_input  = request.POST['order_quantity']

    # Customer,Itemの検索
    customer = Customer.objects.get(email=email_input)
    print(customer.name)
    item = Item.objects.get(name=item_name_input)

    if(customer != None and Item  != None):
        # カートテーブルに追加する
        cart = Cart.objects.create(item=item, customer=customer, order_quantity=order_quantity_input)
        cart.save()

    # Cartの検索
    carts = Cart.objects.filter(customer=customer)

    context = {
        'carts': carts,
        'process_message':"カートに追加しました"
    }

    return render(request, 'shopapp/lookCart.html', context)


# カートレコードの注文数量を変更する
def changeorderquantity(request):
    #値の取得はrequest.POST['フォームのID']
    cart_id = request.POST['cart_id']
    order_quantity_input = request.POST['order_quantity']
    cart_customer_email  = request.POST['cart_customer_email']

    if(order_quantity_input != None):
        cart = Cart.objects.get(id=cart_id)
        # カートレコードの注文数量を変更する
        cart.order_quantity = order_quantity_input
        cart.save()
    
    # Customerの検索
    customer = Customer.objects.get(email=cart_customer_email)
    print(customer.name)

    # Cartの検索
    carts = Cart.objects.filter(customer=customer)

    context = {
        'carts': carts,
        'process_message':"注文数量を変更しました"
    }

    return render(request, 'shopapp/lookCart.html', context)



# カートレコードの注文数量を変更する
def deletecartrecord(request):
     # cart_id値の取得
    cart_id = request.POST['cart_id']
    cart_customer_email  = request.POST['cart_customer_email']

    # カートレコードから検索
    cart = Cart.objects.get(id=cart_id)
    # 該当カートレコードを削除
    cart.delete()

    # Customerの検索
    customer = Customer.objects.get(email=cart_customer_email)
    print(customer.name)

    # Cartの検索
    carts = Cart.objects.filter(customer=customer)

    context = {
        'carts': carts,
        'process_message':"カートのアイテムを削除しました"
    }

    return render(request, 'shopapp/lookCart.html', context)