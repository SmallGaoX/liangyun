import pymysql


def warps(func):
    def inner(data):
        db = pymysql.connect("localhost", "root", "Qzbnx1314.", "liangyun")
        try:
            with db.cursor() as cursor:
                sql = func()
                cursor.execute(sql % data)
                cursor.execute("select version()")
                # if sql == shop:
                #     print("%s插入成功"%data[2])
                # else:
                #     print("%s插入成功"%data[0])
                # Version_info = cursor.fetchall()
                # print("Database Version:%s" % Version_info)
            db.commit()
        except pymysql.err.IntegrityError:
            # print("\033[1;31m %s\033[0m语句引起数据库的关系完整性时引发异常!" % sql)
            db.rollback()
        finally:
            db.close()

    return inner


@warps
def shop():
    sql = "INSERT INTO `liangyun`.`liangyun_app_shopinfo`(`d_no`, `d_id`, `d_shop_name`, `d_area`, `d_address`, " \
          "`d_shop_contact`, `d_shop_tel`, `d_buildtime`, `seller`, `shop_sence`, `d_version_id`) " \
          "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
    return sql


@warps
def machine():
    sql = "INSERT INTO `liangyun`.`liangyun_app_machine`(`machine_id`, `fans`, `show`, `time`, `used`) VALUES ('%s', '%s', '%s', '%s', '%s')"
    return sql

#
# data = ['027D', 1153, '巴南区新民街上口奇缘茶饮', '重庆巴南区城区', '巴南区新民街上口后巷口121-1奇缘茶饮', '陈', '17318487591', '2018-12-12', '唐孝益',
#         '其他', '19']
#
# shop(tuple(data))
