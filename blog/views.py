from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm


from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Quiz, Question, PossibleAnswer, UserResponse
from .forms import QuizForm

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
                "comment_form": CommentForm()

            },
        )
class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))   

@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            for question in questions:
                selected_answer_id = form.cleaned_data[f'question_{question.id}']
                selected_answer = get_object_or_404(PossibleAnswer, pk=selected_answer_id)
                correct = selected_answer.is_correct

                UserResponse.objects.create(
                    user=request.user,
                    quiz=quiz,
                    question=question,
                    selected_answer=selected_answer,
                    correct=correct
                )

            return HttpResponseRedirect(reverse('quiz_result', args=[quiz.id]))

    else:
        form = QuizForm(questions=questions)

    return render(request, 'take_quiz.html', {'quiz': quiz, 'form': form})

@login_required
def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    user_responses = UserResponse.objects.filter(user=request.user, quiz=quiz)

    correct_answers = user_responses.filter(correct=True).count()
    total_questions = quiz.questions.count()

    context = {
        'quiz': quiz,
        'correct_answers': correct_answers,
        'total_questions': total_questions,
        'user_responses': user_responses
    }

    return render(request, 'quiz_result.html', context)
