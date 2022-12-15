from django.urls import path, include
from . import views


app_name = 'shop'

bucket_urls = [
	path('', views.BucketHome.as_view(), name='bucket'),
	path('delete_obj/<str:key>/', views.DeleteBucketObject.as_view(), name='delete_obj_bucket'),
    path('download_obj/<str:key>/', views.DownloadBucketObject.as_view(), name='download_obj_bucket'),
]

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('favorites/', views.FavouriteView.as_view(), name='favorites'),
    path('favorites/<int:product_id>/', views.AddFavouriteView.as_view(), name='add_favorites'),
    path('search/', views.SearchView.as_view(), name="search"),
    path('bucket/', include(bucket_urls)),
    path('products/<slug:slug>/', views.DetailView.as_view(), name='detail'),
    path('category/<slug:category_slug>/', views.CategoryView.as_view(), name='category_filter'),
]
