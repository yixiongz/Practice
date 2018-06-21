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


# 老师列表
def tlist(request):
    ret = models.Teacher.objects.all()
    return render(request, "teacher_list.html", {"teacher_list": ret})


# 添加老师以及对应学校关系
def tadd(request):
    if request.method == "POST":
        # 获取POST的值，然后更新数据库
        tname = request.POST.get("name")
        tschool = request.POST.get("school")
        models.Teacher.objects.create(name=tname, sid_id=tschool)
        return redirect("/teacher_list/")

    # 点击页面 methed = get时 将学校列表展示到增加页面中
    ret = models.school.objects.all()
    return render(request, "teacher_add.html", {"school_list": ret})


#  删除
def tdel(request):
    if request.method == "GET":
        # 获取要删除的学校ID号
        sid = request.GET.get("id")
        models.Teacher.objects.get(id=sid).delete()
    return redirect("/teacher_list/")


# 修改
def tedit(requset):

    if requset.method == "POST":
        #  以ID做为固定值，然后来进行修改
        old_sid = requset.POST.get("sid")
        #  获取修改之后新的数据
        new_tname = requset.POST.get("name")
        new_school_id = requset.POST.get("school")
        # 获取老的数据行
        new_school_tname = models.Teacher.objects.get(id=old_sid)
        # 修改
        new_school_tname.name = new_tname
        new_school_tname.sid_id = new_school_id
        new_school_tname.save()
        return redirect("/teacher_list/")

    tid = requset.GET.get("techer_id")
    # 点击修改获取的原本的值
    obj = models.Teacher.objects.get(id=tid)

    # 页面点击修改时获取 id 获取在数据库中查这个ID， 并且返回给修改页面中
    # 学校列表
    ret = models.school.objects.all()
    return render(
        requset,
        "teacher_edit.html",
        {"school_list": ret,"school_obj": obj}
    )