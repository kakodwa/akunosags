from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



admin.site.index_title= 'Akunosags Site Administration - For Support call/Wap 0993344416(Isaac Kakodwa)'
admin.site.site_header = 'Akunosags Administration'
admin.site.site_title = "Akunosags Admin Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] 

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)