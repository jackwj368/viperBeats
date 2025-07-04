from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def favorite_list(request):
    beats = (
        Product.objects.filter(is_favorite=True)
        if hasattr(Product, "is_favorite")
        else Product.objects.all()[:12]
    )
    return render(request, "store/beat_list.html", {
        "page_title": "Shop Favorites",
        "beats": beats,
    })

def recent_list(request):
    order_field = "-created_at" if hasattr(Product, "created_at") else "-id"
    beats = Product.objects.order_by(order_field)[:20]
    return render(request, "store/beat_list.html", {
        "page_title": "Recently Added",
        "beats": beats,
    })

def shop_by_mood(request, mood):
    # TODO: filter your Product model by mood
    return render(request, 'store/shop_by_mood.html', {
        # 'beats': beats,
        # 'selected_mood': mood
    })

def shop_by_genre(request, genre):
    # TODO: filter your Product model by genre
    return render(request, 'store/shop_by_genre.html', {
        # 'beats': beats,
        # 'selected_genre': genre
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                "Your account has been created! You can now log in."
            )
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', { 'form': form })

def cart(request):
    """
    TODO: replace with real Cart logic:
      - pull cart items from session or DB
      - calculate totals, etc.
    """
    return render(request, 'store/cart.html', {
        # 'items': items,
        # 'total': total,
    })