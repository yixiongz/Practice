# 多表 操作

学校 school

老师 teacher


mysql> insert into app01_school (name) values ("中海小学"),("南京大学")

mysql> insert into app01_school (name) values ("天海中学"),("南开大学");


mysql> desc app01_school;
+-------+-------------+------+-----+---------+----------------+

| Field | Type        | Null | Key | Default | Extra          |

+-------+-------------+------+-----+---------+----------------+

| id    | int(11)     | NO   | PRI | NULL    | auto_increment |

| name  | varchar(30) | NO   |     | NULL    |                |

+-------+-------------+------+-----+---------+----------------+

2 rows in set (0.00 sec)



mysql> insert into app01_teacher (name, sid_id) values ("xiong","1"),("yu","4");

mysql> desc app01_teacher;
+--------+-------------+------+-----+---------+----------------+

| Field  | Type        | Null | Key | Default | Extra          |

+--------+-------------+------+-----+---------+----------------+

| id     | int(11)     | NO   | PRI | NULL    | auto_increment |

| name   | varchar(30) | NO   | UNI | NULL    |                |

| sid_id | int(11)     | NO   | MUL | NULL    |                |

+--------+-------------+------+-----+---------+----------------+

3 rows in set (0.00 sec)



应用app01 views.py中配置函数


项目文件中修改  urls.py文件
