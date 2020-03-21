from django.db import models

# Create your models here.
class CafeData(models.Model):
    # title = 글목록 제목
    title = models.CharField(max_length=200)
    # link = 글의 링크주소
    link = models.URLField()
    # time = 글이 올라온 시간
    time = models.TimeField()

    #django admin page title overload
    def __str__(self):
        return self.title

