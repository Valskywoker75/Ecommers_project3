from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment, Category, User
from .forms import CommentForm
from django.contrib.auth.views import LoginView
from .forms import UserForm

def index(request):
    categories = Category.objects.all()
    if 'cart' in request.session:
        cart_count = len(request.session['cart'].split(','))
    else:
        cart_count = 0
    return render(request, 'products/home.html', {'categories': categories, 'request':request, 'cart_count': cart_count})

def category_detail(request, pk):
    if 'cart' in request.session:
        cart_count = len(request.session['cart'].split(','))
    else:
        cart_count = 0
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'products/category_detail.html', {'category': category, 'products': products, 'cart_count': cart_count})

def addcart(request, pk):
    if 'cart' in request.session:
        request.session['cart'] = request.session['cart']+', '+str(pk)
    else:
        request.session['cart'] = str(pk)
    return redirect('/product/product/'+str(pk))
def cart(request):
    if 'cart' in request.session:
        cart_count = len(request.session['cart'].split(','))
    else:
        cart_count = 0
    if 'cart' in request.session:
        carts = request.session['cart'].split(',')
        cart_list = Product.objects.filter(id__in=carts)
        return render(request, 'products/list_cart.html',{'request': request, 'cart_list':cart_list, 'cart_count':cart_count})


def product_detail(request, product_id):
    if 'cart' in request.session:
        cart_count = len(request.session['cart'].split(','))
    else:
        cart_count = 0
    product = Product.objects.filter(id=product_id).first()
    comments = Comment.objects.filter(product=product).order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = CommentForm()

    return render(request, 'products/product_detail.html', {'request':request, 'product': product, 'comments': comments, 'form': form, 'cart_count': cart_count})


def create_game_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'mygameapp/success_registration.html',)
    else:
        form = UserForm()

    return render(request,'mygameapp/create_game_user.html',{'form': form})

def success_auth(request):
    if request.user.is_authenticated:
        return render(request, 'mygameapp/success_auth.html')
    else:
        return redirect('login_page')

def login_view(request):
    if request.method == 'POST':
        #categories = Category.objects.all()
        if User.objects.filter(nickname=request.POST['nickname']).exists():
            request.session['login'] = request.POST['nickname']
            return redirect('/')
        else:
            return redirect('/login_page')
    else:
        return render(request, 'mygameapp/login_page.html')

def logout(request):
    if 'login' in request.session:
        del request.session['login']
    return redirect('/')

def cartclear(request):
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('/')
