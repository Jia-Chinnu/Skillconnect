from django.urls import path
from . import views
from .views import login_view, signup  # Import your views
from .views import login_view, signup  # Import your views

urlpatterns = [

    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('documentation.html', views.documentation, name='documentation'),
    path('find_jobs/', views.find_jobs, name='find_jobs'),
    path('login.html', views.login_view, name='login'),  # Correct route
    path('digital assistance.html', views.digital_assistance, name='digital assistance'),

    path('login/', login_view, name='login'),
    path('signup.html', signup, name='signup'),

]
