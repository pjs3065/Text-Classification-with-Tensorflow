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
    five_thousand_word.append(word)
print("5000개 단어")
print(five_thousand_word)

# 카테고리 별 딕셔너리
category = {"child": 129, "culture": 220, "economy": 167, "education": 121, "health": 192, "life": 113, "person": 173,
            "policy": 253, "society": 328}

# 전체 카테고리 별 빈도 수 딕셔너리
ca_dict = {}

# 모든 단어 리스트
total_list = []

## 여기에 넣어줄거단
total_dict = {}

count = 1
print("<문서별 단어 빈도수>")
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
                    w = p.sub("", r.group())

                    word_frequence.append(w)
                    word_list.append(w)
                    total_list.append(w)
        file.close()
        
        word_frequence_count = {}
        for word2 in word_frequence:
            if word2 in word_frequence_count.keys():
                continue;
            word_frequence_count[word2] = word_frequence.count(word2)
        
        



    # 카테고리 별 단어의 빈도 수
    word_count = {}

    # 카테고리 별 단어의 빈도 수 딕셔너리로 만들기
    for word2 in word_list:
        if word2 in word_count.keys():
            continue;
        word_count[word2] = word_list.count(word2)

    # 파일 읽는데 걸리는 시간을 없애기 위해
    print("--" + ca + "--")
    print(word_count)

    ca_dict[ca] = word_count