from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('form/',views.submit_form,name='submit_form'),
    path('djangoform/',views.PasswordValidation,name='django_form'),
    path('form_practise/',views.form_practise,name='p_form')
]