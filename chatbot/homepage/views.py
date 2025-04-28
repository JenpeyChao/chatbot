import os
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import JsonResponse
import requests

# Create your views here.
user_questions = []
bot_answer = []

def home(request):
    return render(request,'homepage/home.html',{'conversation':zip(user_questions,bot_answer)})

def get_answer(request):
    request.session['last_url'] = request.build_absolute_uri()
    # Replace with your OpenRouter API key
    print(request.method)
    API_KEY = ''
    question = request.POST.get('text', '')
    user_questions.append(question)
    try:
        api_key_path = os.path.join(settings.BASE_DIR, 'homepage', 'apiKey.txt')
        with open(api_key_path, 'r') as file:  # Path to your .txt file
            API_KEY = file.read().strip()
    except FileNotFoundError:
        raise print("API key file not found!")
    
    API_URL = 'https://openrouter.ai/api/v1/chat/completions'

    # Define the headers for the API request
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    # Define the request payload (data)
    data = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [{"role": "user", "content": question}]
    }
    print("Request being sent:")
    print("Headers:", headers)
    print("Data:", data)
    print("Full question:", question)
    # Send the POST request to the DeepSeek API
    response = requests.post(API_URL, json=data, headers=headers)
    response_data = response.json()
    # Check if the request was successful
    if response.status_code == 200:
        print("API Response:", response_data)
        if 'error' in response_data:
            bot_answer.append(response_data['error']['message'])
        else:
            bot_answer.append(response_data['choices'][0]['message']['content'])

    else:
        print("Failed to fetch data from API. Status Code:", response.status_code)
        bot_answer.append("Failed to fetch data from API. Status Code:", response.status_code)
    return redirect(home)

def clear(request):
    global user_questions, bot_answer
    current_url = request.build_absolute_uri()

    print(current_url)

    user_questions.clear()
    bot_answer.clear()
    return redirect(home)