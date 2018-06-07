# -*- coding: utf-8 -*-
import re
import operator
import math

#5000개 단어 읽어오기
five_thousand_word = []

file = file = open('./five_thousand_word.txt', 'r', encoding='utf8')
data = file.read()
file.close()

words = data.split("\t")

for word in words:
    if word == '':
        continue
    five_thousand_word.append(word)
print("5000개 단어")
print(five_thousand_word)

#Input_data 구하기
# 카테고리
category = {"child": 129, "culture": 220, "economy": 167, "education": 121, "health": 192, "life": 113, "person": 173,
            "policy": 253, "society": 328}

# 문서에 등장하는 단어들의 빈도수 구하기
df = {}
f = {}
count = 1

#f와 df 구하기
print("tf와 df 구하기")
for ca in category:
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
                    w = p.sub("", r.group())
                    word_frequence.append(w)
        file.close()

        # 문서마다 tf 구하기
        word_frequence_count = {}
        for word2 in word_frequence:
            if word2 in word_frequence_count.keys():
                continue;
            word_frequence_count[word2] = word_frequence.count(word2)
        f["D" + str(count)] = word_frequence_count

        # 단어마다 df 구하기
        for word3 in word_frequence_count:
            if word3 in df.keys():
                df[word3] += 1
            else:
                df[word3] = 1
        count += 1

#tf와 idf 와 tf_idf 구하기

#tf구하기
tf = {}
for word in f:
    d_f_list = f[word]
    d_tf = {}
    for word2 in d_f_list:
        d_f = d_f_list[word2]
        d_tf[word2] = math.log10(d_f+1)
    tf[word] = d_tf

#전체 문서의 수
D = count -1

idf = {}
#idf구하기
for word in df:
    d_df = df[word]
    idf[word]= math.log10(D/(1+d_df))

'''
#71퍼 나옴

dict = sorted(idf.items(), key = operator.itemgetter(1))
print(dict)


five_thousand_word = []
#5000개 단어 만들기
for i in range(5000):
    five_thousand_word.append(dict[i][0])
five_thousand_word.sort()
print(len(five_thousand_word))

'''
tf_idf = {}
#tf_idf 구하기
for word in tf:
    d_tf_list = tf[word]
    d_tf_idf = {}
    for word2 in d_tf_list:
        d_tf = d_tf_list[word2]
        d_idf = idf[word2]
        d_tf_idf[word2] = d_tf * d_idf
    tf_idf[word] = d_tf_idf

# tf_idf 정규화 만들기 과정
tf_idf_normalization = {}
tf_idf_sum ={}

for word in tf_idf:
    d_tf_idf_list = tf_idf[word]
    d_tf_idf_normalization = {}
    for word2 in five_thousand_word:
        if word2 in d_tf_idf_list.keys():
            d_tf_idf_normalization[word2] = d_tf_idf_list[word2]
        else:
            d_tf_idf_normalization[word2] = 0
    tf_idf_normalization[word] =  d_tf_idf_normalization


'''
# tf_idf 정규화 만들기 과정
tf_idf_normalization = {}
tf_idf_sum ={}

#tf_idf의 모든 제곱의 합
for word in tf_idf:
    d_tf_idf_list = tf_idf[word]
    d_tf_idf_sum = 0
    for word2 in five_thousand_word:
        if word2 in d_tf_idf_list.keys():
            d_tf_idf_sum += (d_tf_idf_list[word2] ** 2)
    tf_idf_sum[word] = (d_tf_idf_sum ** 0.5)

# tf_idf의 정규화
for word in tf_idf_sum:
    d_tf_idf_sum = tf_idf_sum[word]
    d_tf_idf_list = tf_idf[word]
    d_tf_idf_normalization = {}
    for word2 in five_thousand_word:
        if word2 in d_tf_idf_list.keys() and d_tf_idf_sum != 0:
                d_tf_idf = d_tf_idf_list[word2]
                d_tf_idf_normalization[word2] = d_tf_idf / d_tf_idf_sum
        else:
            d_tf_idf_normalization[word2] = 0
    tf_idf_normalization[word] = d_tf_idf_normalization
'''
#input_data 파일쓰기

number = 1

for ca in category:
    for index in range(1, category[ca]):
        file = open('./feature/Input_Data/' + ca + '/(POS)' + ca + '_' + str(index) + '.txt', 'w')

        d = "D" + str(number)
        words = tf_idf_normalization[d]

        for word in words:
            value = str(words[word])
            file.write(value)
            file.write("\t")

        file.close()
        number += 1

# test_data

# 카테고리
category2 = {"child": 139, "culture": 230, "economy": 177, "education": 131, "health": 202, "life": 123, "person": 183,
            "policy": 268, "society": 343}

# 문서에 등장하는 단어들의 빈도수 구하기
f = {}
number = count

#f구하기
print("tf와 df 구하기")
for ca in category:
    for index in range(category[ca], category2[ca]):
        file = open('./Test_Data/' + ca + '/(POS)' + ca + '_' + str(index) + '.txt', 'r', encoding='utf8')
        data = file.readlines()
        word_frequence = []

        # 명사만 뽑아 내기
        for word1 in data:
            p = re.compile('(/(NNP|NNG))')
            m = re.finditer('[가-힣]+/(NN(G|P))', word1)
            if m:
                for r in m:
                    w = p.sub("", r.group())
                    word_frequence.append(w)
        file.close()

        # 문서마다 tf 구하기
        word_frequence_count = {}
        for word2 in word_frequence:
            if word2 in word_frequence_count.keys():
                continue
            word_frequence_count[word2] = word_frequence.count(word2)
        f["D" + str(count)] = word_frequence_count
        count += 1

tf = {}
tf_idf = {}

#tf와 idf 와 tf_idf 구하기

#tf구하기
for word in f:
    d_f_list = f[word]
    d_tf = {}
    for word2 in d_f_list:
        d_f = d_f_list[word2]
        d_tf[word2] = math.log10(d_f+1)
    tf[word] = d_tf

#tf_idf 구하기
for word in tf:
    d_tf_list = tf[word]
    d_tf_idf = {}
    for word2 in d_tf_list:
        if word2 in idf.keys():
            d_tf = d_tf_list[word2]
            d_idf = idf[word2]
            d_tf_idf[word2] = d_tf * d_idf
        else:
            d_tf_idf[word2] = 0
    tf_idf[word] = d_tf_idf

# tf_idf 정규화 만들기 과정
tf_idf_normalization = {}
tf_idf_sum ={}

for word in tf_idf:
    d_tf_idf_list = tf_idf[word]
    d_tf_idf_normalization = {}
    for word2 in five_thousand_word:
        if word2 in d_tf_idf_list.keys():
            d_tf_idf_normalization[word2] = d_tf_idf_list[word2]
        else:
            d_tf_idf_normalization[word2] = 0
    tf_idf_normalization[word] =  d_tf_idf_normalization

'''
#tf_idf의 모든 제곱의 합
for word in tf_idf:
    d_tf_idf = tf_idf[word]
    d_tf_idf_sum = 0
    for word2 in five_thousand_word:
        if word2 in d_tf_idf.keys():
            d_tf_idf_sum += (d_tf_idf[word2] **2)
    tf_idf_sum[word] = (d_tf_idf_sum ** 0.5)

# tf_idf의 정규화
for word in tf_idf_sum:
    d_tf_idf_sum = tf_idf_sum[word]
    d_tf_idf_list = tf_idf[word]
    d_tf_idf_normalization = {}
    for word2 in five_thousand_word:
        if word2 in d_tf_idf_list.keys() and d_tf_idf_sum != 0:
                d_tf_idf = d_tf_idf_list[word2]
                d_tf_idf_normalization[word2] = d_tf_idf / d_tf_idf_sum
        else:
            d_tf_idf_normalization[word2] = 0
    tf_idf_normalization[word] = d_tf_idf_normalization
'''
#test data 파일쓰기

for ca in category:
    for index in range(category[ca], category2[ca]):
        file = open('./feature/Test_Feature_Data/' + ca + '/(POS)' + ca + '_' + str(index) + '.txt', 'w')

        d = "D" + str(number)
        words = tf_idf_normalization[d]

        for word in words:
            value = str(words[word])
            file.write(value)
            file.write("\t")

        file.close()
        number += 1

'''
for word in tf_idf_normalization:
    d = tf_idf_normalization[word]
    for word2 in d:
        if d[word2] > 0:
            print(word, word2, d[word2])
'''






'''
print((f["D1"])["인화학교"])
print(df["인화학교"])
print((tf["D1"])["인화학교"])
print(idf["인화학교"])
print((tf_idf["D1"])["인화학교"])
'''