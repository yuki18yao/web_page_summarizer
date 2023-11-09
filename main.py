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
  SYSTEM_MESSAGE = "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text. Please avoid unnecessary details or tangential points."
  completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      #model="gpt-4",
      temperature=0,
      messages=[
          {"role": "system", "content": SYSTEM_MESSAGE},
          {"role": "user", "content": USER_MESSAGE},
      ],
  )

  summary = completion.choices[0].message.content
  return summary