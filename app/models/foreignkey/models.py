from django.db import models


class Car(models.Model):
    manufacturer = models.ForeignKey(
        # 원래는 class Manufacturer이 위에 있었는데 아래로 내려가면 참조를 하지 못한다.
        # 이때는 Manufacturer를 문자열로 설정을 하면 일단 이부분은 넘어가고
        # 실제 Manufacturer을 사용할때 아래를 참조할 수 있게 된다.
        'Manufacturer',
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=50)
    instructor = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='students',
        blank=True,
        null=True
    )
