#基本类的建立
class admin:
    __aid=-1        #管理员id,int PK
    __keyword=None  #密码varchar(12)
    __post=None     #职位varchar(12)
    def __init__(self) -> None:
        pass
    def __init__(self,aid,keyword,post):
        self.__aid=aid
        self.__keyword=keyword
        self.__post=post
    # def test_show(self):
    #     print(self.__aid)
    #     print(self.__keyword)


class user:
    __uid=-1        #用户id，int PK
    __username=None #用户名varchar(16)
    __keyword=None  #用户密码varchar(12)
    __tel=None      #联系方式char(11)
    __account=None  #账户char(20) 待定
    def __init__(self) -> None:
        pass
    def __init__(self,uid,keyword,username,tel,account):
        self.__uid=uid
        self.__keyword=keyword
        self.__username=username
        self.__tel=tel
        self.__account=account

class good:
    __gid=-1        #商品id,int PK
    __gname=None    #商品名varchar(24)
    __price=None    #价格float
    __type=None     #商品类型 varchar(12)
    __left_num=None #剩余数量 int
    __uid=-1        #商品所属用户id int FK
    def __init__(self) -> None:
        pass
    def __init__(self,gid,gname,price,type,left_num,uid):
        self.__gid=gid
        self.__gname=gname
        self.__price=price
        self.__type=type
        self.__left_num=left_num
        self.__uid=uid

class trade:
    __uid1=-1         #买家id int PK
    __uid2=-1         #卖家id int PK
    __gid=-1          #商品号 int PK
    __num=None        #交易数量 int
    def __init__(self) -> None:
        pass
    def __init__(self,uid1,uid2,gid,num):
        self.__uid1=uid1
        self.__uid2-uid2
        self.__gid=gid
        self.__num=num

# a=admin(3,123456,'userinfo')
# a.test_show()