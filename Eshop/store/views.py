from django.shortcuts import render, redirect, HttpResponse
from .models import Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    products = None
    categories = Category.objects.all()
    template_name = 'store/home.html'
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.objects.all()
    context = {'products':products, 'categories': categories}
    return render(request, template_name, context)

def validateCustomer(customer):

    error_message = None

    if len(customer.first_name)<4:
            error_message = 'First Name should be atleast 4 characters'
        
    elif len(customer.last_name)<=2:
        error_message = 'First Name should be atleast 4 characters'

    elif customer.isExist():
        error_message = 'Email Already Registered'

    elif len(customer.phone)<10 or len(customer.phone)>10:
        error_message = 'Please Enter Correct Phone'

    elif len(customer.password)<8:
        error_message = 'Password Must be atleast 8 characters'
    
    return error_message

def signup(request):
    template_name = 'store/signup.html'
    context = {}
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        country = request.POST.get('country')
        password = request.POST.get('password')

        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'phone' : phone,
            'email' : email
        }

        customer = Customer(
                    first_name = first_name,
                    last_name = last_name,
                    phone = phone,
                    email = email,
                    password = password)
        
        error_message = validateCustomer(customer)
       
        # Proceeding if no error found
        if not error_message:
            customer.password = make_password(customer.password) # Password Hashing is used to encrypt password
            customer.register()
            return redirect('home_url')
        else:
            data = {
                'error':error_message, 
                'values': value
                }
            return render(request, template_name, data)
    return render(request, template_name, context)

def login(request):
    template_name = 'store/login.html'
    error_message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect('home_url')
            else:
                error_message = 'Email or Password invalid'
        else:
            error_message = 'Email or Password invalid'
        
    return render(request, template_name, {'error' : error_message})