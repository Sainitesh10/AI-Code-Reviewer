import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class CodeReviewer:
    def __init__(self):
        # We use Gemini 1.5 Pro as it's excellent for coding tasks and has a huge context window
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.2, # Low temperature for more deterministic/factual analysis
            convert_system_message_to_human=True # Required for some older LangChain setups, but safe to include
        )
        
        self.system_prompt = """
        You are a Senior Software Engineer acting as a Code Review Assistant.
        Your task is to review the provided code snippet written in {language}.
        
        Please provide your review structured in Markdown format with the following exact headers:
        
        ## 🐛 Bug Detection
        Identify any syntax errors, logical bugs, edge cases, or unhandled exceptions. If there are no bugs, explicitly state "No bugs detected."
        
        ## 🧠 Code Explanation
        Briefly explain what this code does in plain English.
        
        ## 🚀 Optimizations & Best Practices
        Suggest ways to improve the time/space complexity, refactor the code for better readability, and mention any security vulnerabilities (like SQL injection).
        
        Code to review:
        ```{language}
        {code}
        ```
        """
        
        self.prompt_template = ChatPromptTemplate.from_template(self.system_prompt)
        
        # We create a simple chain: Prompt -> LLM -> String Output
        self.chain = self.prompt_template | self.llm | StrOutputParser()

    def review_code(self, code: str, language: str) -> str:
        """
        Takes the source code and language, passes it to the LLM, 
        and returns the structured markdown review.
        """
        if not code.strip():
            return "Please provide some code to review."
            
        try:
            # Execute the LangChain chain
            response = self.chain.invoke({
                "code": code,
                "language": language
            })
            return response
        except Exception as e:
            return f"**Error during analysis:** {str(e)}\n\nMake sure your GOOGLE_API_KEY is correctly set in the .env file."
