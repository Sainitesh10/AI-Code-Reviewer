import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class PRReviewer:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.2, # Low temperature for accurate analysis
            convert_system_message_to_human=True
        )
        
        self.system_prompt = """
        You are an expert Senior Software Engineer performing an automated Code Review on a Pull Request.
        Your task is to review the provided Git Diff. 
        
        Guidelines:
        - Lines starting with `+` are additions.
        - Lines starting with `-` are deletions.
        - Focus ONLY on the changes. Do not comment on code that hasn't changed unless it's fundamentally broken by the new changes.
        - If the diff looks good and contains no obvious issues, explicitly say so and approve the changes.
        - Be concise and professional.
        
        Please structure your review in Markdown format with the following headers (skip any headers if they don't apply):
        
        ## 🐛 Bug Detection
        Identify any syntax errors, logical bugs, edge cases, or unhandled exceptions introduced in the additions.
        
        ## 🚀 Optimizations & Best Practices
        Suggest ways to improve time/space complexity, readability, or mention any security vulnerabilities introduced.
        
        ## 💡 Overall Feedback
        A brief 1-2 sentence summary of your thoughts on the Pull Request.

        Git Diff to review:
        ```diff
        {diff}
        ```
        """
        
        self.prompt_template = ChatPromptTemplate.from_template(self.system_prompt)
        self.chain = self.prompt_template | self.llm | StrOutputParser()

    def review_diff(self, diff: str) -> str:
        """
        Takes the Git Diff string, passes it to the LLM, 
        and returns the structured markdown review.
        """
        if not diff.strip():
            return "No changes detected in the diff."
            
        try:
            response = self.chain.invoke({
                "diff": diff
            })
            return response
        except Exception as e:
            return f"**Error during automated PR analysis:** {str(e)}\n\nCheck GOOGLE_API_KEY."
