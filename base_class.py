#建立基本类
class admin:
    """管理员"""   
    def __init__(self) -> None:
        pass
    def __init__(self,aid,keyword,post):
        self.__aid=aid          #管理员id,int PK
        self.__keyword=keyword  #密码varchar(12)
        self.__post=post        #职位varchar(12)


class user:
    """用户类"""
    def __init__(self) -> None:
        pass
    def __init__(self,uid,keyword,username,tel,account):
        self.__uid=uid          #用户id，int PK
        self.__keyword=keyword  #用户名varchar(16)
        self.__username=username#用户密码varchar(12)
        self.__tel=tel          #联系方式char(11)
        self.__account=account  #账户char(20) 待定

class good:       
    """商品类"""
    def __init__(self) -> None:
        pass
    def __init__(self,gid,gname,price,type,left_num,uid):
        self.__gid=gid          #商品id,int PK
        self.__gname=gname      #商品名varchar(24)
        self.__price=price      #价格float
        self.__type=type        #商品类型 varchar(12)
        self.__left_num=left_num#剩余数量 int
        self.__uid=uid          #商品所属用户id int FK

class trade:       
    """交易类"""
    def __init__(self) -> None:
        pass
    def __init__(self,uid1,uid2,gid,num):
        self.__uid1=uid1        #买家id int PK
        self.__uid2-uid2        #卖家id int PK
        self.__gid=gid          #商品号 int PK
        self.__num=num           #交易数量 int

