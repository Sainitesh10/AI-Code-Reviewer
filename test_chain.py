import os
from dotenv import load_dotenv
from core.reviewer import CodeReviewer

load_dotenv()
try:
    reviewer = CodeReviewer()
    print("Reviewer initialized.")
    res = reviewer.review_code("print('hello')", "Python")
    print(res)
except Exception as e:
    print("ERROR:", e)
