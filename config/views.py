# from django.http import HttpResponse
#
# def main(request):
#     return HttpResponse("안녕하세요, pyburger입니다")
#
# def burger_list(request):
#     return HttpResponse("pyburger의 햄버거 목록입니다")
from django.shortcuts import render # render 함수를 import

def main(request):
    return render(request, "main.html") #HttpResponse 대신 render 함수 사용

def burger_list(request):
    return render(request, "burger_list.html") #HttpResponse 대신 render 함수 사용