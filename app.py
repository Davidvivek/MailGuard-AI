from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

def get_system_prompt():
    try:
        with open('identity_check.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "You are a helpful AI assistant."
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_email():
    data = request.json
    email_content = data.get('email_text', '')

    if not email_content:
        return jsonify({"error": "No email content provided"}), 400

    try:
        # Connect to the AI Model
        model = genai.GenerativeModel('gemini-pro')
        
        # Combine user instructions with the user's email
        system_instruction = get_system_prompt()
        full_prompt = f"{system_instruction}\n\nEMAIL CONTENT:\n{email_content}"
          
        # Send to Google
        response = model.generate_content(full_prompt)
        
        # Clean up the response (remove Markdown formatting if present)
        cleaned_response = response.text.replace('```json', '').replace('```', '')
        
        return cleaned_response, 200, {'Content-Type': 'application/json'}

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- START THE SERVER ---
if __name__ == '__main__':
    app.run(debug=True)