from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import SignupForm, LoginUserForm, PasswordChangingForm, EditUserProfileForm
from django.contrib.auth import authenticate, login, logout
from main.models import Blog
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
# def signUp(request):
#   if request.method == "POST":
#     form = SignupForm(request.POST)
#     if form.is_valid():
#       form.save()
#       messages.success(request, "Your account is created successfully")
#       new_user = authenticate(
#                 username = form.cleaned_data['username'],
#                 password = form.cleaned_data['password1']
#             )
#       login(request, new_user)
#       return redirect('blog_home')
#     else:
#       messages.error(request, "Error")
#   else:
#     form = SignupForm()
#   return render(request, "authors/register.html", {'form': form})

# def logIn(request):
#   if request.method == "POST":
#     form = LoginUserForm(request, data = request.POST)
#     if form.is_valid():
#       username = form.cleaned_data.get('username')
#       password = form.cleaned_data.get('password')

#       user = authenticate(username = username, password=password)

#       if user is not None:
#         login(request, user)
#         messages.success(request, f"You are logged in as {username}")
#         return redirect('blog_home')
#       else:
#         messages.error(request, "Error")
#     else:
#       messages.error(request, "Username or password incorrect")
#   form = LoginUserForm()
#   return render(request, "authors/login.html", {"login_form": form})

# def logOut(request):
#   logout(request)
#   messages.success(request, "You have successfully logged out.")
#   return redirect('blog_home')

# def profile(request, user_name):
#   user_related_data = Blog.objects.filter(author__username = user_name)
#   context = {
#       "user_related_data": user_related_data
#   }
#   return render(request, "authors/profile.html", context)

class signUp(SuccessMessageMixin, generic.CreateView):
    form_class = SignupForm
    template_name = "authors/register.html"
    success_url = reverse_lazy('login')
    success_message = "User has been created, please login with your username and password"

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please enter details properly")
        return redirect('home')


class logIn(generic.View):
    form_class = LoginUserForm
    template_name = "authors/login.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.method == "POST":
            form = LoginUserForm(request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username = username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, f"You are logged in as {username}")
                    return redirect('home')
                else:
                    messages.error(request, "Error")
            else:
              messages.error(request, "Username or password incorrect")
        form = LoginUserForm()
        return render(request, "authors/login.html", {"form": form})


class logOut(generic.View):
  def get(self, request):
      logout(request)
      messages.success(request, "User logged out")
      return redirect('home')

class profile(generic.View):
    model = Blog
    template_name = "authors/profile.html"

    def get(self, request, user_name):
        user_related_data = Blog.objects.filter(author__username = user_name)
        context = {
            "user_related_data": user_related_data
        }
        return render(request, self.template_name, context)


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, "authors/password_change_success.html")

class UpdateUserView(SuccessMessageMixin, generic.UpdateView):
    form_class = EditUserProfileForm
    template_name = "authors/edit_user_profile.html"
    success_url = reverse_lazy('home')
    success_message = "User updated"

    def get_object(slef):
        return slef.request.user
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please submit the form carefully")
        return redirect('home')

# https://www.youtube.com/watch?v=D_KyndgwD1o&list=PLKnjLEpehhFnb210PantMg9sdQNrygxUL&index=27
# https://github.com/yash-2115/django_blog_youtube




