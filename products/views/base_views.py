from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from django.http import HttpResponse
import re

from ..models import Products, Images


def index(request):
    """
    product 목록 출력
    """
    # 입력 인자
    # page = request.GET.get('page', '1')  # 페이지
    # kw = request.GET.get('kw', '')       # 검색어
    # so = request.GET.get('so', 'recent')  # 정렬 기준

    # # 정렬
    # if so == 'recommend':
    #     question_list = Question.objects.annotate(
    #         num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    # elif so == 'popular':
    #     question_list = Question.objects.annotate(
    #         num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    # else:  # recent
    #     question_list = Question.objects.order_by('-create_date')

    # 조 회
    # if kw:
    #     question_list = question_list.filter(
    #         Q(subject__icontains=kw) |                  # 제목 검색
    #         Q(content__icontains=kw) |                  # 내용 검색
    #         Q(author__username__icontains=kw) |         # 질문 글쓴이 검색
    #         Q(answer__author__username__icontains=kw)   # 답변 글쓴이 검색
    #     ).distinct()

    # 페이징 처리
    # paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    # page_obj = paginator.get_page(page)

    # context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    # return HttpResponse("Product Page!!!!!!!!!")
    product_list = Products.objects.order_by('-upload_date')
    context = {'product_list': product_list}
    return render(request, 'products/product_list.html', context)


def detail(request, product_id):
    """
    pybo 내용 출력
    """
    product_size = []
    product = get_object_or_404(Products, pk=product_id)
    size = product.product_size.split()
    for i in range(len(size)):
        product_size += re.findall(r'\d+', size[i])

    context = {'product': product, 'product_size': product_size}
    return render(request, 'products/product_detail.html', context)
