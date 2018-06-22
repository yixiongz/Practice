# 多表 操作   多对多操作

学校 school

老师 teacher

学生 student






数据库表连接关系
------------------ school --------------	
id			
name		

------------------ Teacher --------------
id	
name
sid	  外键关连school	

----------------- Student ---------------
id
name
teacher	  多表连接 teacher

--------------- student2teacher ---------
id	
student_id	
teacher_id		


Django ORM 多表连接操作
teacher = models.ManyToManyField(to="Teacher")

应用修改models.py需要运行 python manage.py makemigrations



重要代码块  student.teacher.all 获取ORM对象  forloop.last： 序号最后一个
        {% for student in students_list %}

            <tr>

            <td>{{ forloop.counter }}</td>

            <td>{{ student.sname }}</td>

            <td>

                {% for students in student.teacher.all %}

                    {#  如果是最后一个那么就直接打印      #}

                    {% if forloop.last %}

                        {{ students.name }}

                    {#  如果不是最后一那就加一个逗号 ,      #}

                    {% else %}

                        {{ students.name }},

                    {% endif %}

                {% endfor %}

            </td>

             </tr>

