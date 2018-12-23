from django.shortcuts import render
from liangyun_app import models
from django.db import connection
from collections import namedtuple
import datetime
import json


class CJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


# Create your views here.

def home(request):
    return render(request, "overall.html")


# 以元组的形式返回所有数据
def my_custom_sql():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT liangyun_app_machine.time, Sum( liangyun_app_machine.fans ), Sum( liangyun_app_machine.`show` ), Sum( liangyun_app_machine.used )  FROM liangyun_app_machine GROUP BY liangyun_app_machine.time ORDER BY liangyun_app_machine.time ASC")
        row = cursor.fetchall()
    return row


# 以字典的形式返回所有数据
def my_custom_sql1():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT liangyun_app_machine.time, Sum( liangyun_app_machine.fans ), Sum( liangyun_app_machine.`show` ), Sum( liangyun_app_machine.used )  FROM liangyun_app_machine GROUP BY liangyun_app_machine.time ORDER BY liangyun_app_machine.time DESC")
        # row = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def namedtuplefetchall():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT liangyun_app_machine.time, Sum( liangyun_app_machine.fans ), Sum( liangyun_app_machine.`show` ), Sum( liangyun_app_machine.used )  FROM liangyun_app_machine GROUP BY liangyun_app_machine.time ORDER BY liangyun_app_machine.time DESC")
    desc = cursor.description
    nt_reslt = namedtuple('Result', [col[0] for col in desc])
    return [nt_reslt(*row) for row in cursor.fetchall()]


def machine(request):
    all_data = my_custom_sql()
    time = []
    used = []
    show = []
    fans = []
    for lin in all_data:
        # 时间类型转换
        # time.append(datetime.date.isoformat(lin[0]))
        time.append(lin[0].strftime('%Y-%m-%d'))
        # print(datetime.date.isoformat(lin[0]))
        # time.append(lin[0])
        fans.append(int(lin[1]))
        show.append(int(lin[2]))
        used.append(int(lin[3]))
    print(time)
    # print(used)
    # print(show)
    # print(fans)
    return render(request, 'overall.html',
                  {'datatime': json.dumps(time), 'fans_data': json.dumps(fans), 'show_data': json.dumps(show),
                   'used': used})
