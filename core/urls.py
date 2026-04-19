from django.urls import path
from . import views

urlpatterns = [
    path('', views.step_s),
    path('c/', views.step_c),
    path('o/', views.step_o),
    path('r/', views.step_r),
    path('e/', views.step_e),
    path('report/<int:session_id>/', views.report),
]