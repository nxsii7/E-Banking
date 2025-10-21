from django.shortcuts import render

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def account(request):
    return render(request,'users/account.html')

def transaction(request):
    return render(request,'users/transaction.html')

def confirmation(request):
    return render(request,'users/confirmation.html')

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'users/home.html')

def home_base(request):
    return render(request,'home_base.html')

def add_money(request):
    return render(request,'add_money.html')

def tranfer(request):
    return render(request,'transfer.html')

def pay(request):
    return render(request,'users/pay.html')

def payment(request):
    return render(request,'payment.html')

def pin_base(request):
    return render(request,'pin_base.html')







