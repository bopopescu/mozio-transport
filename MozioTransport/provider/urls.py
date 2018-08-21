from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from provider import views

urlpatterns = [
    path('', views.ProviderList.as_view(), name="providers-list"),
    path('<int:pk>/', views.ProviderDetail.as_view(), name="providers-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)