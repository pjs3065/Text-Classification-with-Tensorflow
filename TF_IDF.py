import re
import operator
import math

# 파일 읽기
file = open('./Input_Data/child/(POS)child_1.txt','r', encoding='utf8')
data = file.readlines()

# 명사끼리 모으기
list = []
for word in data:
    p = re.compile('(/(NNP|NNG))')
    m = re.finditer('[가-힣]+/(NN(G|P))',word)
    if m :
        for r in m:
            list.append(p.sub("",r.group()))

# 명사의 빈도
dict ={}
for word in list:
    dict[word] = list.count(word)

# 빈도수가 높은 순서대로 소팅(리스트 안의 튜플이 됨)
dict = sorted(dict.items(), key = operator.itemgetter(0))

# TF 구하기
for i in range(0,len(dict)):
    TF = round(math.log10(dict[i][1] + 1),4)
    dict[i] = dict[i] + (TF,)
print(dict)

# 파일 닫기
file.close()