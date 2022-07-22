from django.contrib import messages, admin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import ProductPostForm
from ..models import Products, Images


def product_create(request):
    """
    Products 상품 등록
    """
    if request.method == 'POST':
        form = ProductPostForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.product_name = request.POST['product_name']
            product.product_price = request.POST['product_price']
            product.product_size = request.POST.getlist('selected_size[]')
            product.upload_date = timezone.now()
            product.save()
            product_img = Images()
            product_img.product = product
            product_img.img = request.FILES['product_thumb']
            product_img.save()
            # for img in request.FILES.getlist('imgs'):
            #     # Photo 객체를 하나 생성한다.
            #     imgs = Images()
            #     # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            #     imgs.product = imgs
            #     # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            #     imgs.image = img
            #     # 데이터베이스에 저장
            #     img.save()
            return redirect('products:index')
    else:
        form = ProductPostForm()
    context = {'form': form}
    return render(request, 'products/product_form.html', context)

