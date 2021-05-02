from django.shortcuts import render, redirect
from .models import optimized_pair
from .forms import MacthForm

def index(request):
     return render(request, 'MatchBatch/home.html') 

def addnew(request):  
    if request.method == "POST":  
        form = MacthForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('matchresult/')  
            except:  
                pass 
    else:  
        form = MacthForm()  
    return render(request,'MatchBatch/index.html',{'form':form})  

def matchresult(request):  
    match = optimized_pair.objects.all()  
    return render(request,"MatchBatch/matchresult.html",{'match':match})  

def edit(request, id):  
    match = optimized_pair.objects.get(id=id)  
    return render(request,'MatchBatch/edit.html', {'match':match})

def update(request, id):  
    match = optimized_pair.objects.get(id=id)  
    form = MacthForm(request.POST, instance = match)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'MatchBatch/edit.html', {'match': match})

def destroy(request, id):  
    match = optimized_pair.objects.get(id=id)  
    match.delete()  
    return redirect("/")  
