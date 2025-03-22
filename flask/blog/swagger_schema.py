# blog/swagger_schema.py
blog_swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Blog API",
        "description": "API for managing blog posts and comments",
        "version": "1.0.0"
    },
    "paths": {
        "/blog/post": {
            "get": {
                "summary": "Returns a blog post",
                "responses": {
                    "200": {
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
        "/blog/comment": {
            "get": {
                "summary": "Returns a blog comment",
                "responses": {
                    "200": {
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
}