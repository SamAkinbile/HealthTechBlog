from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Contact
from .forms import ContactForm, NewsletterForm, PostForm
from .models import NewsletterSubscription
from django.contrib import messages
from django.utils.text import slugify


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
                "liked": liked
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
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            # Generate slug from title
            post.slug = slugify(post.title)
            
            # Ensure slug is unique
            original_slug = post.slug
            counter = 1
            while Post.objects.filter(slug=post.slug).exists():
                post.slug = f"{original_slug}-{counter}"
                counter += 1

            # Save the post after ensuring unique slug
            post.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})




 # Ensure only the superuser can edit
    if not request.user.is_superuser:
        return redirect(reverse('post_detail', kwargs={'slug': slug}))  # Redirect if not allowed

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('post_detail', kwargs={'slug': post.slug}))  # Redirect to updated post
    else:
        form = PostForm(instance=post)  # Load existing data

    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})

def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if not request.user.is_superuser:
        return redirect(reverse('post_detail', kwargs={'slug': slug}))

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('post_detail', kwargs={'slug': post.slug}))
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})


# Delete Post
@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        return redirect('post_list')

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

# newletter and contact us
def newsletter_subscription(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subscribed to newsletter successfully!")
            return redirect('welcome')  # Change to your desired redirect URL
    else:
        form = NewsletterForm()
    return render(request, 'blog/newsletter_subscription.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('welcome')  
    else:
        form = ContactForm()
    return render(request, 'blog/contact_form.html', {'form': form})


def welcome(request):
    return render(request, 'welcome.html')

def blog_home(request):
    return render(request, 'blog/post_detail')


