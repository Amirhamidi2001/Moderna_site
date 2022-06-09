from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog, name= 'blog'),
    path('<int:pid>', blog_single, name= 'single'),
    path('category/<str:cat_name>', blog, name= 'category'),
    path('author/<str:author_username>', blog, name= 'author'),
]
