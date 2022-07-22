import os
from uuid import uuid4
from django.utils import timezone


def date_upload_to(instance, filename):
    ymd_path = timezone.now().strftime('%Y/%m/%d')  # 날짜 세분화
    uuid_name = uuid4().hex  # 길이 32인 uuid값
    extension = os.path.splitext(filename)[-1].lower()  # 확장자 추출
    return '/'.join([
        ymd_path,
        uuid_name + extension,
    ])


