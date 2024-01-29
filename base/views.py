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
	categories = Category.objects.all()
	products = Product.objects.order_by("-id")

	context = {
		'categories': categories,
		'products': products
	}

	return render(request, 'shop.html', context)

def product(request):
	products = Product.objects.filter(product_status="published")

	context = {
		'products': products
	}

	return render(request, 'product.html', context)

def CategoryProduct(request, cid):
	category = Category.objects.get(cid=cid)
	products = Product.objects.filter(product_status="published", category=category)

	context = {
		'category': category,
		'products': products
	}

	return render(request, 'categoryProduct.html', context)

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