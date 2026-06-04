# 🚀 AI Code Review Assistant

A blazingly fast, highly responsive web application that leverages Google's Gemini 2.5 AI model to automatically review, debug, and optimize source code. Built with a lightweight Python backend and a stunning Glassmorphism UI.

**[🔴 Live Demo (Coming Soon)](#)**

<div align="center">
  <!-- TODO: Add a screenshot of your beautiful Glassmorphism UI here -->
  <img src="https://via.placeholder.com/800x450.png?text=Glassmorphism+UI+Screenshot" alt="AI Code Review Assistant" width="100%">
</div>
## ✨ Key Features
- **Intelligent Bug Detection:** Instantly identifies syntax errors, logical bugs, and edge cases in your code.
- **Deep Explanations:** Provides plain-English breakdowns of complex logic.
- **Optimization Suggestions:** Recommends refactoring strategies, time/space complexity improvements, and security best practices.
- **Glassmorphism UI:** A bespoke, dark-mode frosted glass interface featuring smooth micro-animations.
- **Real-Time Markdown Rendering:** Elegantly renders the AI's markdown response directly in the browser with syntax highlighting.

## 🛠️ Tech Stack
- **Backend:** FastAPI, Python, Uvicorn, LangChain
- **AI Model:** Google Gemini 2.5 Flash (`google-genai` SDK)
- **Frontend:** Vanilla HTML, CSS (Custom Glassmorphism), JavaScript
- **Libraries:** Marked.js (Markdown parsing), Highlight.js (Code highlighting)

## ⚙️ Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sainitesh10/AI-Code-Reviewer.git
   cd AI-Code-Reviewer
   ```

2. **Install dependencies:**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Rename `.env.example` to `.env` and add your Google Gemini API key:
   ```env
   GOOGLE_API_KEY="your_api_key_here"
   ```

4. **Start the Application:**
   Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

5. **Open in Browser:**
   Navigate to [http://localhost:8000](http://localhost:8000) to use the app!

> [!WARNING]
> **Production Security Note:** The CORS middleware in `main.py` is currently set to `allow_origins=["*"]` for local development and demo purposes. Before deploying this application to a production environment (like Render or Railway), ensure you restrict the origins to your specific frontend domain.

---
*Developed by Gudala Sai Nitesh*
