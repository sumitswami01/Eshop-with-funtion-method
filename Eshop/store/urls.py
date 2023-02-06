from django.urls import path
from .import views
from django.conf.urls.static import static
from Eshop import settings

urlpatterns = [
    path('home/', views.index, name = 'home_url'),
    path('signup/', views.signup, name='signup_url'),
    path('login/', views.login, name='login_url')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)