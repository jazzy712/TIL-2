from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def index(request):
    context = {}
    
    if request.method == 'POST':
        company_name = request.POST.get('company_name', '').strip()
        
        if company_name:
            try:
                # 토스증권 검색 URL
                search_url = f'https://tossinvest.com/search?keyword={company_name}'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                
                # 요청 및 HTML 파싱
                response = requests.get(search_url, headers=headers)
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # 첫 번째 검색 결과 찾기
                top_result = soup.find('span', class_='tw-1r5dc8g0 _60z0ev1 _60z0ev0')
                
                if top_result:
                    # 회사 이름 가져오기
                    company_name_result = top_result.text.strip()
                    
                    # 결과를 컨텍스트에 추가
                    context['result'] = {
                        'name': company_name_result,
                    }
                else:
                    context['no_results'] = True  # 검색 결과가 없을 경우 처리
            except Exception as e:
                context['error'] = str(e)  # 에러 메시지 처리
        else:
            context['no_results'] = True  # 입력 값이 없는 경우 처리
    
    return render(request, 'crawlings/stock_finder.html', context)
