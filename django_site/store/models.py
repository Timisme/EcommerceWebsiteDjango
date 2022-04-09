from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from datetime import datetime

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length= 50, default='General')

	def __str__(self):
		return self.name 

class Customer(models.Model):
    user = models.OneToOneField(User, null= True, blank= True, on_delete= models.CASCADE)
    name = models.CharField(max_length=255, null= True)
    email = models.CharField(max_length=255, null= True)

    def __str__(self):
        return self.name

class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.DecimalField(
		max_digits=7,
		decimal_places=2
	)
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null= True, blank= True, upload_to= 'products/')
	category = models.ForeignKey(Category, on_delete= models.SET_NULL, blank=True, null= True)
	description = models.CharField(max_length=252, blank= True, null= True)
	is_featured = models.BooleanField(default= False)

	def __str__(self):
		return self.name

	@property #access as an attribute rather than a method
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url 

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)
	shipping_fee = models.DecimalField(decimal_places=2, default= 60.00, max_digits= 7)

	def __str__(self):
		return str(self.id)

	@property # 將 function 視為 property (加工好的東西變成 attr)
	def shipping(self):
		shipping = False 
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True 
		
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total
	
	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 
	
	@property
	def get_cart_total_final(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total + self.shipping_fee

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total 

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address


# 之後改成 form post 後寄email 

class Contact(models.Model):
	name = models.CharField(max_length= 50)
	email = models.EmailField()
	subject = models.CharField(max_length= 100)
	message = models.TextField(max_length= 525)
	date_sent = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		# return datetime.strftime(self.date_sent, '%Y-%m-%d %H:%M:%S')
		return self.subject

class Newsletter(models.Model):
	email = models.EmailField(unique= True, blank= False, null= False)
	date_sent = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return self.email

class Coupon(models.Model):

	DISCOUNT_TYPE_CHOICES = (
        ('shipping', 'shipping'),
        ('product', 'product'),
		('order', 'order'),
    )
	
	code = models.CharField(max_length=100, blank= False, null= False)
	description = models.CharField(max_length=252)
	discount = models.FloatField(blank= False, null= False)
	discount_type = models.CharField(max_length=50, blank= False, null= False, choices= DISCOUNT_TYPE_CHOICES)
	is_enabled = models.BooleanField(blank= False, null= False)

	def __str__(self):
		return self.code
	