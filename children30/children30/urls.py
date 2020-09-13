
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from teachers.views import CourseListView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('pupils/', include('pupils.urls')),
    path('teachers/', include('teachers.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
