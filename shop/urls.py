"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main import views
from main.views import ProductViewSet, TypeViewSet, CommentViewSet

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static

# from django.conf.urls import static
# from django.urls import re_path as url
# from django.urls import re_path
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title='My API',
        description='API of shoping app',
        default_version='v1'
    ),
    public=True
)

router = DefaultRouter()
router.register('details', ProductViewSet)
router.register('edit', ProductViewSet)
router.register('types', TypeViewSet)
router.register('comment', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('v1/account/', include('account.urls')),
    path('docs/', schema_view.with_ui('swagger')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('rest_framework_social_oauth2.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)