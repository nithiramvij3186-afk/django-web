from django.shortcuts import render,redirect
from app.models import menu
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.core.mail import send_mail
from django.conf import settings
import random,time,string
from django.contrib.auth.decorators import login_required
# Create your views here.


def index_page(request):
    n=menu.objects.all()
    return render(request,'index.html',{'n':n})

@login_required
def menu_page(request):
    a=menu.objects.all()
    return render(request,'menu.html',{'a':a})

@login_required
def order(request):
    drink_name=request.GET.get('drink')
    selected_drink=menu.objects.get(menu_name=drink_name)
    return render(request,'order.html',{'drink':selected_drink})


def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password,email=email)
        if user is not None:
            otp=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=5))
            request.session['otp']=str(otp)
            request.session['user_id']=user.id
            request.session['otp_time']=time.time()
            send_mail(
                subject='otp',
                message=f'''{otp}''',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
            )
            return redirect('otp')

    return render(request,'login.html')


def signup_page(request):
    if request.method =='POST':
        username=request.POST.get('username')     
        email=request.POST.get('email')
        password=request.POST.get('password')
        current_password=request.POST.get('current_password')
        if password!=current_password:
            return redirect('signup')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('login')
    return render(request,'signup.html')


@login_required
def logout_page(request):
    logout(request)
    return redirect('login')
    
@login_required
def contact_page(request):
    if request.method=='POST':
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        message=request.POST.get('Message')
        send_mail(
            subject='someone is messaging',
            message=f'''the {name} and the {email} and the message was \n\n{message}''',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['internadmin97@gmail.com'],
        )
        send_mail(
            subject='thankyou for contacting us',
            message=f'''i will contact soon''',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )

    return render(request,'contact.html' ,{'success':'Thanking you check your email'})


def otp_page(request):
    if request.method=='POST':
        entered_otp=request.POST.get('otp')
        saved_otp=request.session.get('otp')
        otp_time=request.session.get('otp_time')
        current_time=time.time()
        if current_time-otp_time<60:
            if entered_otp==saved_otp:
                user_id=request.session.get('user_id')
                user=User.objects.get(id=user_id)
                login(request,user)
                return redirect('index')
            else:
                return render(request,'otp.html',{'error':'time exist'})
        else:
            return render(request,'otp.html',{'error':'otp invalid'})
            
    return render(request,'otp.html')



@login_required
def add_cart(request,id):
    b=menu.objects.get(id=id)
    cart=request.session.get('cart',[])
    cart.append({
        'id':b.id,
        'name':b.menu_name,
        'price':b.menu_price,
        'image':b.menu_image.url,
        'description':b.menu_description,
    })
    request.session['cart']=cart
    return redirect('menu')


@login_required
def cart_page(request):
    cart=request.session.get('cart',[])
    return render(request,'cart.html',{'cart':cart})


def buy_page(request):
    return render(request,'buy.html')