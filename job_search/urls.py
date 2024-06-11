from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('vacancy/', include("vacancy.urls")),
    path('about_us/', include("about_us.urls")),
    path('pricing/', include("privilegy.urls")),
    path('user/', include("accounts.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)