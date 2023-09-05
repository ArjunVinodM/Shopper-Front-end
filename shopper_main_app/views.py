from django.shortcuts import render

# Create your views here.


# user views
def home(request):
  return render(request, 'home.html')

def signin(request):
  return render(request, 'signin.html')

def signup(request):
  return render(request, 'signup.html')

def view_profile(request):
  return render(request, 'view_user_profile.html')

def mobiles(request):
  return render(request, 'mobile.html')

def electronics(request):
  return render(request, 'electronics.html')

def fashion_items(request):
  return render(request, 'fashion.html')

def laptops(request):
  return render(request, 'laptop.html')



# admin views
def admin_home(request):
  return render(request, 'admin_home.html')

def add_category(request):
  return render(request, 'add_category.html')

def add_product(request):
  return render(request, 'add_product.html')