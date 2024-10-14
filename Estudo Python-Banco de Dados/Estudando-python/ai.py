import google.generativeai as genai
import os
import dotenv

dotenv.load_dotenv()


pergunta = input('Digite sua pergunta: ')

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content(pergunta)
print(response.text)