from django.urls import path, include
from rest_framework.routers import DefaultRouter 
# 장고 레스트 프레임워크는 라우터를 통해 url을 전달함
from . import views  
appname ='post'

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)), # 실제로 url을 작성하게 하는 것 
]
