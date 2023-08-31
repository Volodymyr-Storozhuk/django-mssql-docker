from django.shortcuts import render
from django.db import connection


# Create your views here.
def show_index_page(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT @@servername;")
        servername_rows = cursor.fetchall()   # получаем все строки
        # for row in rows:
        #     host_name = row
        #     print(row)
    with connection.cursor() as cursor:
        cursor.execute("SELECT @@version;")
        version_rows = cursor.fetchall()   # получаем все строки
        # server_info = rows
        # server_list = str(rows[0][0]).split('\n')
        # print(type(server_list))
        # print(server_list)
        # print(rows[0][0])
        # for row in rows:
        #     print(row)

    return render(request, 'app/index.html',
                  {
                      'HOST_NAME': servername_rows[0][0],
                      'SERVER_INFO': str(version_rows[0][0]).split('\n')
                  })
