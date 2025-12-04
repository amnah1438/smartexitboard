from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # روابط التطبيقات (عندما نضيف views لاحقًا سنربطها هنا)
    path('', include('core.urls')),              # الصفحة الرئيسية
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('schedule/', include('schedule.urls')),
    path('exit/', include('exit_requests.urls')),
    path('display/', include('display_board.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('notify/', include('notifications.urls')),
]

# ------------------------------------------------------
# 📁 دعم ملفات static و media أثناء التطوير (Development)
# ------------------------------------------------------

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
