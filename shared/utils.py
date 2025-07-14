import os
import google.generativeai as genai
#from dotenv import load_dotenv

#load_dotenv()
genai.configure(api_key="AIzaSyDpP8HI8SdZ0APj5HcAQMvtyI2ECFwqso8")

def generate_text(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
