import pymysql
import get_liangyun.get_cookies
import datetime


def warps(func):
    def inner(data):
        db = pymysql.connect("localhost", "root", "Qzbnx1314.", "test_table")
        try:
            with db.cursor() as cursor:
                sql = func()
                info = cursor.execute(sql % data)
            db.commit()
            print("插入成功！")
        except pymysql.err.IntegrityError:
            print("\033[1;31m %s\033[0m语句引起数据库的关系完整性时引发异常!" % sql)
            db.rollback()
        finally:
            db.close()

    return inner


@warps
def shop():
    sql = "INSERT INTO `test_table`.`table_name`(`d_no`, `d_id`, `d_shop_name`, `d_area`, `d_address`, `d_shop_contact`, `d_shop_tel`, `d_buildtime`, `seller`, `shop_sence`, `d_version_id`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s','%s')"
    return sql


@warps
def machine():
    sql = "INSERT INTO `liangyun`.`liangyun_app_machine`(`machine_id`, `fans`, `show`, `time`, `used`) VALUES ('%s', '%s', '%s', '%s', '%s')"
    return sql


ata = ['027D', 1153, '巴南区新民街上口奇缘茶饮', '重庆巴南区城区', '巴南区新民街上口后巷口121-1奇缘茶饮', '陈', '17318487591', '2018-12-12 16:11:11',
       '唐孝益', '其他', '19']
ata = tuple(ata)
shop(ata)

# data1 = [
#     ['027D', 1153, '巴南区新民街上口奇缘茶饮', '重庆巴南区城区', '巴南区新民街上口后巷口121-1奇缘茶饮', '陈', '17318487591', '2018-12-12 16:11:11', '唐孝益',
#      '其他', '19'],
#     ['026E', 1157, '铜梁区通天大药房中兴东路店', '重庆铜梁区县城内', '重庆市铜梁区东城街道办事处中兴东路319号附1号', '李晓丽', '13452880633', '2018-12-15 12:21:47',
#      '谢金龙', '药房', '19'],
#     ['026B', 1099, '桐君阁长寿40店', '重庆长寿区城区', '重庆市长寿区桃源南路2号宝润国际', '冯小莉', '40664220', '2018-12-13 14:49:45', '郑志辉', '药房',
#      '19'],
#     ['0267', 1128, '重庆药客药房连锁有限公司下石门店', '重庆江北区内环以内', '江北区下石门619号1幢8号门面（海通店，可坐113,202至下石门齐祥灯饰站下）', '施思', '67107867',
#      '2018-12-08 10:56:27', '蒲雪锋', '药房', '19'],
#     ['0265', 1093, '桐君阁长寿43店', '重庆长寿区城区', '重庆市长寿区凤城桃花大道22号', '彭瑶', '40664225', '2018-12-13 12:11:58', '郑志辉', '药房',
#      '19'], ['0263', 1091, '体重秤测试', '重庆渝中区全境', '公司', '公司', '公司', '2018-11-30 11:23:48', '高晓刚', '其他', '19']]
#
# a = [['4', 'd', 'e'], ['5', 'd', 'e'], ['6', 'd', 'e'], ['7', 'd', 'e']]
# # machine(a)
# liangyun_data = {
#     "yipushe": ["http://e.ailiangyun.com/aspx/machine/yipushe.aspx?", {
#         "page": "1",
#         "limit": "90",
#         "field": "d_no",
#         "order": "desc",
#         "keyword": "",
#         "province": "",
#         "city": "",
#         "district": "",
#         "cat_id": "",
#         "mp_id": "",
#         "run_state": "",
#         "pushetime_begin": "",
#         "pushetime_end": "",
#         "seller": "",
#         "builer": "",
#         "finished": "",
#     }],
#     "machine": ["http://e.ailiangyun.com/aspx/machine/machine_data.aspx?", {"machine_id": 1040,
#                                                                             "date_begin": 2018 - 11 - 26,
#                                                                             "date_end": 2018 - 12 - 14,
#                                                                             "_": 1544768469698, }],
#     "shop": ["http://e.ailiangyun.com/aspx/machine/shop_list.aspx?", {"keyword": ""}],
# }
#
# # datetimea = time.strptime(data1[0][7],"%Y-%m-%d")
# """
# INSERT INTO `liangyun`.`liangyun_app_machine`(`ID`, `machine_id`, `fans`, `show`, `time`, `used`) VALUES (NULL, NULL, NULL, NULL, NULL, NULL);
# """
# # 循环遍历所有设备
# for arg in data1:
#     # 获取当前时间
#     now_time = datetime.datetime.now().date()
#     # 更新URL参数：设备ID，起始日期
#     liangyun_data["machine"][1]['machine_id'] = arg[1]
#     liangyun_data["machine"][1]['date_begin'] = arg[7]
#     liangyun_data["machine"][1]['date_end'] = now_time
#     # 请求数据
#     data2 = get_liangyun.get_cookies.get_liangyun_data(liangyun_data["machine"][0], **liangyun_data["machine"][1])
#     print(data2['time'])
#     temp_data = []
#     totalday = data2['totalday']
#     print(totalday)
#     for i in range(totalday):
#         temp_data.append(arg[1])
#         temp_data.append(data2['fans'][i])
#         temp_data.append(data2['show'][i])
#         temp_data.append(data2['time'][i])
#         temp_data.append(data2['used'][i])
#         machine(tuple(temp_data))
#         temp_data.clear()
