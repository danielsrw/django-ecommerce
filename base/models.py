from pyexpat import model
from django.db import models
from shortuuidfield import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import CustomUser

STATUS_CHOICES = (
	("process", "Processing"),
	("shipped", "Shipped"),
	("delivered", "Delivered"),
)

STATUS = (
	("draft", "Draft"),
	("disabled", "Disabled"),
	("rejected", "Rejected"),
	("in_review", "In Review"),
	("published", "Published"),
)

RATING = (
	(1, "⭐"),
	(2, "⭐⭐"),
	(3, "⭐⭐⭐"),
	(4, "⭐⭐⭐⭐"),
	(5, "⭐⭐⭐⭐⭐"),
)

def use_directory_path(instance, filename):
	return 'user_{0}/{1}'.format(instance.user.id, filename)

def validate_svg(value):
    """
    Validate that the uploaded file is an SVG.
    """
    if value.file.content_type != 'image/svg+xml':
        raise ValidationError("Only SVG files are allowed.")

class Category(models.Model):
    cid = ShortUUIDField(unique=True, max_length=20)
    title = models.CharField(max_length=100, default="Category Name")
    image = models.FileField(upload_to="category", default="category.jpg", validators=[validate_svg])

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        # Adjust this part if you want to display the SVG differently
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

class Tag(models.Model):
    tid = ShortUUIDField(unique=True, max_length=20)
    title = models.CharField(max_length=100, default="Tag Name")

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.title

class Vendor(models.Model):
	vid = ShortUUIDField(unique=True, max_length=20)

	title = models.CharField(max_length=100, default="John Doe")
	image = models.ImageField(upload_to=use_directory_path, default="vendor.jpg")
	description = models.TextField(null=True, blank=False, default="Vendor description here,.....")

	address = models.CharField(max_length=100, default="123 Kigali Rwanda")
	contact = models.CharField(max_length=100, default="123456789")
	chat_resp_time = models.CharField(max_length=100, default="100")
	shipping_on_time = models.CharField(max_length=100, default="100")
	authentic_rating = models.CharField(max_length=100, default="100")
	days_return = models.CharField(max_length=100, default="100")
	warranty_period = models.CharField(max_length=100, default="100")

	user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

	class Meta:
		verbose_name_plural = "Vendors"

	def vendor_image(self):
		return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

	def __str__(self):
		return self.title

class Product(models.Model):
	pid = ShortUUIDField(unique=True, max_length=20)

	user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
	vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
	
	title = models.CharField(max_length=100, default="Product Title")
	image = models.ImageField(upload_to=use_directory_path, default="product.jpg")
	description = models.TextField(null=True, blank=False, default="This is the Product")

	price = models.DecimalField(max_digits=99999999999, decimal_places=2, default="1.99")
	old_price = models.DecimalField(max_digits=9999999999, decimal_places=2, default="2.99")

	specifications = models.TextField(null=True, blank=True)

	product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")

	status = models.BooleanField(default=True)
	in_stock = models.BooleanField(default=True)
	featured = models.BooleanField(default=True)
	digital = models.BooleanField(default=True)

	sku = ShortUUIDField(unique=True, max_length=10)

	date = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(null=True, blank=True)

	class Meta:
		verbose_name_plural = "Products"

	def product_image(self):
		return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

	def __str__(self):
		return self.title

	def get_percentage(self):
		new_price = (self.price / self.old_price) * 100

		return new_price

class ProductImages(models.Model):
	images = models.ImageField(upload_to="product-images", default="product.jpg")
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Product Images"

class CartOrder(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=99999999999, decimal_places=2, default="1.99")
	paid_status = models.BooleanField(default=False)
	order_date = models.DateTimeField(auto_now_add=True)
	product_status = models.CharField(choices=STATUS_CHOICES, max_length=30, default="processing")

	class Meta:
		verbose_name_plural = "Cart Order"

class CartOrderItems(models.Model):
	order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
	invoice_no = models.CharField(max_length=200)
	product_status = models.CharField(max_length=200)
	item = models.CharField(max_length=200)
	image = models.CharField(max_length=200)
	qty = models.IntegerField(default=0)
	price = models.DecimalField(max_digits=99999999999, decimal_places=2, default=1.99)
	total = models.DecimalField(max_digits=99999999999, decimal_places=2, default=1.99)

	class Meta:
		verbose_name_plural = "Cart Order Items"

	def order_img(self):
		return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image.url))

class ProductReview(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	review = models.TextField()
	rating = models.IntegerField(choices=RATING, default=None)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Product Reviews"

	def __str__(self):
		return self.product.title

	def get_rating(self):
		return self.rating

class Wishlist(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Wishlists"

	def __str__(self):
		return self.product.title

class Address(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=100, null=True)
	status = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = "Address"