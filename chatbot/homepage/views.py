from django.shortcuts import render
from django.http import JsonResponse
import requests
# Create your views here.
user_questions = []
bot_answer = []

def home(request):
    # # Replace with your OpenRouter API key
    # API_KEY = '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'
    # API_URL = 'https://openrouter.ai/api/v1/chat/completions'

    # # Define the headers for the API request
    # headers = {
    #     'Authorization': f'Bearer {API_KEY}',
    #     'Content-Type': 'application/json'
    # }

    # # Define the request payload (data)
    # data = {
    #     "model": "deepseek/deepseek-chat:free",
    #     "messages": [{"role": "user", "content": "What is the meaning of life?"}]
    # }

    # # Send the POST request to the DeepSeek API
    # response = requests.post(API_URL, json=data, headers=headers)

    # # Check if the request was successful
    # if response.status_code == 200:
    #     print("API Response:", response.json())
    # else:
    #     print("Failed to fetch data from API. Status Code:", response.status_code)
    return render(request,'homepage/home.html',{'user':user_questions,'bot':bot_answer})
def getAnswer(request):
    return render(request)