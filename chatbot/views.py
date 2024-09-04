from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chitchat',read_only=False,
              logic_adapters=[
                  {
                      'import_path':'chatterbot.logic.BestMatch'
                    #   'default_response':'Sorry, i dont know what you mean',
                    #   'maxixum_similarity_threshold':0.90
                      
                      
                      }])

list_to_train = [

    "hi",
    "hi, there",
    "what's your name?",
    "I'm just a chatbot",
    "what is your fav food?",
    "I like cheese",
    "what's your fav sport",
    "swimming",
    "do you have children?",
    "No",
]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)
chatterbotCorpusTrainer.train('chatterbot.corpus.english')

# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)

def index(request):
    return render(request, 'chatbot/index.html')

def specific(request):
    return HttpResponse("list1")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)

