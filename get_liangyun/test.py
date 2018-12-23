#!/usr/bin/env python
# -*- coding:utf-8 -*-
import get_liangyun.get_cookies
import get_liangyun.mysql_update
import datetime
from tqdm import tqdm

liangyun_data = {
    "yipushe": ["http://e.ailiangyun.com/aspx/machine/yipushe.aspx?", {
        "page": "1",
        "limit": "90",
        "field": "d_no",
        "order": "desc",
        "keyword": "",
        "province": "",
        "city": "",
        "district": "",
        "cat_id": "",
        "mp_id": "",
        "run_state": "",
        "pushetime_begin": "",
        "pushetime_end": "",
        "seller": "",
        "builer": "",
        "finished": "",
    }],
    "machine": ["http://e.ailiangyun.com/aspx/machine/machine_data.aspx?", {"machine_id": 1040,
                                                                            "date_begin": 2018 - 11 - 26,
                                                                            "date_end": 2018 - 12 - 14,
                                                                            "_": 1544768469698, }],
    "shop": ["http://e.ailiangyun.com/aspx/machine/shop_list.aspx?", {"keyword": ""}],
}

database_name = ["d_no", "d_id", "d_shop_name", "d_area", "d_address", "d_shop_contact", "d_shop_tel", "d_buildtime",
                 "seller", "shop_sence", "d_version_id"]

# 获取总记录数量
count = get_liangyun.get_cookies.get_liangyun_data(liangyun_data["yipushe"][0], **liangyun_data["yipushe"][1])['count']

print(count)
# 循环获取页码
for arg in tqdm(range(1, int(count) // int(liangyun_data["yipushe"][1]["limit"]) + 2)):
    # 给参数赋值页码
    liangyun_data["yipushe"][1]["page"] = arg
    # 获取一页记录
    data = get_liangyun.get_cookies.get_liangyun_data(liangyun_data["yipushe"][0], **liangyun_data["yipushe"][1])[
        'data']
    # 循环每一页记录
    for record in tqdm(data):
        # print(record)
        temp_list = []
        # 以数据表列名为获取每一页的记录字典的key值
        for key in database_name:
            temp_list.append(record[key])
        # 如果店名为“预铺设”就不用获取区域名称
        if temp_list[2] != "预铺设":
            # 从临时列表中取到店名名称
            liangyun_data["shop"][1]["keyword"] = temp_list[2]
            # 以店铺名称为参数获取区域名称
            d_area = \
                get_liangyun.get_cookies.get_liangyun_data(liangyun_data["shop"][0], **liangyun_data["shop"][1])[
                    "data"][0][
                    "shop_area"]

            temp_list[3] = d_area
            # 写入数据库
            get_liangyun.mysql_update.shop(tuple(temp_list))

            # 查询这台设备的粉丝数据
            now_time = datetime.datetime.now().date()
            # 更新URL参数：设备ID，起始日期
            liangyun_data["machine"][1]['machine_id'] = temp_list[1]
            liangyun_data["machine"][1]['date_begin'] = temp_list[7]
            liangyun_data["machine"][1]['date_end'] = now_time
            # 请求数据
            data2 = get_liangyun.get_cookies.get_liangyun_data(liangyun_data["machine"][0],
                                                               **liangyun_data["machine"][1])
            # print(data2['time'])
            temp_data = []
            totalday = data2['totalday']
            print(totalday)
            # print(totalday)
            for i in range(totalday):
                temp_data.append(temp_list[1])
                temp_data.append(data2['fans'][i])
                temp_data.append(data2['show'][i])
                temp_data.append(data2['time'][i])
                temp_data.append(data2['used'][i])
                get_liangyun.mysql_update.machine(tuple(temp_data))
                temp_data.clear()
