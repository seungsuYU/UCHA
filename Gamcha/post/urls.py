from django.urls import path
from . import  views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)