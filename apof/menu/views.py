from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic import TemplateView, View
from menu.models import Restaurant, Menu

# Create your views here.

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")

#class restaurant_list(TemplateView):
#    template_name = 'restaurant_list.html'
    
class restaurant_list(View):
	def get(self, request):
		context = {'members': Restaurant.objects.all()}
		return render(request,'restaurant_list.html', context=context)

class restaurant_menu(TemplateView):
	#template_name = 'restaurant_menu.html'
	
	def get(self, request, restaurant):
		context = {'members': Menu.objects.filter(restaurant__slug=restaurant)}
		return render(request,'restaurant_menu.html', context=context)

#class add_to_cart(View):
	
		
			
		
		
		
    
