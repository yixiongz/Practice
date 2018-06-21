from django.db import models

# Create your models here.

#  学校表
class school(models.Model):
    # id: 学校ID
    # name: 名称
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


#  老师表关连学校ID
class Teacher(models.Model):
    # ID 自增长
    id = models.AutoField(primary_key=True)
    #  老师名字不能相同
    name = models.CharField(max_length=30, unique=True, null=False)
    # 外健关连学校  它会自动关连school的主健，在数据库中的表现是 sid_id
    # 需要注意的是 配置好数据库类的时候需要 重新运行以下命令
    # python manage.py makemigrations
    # python manage.py migrate
    sid = models.ForeignKey(to="school",on_delete="CASCADE")
    # 2之后就需要加上on_delete这个参数 参考 https://www.cnblogs.com/phyger/p/8035253.html

