import re
import operator
import math

# 카테고리 별 딕셔너리
category = {"child": 129, "culture": 220, "economy": 167, "education": 121, "health": 192, "life": 113, "person": 173,
            "policy": 253, "society": 328}

# 전체 카테고리 별 빈도 수 딕셔너리
ca_dict = {}

# 모든 단어 리스트
total_list = []

df = {}

print("<카테고리 별 단어 빈도수>")
for ca in category:
    word_list = []
    for index in range(1, category[ca]):
        file = open('./Input_Data/' + ca + '/(POS)' + ca + '_' + str(index) + '.txt', 'r', encoding='utf8')
        data = file.readlines()
        word_frequence = []

        # 명사만 뽑아 내기
        for word1 in data:
            p = re.compile('(/(NNP|NNG))')
            m = re.finditer('[가-힣]+/(NN(G|P))', word1)
            if m:
                for r in m:
                    word_frequence.append(p.sub("", r.group()))
                    word_list.append(p.sub("", r.group()))
                    total_list.append(p.sub("", r.group()))
        file.close()

        # 문서마다 tf 구하기
        word_frequence_count = {}
        for word2 in word_frequence:
            if word2 in word_frequence_count.keys():
                continue;
            word_frequence_count[word2] = word_frequence.count(word2)

        # 단어마다 df 구하기
        for word3 in word_frequence_count:
            if word3 in df.keys():
                df[word3] += 1
            else:
                df[word3] = 1

    # 카테고리 별 단어의 빈도 수
    word_count = {}

    # 카테고리 별 단어의 빈도 수 딕셔너리로 만들기
    for word2 in word_list:
        if word2 in word_count.keys():
            continue
        word_count[word2] = word_list.count(word2)

    # 읽는데 걸리는 시간을 없애기 위해
    print("--" + ca + "--")
    ca_dict[ca] = word_count

#전체 문서의 수
D = 1687

idf = {}
#idf구하기
for word in df:
    d_df = df[word]
    idf[word]= math.log10(D/(1+d_df))

dict1 = sorted(idf.items(), key = operator.itemgetter(1), reverse= True)
print(dict1)

five_thousand_word1 = []
#5000개 단어 만들기
for i in range(10000):
    five_thousand_word1.append(dict1[i][0])

#cf 구하기
cf = {}

for word in ca_dict:
    c_word_list = ca_dict[word]
    for word2 in c_word_list:
        if word2 in cf.keys():
            cf[word2] += 1
        else:
            cf[word2] = 1

#전체 카테고리의 수
C = 9

icf = {}
#icf구하기

for word in cf:
    d_cf = cf[word]
    icf[word]= math.log10(C/(1+d_cf))

dict = sorted(icf.items(), key = operator.itemgetter(1), reverse= True)
print(dict)

five_thousand_word = {}

#5000개 단어 만들기
for i in range(10000):
    five_thousand_word1.append(dict[i][0])

for word in five_thousand_word1:
    if word in five_thousand_word.keys():
        continue
    else:
        five_thousand_word[word] = five_thousand_word1.count(word)

five_thousand_word_list = []

limit = 0

for word in five_thousand_word:
    if five_thousand_word[word] == 2 and limit != 5000:
        five_thousand_word_list.append(word)
        limit += 1
five_thousand_word_list.sort()
print(five_thousand_word_list)
print(len(five_thousand_word_list))


file = open('./five_thousand_word.txt', 'w', encoding='utf8')
for word in five_thousand_word_list:
    file.write(word + '\t')
file.close()

'''
# 전체 단어의 빈도수 딕셔너리
total_count = {}

for word3 in total_list:
    if word3 in total_count.keys():
        continue;
    total_count[word3] = total_list.count(word3)


# 전체 단어 빈도수 딕셔너리 출력
print("전체 문서 단어의 빈도수 출력")
print(total_count)

# 등장하는 모든 단어 출력
total_list = list(set(total_list))
print("전체 문서 단어 출력")
print(total_list)
'''
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