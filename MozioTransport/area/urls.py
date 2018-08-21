from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from area import views

urlpatterns = [
    path('', views.AreaList.as_view(), name="areas-list"),
    path('<int:pk>/', views.AreaDetail.as_view(), name="areas-detail"),
    re_path(r'(?P<lati>\d+\.\d+)/(?P<lngi>\d+\.\d+)/$', views.AreaListCoord.as_view(), name="areas-coords"),
]

urlpatterns = format_suffix_patterns(urlpatterns)