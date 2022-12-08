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
    DisciplinaViewSet,
    ConteudoViewSet,
    AlternativaViewSet,
    PerguntaViewSet,
    FormularioViewSet,
)

router = DefaultRouter()
router.register(r"disciplinas", DisciplinaViewSet)
router.register(r"counteudos", ConteudoViewSet)
router.register(r"alternativas", AlternativaViewSet)
router.register(r"perguntas", PerguntaViewSet)
router.register(r"formularios", FormularioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Auth
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    # Api
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
