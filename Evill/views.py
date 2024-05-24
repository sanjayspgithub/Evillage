from django.shortcuts import render,redirect
from datetime import datetime
#import razorpay # type: ignore
from Evill.models import *
from Evillage.settings import razor_pay_key_id,razor_pay_key_secret
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from Evill.decorators import *
from Evill.models import *
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

@login_required(login_url='/login_us')
def donate(request):
    info = donate_data.objects.all()
    data = {"information":info}
    return render(request,"donate.html",data)
@login_required(login_url='/login_us')
def donate1(request):
    context = {}
    client = razorpay.Client(auth=(razor_pay_key_id,razor_pay_key_secret))
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = int(request.POST.get('amount'))*100
        email = str(request.POST.get('email'))
        number = int(request.POST.get('number'))
        DATA = {
            "amount" : amount,
            "currency" : "INR",
            "receipt" : "receipt#1",
            "notes":{
                "key1" : "value3",
                "key2" : "value2"
            },
            "payment_capture":1
        }
        payment_order = client.order.create(data=DATA)
        context ={
            'api_key' : razor_pay_key_id,
            'payment_order_id' : payment_order['id'],
            'amountPaise' : amount,
            'amountINR' : amount/100,
            'name' : name,
            'email' : email,
            'number' : number
        }
        donated = donate_data(name = name,email = email,phone = number,amount = amount/100)
        donated.save()
        return render(request,"donate1.html",context)
    return render(request,"donate1.html",context)

def school(request):
    return render(request,"school.html")


def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        mess = request.POST.get('message')

        data = contact_data(name = name,email = email,subject = subject,mess = mess)
        data.save()
        # messages.success("Messages has been sent Successfully")
    return render(request,"contact.html")

def gram(request):
    return render(request,"gram.html")


@unauthorized_user
def login_us(request):
    if request.method == "POST":
        username = request.POST.get("User")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            request.session['username_id'] = username
            if user.is_superuser or user.is_staff:
                return redirect('about')
            else:
                return redirect('home')
        else:
            messages.error(request, 'In-correct username or password!..')
    return render(request,'login_us.html')


@unauthorized_user
def signup_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('user')
        email = request.POST.get('email')
        cpass = request.POST.get('cpass')
        password = request.POST.get('password')
        if User.objects.filter(email=email):
            messages.error(request,"Email already registered!")
            return redirect('login_us')
        elif User.objects.filter(username=username):
            messages.error(request,"Username already registered!")
            return redirect('login_us')
        elif cpass != password:
            messages.error(request,"Password dont match")
            return redirect('signup_us')
        elif len(username)>=10:
            messages.error(request,"Username must be under 10 characters")
            return redirect('signup_us')
        elif not username.isalnum():
            messages.error(request,"Username Must be Alpha Numeric")
            return redirect('signup_us')
        else:
            names = name.split(' ')
            myuser = User.objects.create_user(username,email,cpass)
            myuser.first_name = names[0] 
            myuser.last_name = names[1] 
            myuser.save()
            messages.success(request,"Account successfully created")
            return redirect('login_us')
    
    return render(request,'signup_us.html')

def logout_us(request):
    logout(request)
    messages.success(request,"logout Successfully")
    return redirect('home')
    
