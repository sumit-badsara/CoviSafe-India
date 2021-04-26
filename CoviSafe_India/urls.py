from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('requirements/', include('Requirements.urls')),
    path('supplies/', include('Supplies.urls'))
]
