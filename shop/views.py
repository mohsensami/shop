from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product, Category
from orders.forms import CartAddForm
from .tasks import all_bucket_objects_task
from . import tasks
from django.contrib import messages
from utils import IsAdminUserMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        categories = Category.objects.filter(is_sub=False)
        return render(request, 'shop/home.html', {'products':products, 'categories':categories})


class DetailView(View):
    def get(self, request, slug):
        form = CartAddForm()
        product = Product.objects.get(slug=slug)
        is_favourite = False
    
        if product.favourites.filter(id=request.user.id).exists():
            is_favourite = True
        return render(request, 'shop/detail.html', {'product': product, 'form': form, 'is_favourite': is_favourite})


class CategoryView(View):
    def get(self, request, category_slug):

        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category)
        return render(request, 'shop/category.html', {'category' : category, 'products': products})


class BucketHome(IsAdminUserMixin, View):
	template_name = 'shop/bucket.html'

	def get(self, request):
		objects = all_bucket_objects_task()
		return render(request, self.template_name, {'objects':objects})


class DeleteBucketObject(IsAdminUserMixin, View):
	def get(self, request, key):
		tasks.delete_object_task.delay(key)
		messages.success(request, 'your object will be delete soon.', 'info')
		return redirect('shop:bucket')


class DownloadBucketObject(IsAdminUserMixin, View):
	def get(self, request, key):
		tasks.download_object_task.delay(key)
		messages.success(request, 'your download will start soon.', 'info')
		return redirect('shop:bucket')


class SearchView(View):
    def get(self, request):
        if request.GET.get('search'):
            products = Product.objects.filter(name__icontains = request.GET['search'])
            search = self.request.GET.get('search')
            return render(request, 'shop/search.html', {'products': products, 'search': search})
        return redirect('shop:home' )


class FavouriteView(LoginRequiredMixin, View):
    def get(self, request):
        user=request.user
        favourite_products = user.favourites.all()
        return render(request, 'shop/favorites.html', {'favourite_products': favourite_products})


class AddFavouriteView(LoginRequiredMixin, View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        if product.favourites.filter(id=request.user.id):
            product.favourites.remove(request.user)
        else:
            product.favourites.add(request.user)
            
        return redirect('shop:favorites' )