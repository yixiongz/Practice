# 数据库连接操作




应用中增加
class school(models.Model):
    # id: 学校ID
    # name: 名称
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


项目文件中修改
    # 注释这行，不让它解析
    # 'django.middleware.csrf.CsrfViewMiddleware',

# 连接数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "practice",     # 数据库名
        'PORT': 3306,
        "USER": "test",
        "PASSWORD": "test",
        "HOST": "192.168.9.224"
    }
}


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]


命令行添加应用 
python manage.py startapp appname