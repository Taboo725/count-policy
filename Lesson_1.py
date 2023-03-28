'''
import numpy as np
import matplotlib.pyplot as plt
plt.rc("font", family='Microsoft YaHei')

def noise(length):
    e_values = [] #空列表
    for i in range(length):
        e = np.random.randn()
        e_values.append(e)
    plt.plot(e_values)
    plt.show()
    return

noise(100)


animals = ["dog","cat","bird"]
for animal in animals:
    print("The plural of",animal,"is",animal+"s")

a = ["cat","dog",1,2,4,3]
b = [1,2,4,3]
a.pop(1)
output = 2*a+b
print(output)
'''

'''
r = 0.025 #利率
T = 50 #期数
b = np.empty(T+1)
b[0] = 10 #初始值
for t in range(T):
    b[t+1] = (1+r)*b[t] + np.random.randn()
plt.plot(b,label = "银行账户_bank balance")
plt.legend()
plt.show()

sum = 1
for i in range(25):
    sum = sum*(i+1)
print(sum)

x = np.linspace(-np.pi)
plt.figure(1)
plt.subplot(223)
plt.show()

import pandas as pd
lesson = pd.read_excel(r'F:\经济学院2022-2023学年春季开课课程汇总表.xlsx')

a = np.array([2,0,1,5])
print(a)
print(a[0:4])
print(a.min())
a.sort()
b = np.array([[1,2,3],[16,25,16]])
print(b*b)

import pandas as pd
df = pd.read_csv("F:\学习\大三下\面向经济和金融的Python编程\\air_tianjin_2017.csv")
print(df)
df.to_excel()

import numpy as np
import pandas as pd
index =['a','b','c']
df1 = pd.DataFrame(np.random.randn(3,4),index = index , columns = list('ABCD'))

df2 = pd.DataFrame({'C':[1,2,3,4],'D':[4,5,6,7],'E':[7,8,9,10]}, index = ['b','c','d','e'])
df3 = df1.mul(df2,fill_value = 0)
print('Original:')
print(df3)
print('Processed:')
print(df3.fillna(method='ffill'))
'''

import pandas as pd
pd.set_option('display.max_columns',1000)         #设置最大的列数为1000行（小于1000行均可以输出）
pd.set_option('display.width', 1000)                      #设置最大的行宽度（小于1000行均可以输出）
pd.set_option('display.max_colwidth',1000)           #设置最大的列宽1000行（小于1000行均可以输出）
data = pd.read_excel(r"F:\学习\大三下\面向经济和金融的Python编程\directory.xls")

data['City'] = data['City'].fillna(data['State/Province'])
print(data[data['Country']=='EG'])
data[data['Country']=='TW'] ='CN'

country_count = data['Country'].value_counts()[0:10]
print(country_count)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['simhei'] #制定默认字体
plt.rcParams['axes.unicode_minus'] = False
country_count.plot(kind = 'barh',color='lightblue')
plt.show()


