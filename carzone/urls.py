from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('cars/', include('cars.urls')),
   
    path('marbles/', include('marbles.urls')),
    path('marblecontacts/', include('marblecontacts.urls')),    

    path('tiles/', include('tiles.urls')),
    path('tilecontacts/', include('tilecontacts.urls')),    
    
    path('store/', include('store.urls')),

    path('accounts/', include('accounts.urls')),
    path('socialaccounts/', include('allauth.urls')),
    path('contacts/', include('contacts.urls')),

    path('cements/', include('cements.urls')),
    path('cementcontacts/', include('cementcontacts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
