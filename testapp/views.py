from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect

def home_page_view(request):
    return render(request, 'home.html')

@login_required
def java_exam_view(request):
    return render(request, 'javaexam.html')

@login_required
def python_exam_view(request):
    return render(request, 'pythonexam.html')

@login_required
def aptitude_exam_view(request):
    return render(request, 'aptitudeexam.html')

def logout_view(request):
    return render(request, 'logout.html')

def SignUp_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        User=form.save()
        User.set_password(User.password)
        User.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'signup.html',{'form':form})


