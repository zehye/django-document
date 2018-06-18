from django.db import models

__all__ = (
    'TwitterUser',
    'Relation',
)


class TwitterUser(models.Model):
    """
    User간의 관계는 2종류로 나뉨
    follow
    block

    관계를 나타내는 Relation클래스 사용(중계모델)
    """
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
    )

    def __str__(self):
        return self.name


class Relation(models.Model):
    """
    TwitterUser간의 MTM관계를 정의
        from_user
        to_user
        follow인지, block인지
    """

    CHOICES_RELATION_TYPE = (
        ('f', 'Follow'),
        ('b', 'Block'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_from_user',
    )

    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_to_user'
    )

    # 입력값을 제한하는 choices옵션 추가
    relation_type = models.CharField(
        max_length=1,
        choices=CHOICES_RELATION_TYPE,
    )

    # 관계의 생성일을 기록
    # 이 클래스에 새로운 레코드가 하나 생기는 순간 그 시간을 저장(맨처음 생길때에만 저장하는 옵션 = auto_now_add)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # get_FOO_display() 함수를 사용해서 choices를 사용한 필드의 출력값을 사용
        return 'from({}), to({}), {}'.format(
            self.from_user.name,
            self.to_user.name,
            # 무슨 관계인지
            self.get_relation_type_display(),
        )


