from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)
    
    class Meta:
        abstract = True

class Post(BaseModel): # 방명록
    id = models.AutoField(primary_key=True) # 방명록 구분을 위한 ID
    title = models.CharField(verbose_name="제목", max_length=20)
    writer = models.CharField(verbose_name="작성자", max_length=10)
    content = models.TextField(verbose_name="내용")
    password = models.IntegerField(verbose_name="게시글 비밀번호")