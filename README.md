# 多表 操作

学校 school

老师 teacher


mysql> insert into app01_school (name) values ("中海小学"),("南京大学")

mysql> insert into app01_school (name) values ("天海中学"),("南开大学");


mysql> insert into app01_teacher (name, sid_id) values ("xiong","1"),("yu","4");




应用app01 views.py中配置函数


项目文件中修改  urls.py文件
