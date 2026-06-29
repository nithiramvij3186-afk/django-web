"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index_page,name='index'),
    path('menu/',views.menu_page,name='menu'),
    path('order/',views.order,name='order'),
    path('login/',views.login_page,name='login'),
    path('signup/',views.signup_page,name='signup'),
    path('logout/',views.logout_page,name='logout'),
    path('contact/',views.contact_page,name='contact'),
    path('otp/',views.otp_page,name='otp'),
    path('cart/',views.cart_page,name='cart'),
    path('add_cart/<int:id>',views.add_cart,name='addcart'),
    path('buy_page/',views.buy_page,name='buyed'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
