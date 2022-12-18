#基本信息入库方法
import pymysql
def admin_regist(aid,keyword,post):
    info=[aid,keyword,post]
    db=pymysql.connect(host="localhost",user="root",passwd="020629",database="stp")
    cursor=db.cursor()
    sql="""
    INSERT INTO admin(aid,keyword,post)
    VALUES (%s,%s,%s)
    """
    cursor.execute(sql,info)
    db.commit()# 修改数据的SQL语句必须手动提交！
    db.close()

def user_regist(uid,keyword,username,tel,account):
    info=[uid,keyword,username,tel,account]
    db=pymysql.connect(host="localhost",user="root",passwd="020629",database="stp")
    cursor=db.cursor()
    sql="""
    INSERT INTO user(uid,keyword,username,tel,account)
    VALUES (%s,%s,%s,%s,%s)
    """
    cursor.execute(sql,info)
    db.commit()
    db.close()

def good_regist(gid,gname,price,type,left_num,uid):
    info=[gid,gname,price,type,left_num,uid]
    db=pymysql.connect(host="localhost",user="root",passwd="020629",database="stp")
    cursor=db.cursor()
    sql="""
    INSERT INTO good(gid,gname,price,type,left_num,uid)
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    cursor.execute(sql,info)
    db.commit()
    db.close()

def trade_regist(uid1,uid2,gid,num):
    info=[uid1,uid2,gid,num]
    db=pymysql.connect(host="localhost",user="root",passwd="020629",database="stp")
    cursor=db.cursor()
    sql="""
    INSERT INTO trade(uid1,uid2,gid,num)
    VALUES (%s,%s,%s,%s)
    """
    cursor.execute(sql,info)
    db.commit()
    db.close()


# user_regist(0,'000000','test_name','12345678901','12345678901234567890')
# good_regist(1,'test_good_name','1.00','food',50,13)
# trade_regist(0,1,0,5)