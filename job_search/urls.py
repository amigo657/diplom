from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('vacancy/', include("vacancy.urls")),
    path('about_us/', include("about_us.urls")),
    path('pricing/', include("privilegy.urls")),
    path('user/', include("accounts.urls")),
]