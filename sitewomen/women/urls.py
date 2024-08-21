from django.urls import path, re_path, register_converter, include
from . import views
from . import converters

from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'women', views.WomenViewSet)


register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.WomenHome.as_view(), name='home'),  # http://127.0.0.1:8000
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/women/', views.WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', views.WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', views.WomenAPIDestroy.as_view()),
    # path('api/v1/', include(router.urls)),
    # path('api/v1/womenlist/', views.WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', views.WomenViewSet.as_view({'put': 'update'})),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.TagPostList.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
    path('delete/<int:pk>/', views.DeletePage.as_view(), name='delete_page'),
]
