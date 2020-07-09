# coding=utf-8 
"""
@Time    : 2020/07/08  下午 14:42
@Author  : wangqn
@FileName: database.py
@IDE     : PyCharm
"""
import pymysql
from common.readConfig import confParam


class dataBase:
    def __init__(self, db):
        self.host = confParam("host")
        self.user = confParam("user")
        self.password = confParam("password")
        self.db = db
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                  db=self.db, port=3306, charset="utf8")
        self.cur = self.con.cursor()


    # def getId(self, col_name, table_name, project_name, key):
    #     sql = "Select {} from {} where {} ='{}'".format(col_name, table_name,project_name, key)
    #     self.cur.execute(sql)
    #     return self.cur.fetchall()[0][0]

    def update_power(self, table_name, f_uid):
        sql = "UPDATE {} SET f_power=60 where f_uid ={}".format(table_name, f_uid)
        self.cur.execute(sql)
        self.con.commit()

    def update_money(self, table_name, f_uid):
         sql = "UPDATE {} SET f_total=50 where f_uid ={}".format(table_name, f_uid)
         self.cur.execute(sql)
         self.con.commit()


    def delete_money_list(self, table_name, f_uid):
         sql = "DELETE  FROM {}  where f_thing='draw_money_newbie_05' and f_uid ={}".format(table_name, f_uid)
         self.cur.execute(sql)
         self.con.commit()

    # def delete_role_id(self, role_name):
    #     role_id = self.getId("role_id", "t_auth_role", "role_name", role_name)
    #     self.delete("t_auth_data_auth_role", "role_id", role_id)
    #     self.delete("t_auth_permission_role", "role_id", role_id)
    #     self.delete("t_auth_role", "role_id", role_id)
    #
    # def delete_carModel_carId(self):
    #     self.delete("t_info_car_model", "brand_name", "比亚迪OFO")
    #     self.delete("t_info_car_brand", "brand_name", "比亚迪OFO")
    #     self.delete("t_info_car_basic", "car_no", "豫G123G67G")
    #
    # def delete_user(self, user_name):
    #     self.delete("t_basic_sys_user", "user_name", user_name)
    #
    # def getSumAmount(self, sql):
    #     self.cur.execute(sql)
    #     return self.cur.fetchall()[0][0]

    def closeDb(self):
        self.cur.close()
        self.con.close()


if __name__ == "__main__":
    dbName = confParam('db')
    db = dataBase(dbName)
    db.update_power("t_user_power", 12805)
    db.update_money("t_user_money", 12805)
    db.delete_money_list("t_user_status", 12805)
    db.closeDb()

