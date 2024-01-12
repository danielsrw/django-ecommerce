from django.shortcuts import render

def home(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def shop(request):
	return render(request, 'shop.html')

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

def register(request):
    return render(request, 'registration/register.html')

def userDashboard(request):
	return render(request, 'profile/dashboard.html')

def userEditProfile(request):
	return render(request, 'profile/edit-profile.html')

def termsAndConditions(request):
	return render(request, 'terms-and-conditions.html')