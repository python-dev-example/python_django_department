from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    # url(r'^auth/', include('djoser.urls.jwt')),

    path('admin/', admin.site.urls),
    path(r'api/v1/departments/', include('departments_api.urls'))
]
