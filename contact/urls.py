from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    
    # URL's for contact(CRUD)
    path('contact/<int:contact_id>/detail', views.contact, name='contact'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    path('contact/create/', views.create, name='create'),  
    
    # URL's to create contacts
    path('user/create/', views.register, name='register'),
    
    # URL to login and logout
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),
]