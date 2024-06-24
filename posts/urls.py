from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    
    path('',views.posts_list, name="list"),
    
    #slug adalah konverter jalur, untuk memberi tau django bahwa nilai yang ditangkpak harus sesuai dengan format slug
    #slug: adalah nama parameter yang akan diteruskan ke view, dalam hal ini slug dari UTL akan tersedia dalam view sebagai argumen bernama slug
    path('<slug:slug>',views.post_page, name="page"),
   
]