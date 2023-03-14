from django.shortcuts import render

# Create your views here.

def condition(request):
    d={'a':100,'b':200}
    return render(request,'condition.html',context=d)

def ifelse(request):
    d={'a':10,'b':30}
    return render(request,'ifelse.html',context=d)

def ifelifelse(request):
    d={'a':20,'b':30,'c':45}
    return render(request,'ifelifelse.html',context=d)

def nestedif(request):
    d={'a':20,'b':30,'c':50}
    return render(request,'nestedif.html',context=d)




def looping(request):
    d={'name':'siri'}
    return render(request,'looping.html',context=d)



