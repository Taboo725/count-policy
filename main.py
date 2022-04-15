from bs4 import BeautifulSoup
import re, os, time
def parseAll():
    standard = re.compile("标准答案：\s*(.{1,5})")
    your = re.compile("你的答案：\s*(.{1,5})")
    def parse_answer(node):
        res = standard.search(node.text)
        if res:
            return res.group(1).strip()
        else:
            return your.search(node.text).group(1).strip()
    f = open("res.html", encoding = 'utf-8')
    soup = BeautifulSoup(f.read(), "html.parser")
    f.close()
    shiti = soup.find_all(class_ = "shiti")

    res = [(i.find("strong").text, parse_answer(i))for i in shiti]
    ans = []
    if os.path.exists('res.txt'):
        with open('res.txt', encoding = 'utf-8') as f:
            answer = f.readlines()
        for i in answer:
            s = i.split(":")
            qu = ""
            for i in range(len(s) - 1):
                qu += s[i]
            ans.append((qu.strip(), s[-1].strip()))
    res += ans
    res = set(res)
    res = sorted(res,key = lambda x:x[1])
    res.reverse()
    res = [i[0]+" : "+i[1]+"\n" for i in res]
    with open("res.txt", "w",encoding='utf-8') as f:
        f.writelines(res)

while True:
    if not os.path.exists('res.html'):
        time.sleep(10)
        continue
    else:
        parseAll()
    if not os.path.exists('res.txt'):
        time.sleep(10)
    with open('res.txt', encoding = 'utf-8') as f:
        answer = f.readlines()
    answer_dict = {i.split(":")[0].strip() : i.split(":")[-1].strip() for i in answer}
    if not os.path.exists('ques.html'):
        time.sleep(2)
        continue
    with open('ques.html', encoding = 'utf-8') as f:
        soup = BeautifulSoup(f.read(),"html.parser")
    os.remove('ques.html')
    shiti = soup.find_all(class_ = "shiti")
    shiti = [i.find('p').text for i in shiti]
    pat = re.compile("\d{1,2}、(.*)")
    ti = []
    for i in shiti:
        mat = pat.search(i)
        if mat:
            ti.append(mat.group(1).split(":")[0])
        else:
            ti.append(i)
    os.system('cls')
    for i in ti:
        print(i, '\033[1;35m ' + str(answer_dict.get(i)) + ' \033[0m')