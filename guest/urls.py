from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.guest_detail, name="guest_detail"),
    path('',views.show),  
    path('add',views.add),  
    path('edit/<int:id>', views.edit),  
    path('delete/<int:id>', views.destroy),  
]