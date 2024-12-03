from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import TodoLIst, Category

def redirect_view(request):
    return redirect('/category')
def todo(request):
    todos = TodoLIst.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        if 'Add' in request.POST:
            title = request.POST('description')
            date = str(request.POST['date'])
            category = request.POST['category_select']
            content = title + '--' + date+' ' + category
            todo = TodoLIst(title=title, content=content, due_time=date,
                            category=Category.objects.get(name=category))
            todo.save()

            return redirect('/todo')

        if 'Delete' in request.POST:
            checkedlist = request.POST.getlist('checkbox')

            for i in range(len(checkedlist)):
                todo = TodoLIst.objects.filter(id=int(checkedlist[i]))
                todo.delete()

    return render(request, 'todo.html', {'todo':todos, 'categories': categories})
def category(request):
    if request.method == 'POST':
        if 'Add' in request.POST:
            name = request.POST['name']
            category = Category(name=name)
            category.save()
            return redirect('/category')
        if 'Delete' in request.POST:
            check = request.POST.getlist('check')
            for i in range(len(check)):
                try:
                    categ = Category.objects.filter(id=int(check[i]))
                    categ.delete()
                except BaseException:
                    return HttpResponse('<h1>Сначала удалите карточки с этими категориями</h1>')
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories':categories})