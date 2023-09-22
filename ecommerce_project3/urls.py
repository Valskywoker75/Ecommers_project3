from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from products import views as product_views

urlpatterns = [
    path('', product_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('product/', include('products.urls')),
    path('category/<int:pk>/', product_views.category_detail, name='category_detail'),
    path('create_game_user/', product_views.create_game_user, name='create_game_user'),
    path('login_page/', product_views.login_view, name='login_page'),
    path('success_auth/', product_views.login_view, name='success_auth'),
    path('logout/', product_views.logout, name='success_auth'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
