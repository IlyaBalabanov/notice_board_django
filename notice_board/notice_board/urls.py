from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from notice_board import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user_auth.urls')),
    path('', include('board.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]