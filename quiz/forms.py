from django import forms
from .models import Quiz,Question


class QuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = ['topic','total_marks']

class QuestionForm(forms.ModelForm):
    
    OPTIONS = (
        ('1','Option 1'),
        ('2','Option 2'),
        ('3','Option 3'),
        ('4','Option 4'),

    )
    correct_choice = forms.ChoiceField(choices=OPTIONS,required=True)
    class Meta:
        model = Question
        fields = ['question_text','choice1','choice2','choice3','choice4','correct_choice']
        labels = {
            "question_text" : "Question",
            "choice1" : "Option 1",
            "choice2" : "Option 2",
            "choice3" : "Option 3",
            "choice4" : "Option 4",
            "correct_choice" : "Correct Option"
        }