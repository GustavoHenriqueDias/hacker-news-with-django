
from django.contrib import admin
from django.urls import path, include

from core.views import signup
from story.views import frontpage, search, submit, newest, vote, story

from django.contrib.auth import views 


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('newest/', newest, name='newest'),
    path('s/<int:story_id/vote>', vote, name='vote'),
    path('s/<int:story_id>', story, name='story'),
    path('u/', include('userprofile.urls')), 
    path('submit/', submit, name='submit'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('search/', search, name='search'),
]
