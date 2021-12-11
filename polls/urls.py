from django.urls import __path__
from . import views
from django.urls import path,include

app_name='polls'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
    path('fritz/',views.fritz,name='Fritz'),
]