import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env from the project root (one level up from the backend folder)
current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(os.path.dirname(current_dir), ".env")
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print(f"Warning: GEMINI_API_KEY not found. Checked .env at: {env_path}")

genai.configure(api_key=api_key)

def get_ai_explanation(language, code):
    prompt = (
        "You are an expert software engineer. "
        f"Analyze this {language} code snippet.\n"
        "Provide the output in the following format:\n"
        "### 1. 🪜 Step-by-Step Explanation\nProvide a detailed walkthrough of how the code executes line by line.\n\n"
        "### 2. ⏳ Time and Space Complexity\nAnalyze the performance using Big O notation.\n\n"
        "### 3. 🚀 Suggested Improvements\nRecommendations for better code quality, performance, or security.\n\n"
        f"Code:\n{code}"
    )
    try:
        # Dynamically discover models available to this API key
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        preferred_order = [
            'models/gemini-1.5-flash', 
            'models/gemini-1.5-pro', 
            'models/gemini-pro',
            'gemini-1.5-flash',
            'gemini-pro'
        ]
        
        models_to_try = [m for m in preferred_order if m in available_models or m.replace('models/', '') in available_models]
        
        if not models_to_try and available_models:
            models_to_try = [available_models[0]]

        for model_name in models_to_try:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(prompt)
                return response.text
            except Exception:
                continue
        
        if not available_models:
            return "AI Error: No models available for this API key. Ensure the Gemini API is enabled in your Google Cloud Project."
            
        return f"AI Error: Failed to generate content using available models: {', '.join(models_to_try)}"

    except Exception as e:
        return f"AI Error: {str(e)}"
