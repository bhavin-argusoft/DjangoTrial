from django.shortcuts import render
from guest.forms import GuestForm
from guest.models import Guest
from django.shortcuts import render, redirect  

def guest_detail(request, pk):

    guest_obj = Guest.objects.get(pk=pk)
    context = {
        "guest": guest_obj,
    }
    return render(request, "guest_detail.html", context)

def add(request):  
    if request.method == "POST":  
        form = GuestForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = GuestForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    guests = Guest.objects.all()  
    return render(request,"show.html",{'guests':guests})  

def edit(request, id):  
    guest = Guest.objects.get(id=id)  
    form = GuestForm(request.POST or None, instance = guest)  
    if form.is_valid():  
        form.save()  
        return redirect("/") 

    print(form) 
    return render(request, 'edit.html', {'guest': guest, 'form' : form}) 


def destroy(request, id):  
    guests = Guest.objects.get(id=id)  
    guests.delete()  
    return redirect("/")  