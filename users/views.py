from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .models import Prodeuct,Cart,Category

class HomeView(View):
    def get(self,request):
        products = Prodeuct.objects.filter(in_stock=True)
        cart = Cart.objects.count()
        return render(request,'users/home.html',{'products':products,'cart':cart})

class DetailView(View):
    def get(self,request,id):
        product = get_object_or_404(Prodeuct,id=id)
        cart = Cart.objects.count()
        return render(request,'users/detail.html',{'product':product,'cart':cart})
    def post(self,request,id):
        product = get_object_or_404(Prodeuct,id=id)
        quontity = int(request.POST['cart'])
        if Cart.objects.filter(product=product).exists():
            cart = Cart.objects.filter(product=product).first()
            cart.quontity += quontity
            cart.save()
        

        else:
            cart = Cart()
            cart.product=product
            cart.quontity=quontity
            cart.save()
        return redirect('users/')
    
class Categoryes(View):
    def get(self,request,id):
        categor = get_object_or_404(Category,id=id)
        products = categor.products.all()
        categories = Category.objects.all()
        return render(request,'users/home.html',{"products":products,'cats':categories})
    
class CartDetailView(View):
    def get(self,request):
        products = Cart.objects.all()
        return render(request,'users/cart.html',{"products":products})

def delete(request,id):
    cart = get_object_or_404(Cart,id=id)
    cart.delete()
    return redirect('users/')
