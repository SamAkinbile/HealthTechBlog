from .models import Comment, Question, PossibleAnswer
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)

        for question in questions:
            choices = [(answer.id, answer.text) for answer in question.possible_answers.all()]
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.text,
                choices=choices,
                widget=forms.RadioSelect,
                required=True
            )
