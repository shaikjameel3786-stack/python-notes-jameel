from django.contrib import admin
from django.urls import path, include
from . import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('mrcetapp/', include('mrcetapp.urls')),

]
