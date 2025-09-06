from math import ceil
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import product, contact, orders
import json
import logging

logger = logging.getLogger(__name__)

def index(request):
    products = product.objects.all()
    allprods = []
    
    catprods = product.objects.values('category', 'product_id')
    cats = {item["category"] for item in catprods}
    
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides + 1), nSlides])
    
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    
    params = {
        'no_of_slides': nSlides,
        'range': range(1, nSlides + 1),
        'prodcut': products,
        'allprods': allprods
    }
    return render(request, "shop/index.html", params)

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        
        contact_instance = contact(name=name, email=email, phone=phone, desc=desc)
        contact_instance.save()
        
        messages.success(request, 'Your message has been sent successfully!')
    
    return render(request, "shop/contact.html")

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        
        try:
            order = orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                response = json.dumps({
                    "status": "success", 
                    "message": "Order found",
                    "itemsJson": order[0].items_json
                }, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            logger.error(f"Tracker error: {e}")
            return HttpResponse('{"status":"error"}')
            
    return render(request, "shop/tracker.html")

def search(request):
    query = request.GET.get('q', '')
    if query:
        products = product.objects.filter(product_name__icontains=query)
        return render(request, "shop/search.html", {'products': products, 'query': query})
    return render(request, "shop/search.html")

def productView(request, myid):
    single_product = get_object_or_404(product, id=myid)
    return render(request, "shop/prodView.html", {'product': single_product})

def checkout(request):
    if request.method == "POST":
        itemsJson = request.POST.get("itemsJson", "")
        amount = request.POST.get("amount", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        address = request.POST.get("address", "") + " " + request.POST.get("address2", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        zip_code = request.POST.get("zip_code", "")
        
        order = orders(
            items_json=itemsJson,
            amount=amount,
            name=name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
        )
        order.save()
        
        return render(request, "shop/checkout.html", {"thank": 1, "id": order.order_id})
        
    return render(request, "shop/checkout.html")