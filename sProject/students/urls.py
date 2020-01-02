from django.urls import path
from . import views


app_name = 'students'
urlpatterns = [
    path('reg/', views.regStudent, name = 'reg'),
    path('regCon/', views.regConStudent, name = 'regCon'),
    path('all/', views.reaStudentAll, name = 'stuAll'),
    path('<str:name>/detail/', views.detailStudent, name = 'stuDetail'),
    path('<str:name>/modify/', views.modifyStudentOne, name = 'stuModify'),
    path('modifyCon/', views.modifyConStudent, name = 'modifyCon'),
    path('<str:name>/delete/', views.delConStudent, name = 'stuDel'),
    path('login/', views.login, name = 'login'),
    path('user/', views.user, name = 'user'),
    path('userAll/', views.userAll, name = 'userAll'),
    path('<str:name>/userDelete/', views.userDel, name = 'userDel'),
    path('main/', views.main, name='name'),
    

]
