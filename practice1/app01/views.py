from django.shortcuts import render, HttpResponse, redirect

from app01 import models
# Create your views here.

# 列出
def list(request):
    # 获取数据库中所有的值
    ret = models.school.objects.all()
    return render(request,"list.html", {"school_list": ret})


# 增加
def add(request):
    msg_error = ""
    if request.method == "POST":
        # 如果获取不到设置为空
        get_name = request.POST.get("schoolname",None)
        # 如果不为空就创建
        get_db = models.school.objects.filter(name=get_name)
        print(get_db)
        if get_name or get_db:
            models.school.objects.create(name=get_name)
            return redirect("/list/")
        else:
            msg_error = "输入为空或已存在"
    return render(request, "add.html",{"error": msg_error})


# 删除
def delete(request):
    if request.method == "GET":
        ret = request.GET.get("id")
        # 如果存在 获取并直接删除
        if ret:
            models.school.objects.get(id=ret).delete()
            return redirect("/list/")
    return HttpResponse("输入错误")


# 1、先获取要修改的ID
def change(request):
    if request.method == "GET":
        ret = request.GET.get("id")
        if ret:
            # 获取数据库的ID，得到数据行，取出name
            school_name = models.school.objects.get(id=ret)
            return render(request, "change.html", {"change_val": school_name})

    if request.method == "POST":
        post_id = request.POST.get("schoolId")
        old_name = models.school.objects.get(id=post_id)
        new_name = request.POST.get("schoolname")
        old_name.name = new_name
        old_name.save()
        return redirect("/list/")
    return HttpResponse("不存在....")

