import os 
import openai
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)  

@app.get("/")
def read_root():
  USER_MESSAGE = input("Enter the URL: ")
  SYSTEM_MESSAGE = "You are a helpful assistant that summarizes the content of a webpage. Summarize and elaborate on the web page by finding central arguments. Then, list out supporting evidences the article uses. Do not contain information that are not in the web page. Be as specific as possible. "

  completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": SYSTEM_MESSAGE},
          {"role": "user", "content": USER_MESSAGE},
      ],
  )

  summary = completion.choices[0].message.content
  return summary