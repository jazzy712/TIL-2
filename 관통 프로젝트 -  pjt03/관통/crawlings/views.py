from django.shortcuts import render, redirect
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from webdriver_manager.chrome import ChromeDriverManager
from .toss_crawler import crawl_toss_discussion
from .models import Comment
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options


# Create your views here.
def index(request):
    if request.method == "POST":
        keyword = request.POST.get("company_name")
        
        # 종목명, 종목코드, 댓글 리스트를 받아옴
        company_name, stock_code, comments = crawl_toss_discussion(keyword)

        Comment.objects.all().delete()
        
        # DB에 저장
        for comment_text in comments:
            Comment.objects.create(
                company_name=company_name,
                stock_code=stock_code,
                comments=comment_text,
            )
        return redirect('crawlings:index')

    else:
        all_comments = Comment.objects.all()
        if all_comments.exists():
            latest_comment = all_comments.first()
            company_name = latest_comment.company_name
            stock_code = latest_comment.stock_code
        else:
            company_name = ""
            stock_code = ""

        context = {
            "company_name": company_name,
            "stock_code": stock_code,
            "comments": all_comments,
        }

        return render(request, 'crawlings/stock_finder.html', context)



def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect('crawlings:index')