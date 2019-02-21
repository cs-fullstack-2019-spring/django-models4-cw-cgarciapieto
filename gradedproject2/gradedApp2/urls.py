from django.urls import path

from . import views
# paths or outes
urlpatterns = [
    path('', views.index, name='index'),
    path('mothers/', views.mothers, name='mothers'),
    path('children/', views.children, name='children'),

]