from math import ceil
from django.shortcuts import render
from django.http import HttpResponse
from .models import product,contact,orders
import  logging
logger =logging.getLogger(__name__)
def index(request):
    products = product.objects.all()
    allprods=[]
    catprods=product.objects.values('category','id')
    cats = {item["category"]for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n/4)-(n//4))
        allprods.append([prod, range(1, nSlides), nSlides])
    print(products)
    n=len(products)
    nSlides = n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides,'range':range(1,nSlides), 'prodcut':products}
    return render(request,"shop/index.html",params)

def about(request):
    return render(request,"shop/about.html")
def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc= request.POST.get('desc','')
        contact_instance=contact(name=name,email=email,phone=phone,desc=desc)
        contact_instance.save()

    return render(request,"shop/contact.html")
def tracker(request):
    if request.methods =="POST":
        orderId=request.POST.get('orderId','')
        email=request.POST.get('email','')
        try:
            order=orders.objects.filter(order_id=orderId,email=email)
            if len(order)>0:
                update=orderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps({"status":"success","updates":updates,"itemsJson":order[0].items_json},default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{}')
    return HttpResponse('{}')
def search(request):
    return HttpResponse("We are at Search")
def productView(request):
    product=product.objects.filter(id=myid)
    print(product)
    return render(request,"shop/prodView.html",{'product':product[0]})
def checkout(request):
    if request.method == "POST":
        itemsJson = request.POST.get("itemsJson", "")
        amount = request.POST.get("amount", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        address = request.POST.get("address", "") + request.POST.get("address2", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        zip_code = request.POST.get("zip_code", "")
        order = order(
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
        update = orderUpdate(
            order_id=order.order_id, update_desc="The order has been placed."
        )
        update.save()
        return render(request, "shop/checkout.html", {"thank": 1, "id": order.order_id})
    return render(request, "shop/checkout.html")