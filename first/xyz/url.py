from rest_framework import routers
from .views import ViewSet, users_detail
from django.urls import path,include



router = routers.DefaultRouter()

router.register('user',ViewSet, base_name='texts')

urlpatterns = [
    path('',include(router.urls))
    
    #path("users/<int:id>/",users_detail,name ="users_detail"),

]
