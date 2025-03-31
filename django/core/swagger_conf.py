from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import json
from pathlib import Path
from django.conf import settings

def load_swagger_schema():
    """Load and return the Swagger JSON schema."""
    json_path = settings.BASE_DIR / "blog" / "swagger_docs.json"
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Now use `blog_schema` (it will be a Python dict)

class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False, app_name='blog'):
        # 1. Get base schema
        schema = super().get_schema(request, public)
        
        # 2. Load custom paths
        custom_paths = load_swagger_schema()  # Your function that loads the JSON
        
        # 3. Process each path to add app prefix and tags
        processed_paths = {}
        for path, methods in custom_paths.items():
            # Add app prefix if not already present
            if not path.startswith(f'/{app_name}/'):
                new_path = f'/{app_name}{path}'
            else:
                new_path = path
            
            # Add tag to each method
            for method_data in methods.values():
                if 'tags' not in method_data:
                    method_data['tags'] = [app_name]
                elif app_name not in method_data['tags']:
                    method_data['tags'].append(app_name)
            
            processed_paths[new_path] = methods
        
        # 4. Replace paths in schema
        schema['paths'].update(processed_paths)
        
        return schema
 
 
swagger_info = openapi.Info(
    title="Multi-App API",
    default_version='v1',
    description="API for blog and football apps"
)

schema_view = get_schema_view(
    swagger_info,
    public=True,
    generator_class=CustomSchemaGenerator,  
)