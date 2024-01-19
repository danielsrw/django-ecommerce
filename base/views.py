from django.shortcuts import render
from base.models import Category, Product

def home(request):
	categories = Category.objects.all()
	products = Product.objects.filter(product_status="published", featured=True)

	context = {
		'categories': categories,
		'products': products
	}

	return render(request, 'index.html', context)

def about(request):
	return render(request, 'about.html')

def shop(request):
	products = Product.objects.order_by("-id")

	context = {
		'products': products
	}

	return render(request, 'shop.html', context)

def product(request):
	return render(request, 'product.html')

def faq(request):
	return render(request, 'faq.html')

def blog(request):
	return render(request, 'blog.html')

def showBlog(request):
	return render(request, 'blog-show.html')

def contact(request):
	return render(request, 'contact.html')

def userDashboard(request):
	return render(request, 'profile/dashboard.html')

def userEditProfile(request):
	return render(request, 'profile/edit-profile.html')

def termsAndConditions(request):
	return render(request, 'terms-and-conditions.html')