from django.db.models import Count
from django.shortcuts import render,redirect,reverse
from .forms import QuizForm,QuestionForm
from .models import Question,Quiz
from account.models import Teacher 


# Create your views here.

def index(request):
    quizzes = Quiz.objects.all()
    context = {
        'quizzes' : quizzes
    }
    return render(request,'index.html',context)

def create_info(request):
    form = QuizForm()
    context = {
        'form' : form
    }
    return render(request,'create_info.html',context)


def create(request):
    if request.method == 'POST':
        quiz_id = request.POST['object']
        instance = Quiz.objects.get(id=quiz_id)
        form = QuestionForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.quiz = instance
            temp.save()
        count = Question.objects.filter(quiz=instance).aggregate(Count('question_text'))['question_text__count'] + 1
        if count != instance.total_marks :
            context = {
                'quiz' : quiz_id,
                'form' : QuestionForm()
            }
        else:
            context = {
                'last' : True,
                'quiz' : quiz_id,
                'form' : QuestionForm
            }
        return render(request,'create.html',context)

    else:
        topic = request.GET['topic']
        total_marks = request.GET['total_marks']
        teacher = Teacher.objects.get(email=request.user)
        quiz = Quiz.objects.create(topic=topic,total_marks=total_marks,teacher=teacher)
        form = QuestionForm()
        context = {
            'form' : form,
            'quiz' : quiz.id
        }
        return render(request,'create.html',context)

def delete(request,quiz_id):
    Quiz.objects.filter(id=quiz_id).delete()
    return redirect(request.META['HTTP_REFERER'])


def display(request,quiz_id):
    questions = Question.objects.filter(quiz=quiz_id)
    context = {
        'questions' : questions
    }
    return render(request,'display.html',context)

def update(request,question_id):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        question = Question.objects.get(id=question_id)
        if form.is_valid():
            question.question_text = form.cleaned_data['question_text']
            question.choice1 = form.cleaned_data['choice1']
            question.choice2 = form.cleaned_data['choice2']
            question.choice3 = form.cleaned_data['choice3']
            question.choice4 = form.cleaned_data['choice4']
            question.correct_choice = form.cleaned_data['correct_choice']
            question.save()
        return redirect(reverse('index'))

    else:
        question = Question.objects.get(id=question_id)
        form = QuestionForm(instance=question)
        context = {
            'form' : form,
            'question' : question
        }
        return render(request,'update.html',context)
