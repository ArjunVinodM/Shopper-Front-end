# from django.urls import path
# from .views import *


# urlpatterns = [
#   path('', home)
# ]


from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('login', views.signin, name='login'),
  path('profile', views.view_profile, name='profile'),
  path('register', views.signup, name='register'),
  path('mobile', views.mobiles, name='mobile'),
  path('electronics', views.electronics, name='electronics'),
  path('fashion', views.fashion_items, name='fashion'),
  path('laptop', views.laptops, name='laptop'),
  path('fashion-card', views.fashion_items, name='fashion-card'),
  
  
  path('add_category', views.add_category, name='add_category'),
  path('add_product', views.add_product, name='add_product'),
  
]