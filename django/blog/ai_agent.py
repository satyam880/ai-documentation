import openai
import re
import os
import json
from typing import Dict, Any
from dotenv import load_dotenv

env = load_dotenv("../../.env")
class FullContextDjangoSwaggerGenerator:
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key
        
    def generate_swagger(self, urls_content: str, views_content: str, models_content: str, serializers_content: str) -> Dict[str, Any]:
        """Generate complete Swagger docs with full Django context"""
        prompt = self._create_prompt(urls_content, views_content, models_content, serializers_content)
        response = self._get_ai_response(prompt)
        return self._parse_ai_response(response)
    
    def _create_prompt(self, urls_content: str, views_content: str, models_content: str, serializers_content: str) -> str:
        """Create detailed prompt with full Django context"""
        return f"""
        Analyze these Django files and generate comprehensive Swagger/OpenAPI documentation.
        Consider all relationships between URLs, views, serializers, and models.

        RULES:
        1. URL PATHS:
        - Use exact paths from urls.py including parameters
        - Convert path converters to Swagger formats:
          - <int:pk> → {{pk}} (integer)
          - <slug:title> → {{title}} (string)
          - <uuid:id> → {{id}} (string format: uuid)

        2. VIEWS:
        - Determine HTTP methods from view classes or @api_view
        - For APIView classes, map methods to operations (get → GET, post → POST)
        - For ViewSets, include all actions with proper decorators

        3. SERIALIZERS:
        - Use serializer fields to determine request/response schemas
        - Include field attributes like required, max_length, allow_null
        - Handle nested serializers recursively
        - For ModelSerializers, consider the model fields

        4. MODELS:
        - Use model fields to enhance serializer understanding
        - Include model relationships (ForeignKey, ManyToMany)
        - Use model Meta options if available

        5. DOCSTRINGS:
        - Use view docstrings for operation descriptions
        - Include parameter descriptions from docstrings

        6. OUTPUT:
        - Generate ONLY the paths section of Swagger
        - Include schemas for requests/responses
        - Add parameters from URLs and queries
        - Output pure JSON with no explanations

        urls.py:
        {urls_content}

        views.py:
        {views_content}

        models.py:
        {models_content}

        serializers.py:
        {serializers_content}

        Output ONLY the Swagger paths object:
        """

    def _get_ai_response(self, prompt: str) -> str:
        """Get response from OpenAI API with precise instructions"""
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a Django expert that generates perfect OpenAPI docs from Django files."
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=4000
        )
        return response.choices[0].message.content
    
    def _parse_ai_response(self, response: str) -> Dict[str, Any]:
        """Extract clean JSON from AI response"""
        try:
            json_str = re.search(r'\{.*\}', response, re.DOTALL).group()
            import json
            return json.loads(json_str)
        except Exception as e:
            return {"error": f"Response parsing failed: {str(e)}", "raw_response": response}


def main():

    API_KEY = os.getenv('OPENAI_API_KEY')

    # Define file paths relative to the script location
    base_dir = os.path.dirname(os.path.abspath(__file__))
    paths = {
        "urls": os.path.join(base_dir, "urls.py"),
        "views": os.path.join(base_dir, "views.py"),
        "models": os.path.join(base_dir, "models.py"),
        "serializers": os.path.join(base_dir, "serializers.py")
    }

    # Read file contents with validation
    def read_file(filepath):
        try:
            with open(filepath, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Warning: {filepath} not found")
            return None
        except Exception as e:
            print(f"Error reading {filepath}: {str(e)}")
            return None

    # Collect all file contents
    file_contents = {}
    for key, path in paths.items():
        content = read_file(path)
        if content is not None:
            file_contents[key] = content
        else:
            print(f"Skipping {key} due to missing file")

    # Check if we have minimum required files
    if not all(k in file_contents for k in ['urls', 'views']):
        print("Error: Missing required files (urls.py and views.py)")
        return

    # Generate Swagger documentation
    generator = FullContextDjangoSwaggerGenerator(API_KEY)
    swagger_docs = generator.generate_swagger(
        file_contents.get('urls', ''),
        file_contents.get('views', ''),
        file_contents.get('models', ''),
        file_contents.get('serializers', '')
    )

    # Output results
    if 'error' in swagger_docs:
        print("Error generating documentation:")
        print(swagger_docs['error'])
        if 'raw_response' in swagger_docs:
            print("Raw response:")
            print(swagger_docs['raw_response'])
    else:
        print("Generated Swagger Documentation:")
        print(json.dumps(swagger_docs, indent=2))
        
        # Save to file
        output_path = os.path.join(base_dir, "swagger_doc.json")
        try:
            with open(output_path, 'w') as f:
                json.dump(swagger_docs, f, indent=2)
            print(f"Saved to {output_path}")
        except Exception as e:
            print(f"Failed to save documentation: {str(e)}")
            
if __name__==main():
        main()