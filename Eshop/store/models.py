from django.db import models
from django_countries.fields import CountryField

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_catagories():
       return  Category.objects.all()

class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField(default=0)
    catagory = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products(self):
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()

class Customer(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    #country = CountryField(blank=True)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.email

    def register(self):
        self.save()
    
    'For Existing User'
    def isExist(self):
        if Customer.objects.filter(email = self.email):
            return True
        
        return False
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False
