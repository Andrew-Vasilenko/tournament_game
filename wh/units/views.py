from django.shortcuts import render

# Create your views here.
from .models import Unit

def unit_view(request):

	unitName = request.GET.get('name')
	print(unitName)
	# берешь name юнита и ищешь его в базе
	obj = Unit.objects.get(name=unitName)
	print(obj)
	#context = {
		#'product_title': obj.title,
		#'product_description': obj.description
	#}
	context = { 'object': obj }
	return render(request, "units/unit.html", context)