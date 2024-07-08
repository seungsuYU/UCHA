from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('username_find/', views.username_find, name='username_find'),
    path('username_find_done/', views.username_find_done, name='username_find_done'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('signup/', views.signup, name='signup'),
    path('signup_done/', views.signup_done, name='signup_done')
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)