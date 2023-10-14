from django.shortcuts import render
from account.models import Account

# Create your views here.

def home_screen_view(request):

    # context = {}
    # # # passing satuan
    # # context['some_string'] = "this is some string"

    # # # passing list
    # # list_of_values = [1,2,3,4]
    # # context['list_values'] = list_of_values

    # # passing dari database
    # questions = Question.objects.all()
    # context['questions'] = questions

    context = {}

    accounts =  Account.objects.all()
    context['accounts'] = accounts

    return render(request, "personal/home.html", context)