from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),

]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)