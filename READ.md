# 🤖 AI Code Explainer

A professional AI-powered tool built with **Streamlit** and **Google Gemini** to help developers understand, optimize, and debug code snippets across multiple languages.

## 🚀 Features
- **Step-by-Step Logic**: Line-by-line walkthrough of execution.
- **Complexity Analysis**: Big O notation for time and space.
- **Optimization**: Tailored suggestions for security and performance.

## 🛠️ Local Setup
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Environment Variables**:
   Create a `.env` file and add `GEMINI_API_KEY=your_key_here`.
3. **Run**:
   ```bash
   streamlit run app.py
   ```

## 🌐 Deployment
This app is configured for **Streamlit Community Cloud**. 
Ensure that the `GEMINI_API_KEY` is added to the application secrets in the Streamlit dashboard.
