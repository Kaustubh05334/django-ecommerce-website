from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .models import Seller_user,Product,ProductImage
from userAccount.models import Customer,Order
from django.urls import reverse
# Create your views here.
def register_seller(request):
    if request.method=="POST":
        name = request.POST.get('name')
        gstn = request.POST.get('gstn')
        address = request.POST.get('address')
        user= request.user
        s1 = Seller_user(user=user,shop_or_company_name=name,GST_number=gstn,shop_address=address)
        s1.save()
        seller_group = Group.objects.get(name='Seller')
        user.groups.add(seller_group)
        user.save()
        login(request,user)
        return redirect('home')
    return render(request,'products/register_seller.html')

def seller_add_product(request):
    if request.method=="POST":
        name = request.POST.get('name')
        price = float(request.POST.get('price'))
        qty = int(request.POST.get('qty'))
        desc = request.POST.get('desc')
        cat = request.POST.get('cat')
        subcat = request.POST.get('subcat')
        form = request.FILES.getlist('images')
        p1= Product(name=name,price=price,description=desc,category=cat,sub_category=subcat,seller=request.user,qty=qty)  
        p1.save()     
        for image in form:
            i1 = ProductImage(product=p1,image=image)
            i1.save()
        message= "Product Added"
        return render(request,'products/add_prod.html',{'message':message})
    return render(request,'products/add_prod.html')


def individual_product(request,product_id,product_name):
    product= Product.objects.get(id=product_id)
    prod_img = ProductImage.objects.filter(product=product)
    if request.method == "POST":
        type= request.POST.get('type')
        if type=="buy":
            url = reverse('buy_prod', kwargs={"product_id":product_id})
            return redirect(url)
        elif type=="cart":
            user=request.user
            if user.is_authenticated:
                customer = Customer.objects.get(user=user)
                customer.cart_items.add(Product.objects.get(id=product_id))
            else:
                return redirect(reverse("login"))
    return render(request,'products/prod.html',{'product':product,'prod_img':prod_img})

def buy_prod(request,product_id):
    prod = Product.objects.get(id=product_id)
    customer = Customer.objects.get(user=request.user)
    if request.method=="POST":
        mode = request.POST.get('mode')
        qty = request.POST.get('quantity')
        if mode=="online":
            return redirect('home')
        else:
            order = Order(customer=customer,product=prod,qty=qty,mode_of_payment="Cash on Delivery",order_status="Shipped")
            order.save()
            return redirect(reverse("order_con",kwargs={"order_id":order.id}))
    return render(request,"products/prod_buy.html",{"prod":prod,"customer":customer})

def order_confirm(request,order_id):
    order = Order.objects.get(id = order_id)
    return render(request,"products/ordercon.html")
