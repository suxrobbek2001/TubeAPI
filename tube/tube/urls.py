from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authtoken.views import obtain_auth_token

from tubeapp.views import MijozLC, MijozRUD, PlaylistLC, PlaylistRUD, VideoLC, VideoD, CommentLC, CommentD


schema_view = get_schema_view(
   openapi.Info(
      title="Youtube clone API",
      default_version='v1',
      description="Youtube clone versiyasi",
      contact=openapi.Contact("Sukhrobbek Mukhammadjonov <surobbekmuxammadjonov2gmail.com>, <+998993930242>"),
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mijoz/', MijozLC.as_view()),
    path('mijoz/<int:pk>/', MijozRUD.as_view()),
    path('playlist/', PlaylistLC.as_view()),
    path('playlist/<int:pk>/', PlaylistRUD.as_view()),
    path('video/', VideoLC.as_view()),
    path('video/<int:pk>/', VideoD.as_view()),
    path('comment/', CommentLC.as_view()),
    path('comment/<int:pk>/', CommentD.as_view()),


    path('docs/', schema_view.with_ui("swagger", cache_timeout=0), name="swagger-doc"),
    path('doc/', schema_view.with_ui("redoc", cache_timeout=0), name="redoc-doc"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
