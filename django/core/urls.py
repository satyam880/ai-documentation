from django.contrib import admin
from django.urls import path, include
from .swagger_conf import schema_view


# Define URL patterns for the apps
app_patterns = [
    path('blog/', include('blog.urls')),  
    path('football/', include('football.urls')), 
]



urlpatterns = [
    path('admin/', admin.site.urls),
    *app_patterns,  
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc UI
]