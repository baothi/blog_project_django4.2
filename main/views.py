from django.shortcuts import redirect, render
from .models import Blog, BlogComment, Contact
from .forms import ContactForm, CreateBlogForm, UpdateBlogForm, CommentBlogForm
from django.contrib import messages
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


# def blog_home(request):
#     all_blogs = Blog.objects.all()
#     context = {
#         'blogs': all_blogs
#     }
#     return render(request, "main/blog_home.html", context)


def blog_detail(request, slug_url):
    blog = Blog.objects.get(slug=slug_url)
    all_comments = BlogComment.objects.filter(blog = blog.id)
    all_blogs = Blog.objects.all().order_by('-post_date')[:10]
    form = CommentBlogForm()
    if request.method == "POST":
        form = CommentBlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your comment on this blog has been posted")
            return redirect("/blog_detail/"+blog.slug)
    else:
        form = CommentBlogForm()
    context = {
        'blog':blog,
        'all_blogs': all_blogs,
        'form': form,
        'all_comments': all_comments
    }
    return render(request, "main/blog_detail.html", context)

# def profile(request):
#   return render(request,"main/profile.html")

# def contactUs(request):
#     form = ContactForm()
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "your form is submitted successfully")
#             return redirect("blog_home")
            
#     else:
#         form = ContactForm()
#         messages.success(request, "please fill the details profile")
#     return render(request, "main/contact_us.html", {"form": form})

class blog_home(generic.ListView):
    model = Blog
    template_name = "main/blog_home.html"

# class blog_detail(generic.DetailView):
#     model = Blog
#     template_name = "main/blog_detail.html"

class contactUs(SuccessMessageMixin, generic.CreateView):
    form_class = ContactForm
    template_name = "main/contact_us.html"
    success_url = "/"
    success_message = "Your query has been submited successfully, we will contact you soon."

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please submit the form carefully")
        return redirect('home')


class CreateBlog(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = CreateBlogForm
    template_name = "main/create_blog.html"
    login_url = 'login'
    success_url = "/"
    success_message = "Your blog has been created"

class UpdateBlogView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Blog
    form_class = UpdateBlogForm
    template_name = "main/update_blog.html"
    login_url = 'login'
    success_url = "/"
    success_message = "Your blog has been updated"

class DeleteBlogView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Blog
    template_name = "main/delete_blog.html"
    login_url = 'login'
    success_url = "/"
    success_message = "Your blog has been deleted"




