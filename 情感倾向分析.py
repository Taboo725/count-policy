# import pandas as pd
# from textblob import TextBlob
#
# # 读取xlsx文件
# df = pd.read_excel('F:\杂项\聊天记录可视化\聊天记录.xlsx')
#
# # 定义情感分析函数
# def analyze_sentiment(text):
#     blob = TextBlob(str(text))
#     sentiment_score = blob.sentiment.polarity
#     if sentiment_score > 0:
#         return 'Positive'
#     elif sentiment_score < 0:
#         return 'Negative'
#     else:
#         return 'Neutral'
#
# # 对contend列进行情感分析，并添加新列存储情感倾向信息
# df['Sentiment'] = df['content'].apply(analyze_sentiment)
#
# # 将结果保存到新的xlsx文件
# df.to_excel('F:\杂项\聊天记录可视化\【情感分析】聊天记录.xlsx', index=False)



import pandas as pd
from textblob import TextBlob

# 读取xlsx文件
df = pd.read_excel("F:\杂项\聊天记录可视化\聊天记录.xlsx")

# 定义函数进行情感分析
def analyze_sentiment(text):
    analysis = TextBlob(str(text))
    return analysis.sentiment.polarity

# 对消息内容进行情感分析，并存储结果到新列
df['sentiment'] = df['content'].apply(analyze_sentiment)

# 输出结果
print(df)

# 将结果保存到新文件
df.to_excel("F:\杂项\聊天记录可视化\【情感分析】聊天记录.xlsx", index=False)
