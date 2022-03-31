# -*- codeing = utf-8 -*-
# @TIME:2021/3/416:29
# @File:2021.3.4政策分析.py
# @Software:PyCharm



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import re # 正则表达式库
import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
import wordcloud # 词云展示库
from PIL import Image # 图像处理库
import matplotlib.pyplot as plt # 图像展示库

# 读取文件
fn = open('C://Users//jr//Desktop//顶层设计.txt','rt',encoding='utf-8') # 打开文件
string_data = fn.read() # 读出整个文件
fn.close() # 关闭文件

# 文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"') # 定义正则表达式匹配模式
string_data = re.sub(pattern, '', string_data) # 将符合模式的字符去除

# 文本分词
seg_list_exact = jieba.cut(string_data, cut_all = False) # 精确模式分词
object_list = []
remove_words = [u"搞",u"提供",u"可能",u"造成",u"大",u"按规定",u"报告",u"有关",u"问题",u"个人",u"工作",u"八项",u"影响",u'”',u'“',u'时',u'或',u'会',u'党',u'其中',u'所',u'与',u'如实',u'事项',u'涉嫌',u'有关'u'影响',u'干部',u'审查',u'方面',u'规定',u'政治',u'中央',u'并',u'组织',u'不',u'违规',u'上',u'严重',u'纪律',u'他人',u'为',u'收受',u'违反',u'；',u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',
               ] # 自定义去除词库

for word in seg_list_exact: # 循环读出每个分词
    if word not in remove_words: # 如果不在去除词库中
        object_list.append(word) # 分词追加到列表

# 词频统计
word_counts = collections.Counter(object_list) # 对分词做词频统计
word_counts_top10 = word_counts.most_common(100) # 获取前10最高频的词
print (word_counts_top10) # 输出检查

# 词频展示
mask = np.array(Image.open('C://Users//jr//Desktop//四川地图.png')) # 定义词频背景
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simhei.ttf', # 设置字体格式
    mask=mask, # 设置背景图
    max_words=200, # 最多显示词数
    max_font_size=100 # 字体最大值
)

wc.generate_from_frequencies(word_counts) # 从字典生成词云
image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
plt.imshow(wc) # 显示词云
plt.axis('off') # 关闭坐标轴
plt.show() # 显示图像


