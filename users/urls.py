from django.urls import path

from . import views

urlpatterns = [
    # path('index/', views.index, name='index'),
    path('create/', views.create_question, name='create'),
    path('retrieve/', views.retrieve_question, name="retrieve"),
    path('update/', views.update_question, name="update"),
    path('delete/', views.delete_question, name="delete"),
    path('choice_create/', views.create_choice, name="choice"),
    path('retrieve_choice/', views.retrieve_choice, name="retrieve_choice"),
    path('update_choice/', views.update_choice, name="update_choice"),
    path('delete_choice/', views.delete_choice, name="delete_choice"),
]
