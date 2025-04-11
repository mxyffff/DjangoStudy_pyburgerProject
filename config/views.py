# from django.http import HttpResponse
#
# def main(request):
#     return HttpResponse("안녕하세요, pyburger입니다")
#
# def burger_list(request):
#     return HttpResponse("pyburger의 햄버거 목록입니다")
from django.shortcuts import render # render 함수를 import
from burgers.models import Burger


def main(request):
    return render(request, "main.html") #HttpResponse 대신 render 함수 사용

def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄부기 목록:", burgers)

    # Template으로 전달해줄 dict 객체
    context = {
        "burgers" : burgers, # burgers 키에 burgers 변수(QuerySet 객체)를 전달한다
    }
    # render 함수의 마지막 인수로 딕셔너리 객체인 context 전달
    return render(request, "burger_list.html", context) #HttpResponse 대신 render 함수 사용

def burger_search(request):
    # request.GET에서 "keyword" 키의 값을 가져와 출력
    keyword = request.GET.get("keyword")

    # 이름(name 속성)에 전달받은 키워드 값이 포함된 Burger를 검색한다
    burgers = Burger.objects.filter(name__contains=keyword)

    context = { "burgers": burgers }
    return render(request, "burger_search.html", context)