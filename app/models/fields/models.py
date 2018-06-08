from django.db import models


class Person(models.Model):
    SHIRT_SIZES = (
        # ('데이터베이스', '표시되는 것')
        # 튜플의 묶음안에 또다른 튜플, 클래스 자체의 속성에는 그 변수에는 대문자를 써도 허용이 된다
        # 모듈 차원의 변수에도 대문자를 써도된다.
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField("셔츠 사이즈", help_text="S는 작음", max_length=1, choices=SHIRT_SIZES)
    # get_FOO_display()에서 FOO는 필드 이름
