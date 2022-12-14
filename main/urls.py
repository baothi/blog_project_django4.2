from django.urls import path
from main import views

urlpatterns = [
    # path("", views.blog_home, name="blog_home"),
    path('blog_detail/<str:slug_url>', views.blog_detail, name="blog_detail"),
    # path("user_profile/", views.profile, name="user_profile"),
    # path("contact_us/", views.contactUs, name="contact_us"),
    path('', views.blog_home.as_view(), name="home"),
    # path('blog_detail/<str:slug>', views.blog_detail.as_view(), name="blog_detail"),
    path('contact_us/', views.contactUs.as_view(), name="contact_us"),
    path('create_new_blog/', views.CreateBlog.as_view(), name="create-blog"),
    path('update_blog/<int:pk>/', views.UpdateBlogView.as_view(), name="UpdateBlogView"),
    path('delete_blog/<int:pk>/', views.DeleteBlogView.as_view(), name="DeleteBlogView")
]
