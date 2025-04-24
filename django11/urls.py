from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(('start_django.urls', 'start_django'), namespace='start_django')),
    re_path(r'^cart/', include(('cart.urls', 'cart'), namespace='cart')),
    re_path(r'^orders/', include(('orders.urls', 'orders'), namespace='orders')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

