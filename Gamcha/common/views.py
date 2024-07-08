# common/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import User
from django.core.mail import send_mail
from .forms import SignUpForm
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, '아이디 또는 비밀번호가 잘못되었습니다.')
        else:
            messages.error(request, '아이디 또는 비밀번호가 잘못되었습니다.')
    else:
        form = AuthenticationForm()
    return render(request, 'common/login.html', {'form': form})

def username_find(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            send_mail(
                '아이디 찾기 결과',
                f'회원님의 아이디는 {user.username}입니다.',
                'your_email@example.com',  # 보내는 이메일 주소
                [email],
                fail_silently=False,
            )
            messages.success(request, '아이디가 이메일로 전송되었습니다.')
            return redirect('common:username_find_done')
        except User.DoesNotExist:
            messages.error(request, '해당 이메일을 사용하는 사용자를 찾을 수 없습니다.')
    return render(request, 'common/username_find_form.html')

def username_find_done(request):
    return render(request, 'common/username_find_done.html')

def password_reset(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        try:
            user = User.objects.get(username=username, email=email)
            send_mail(
                '비밀번호 재설정',
                '비밀번호를 재설정하려면 다음 링크를 클릭하세요: http://example.com/reset_password',
                'your_email@example.com',  # 보내는 이메일 주소
                [email],
                fail_silently=False,
            )
            messages.success(request, '비밀번호 재설정 링크가 이메일로 전송되었습니다.')
            return redirect('common:password_reset_done')
        except User.DoesNotExist:
            messages.error(request, '해당 아이디와 이메일을 사용하는 사용자를 찾을 수 없습니다.')
    return render(request, 'common/password_reset_form.html')

def password_reset_done(request):
    return render(request, 'common/password_reset_done.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('common:signup_done')
        else:
            messages.error(request, '회원가입에 실패했습니다. 다시 시도해주세요.')
    else:
        form = SignUpForm()
    return render(request, 'common/signup.html', {'form': form})

def signup_done(request):
    return render(request, 'common/signup_done.html')
