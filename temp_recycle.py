import os
import MySQLdb
import time
from datetime import timedelta,datetime
passwd=''
db=MySQLdb.connect(host='localhost', user='root',db='hhyz',passwd=passwd)
cursor=db.cursor()
#将过期的头像缓存删除
def recycle():
    try:
        cursor.execute('select * form temp_avatar')
        res=cursor.fetchall()
        delta=timedelta(3600)
        for r in res:
            now=datetime.now()
            if now-r[2]>delta:
                path=r[1]
                if os.path.exists(path):
                    os.remove(path)
                cursor.execute('delete from temp_avatar where id=%s',[r[0]])
        db.commit()
    except:
        db.rollback()
    time.sleep(3600)#睡眠一小时继续执行

if __name__ == '__main__':
    recycle()