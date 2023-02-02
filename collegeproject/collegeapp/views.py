from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from .form import OrderForm, Order, Course,Department


def allProdCat(request):
    department=Department.objects.all()
    return render(request, 'base.html')

def login_view(request):
    # Render the login page with a form to input username and password
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return render(request,'new_page.html')
    else:
        return render(request,'login.html', {'error': 'Invalid login'})
    return render(request,'login.html')

def register(request):
    # Render the register page with a form to input username, password, and confirm password
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Log the user in after successful registration
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
        return render(request,'login.html')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html')

def new_page(request):
    # Render the new page with a button to open the order form
    return render(request, 'new_page.html')

def order_form(request):
    # Render the order form with fields for name, DOB, age, gender, phone number, email, address, department, courses, purpose, and materials
    model=Order
    form_class=OrderForm
    form = UserCreationForm(request.POST)
    success_url=reverse_lazy('allProdCat')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Save the form data and return a message confirming the order
            form.save()
            return render(request, 'order_form.html', {'form': form, 'message': 'Order confirmed'})
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})
def load_courses(request):
    department_id=request.GET.get('department_id')
    courses=Course.objects.filter(department_id=department_id).all()
    return render(request,'course_dropdown_list.html', { 'courses':courses})