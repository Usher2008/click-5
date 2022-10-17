from pymouse import PyMouse
import time
import datetime

# 范围时间
while(1):
    time.sleep(1)
    d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '05:00', '%Y-%m-%d%H:%M')
    d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '05:10', '%Y-%m-%d%H:%M')
    n_time = datetime.datetime.now()
    print(n_time.strftime('%Y-%m-%d %H:%M:%S'),end='：')
    if n_time > d_time and n_time < d_time1:
        print(True)
        break
    else:
        print(False)

m = PyMouse()
#a = m.position()    #获取当前坐标的位置
#print(a)
 
#m.move(31, 223)   #鼠标移动到(x,y)位置
#a = m.position()
#print(a)

m.click(935, 180)#移动并且在(x,y)位置左击
time.sleep(1)
m.click(743, 186)

#for i in range(2):
#    m.click(38, 843)
