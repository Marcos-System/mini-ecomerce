from django.urls import path
from ecomerce.views import *
from django.conf.urls.static import static
from django.conf import settings
app_name = 'ecomerce'

urlpatterns = [
    path('', home, name='home'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)