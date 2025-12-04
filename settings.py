from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح السر (لازم يُغيّر في الإنتاج)
SECRET_KEY = 'django-insecure-m@&_w6s15q(a2hmp(f#fbak-)&2io%58=2+_4a9&g1z^#6wd)!'

DEBUG = True

ALLOWED_HOSTS = []

# --------------------------------------------------
# 📌 التطبيقات المثبّتة (مع إضافة تطبيقات المشروع)
# --------------------------------------------------

INSTALLED_APPS = [
    # تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'core',
    'students',
    'teachers',
    'schedule',
    'exit_requests',
    'display_board',
    'dashboard',
    'notifications',
]

# --------------------------------------------------
# 📌 الـ Middleware
# --------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'smartexitboard.urls'

# --------------------------------------------------
# 📌 إعدادات القوالب (Templates)
# --------------------------------------------------
# هنا ربطنا Django بمجلد templates العام
# الذي يحتوي مجلدات: core-templates / students-templates / ...الخ

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',   # <--- التعريف الصحيح لمجلد القوالب
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'smartexitboard.wsgi.application'

# --------------------------------------------------
# 📌 قاعدة البيانات
# --------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --------------------------------------------------
# 📌 التحقق من كلمات المرور
# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------------------------
# 📌 إعدادات اللغة والمنطقة الزمنية
# --------------------------------------------------

LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# 📁 الملفات الثابتة (Static Files)
# --------------------------------------------------

STATIC_URL = 'static/'
STATICFILES_DIRS = []
STATIC_ROOT = BASE_DIR / "staticfiles"

# --------------------------------------------------
# 📌 الإعداد الافتراضي لمعرّف الحقول
# --------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"
