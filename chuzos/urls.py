from django.urls import path
from . import views
urlpatterns = [
    path('', views.chuzos_list_view, name="chuzos"),
    path('<int:id>/', views.chuzos_detail_view, name="chuzo"),
]
