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
    return HttpResponse("We are at Tracker")
def search(request):
    return HttpResponse("We are at Search")
def productView(request):
    product=product.objects.filter(id=myid)
    return render(request,"shop/prodView.html",{'product':product[0]})
def checkout(request):
    if request.method=="POST":
        items_json=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','')+" " request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')
        order_instance = orders(items_json=items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order_instance.save()
        thank=True
        id=order_instance.order_id
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})
    return render(request,"shop/checkout.html")
