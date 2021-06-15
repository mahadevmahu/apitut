
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api/v1/posts/',include('api.v1.posts.urls'),name="api_v1_posts"),
    path('api/v1/auth/',include('api.v1.authentication.urls'),name="api_v1_authentication"),
    path('',include('web.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
