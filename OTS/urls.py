from django.urls import path
from OTS.views import *

app_name='OTS'
urlpatterns = [
    path('', welcome),
    path('new-candidate',candidateRegistrationForm,name='registrationForm'),
    path('store-candidate', candidateRegistration,name='storeCandidate'),
    path('login', loginView,name='login'),
    path('home', candidateHome,name='home'),
    path('test-paper', testPaper,name='testPaper'),
    path('calculate-result', calculateTestResult),
    path('test-history', testResultHistory,name='testHistory'),
    path('result', showTestResult),
    path('logout', logoutView,name='logout'),

]