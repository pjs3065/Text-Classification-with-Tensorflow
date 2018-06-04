import re
import operator
import math

# 파일 읽기

category = {"child": 129, "culture": 220, "economy": 167, "education": 121, "health": 192, "life": 113, "person": 173,
            "policy": 253, "society": 328}

ca_dict = {}

for ca in category:
    word_list = []
    for index in range(1, category[ca]):
        file = open('./Input_Data/' + ca + '/(POS)' + ca + '_' + str(index) + '.txt', 'r', encoding='utf8')
        data = file.readlines()

        for word1 in data:
            p = re.compile('(/(NNP|NNG))')
            m = re.finditer('[가-힣]+/(NN(G|P))', word1)
            if m:
                for r in m:
                    word_list.append(p.sub("", r.group()))
        file.close()

    word_count = {}
    for word2 in word_list:
        word_count[word2] = word_list.count(word2)
    word_count = sorted(word_count.items(), key=operator.itemgetter(0))
    ca_dict[ca] = word_count
    print(ca + " finish")

for index in ca_dict:
    print(ca_dict[index])

''' data = file.readlines()
# 명사끼리 모으기
list = []
for word in data:
p = re.compile('(/(NNP|NNG))')
m = re.finditer('[가-힣]+/(NN(G|P))', word)
    if m:
        for r in m:
            list.append(p.sub("", r.group()))

# 명사의 빈도
dict = {}
for word in list:
    dict[word] = list.count(word)

# 빈도수가 높은 순서대로 소팅(리스트 안의 튜플이 됨)
dict = sorted(dict.items(), key = operator.itemgetter(0))




# TF 구하기
for i in range(0, len(dict)):
    TF = round(math.log10(dict[i][1] + 1), 4)
    dict[i] = dict[i] + (TF,)
print(dict)
'''

# 파일 닫기
file.close()