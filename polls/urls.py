from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [ 
    # FBV
    # path("", views.index, name="index"), # http://127.0.0.1:8000/polls/index
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
    
    # CBV
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

    # CRUD
    path("create/", views.QuestionCreateView.as_view(), name="question_create"),
    # http://127.0.0.1:8000/polls/create/
    # 제너릭에 CreateView 상속받아서 클래스 글 생성을 구현
    # url polls:question_create 탬플릿(html)에서 링크 형태로 호출

    path("<int:pk>/update/", views.QuestionUpdateView.as_view(), name="question_update"),
    # http://127.0.0.1:8000/polls/1/update/
    # 제너릭에 UpdateView 상속받아서 클래스 글 생성을 구현
    # url polls:question_update 탬플릿(html)에서 링크 형태로 호출


    path("<int:pk>/delete/", views.QuestionDeleteView.as_view(), name="question_delete"),
    # http://127.0.0.1:8000/polls/1/delete/
    # 제너릭에 DeleteView 상속받아서 클래스 글 생성을 구현
    # url polls:question_delete 탬플릿(html)에서 링크 형태로 호출

]