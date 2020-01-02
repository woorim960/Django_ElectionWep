from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student, User

def regStudent(request):
    return render(request, 'students/registerStudent.html')

def regConStudent(request):
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']
    
    queryStr = Student(s_name=name, s_major=major, s_age=age, s_grade=grade, s_gender=gender)
    queryStr.save()
    
    return HttpResponseRedirect(reverse('students:stuAll'))

def reaStudentAll(request):
    queryStr = Student.objects.all()
    context = {'student_list' : queryStr}
    return render(request, 'students/readStudentsAll.html', context)

def detailStudent(request, name):
    queryStr = Student.objects.get(s_name=name)
    context = {'student_info' : queryStr}
    return render(request, 'students/detailStudent.html', context )

def modifyStudentOne(request, name):
    queryStr = Student.objects.get(s_name=name)
    context = {'student_info' : queryStr}
    return render(request, 'students/modifyStudentOne.html', context)

def modifyConStudent(request):
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']
    
    queryStr = Student.objects.get(s_name = name)
    queryStr.s_name = name
    queryStr.s_major = major
    queryStr.s_age = age
    queryStr.s_grade = grade
    queryStr.s_gender = gender
    
    queryStr.save()
    
    return HttpResponseRedirect(reverse('students:stuAll'))

def delConStudent(request, name):
    queryStr = Student.objects.get(s_name = name)
    queryStr.delete()
    
    return HttpResponseRedirect(reverse('students:stuAll'))

def login(request):
    return render(request, 'test/login.html')

def user(request):
    userId = request.POST['userId']
    userPw = request.POST['userPw']
    
    queryStr = User(s_userId = userId, s_userPw = userPw)
    queryStr.save()
    
    return HttpResponseRedirect(reverse('students:userAll'))

def userAll(request):
    queryStr = User.objects.all()
    context = {'user_list' : queryStr}
    return render(request, 'test/readUserAll.html', context)

def userDel(request, userId):
    queryStr = User.objects.get(s_userId = userId)
    queryStr.delete()
    
    return HttpResponseRedirect(reverse('students:userAll'))

def main(request):
    return render(request, 'test/htmlTemplates/index.html')




