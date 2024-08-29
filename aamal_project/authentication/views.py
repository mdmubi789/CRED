from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from catalogue.models import Category, Product, SubCategory
from collections import defaultdict

def home(request):
    return render( request,'index.html')

def about(request):
    return render( request,'about.html')

def contact(request):
    return render( request,'contact.html')

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('authentication:home')  # Redirect to a home or dashboard page after login
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')


# views.py
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('authentication:home')


def useradmin(request):
    if request.method == 'POST':
        if 'add_category' in request.POST:
            # Handle category addition
            name = request.POST.get('cat_name')

            
            if name:
                Category.objects.create(
                    cat_name = name,
                )
                messages.success(request, 'Category successfully added!')
                return redirect('authentication:useradmin')
                
            else:
                messages.error(request, 'Category name is required.')
                return redirect('authentication:useradmin')

        
        elif 'add_product' in request.POST:
            # Handle product addition
            product_name = request.POST.get('product_name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            stock = request.POST.get('stock')
            category_id = request.POST.get('category')
            image = request.FILES.get('image')
            if product_name and price:
                category = Category.objects.get(id=category_id)
                Product.objects.create(
                    product_name=product_name,
                    description=description,
                    price=price,
                    stock=stock,
                    category=category,
                    images=image
                )
            messages.success(request, 'Product successfully added!')
            return redirect('authentication:useradmin')
        
        elif 'add_subcategory' in request.POST:
            
            subcat_name = request.POST.get('subcat_name')
            category_id = request.POST.get('category')
            
            parent_category = get_object_or_404(Category, id=category_id)
            
            SubCategory.objects.create( subcat_name = subcat_name, parent_category = parent_category)
            messages.success(request, 'Subcategory successfully added!')
            return redirect('authentication:useradmin')


    else:
        
        categories = Category.objects.all()
        subcategory = SubCategory.objects.all()

        category_dict = {}

        for category in categories:
            
            category_subcategories = subcategories.filter(category=category)
            
            subcategory_list = [sub.subcccccccccccccccccccccccccccccccccccccccccccccccat_name for sub in category_subcategories]
            
            # Add the category and its subcategories to the dictionary
            category_dict[category.cat_name] = subcategory_list

        # `category_dict` now contains category names as keys and lists of subcategory names as values

        
            print(category_dict)
        
        context =  { 'categories': categories, 'subcategory': subcategory }
        
        return render(request, 'useradmin.html', context)
        
        



categories = Category.objects.all()
subcategories = SubCategory.objects.all()

# Create a dictionary to hold categories and their subcategories
category_dict = defaultdict(list)

# Populate the dictionary
for subcategory in subcategories:
    # Append the subcategory to the list of its parent category
    category_dict[subcategory.category].append(subcategory)

# Convert defaultdict to a regular dictionary if needed
category_dict = dict(category_dict)
