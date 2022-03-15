from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls'), name='orders'),
    path('cart/', include('cart.urls'), name='cart'),
    path('', include('shop.urls'), name='shop'),
]


if settings.DEBUG:
    # import debug_toolbar
    # urlpatterns = [
    #     path('__debug__/', include(debug_toolbar.urls)),
    # ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)