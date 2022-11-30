"""Success_Student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import (
    ConteudoViewSet,
    FormularioViewSet,
    MidiaViewSet,
    PerguntaViewSet,
    RespostaViewSet,
)
from media.router import router as media_router

router = DefaultRouter()
router.register(r"resposta", RespostaViewSet)
router.register(r"pergunta", PerguntaViewSet)
router.register(r"formulario", FormularioViewSet)
router.register(r"conteudo", ConteudoViewSet)
router.register(r"midia", MidiaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Auth
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    # Api
    path("api/media/", include(media_router.urls)),
    path("api/", include(router.urls)),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)