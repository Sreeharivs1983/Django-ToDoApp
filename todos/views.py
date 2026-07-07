from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TodoForm
from .models import Todo


def todo_list(request):
    filter_status = request.GET.get("filter", "all")
    todos = Todo.objects.all()

    if filter_status == "active":
        todos = todos.filter(completed=False)
    elif filter_status == "completed":
        todos = todos.filter(completed=True)

    total = Todo.objects.count()
    active_count = Todo.objects.filter(completed=False).count()
    completed_count = total - active_count

    context = {
        "todos": todos,
        "form": TodoForm(),
        "filter": filter_status,
        "total": total,
        "active_count": active_count,
        "completed_count": completed_count,
    }
    return render(request, "todos/list.html", context)


def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully.")
            return redirect("todo_list")
        messages.error(request, "Please fix the errors below.")
        return render(
            request,
            "todos/list.html",
            {
                "todos": Todo.objects.all(),
                "form": form,
                "filter": "all",
                "total": Todo.objects.count(),
                "active_count": Todo.objects.filter(completed=False).count(),
                "completed_count": Todo.objects.filter(completed=True).count(),
            },
        )
    return redirect("todo_list")


def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully.")
            return redirect("todo_list")
    else:
        form = TodoForm(instance=todo)
    return render(request, "todos/edit.html", {"form": form, "todo": todo})


@require_POST
def todo_toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    status = "completed" if todo.completed else "marked as active"
    messages.success(request, f'"{todo.title}" {status}.')
    return redirect("todo_list")


@require_POST
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    title = todo.title
    todo.delete()
    messages.success(request, f'"{title}" deleted.')
    return redirect("todo_list")


@require_POST
def todo_clear_completed(request):
    count, _ = Todo.objects.filter(completed=True).delete()
    if count:
        messages.success(request, f"Cleared {count} completed task(s).")
    else:
        messages.info(request, "No completed tasks to clear.")
    return redirect("todo_list")
