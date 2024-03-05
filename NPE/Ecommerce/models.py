from django.db import models







class ProductCategory(models.Model):

    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class ProductSubCategory(models.Model):
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Product(models.Model):
    sno =models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Image1=models.ImageField(upload_to='images/')
    Image2=models.ImageField(upload_to='images/')
    Image3=models.ImageField(upload_to='images/')
    Usage = models.CharField(max_length=200,default="Utilitarian and decorative purposes")
    Keyword=models.CharField(max_length=1000,blank=True)
    category = models.ManyToManyField(ProductCategory)
    SubCategory= models.ManyToManyField(ProductSubCategory,blank=True)
    Description= models.TextField(max_length=10000)
    InStock=models.BooleanField(default=True)
    Available=models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)



    def __str__(self):
        return self.Name


class notice(models.Model):
    Message=models.CharField(max_length=900)

class Contact(models.Model):
    Email=models.EmailField()
    Subject=models.CharField(max_length=2000)
    Text=models.TextField(max_length=10000)


    def __str__(self):
        return self.Subject





