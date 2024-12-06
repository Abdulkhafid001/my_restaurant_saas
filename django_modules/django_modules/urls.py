from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("auth/", include("naijakitchen_auth.urls")),
    path("cart/", include("cart.urls")),
    path('admin/', admin.site.urls),
    path("", include("naija_kitchen.urls")),
    # path("accounts/", include("allauth.urls") , name=""),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


