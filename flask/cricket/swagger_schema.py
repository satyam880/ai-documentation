# cricket/swagger_schema.py
cricket_swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Cricket API",
        "description": "API for managing cricket scores and players",
        "version": "1.0.0"
    },
    "paths": {
        "/cricket/score": {
            "get": {
                "summary": "Returns the cricket score",
                "responses": {
                    "200": {
                        "description": "A JSON object containing the cricket score",
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
        "/cricket/players": {
            "get": {
                "summary": "Returns the list of cricket players",
                "responses": {
                    "200": {
                        "description": "A JSON object containing the list of cricket players",
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