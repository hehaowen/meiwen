from _sha1 import sha1

from django.shortcuts import render, redirect

# Create your views here.
from .models import UserInfo


def register(request):
    return render(request, 'user/register.html')


def reg_dle(request):
    post = request.POST
    email = post.get('email')
    nickname = post.get('nickname')
    password = post.get('password')
    old_password = post.get('old_password')
    if password == old_password:
        s1 = sha1()
        s1.update(password.encode('utf8'))
        password_hash = s1.hexdigest()

        user = UserInfo()
        user.username = nickname
        user.password = password_hash
        user.email = email
        user.save()
        return redirect('/user/login')
    else:
        return redirect('/user/register')




def login(request):
    return render(request, 'user/login.html')


def login_dle(request):
    post = request.POST
    passwords = post.get('password')
    username = post.get('nickname')
    user = UserInfo.objects.filter(username=username)
    if passwords != None:
        for use in user:
            s1 = sha1()
            s1.update(passwords.encode('utf8'))
            passwords_decode = s1.hexdigest()
            if use.password == passwords_decode:
                request.session['username'] = request.POST['nickname']
                return redirect('/')
            else:
                return redirect('/user/login')
    return redirect('/user/login')
