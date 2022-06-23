from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as _login, logout as _logout

# Create your views here.
from user_auth.forms import AccountForm, AddressForm
from user_auth.models import Account


def register(request):
    if request.method == 'POST':
        form_user = AccountForm(request.POST)
        form_adderess = AddressForm(request.POST)
        if form_user.is_valid() and form_adderess.is_valid():
            address = form_adderess.save()
            user = Account.objects.create_user(
                username=  form_user.cleaned_data['username'],
                email=     form_user.cleaned_data['email'],
                password=  form_user.cleaned_data['password'],
                first_name=form_user.cleaned_data['first_name'],
                last_name= form_user.cleaned_data['last_name'],
            )
            user.address = address
            user.save()
            user = authenticate(
                request,
                username=form_user.cleaned_data['username'],
                password=form_user.cleaned_data['password']
            )
            if user is not None:
                _login(request, user)
            else:
                print('CANT\n' * 5)
            return render(request, 'board/home.html', {'user': user})
    context = {
        'form_user': AccountForm(),
        'form_adderess': AddressForm()
    }
    return render(request, 'auth/register.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                _login(request, user)
            else:
                print('CANT\n' * 5)
            return redirect('/')
        else:
            context = {
                'form': form
            }
            return render(request, 'auth/login.html', context)
    context = {
        'form': AuthenticationForm(),
    }
    return render(request, 'auth/login.html', context)


def logout(request):
    _logout(request)
    return render(request, 'board/home.html', {'user': None})


# TODO: auth required
def profile(request):
    if request.method == 'POST':
        account_form = AccountForm(request.POST, request.FILES, instance=request.user)
        address_form = AddressForm(request.POST, instance=request.user.address)
        if account_form.is_valid() and address_form.is_valid():
            account_form.save()
            address_form.save()

    context = {
        'form_user': AccountForm(instance=request.user),
        'form_adderess': AddressForm(instance=request.user.address)
    }
    return render(request, 'auth/profile.html', context)
