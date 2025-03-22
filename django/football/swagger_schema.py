# football/swagger_schema.py
from drf_yasg import openapi

football_swagger_info = openapi.Info(
    title="football API",
    default_version='v1',
    description="API for managing football scores and players",
)

football_swagger_paths = {
    "/football/score/": {
        "get": {
            "summary": "Returns the football score",
            "responses": {
                200: {
                    "description": "A JSON object containing the football score",
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
    "/football/players/": {
        "get": {
            "summary": "Returns the list of football players",
            "responses": {
                200: {
                    "description": "A JSON object containing the list of football players",
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