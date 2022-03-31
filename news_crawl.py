import csv
import random
import time

import pandas as pd
from bs4 import BeautifulSoup  #网页解析,获取数据
import re   #正则表达式，进行文字匹配
import requests as t
from lxml import etree
import json


def caterror(url, headers, coding='utf-8'):
    while True:
        try:
            resp = t.get(url, headers=headers, timeout=10)
            resp.encoding = coding
            code = resp.status_code
            html = resp.text
        except Exception as e:
            print(e)
            code = 500
            html = ''
        if code == 200 and html:
            return html
        else:
            time.sleep(random.randint(1,4))
            continue


def crawl_pages(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
               'Referer': 'https://www.ccdi.gov.cn/scdc/zggb/djcf/index.html'}
    obj = json.loads(caterror(url, headers))
    news_urls = [i.get('DOCPUBURL') for i in obj.get('data')]
    for news_url in news_urls:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
               }
        html = caterror(news_url, headers)
        html_1 = re.sub(u'<script.*?</script>', '', html, flags=re.S)
        html_2 = re.sub(u'<style.*?</style>', '', html_1, flags=re.S)
        parse_detail(html_2, news_url)


def parse_detail(html, news_url):
    tree = etree.HTML(html)
    title = ''.join(tree.xpath('//*[@class="tit"]//h1/text()')).strip().replace('\n', '')
    pb_tm = ''.join(tree.xpath('//*[@class="daty_con"]//text()')).strip().replace('\n', '')
    try:
        pb_tm = re.findall('\d{4}-\d{1,2}-\d{1,2}', pb_tm, re.S)[0]
    except:
        pb_tm = ''

    content = ''.join(tree.xpath('//*[@class="TRS_Editor"]//text()')).strip().replace('\n', ' ')
    if not content:
        content = ''.join(tree.xpath('//*[@class="article-content"]//text()')).strip().replace('\n', ' ')
    else:
        content = content
    datas = [news_url, title, pb_tm, content]
    if all(datas):
        print('抓取成功：' + news_url)
        with open('{}.csv'.format(file_name), 'a', encoding='utf-8', newline='') as fl:
            csvwriter = csv.writer(fl)
            csvwriter.writerow(datas)
    else:
        print('解析不完整：' + news_url)
        with open('抓取失败链接.txt', 'a', encoding='utf-8') as f:
            f.write(news_url + '\n')


def csv2excel(filename):
    df = pd.read_csv('{}.csv'.format(filename), header=None, names=['新闻链接', '新闻标题', '出版时间', '正文'])
    df.to_excel('{}.xlsx'.format(filename), index=False)
    print('文件生成成功！')


if __name__ == '__main__':
    file_name = '中纪委落马数据'
    url_md = 'http://218.95.174.99:8081/TZSearch/tzsearch.jsp?searchword=%E7%A6%8F%E5%BB%BA&siteId=4&pageIndex={}'
    for page in range(1, 2):
        print('正在抓取第{}页'.format(page))
        url = url_md.format(page)
        crawl_pages(url)
        print('第{}页抓取成功'.format(page))
    csv2excel(file_name)
