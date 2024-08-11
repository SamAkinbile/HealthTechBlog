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
        for i, question in enumerate(questions):
            self.fields[f'question_{i}'] = forms.ChoiceField(
                label=question.text,
                choices=[
                    (1, question.option1),
                    (2, question.option2),
                    (3, question.option3),
                    (4, question.option4),
                ],
                widget=forms.RadioSelect,
                required=True
            )