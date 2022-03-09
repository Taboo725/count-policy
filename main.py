import jieba
file = open("F://教育督导条例.txt", "r", encoding='utf-8') #此处需打开txt格式且编码为UTF-8的文本
txt = file.read()
words = jieba.lcut(txt) # 使用jieba进行分词，将文本分成词语列表

count = {}
for word in words: # 使用 for 循环遍历每个词语并统计个数
    if len(word) < 2: # 排除单个字的干扰，使得输出结果为词语
        continue
    else:
        count[word] = count.get(word, 0) + 1 #如果字典里键为 word 的值存在，则返回键的值并加一，如果不存在键word，则返回0再加上1

exclude = ["可以", "一起", "这样"] # 建立无关词语列表
for key in list(count.keys()): # 遍历字典的所有键，即所有word
    if key in exclude:
        del count[key] # 删除字典中键为无关词语的键值对

list = list(count.items()) # 将字典的所有键值对转化为列表
list.sort(key=lambda x: x[1], reverse=True) # 对列表按照词频从大到小的顺序排序

print("教育",count["教育"])
input("输入任意字符结束…")
#统计最高频次词语
# for i in range(5): # 此处统计排名前五的单词，所以range(5)
# word, number = list[i]
# print("关键字：{:-<10}频次：{:+>8}".format(word, number))