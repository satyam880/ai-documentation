# app.py
from flask import Flask, json
from flask_swagger_ui import get_swaggerui_blueprint
from blog.view import bp_blog  # Import the blog blueprint
from cricket.view import bp_cricket  # Import the cricket blueprint
from blog.swagger_schema import blog_swagger_template  # Import blog Swagger template
from cricket.swagger_schema import cricket_swagger_template  # Import cricket Swagger template

# Create the Flask app
app = Flask(__name__)

# Register the Swagger UI blueprint
SWAGGER_URL = '/swagger'  # The URL where Swagger UI will be accessible
API_URL = '/swagger.json'  # The URL where the Swagger schema will be served

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Multi-Module API"
    }
)

# Register the Swagger UI blueprint in the Flask app
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Combine Swagger templates from all modules
def combine_swagger_templates(*templates):
    combined_template = {
        "swagger": "2.0",
        "info": {
            "title": "Multi-Module API",
            "description": "API for blog and cricket modules",
            "version": "1.0.0"
        },
        "paths": {}
    }

    # Merge paths from all templates
    for template in templates:
        if "paths" in template:
            combined_template["paths"].update(template["paths"])

    return combined_template

# Serve the combined Swagger schema at /swagger.json
@app.route('/swagger.json')
def swagger():
    combined_template = combine_swagger_templates(blog_swagger_template, cricket_swagger_template)
    return app.response_class(
        response=json.dumps(combined_template),
        status=200,
        mimetype='application/json'
    )

# Register the blueprints from each module
app.register_blueprint(bp_blog, url_prefix='/blog')
app.register_blueprint(bp_cricket, url_prefix='/cricket')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)