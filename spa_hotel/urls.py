from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/logout/', logout_view, name='logout'),  #  кастомный выход
    path('accounts/', include('django.contrib.auth.urls')),  # остальное из auth
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
