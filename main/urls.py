from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('gallery/', views.gallery, name='gallery'),
    path('services/', views.services, name='services'),
    path('feedback/', views.feedback, name='feedback'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('logout/', views.logout_view, name='logout'),
    path('page/create/', views.page_create, name='page_create'),
    path('page/<slug:slug>/edit/', views.page_edit, name='page_edit'),
    path('page/<slug:slug>/delete/', views.page_delete, name='page_delete'),
    path('page/<slug:slug>/', views.page_view, name='page_view'),
    path('delete-feedback/<int:pk>/', views.delete_feedback, name='delete_feedback'),
] 