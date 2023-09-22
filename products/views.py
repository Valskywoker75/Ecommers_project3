from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment, Category, User
from .forms import CommentForm
from django.contrib.auth.views import LoginView
from .forms import UserForm

def index(request):
    categories = Category.objects.all()
    return render(request, 'products/home.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'products/category_detail.html', {'category': category, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
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

    return render(request, 'products/product_detail.html', {'product': product, 'comments': comments, 'form': form})


def create_game_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'mygameapp/success_registration.html',)
    else:
        form = UserForm()

    return render(request,'mygameapp/create_game_user.html',{'form': form},)

def success_auth(request):
    print(1)
    if request.user.is_authenticated:
        return render(request, 'mygameapp/success_auth.html')
    else:
        return redirect('login_page')



def login_view(request):
    if request.method == 'POST':
        #categories = Category.objects.all()
        print(request.POST['nickname'])
        if User.objects.filter(nickname=request.POST['nickname']).exists():
            print('login')
            request.session['login'] = request.POST['nickname']
            return redirect('/')
        else:
            return redirect('/login_page')
    else:
        return render(request, 'mygameapp/login_page.html')
def logout(request):
    if 'login' in request.session:
        del request.session['login']
    return redirect('/login_page')


"""class CustomLoginView(LoginView):
    template_name = 'mygameapp/login_page.html'
    success_message = "Авторизация прошла успешно!"
    success_url = '/success_auth/'
    redirect_authenticated_user = False

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response"""
