import openai
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Obter a chave da API da variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

def fazer_pergunta():
    pergunta = input("Digite sua pergunta: ")

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",  # Atualizado para um modelo suportado
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": pergunta}
            ],
            max_tokens=100
        )
        print("Resposta da IA: ", resposta['choices'][0]['message']['content'].strip())

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Executar a função
fazer_pergunta()
