"""apof URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from menu import views
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$','django.contrib.auth.views.login'),
    #url(r'^','django.contrib.auth.views.login'),
    url(r'^restaurant_list/', views.restaurant_list.as_view()),
    url(r'^user_cart/(?P<name>\d+)/',views.user_cart),
    url(r'^admin_cart/', views.admin_cart.as_view()),
    url(r'^restaurant_menu/(?P<restaurant>[-_\w]+)/$', views.restaurant_menu.as_view(), name='restaurant'),
    url(r'^logout/$', logout, {'template_name': 'restaurant_list.html', 'next_page': '/login'}, name='log-out'),
]
