from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import *

app_name = 'main'

urlpatterns = [
                  path('', IndexView.as_view(), name='index'),
                  path('account/login', BBLoginView.as_view(), name='login'),
                  path('account/register', RegisterView.as_view(), name='register'),
                  path('accounts/profile/', ProfileListView.as_view(), name='profile'),
                  path('account/logout/', views.logout_view, name='logout'),
                  path('products/', ProductListView.as_view(), name='products'),
                  path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
                  path('add-to-cart/<int:product_id>', views.add_to_cart, name='add-to-cart'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
