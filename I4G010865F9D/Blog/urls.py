from django.urls import path
from .views import  PostDetailView, PostListview, PostCreateView, PostDeleteView, PostUpdateView

app_name= "blog"
urlpatterns= [
	path('', PostListview.as_view(), name= "all"),
	path('create/', PostCreateView.as_view(), name= "post_create"),
	path('detail/<slug:slug>/', PostDetailView.as_view(), name= "post_detail"),
	path('delete/<slug:slug>/', PostDeleteView.as_view(), name= "post_delete"),
	path('update/<slug:slug>/', PostUpdateView.as_view(), name= "post_update"),


]
