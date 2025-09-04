from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path("api/users/", include("users.urls")),
    path('admin/', admin.site.urls),
    path('api/', include('resumes.urls')),
]

schema_view = get_schema_view(
    permission_classes=[],
    public=True
)
