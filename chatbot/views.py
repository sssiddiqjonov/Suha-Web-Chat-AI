from django.shortcuts import render
from .services import get_chatbot_response 
# Create your views here.

def chatbot_view(request):
    response = None

    if request.method=="POST":
        user_input = request.POST.get('user_input')
        response = get_chatbot_response(user_input)
    return render(request, 'chatbot.html', {'response':response})
