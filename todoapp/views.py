from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TaskForm
from .models import Todo_List

# Create your views here.




#Create and Read

def home(request):
    posts = Todo_List.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Has Been Added')
            return redirect('home')
    else:
        form = TaskForm()  # Display empty form on normal page visit
        
        
    return render(request, 'todoapp/home.html', {'form': form, 'posts': posts})

#update

def update(request, id):
    post = get_object_or_404(Todo_List, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=post)  # Fill form with existing data
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
         form = TaskForm(instance=post)
    return render(request, 'todoapp/update.html', {'form': form})

#delete

def delete(request, id):
    post = get_object_or_404(Todo_List, id=id)
    if request.method == 'POST':                    # Confirm deletion
        post.delete()
        return redirect('home')
    return render(request, 'todoapp/delete.html', {'post': post}) 





