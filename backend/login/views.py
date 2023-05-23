from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import Customer
from .forms import CreateUserForm

def registerPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    else:
        form = CreateUserForm

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                # 該 user 建立 customer 
                user = User.objects.get(username = form.cleaned_data['username'])
                customer, created = Customer.objects.get_or_create(
                    user = user,
                    name = form.cleaned_data['username'],
                    email = form.cleaned_data['email']
                )
                return redirect('login')

        context = {
            'form': form 
        }
        return render(request, 'register.html', context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('account')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            # print(username, password)
            user = authenticate(request, username= username, password= password)

            if user is not None:
                login(request, user)
                print('successfully logged in!')
                return redirect('home')
            
            else:
                messages.info(request, 'username or password incorrect')
                return HttpResponse('username or password incorrect')
        
        else:
            context = {

            }
            return render(request, 'login.html', context)
        

def logoutUser(request):
    logout(request)
    return redirect('/')