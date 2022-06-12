from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer


# insomnia
# Create your views here.
@csrf_exempt
def time_input(request):
    if request.method=="GET":
        order_list = Order.objects.all()
        return render(request,'boss/order_list.html',{'order_list':order_list})
    
    elif request.method=="POST":
        order_item = Order.objects.get(pk=request.POST['order_id'])
        order_item.estimated_time  = int(request.POST['estimated_time'])
        order_item.save()
        # return HttpResponse(status =200)
        return render(request, 'boss/success.html')