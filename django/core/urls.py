from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator
from blog.swagger_schema import blog_swagger_paths  # Import custom paths
from football.swagger_schema import football_swagger_paths  # Import custom paths

# Custom Schema Generator
class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        # Generate the base schema
        schema = super().get_schema(request, public)

        # Merge custom paths into the schema
        if not schema.get('paths'):
            schema['paths'] = {}
        schema['paths'].update(blog_swagger_paths)  # Add blog paths
        schema['paths'].update(football_swagger_paths)  # Add football paths

        return schema

# Define Swagger schema info
swagger_info = openapi.Info(
    title="Multi-App API",
    default_version='v1',
    description="API for blog and football apps",
)

# Define URL patterns for the apps
app_patterns = [
    path('blog/', include('blog.urls')),  # Include blog app URLs
    path('football/', include('football.urls')),  # Include football app URLs
]

# Swagger schema view with custom generator
schema_view = get_schema_view(
    swagger_info,
    public=True,
    generator_class=CustomSchemaGenerator,  # Use the custom schema generator
)

urlpatterns = [
    path('admin/', admin.site.urls),
    *app_patterns,  # Include the app URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc UI
]