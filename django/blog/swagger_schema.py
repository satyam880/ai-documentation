# blog/swagger_schema.py
from drf_yasg import openapi

blog_swagger_info = openapi.Info(
    title="Blog API",
    default_version='v1',
    description="API for managing blog posts and comments",
)

blog_swagger_paths = {
    "/blog/post/": {
        "get": {
            "summary": "Returns a blog post",
            "responses": {
                200: {
                    "description": "A JSON object containing a blog post",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "message": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        }
    },
    "/blog/comment/": {
        "get": {
            "summary": "Returns a blog comment",
            "responses": {
                200: {
                    "description": "A JSON object containing a blog comment",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "message": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        }
    }
}