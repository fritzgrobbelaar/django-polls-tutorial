from django.urls import __path__
from . import views
from django.urls import path

app_name='blog'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.reader,name='reader'),
    path('postnew',views.postnew,name='postnew'),
    path('submit',views.submit,name='submit'),
]