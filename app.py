# app.py


import base64
import logging
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.config import get_config
from src.model import solve_captcha

load_dotenv() # Loads vars from .env

# Basic logging
logging.basicConfig(level=logging.INFO)

def create_app():
    app = Flask(__name__, static_folder='src/static', static_url_path='/static')
    app.config.from_object(get_config)
    CORS(app, resources={r"/api/*": {"origins": app.config["ALLOWED_ORIGINS"]}})

    @app.route("/")
    def index():
        return jsonify({"message": "Hello, World!"})
    
    @app.route('/api/solve', methods=['POST'])
    def solve_captcha_api():
        # Inside a try block for mutation handling
        try:
            # Get the JSON
            data = request.get_json()
        
            if not data or 'image' not in data:
                return jsonify({"error": "No image data provided"}), 400

            base64_str = data['image']
        
            # Decode Base64
            image_bytes = base64.b64decode(base64_str)
            solution = solve_captcha(image_bytes)

            if solution:
                capitalized_solution = solution.upper() # Solution is always in Uppercase
                return jsonify({"solution": capitalized_solution}), 200
            else:
                return jsonify({"error": "Failed to solve CAPTCHA"}), 500

        except Exception:
            return jsonify({"error": "Internal server error"}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=app.config["PORT"], debug=True)
