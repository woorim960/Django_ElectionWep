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
]
