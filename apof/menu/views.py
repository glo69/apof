from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic import TemplateView, View
from menu.models import Restaurant, Menu, Ingredient, Cart
from django.http import HttpResponse

# Create your views here.

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/login")

#class restaurant_list(TemplateView):
#    template_name = 'restaurant_list.html'
    
class restaurant_list(View):
	def get(self, request):
		username = None
		if request.user.is_authenticated():
			username = request.user.username
		context = {'members': Restaurant.objects.all(), 'username': username}
		return render(request,'restaurant_list.html', context=context)

class restaurant_menu(TemplateView):
	#template_name = 'restaurant_menu.html'
	def get(self, request, restaurant):
		username = None
		if request.user.is_authenticated():
			username = request.user.username
		context = {'members': Menu.objects.filter(restaurant__slug=restaurant), 'username': username}
		return render(request,'restaurant_menu.html', context=context)


def user_cart(request, name):
	username = None
	if request.user.is_authenticated():
		username = request.user.username
	danie = Menu.objects.get(pk=name)
	Cart.objects.create(user=username, date = '2016-03-20', dish=danie, restaurant='restaurant')
	return HttpResponse('Dodano do koszyka {}'.format(danie.dish))

class admin_cart(TemplateView):
	def get(self, request):
		context = {'members': Cart.objects.all()}
		return render(request,'admin_cart.html', context=context)
				
				
		
		
			
		
		
		
    
