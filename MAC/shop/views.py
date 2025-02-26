from math import ceil
from django.shortcuts import render
from django.http import HttpResponse
from .models import product
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
    return HttpResponse("We are at Contact")
def tracker(request):
    return HttpResponse("We are at Tracker")
def search(request):
    return HttpResponse("We are at Search")
def productView(request):
    return HttpResponse("We are at ProductView")
def checkout(request):
    return HttpResponse("We are at checkout")

