from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from blogs.models import BlogPost, Comment
from products.models import ProductCategory


class AllBlogs(View):
    def get(self, request):
        posts = BlogPost.objects.all()
        paginator = Paginator(posts, 10)

        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render(request, 'new-blog-list.html', {'posts': posts})


class BlogPostView(View):
    def get(self, request, slug):
        bp = BlogPost.objects.get(slug=slug)
        c = Comment.objects.filter(parent=bp.id)
        bps = BlogPost.objects.all()[:10]
        return render(request, 'new-blog-post.html', {'post': bp, 'comments': c, 'bps': bps})


class ComposeBlogPost(LoginRequiredMixin, View):
    login_url = '/admin/login/'
    redirect_field_name = 'r'

    def get(self, request):
        cats = ProductCategory.objects.all()
        return render(request, 'editor.html', {'cats': cats})

    def post(self, request):
        title = request.POST['post-title']
        content = request.POST['editor1']
        author = request.user
        bp = BlogPost(title=title, content=content, author=author)
        bp.save()
        cats = ProductCategory.objects.all()
        return render(request, 'editor.html', {'success_alert': True, 'cats': cats})


class UpdateBlogPost(LoginRequiredMixin, View):
    login_url = '/admin/login/'
    redirect_field_name = 'r'

    def get(self, request, post_id):
        cats = ProductCategory.objects.all()
        post = BlogPost.objects.get(pk=post_id)
        return render(request, 'update-blog-post.html', {'cats': cats, 'post': post})

    def post(self, request, post_id):
        title = request.POST['post-title']
        content = request.POST['editor1']
        bp = BlogPost.objects.get(pk=post_id)
        bp.title = title
        bp.content = content
        bp.save(force_update=True)
        return redirect('/blogs/'+bp.slug, {'success_alert': True})


class SaveComment(View):
    def post(self, request):
        post_slug = request.POST['slug']

        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        parent = request.POST['parent']

        c = Comment(name=name, email=email, message=message, parent=parent)
        c.save()

        return redirect('/blogs/' + post_slug, {'comment_added': True})
        # return render(request, 'blog-single.html', {'comment_added': True})
