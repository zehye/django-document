from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    # 관계가 대칭적으로 형성됨
    #   A가 B를 friends에 추가 -> B의 freinds에도 A가 추가되어있다.
    friends = models.ManyToManyField(
        'self',
    )

    def __str__(self):
        return self.name

    def show_friends(self):
        # 이한영의 친구 목록
        # - 천이수
        # - 박지혜...
        #
        print(f'{self.name}의 친구 목록')

        for friends in self.friends.all():
            print(f'- {friends.name}')
        print(f'총 {len(self.friends.all())}명입니다.')

