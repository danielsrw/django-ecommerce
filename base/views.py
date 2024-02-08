from django.shortcuts import render, get_object_or_404
from base.models import *

def home(request):
	categories = Category.objects.all()
	products = Product.objects.filter(product_status="published", featured=True)

	context = {
		'categories': categories,
		'products': products
	}

	return render(request, 'index.html', context)

def about(request):
	categories = Category.objects.all()

	context = {
		'categories': categories
	}

	return render(request, 'about.html', context)

def shop(request):
	categories = Category.objects.all()
	products = Product.objects.order_by("-id")

	context = {
		'categories': categories,
		'products': products
	}

	return render(request, 'shop.html', context)

def product(request, pid):
    product = Product.objects.get(pid=pid)
    products = Product.objects.all()
    # product = Product.objects.get_object_or_404(pid=pid)

    # Access related ProductImages using the reverse relationship
    p_images = product.p_images.all()

    context = {
        'product': product,
        'products': products,
        'p_images': p_images  # Renamed p_image to p_images for clarity
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
	categories = Category.objects.all()

	context = {
		'categories': categories
	}

	return render(request, 'faq.html', context)

def blog(request):
	categories = Category.objects.all()

	context = {
		'categories': categories
	}

	return render(request, 'blog.html', context)

def showBlog(request):
	categories = Category.objects.all()

	context = {
		'categories': categories
	}

	return render(request, 'blog-show.html', context)

def contact(request):
	categories = Category.objects.all()

	context = {
		'categories': categories
	}

	return render(request, 'contact.html', context)

def userDashboard(request):
	categories = Category.objects.all()

	context = {
		'categories': categories
	}

	return render(request, 'profile/dashboard.html', context)

def userEditProfile(request):
	categories = Category.objects.all()

	context = {
		'categories': categories
	}

	return render(request, 'profile/edit-profile.html', context)

def termsAndConditions(request):
	categories = Category.objects.all()

	context = {
		'categories': categories
	}

	return render(request, 'terms-and-conditions.html', context)

def vendors(request):
	vendors = Vendor.objects.all()

	context = {
		'vendors': vendors
	}

	return render(request, 'vendors/index.html', context)

def vendorView(request, vid):
	vendor = Vendor.objects.get(vid=vid)
	products = Product.objects.filter(vendor=vendor, product_status="published")

	context = {
		'vendor': vendor,
		'products': products,
	}

	return render(request, 'vendors/show.html', context)
