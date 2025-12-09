from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # لوحة إدارة Django
    path('admin/', admin.site.urls),

    # ==============================
    # 🌐 روابط التطبيقات
    # ==============================
    path('', include('core.urls')),               # الصفحة الرئيسية
    path('students/', include('students.urls')),  # إدارة الطالبات + API
    path('teachers/', include('teachers.urls')),  # المعلمات
    path('schedule/', include('schedule.urls')),  # جدول الحصص
    path('exit/', include('exit_requests.urls')), # الاستئذانات
    path('display/', include('display_board.urls')),  # شاشة العرض
    path('dashboard/', include('dashboard.urls')),    # لوحة التحكم
    path('notify/', include('notifications.urls')),   # الإشعارات / واتساب
]

# ==============================
# 📁 دعم ملفات STATIC + MEDIA أثناء التطوير
# ==============================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
