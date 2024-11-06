from django.views import View
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email

from profile.models import Profile

import json

# Create your views here.
# @method_decorator(csrf_exempt, name='dispatch')
class SignUp(View):
    def get(self, request):
        return HttpResponse('[SignUp API] EndPoint is working')

    def post(self, request):
        data = json.loads(request.body)
        
        username = data.get('username')
        # email = data.get('email') # 이메일 주소
        nickname = data.get('nickname')
        password = data.get('password')
        
        if not username or not password:
            return JsonResponse({'error': '사용자명과 비밀번호를 모두 입력해주세요.'}, status=400)
        
        # try:
        #     validate_email(email)
        # except:
        #     return JsonResponse({'error': '유효한 이메일 주소를 입력해주세요.'}, status=400)
        
        # User = get_user_model()
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': '이미 존재하는 사용자명입니다.'})
        
        if Profile.objects.filter(username=nickname).exists():
            return JsonResponse({'error': '이미 존재하는 닉네임입니다.'})
        
        # if User.objects.filter(email=email).exists():
        #     return JsonResponse({'error': '이미 존재하는 이메일입니다.'})
        
        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, username=nickname, height=0, weight=0)
        
        return JsonResponse({'success': '회원가입이 완료되었습니다.'}, status=201)

# @method_decorator(csrf_exempt, name='dispatch')
class Login(View):
    def get(self, request):
        return HttpResponse('[Login API] EndPoint is working')
    
    def post(self, request):
        data = json.loads(request.body)
        
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return JsonResponse({'error': '사용자명과 비밀번호를 모두 입력해주세요.'}, status=400)
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': '로그인 성공'}, status=200)
        else:
            return JsonResponse({'error': '사용자명 또는 비밀번호가 올바르지 않습니다.'}, status=401)

# @method_decorator(csrf_exempt, name='dispatch')
class Logout(View):
    def post(self, request):
        logout(request)
        return JsonResponse({'success': '로그아웃'}, status=200)