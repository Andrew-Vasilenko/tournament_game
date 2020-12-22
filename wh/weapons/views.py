from django.shortcuts import render

# Create your views here.
from .models import Weapon

def weapon_view(request):

	weaponTitle = request.GET.get('title')
	# берешь title weapon'a и ищешь его в базе
	obj = Weapon.objects.get(title=weaponTitle)
	#context = {
		#'product_title': obj.title,
		#'product_description': obj.description
	#}
	context = { 'object': obj }
	return render(request, "weapons/weapon.html", context)