from django.db import models

# Create your models here.
class Comment(models.Model):
    # 회사 이름
    company_name = models.TextField()
    # 종목 코드
    stock_code = models.TextField()
    # 댓글 내용
    comments = models.TextField()
    # 저장 일자
    save_datetime = models.DateTimeField(auto_now_add=True)
    
    