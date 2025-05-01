import os
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.urls import reverse
from django.utils.safestring import mark_safe
import requests 

import markdown

from homepage.models import ChatInstance
# Create your views here.
user_questions = []
bot_answer = []
debug_mode = os.environ.get("DEBUG", "False") == "True"

def home(request, chat_id):
    chat = ChatInstance.objects.get(id=chat_id)
    return render(request,'homepage/home.html',{'conversation':zip(user_questions,bot_answer),'chat':chat})

def make_instance(request):
    chat = ChatInstance.objects.create()
    return redirect('home',chat_id=chat.id)

def get_answer(request,chat_id):
    #get the chat from the database
    chat = ChatInstance.objects.get(id=chat_id)

    
    #prints the method type
    request.session['last_url'] = request.build_absolute_uri()
    print(request.method)

    API_KEY = os.environ.get('OpenRouterAI')
    if not API_KEY:
        raise Exception("API key file not found!")
    
    question = request.POST.get('text', '')
    user_questions.append(question)
    
    # try:
    #     api_key_path = os.path.join(settings.BASE_DIR, 'homepage', 'apiKey.txt')
    #     with open(api_key_path, 'r') as file:  # Path to your .txt file
    #         API_KEY = file.read().strip()
    # except FileNotFoundError:
    #     raise Exception("API key file not found!")
    
    print(f"API_KEY being used: {API_KEY}")
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
    msg = {
        'user':question,
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
            msg['bot'] = (response_data['error']['message'])
        else:
            text = response_data['choices'][0]['message']['content']
            paragraphs = markdown.markdown(text)
            msg['bot'] = (mark_safe(paragraphs))

    else:
        print("Failed to fetch data from API. Status Code:", response.status_code)
        msg['bot'] = ("Failed to fetch data from API. Status Code: "+ str(response.status_code))
    
    chat.history.append(msg)
    chat.save()
    return redirect(reverse('home', kwargs={'chat_id': chat.id}))


def clear(request, chat_id):
    chat = ChatInstance.objects.get(id=chat_id)
    chat.history.clear()
    chat.save()

    return redirect(reverse('home', kwargs={'chat_id': chat.id}))