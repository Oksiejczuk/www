from django.shortcuts import render
from .models import Question


def question_list(request):
   questions = Question.objects.all()
   return render(request, 'polls/question_list.html', {'questions': questions})
from .models import Question
from django.shortcuts import render, get_object_or_404

def question_list(request):
   questions = Question.objects.all()
   return render(request, 'polls/question_list.html', {'questions':
questions})

def question_detail(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(request, 'polls/question_detail.html', {'question': question})
   question = get_object_or_404(Question,pk=Question_id)
def home_views(request):
   return render(request, 'home.html')