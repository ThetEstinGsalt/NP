from django.shortcuts import render

# Create your views here.

from .models import Product,ProductCategory,ProductSubCategory,Contact



def Index(request):

    prods=Product.objects.all()
    lastest=prods[::-1]


    return render(request, "index.html",{"newest":lastest[0:8]})

def Products(request):
    cats=ProductCategory.objects.all()

    prods=Product.objects.all()
    lastest=prods[::-1]
    last=Product.objects.last()
    prev=lastest[1]
    print(lastest)

    catlist=cats[0:]
    subcats1=ProductSubCategory.objects.all()[0:4]
    subcats2=ProductSubCategory.objects.all()[4:]

    subcats3=cats[0:]





    return render(request, "Products.html",{"Cat":catlist,"Sub1":subcats1,"Sub2":subcats2,"Sub3":subcats3,"newest":lastest[0:8],"Prods":prods,"last":last,"prev":prev})

def Overview(request,sno,):
    
    product=Product.objects.filter(sno=sno)

    sizepre=product.first().Available

    size=str(sizepre).split(",")
    if(product.first().InStock):
        instock="In stock"

    else:
        instock="Out of stock"


    return render(request, "Overview.html",{"Product":product.first(),"size":size,"stock":instock})




def About(request):

    return render(request, "About.html")


def Search(request,slug):

 
    try:

        try:
            categoryfil=ProductCategory.objects.get(name=slug)
            Products=Product.objects.filter(category=categoryfil)

        except:
            subcatfil=ProductSubCategory.objects.get(name=slug)
            Products=Product.objects.filter(SubCategory=subcatfil)
         


    except:


        Products = Product.objects.filter(Keyword__icontains=slug)





    return render(request, "Search.html",{"newest":Products})



def ContactMail(request):

    if request.method == 'POST':
        Email = request.POST['Email']
        Subject = request.POST['Subject']
        Text = request.POST['Text']
        Cont = Contact(Email=Email, Subject=Subject,Text=Text)
        Cont.save()
        return render(request, "Success.html")

  
    

    return render(request, "Contact.html")