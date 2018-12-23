from django.db import models


# Create your models here.

class Machine(models.Model):
    ID = models.AutoField(primary_key=True)
    # 设备设备编号
    machine_id = models.IntegerField(null=False)
    # 粉丝数据
    fans = models.IntegerField(null=False)
    # 上称次数
    show = models.IntegerField(null=False)
    # 时间
    time = models.DateField(null=False)
    # 扫码
    used = models.IntegerField(null=False)


class MachineOne(models.Model):
    ID = models.AutoField(primary_key=True)
    # 设备设备编号
    machine_id = models.CharField(max_length=16, null=False, unique=True)


class TimeMachine(models.Model):
    ID = models.AutoField(primary_key=True)
    time = models.DateField(null=False, unique=False)
    machine = models.ManyToManyField(to=MachineOne)


class FansData(models.Model):
    ID = models.AutoField(primary_key=True)
    fans = models.IntegerField(null=False, unique=True)
    used = models.IntegerField(null=False, unique=True)
    show = models.IntegerField(unique=True, null=False)
    time = models.ManyToManyField(to=TimeMachine)
    machine = models.ManyToManyField(to=MachineOne)


class ShopInfo(models.Model):
    # 自增ID
    ID = models.AutoField(primary_key=True, unique=True, null=False)
    # 设备编号
    d_no = models.CharField(max_length=64, null=False, unique=True)
    # 识别编号
    d_id = models.CharField(max_length=64, null=False, unique=True)
    # 店铺名称
    d_shop_name = models.CharField(max_length=128, null=False, unique=True)
    # 区域
    d_area = models.CharField(max_length=128, null=False)
    # 店铺地址
    d_address = models.CharField(max_length=128, null=False)
    # 联系人
    d_shop_contact = models.CharField(max_length=128, null=False)
    # 联系电话
    d_shop_tel = models.CharField(max_length=128, null=False)
    # 铺设时间
    d_buildtime = models.DateField(null=False)
    # 销售人员
    seller = models.CharField(max_length=128, null=False)
    # 店铺类型
    shop_sence = models.CharField(max_length=128, null=False)
    # 设备软件版本
    d_version_id = models.CharField(max_length=64, null=False)
