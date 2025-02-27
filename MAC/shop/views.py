from math import ceil
from django.shortcuts import render
from django.http import HttpResponse
from .models import product,contact
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
    return HttpResponse("We are at checkout")
