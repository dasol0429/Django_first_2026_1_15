from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.views import generic
from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.urls import reverse_lazy

# def index(request):
# 	latest_question_list = Question.objects.order_by("-pub_date")[:5]
# 	context = {"latest_question_list": latest_question_list}
# 	return render(request, "polls/index.html", context)

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        현재 시각보다 작거나 같은(과거 또는 현재) pub_date를 가진
        질문 5개를 최신순으로 반환합니다.
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by("-pub_date")[:5]



# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, "polls/detail.html", {"question": question})

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    context_object_name = "question"

    def get_queryset(self):
        """
        게시되지 않은(미래 날짜의) 질문은 상세 페이지에서 제외합니다.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    context_object_name = "question"

# def vote(request, question_id):
#     return HttpResponse(f"You're voting on question {question_id}.")

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message":"You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


# CRUD - Create
class QuestionCreateView(generic.CreateView):
    model = Question
    fields = ["question_text", "pub_date"]
    template_name = "polls/question_form.html"
    success_url = reverse_lazy("polls:index")

class QuestionUpdateView(generic.UpdateView):
    model = Question
    fields = ["question_text", "pub_date"]
    template_name = "polls/question_form.html"
    success_url = reverse_lazy("polls:index")

class QuestionDeleteView(generic.DeleteView):
    model = Question
    template_name = "polls/question_confirm_delete.html"
    success_url = reverse_lazy("polls:index")
 


# def aa(request):
# 	# 1. 모델에서 데이터를 모두 불러오기
# 	question_list = Question.objects.all()
# 	choice_list = Choice.objects.all()

# 	# 2. 불러온 데이터를 html에 출력하기
# 	# - 데이터 형식 [ ] { : } {} 중 딕셔너리 데이터로 받아야 한다. json 형식과 비슷하다. 같은 형식으로 만들기가 편해
# 	context = {
# 		"question_list": question_list, 
# 		"choice_list": choice_list,
# 	} # : 딕셔너리 데이터 호출 방법-> 키를 부르면 값이 나온다
# 	# 3. html에 context를 넘겨주기
# 	return render(request, "polls/aa.html", context)
