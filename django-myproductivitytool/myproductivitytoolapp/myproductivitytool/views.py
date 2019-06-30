from django.shortcuts import redirect
from myproductivitytool.models import TaskList, Project
from django.http import HttpResponse
from django.template import loader


def index(request):  # the index view
    tasks = TaskList.objects.all()  # quering all tasks with the object manager
    projects = Project.objects.all()  # getting all projects with object manager
    print (projects)
    if request.method == "POST":  # checking if the request method is a POST
        if "taskAdd" in request.POST:  # checking if there is a request to add a task
            title = request.POST["description"]  # title
            date = str(request.POST["date"])  # date
            project = request.POST["project_select"]  # project
            content = title + " -- " + date + " " + project  # content
            Task = TaskList(title=title, content=content, deadline_date=date,
                            project=Project.objects.get(name=project))
            Task.save()  # saving the task
            return redirect("/")  # reloading the page
        if "taskDelete" in request.POST:  # checking if there is a request to delete a task
            checkedlist = request.POST["checkedbox"]  # checked tasks to be deleted
            for task_id in checkedlist:
                task = TaskList.objects.get(id=int(task_id))  # getting task id
                task.delete()  # deleting task

    template = loader.get_template('index.html')
    context = {"tasks": tasks, "projects": projects}
    return HttpResponse(template.render(context, request))
