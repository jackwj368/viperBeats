from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def favorites(request):
    # TODO: replace with real query & ordering
    return render(request, 'store/favorites.html', {
        # 'beats': beats
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