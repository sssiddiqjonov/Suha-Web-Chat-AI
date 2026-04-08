import requests
import os
from django.conf import settings
from groq import Groq

GROQ_AI_API_KEY = getattr(settings, "GROQ_API_KEY", os.getenv("GROQ_API_KEY"))
client = Groq(api_key=GROQ_AI_API_KEY)

def get_chatbot_response(user_input):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama-3.1-8b-instant", 
    )
    
    return chat_completion.choices[0].message.content

