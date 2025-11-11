from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),  # 👈 new
    path('add-animal/', views.add_animal_view, name='add_animal'),
    path('add-vaccination/', views.add_vaccination_view, name='add_vaccination'),
    path('animal/<int:id>/edit/', views.edit_animal_view, name='edit_animal'),
    path('animal/<int:id>/delete/', views.delete_animal_view, name='delete_animal'),
    path('vaccination/<int:id>/edit/', views.edit_vaccination_view, name='edit_vaccination'),
path('vaccination/<int:id>/delete/', views.delete_vaccination_view, name='delete_vaccination'),


]
