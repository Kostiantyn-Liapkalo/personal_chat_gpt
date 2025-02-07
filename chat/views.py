from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatMessage
from .services import get_chatgpt_response
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from openai import OpenAI
from dotenv import load_dotenv
import os

@login_required
def chat_view(request):
    chat_history = ChatMessage.objects.filter(user=request.user).order_by('-timestamp')[:10]  # Останні 10 повідомлень
    if request.method == 'POST':
        user_message = request.POST.get('message')
        response = get_chatgpt_response(user_message)
        ChatMessage.objects.create(user=request.user, message=user_message, response=response)
        return render(request, 'chat/chat.html', {'response': response, 'chat_history': chat_history})

    return render(request, 'chat/chat.html', {'chat_history': chat_history})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


#
# load_dotenv()
#
# def chat_view(request):
#     #  OpenAI
#     client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#
#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": "Write a haiku about recursion in programming."}
#         ]
#     )
#
#     response = completion.choices[0].message.content
#     return render(request, 'chat/chat.html', {'response': response})
