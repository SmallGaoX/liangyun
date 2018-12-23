import os
import sqlite3
from win32.win32crypt import CryptUnprotectData
import requests


def get_chrome_cookies(host):
    """
    获取浏览器cookies
    :param host:
    :return: cookies
    """
    cookies_path = os.environ['LOCALAPPDATA'] + r"\Google\Chrome\User Data\Default\Cookies"
    with sqlite3.connect(cookies_path) as conn:
        sqlite = "select host_key,name,encrypted_value from cookies where host_key='%s'" % host
        cu = conn.cursor()
        for host_key, name, encrypted_valude in cu.execute(sqlite).fetchall():
            cookies = {name: CryptUnprotectData(encrypted_valude)[1].decode()}

    return cookies


def get_liangyun_data(url, host="e.ailiangyun.com", **kwargs):
    """
    使用
    :param url:
    :return:
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
    cookies = get_chrome_cookies(host)
    resp = requests.get(url, headers=headers, cookies=cookies, params=kwargs).json()
    return resp


utl = "http://e.ailiangyun.com/aspx/machine/yipushe.aspx?page=1&limit=10&field=d_yestoday_fans&order=desc&keyword=&province=&city=&district=&cat_id=&mp_id=&run_state=&pushetime_begin=&pushetime_end=&seller=&builer=&finished="

