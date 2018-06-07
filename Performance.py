def column_value(matrix, i):
    return [row[i] for row in matrix]

# 파일읽기
answer = open("answer.txt", "r", encoding="utf-8")
output = open("output.txt", "r", encoding="utf-8")

matrix = [[0]*9 for i in range(9)]
output_line = output.read().split()

#print(matrix)

count = 0

# 예측한 값이랑 정답값
for start in range(0, len(output_line), 9):
    temp = output_line[start:start + 9]
    max_index = temp.index(max(temp))
    answer_index = int(answer.readline())
    # print(max_index,answer_index)
    if max_index == answer_index:
        count += 1
    matrix[max_index][answer_index] += 1

print(count)
print(matrix)

# precision값과 recall값 리스트로 추가
precision_list = []
recall_list = []
for index in range(0, 9):
    print(matrix)
    precisions = matrix[index][0:9]
    recalls = column_value(matrix, index)
    success = matrix[index][index]

    if sum(precisions) == 0:
        precision_list.insert(index,0)
    else :
        precision_list.insert(index, success / sum(precisions))
    if sum(recalls) == 0:
        recall_list.insert(index,0)
    else :
        recall_list.insert(index, success / sum(recalls))

print("< Performance >")
f1_macro_score = (2 * sum(precision_list) / 9 * sum(recall_list) / 9) / (sum(precision_list) / 9 + sum(recall_list) / 9)
print("Macro_F1 : ", f1_macro_score)
print("")

# TP, FP, FN 이용해서 F1 Score내기
TP = 0
FP = 0
FN = 0
for index in range(0, 9):
    TP += matrix[index][index]
    FP += sum(matrix[index][0:9])
    FN += sum(column_value(matrix, index))
FP = FP - TP
FN = FN - TP

precision_score = TP / (TP + FP)
recall_score = TP / (TP + FN)
f1_micro_score = (2 * precision_score * recall_score) / (precision_score + recall_score)

print("Total Prediction : ", precision_score)
print("Total Recall : ", recall_score)
print("Micro_F1 : ", f1_micro_score)


answer.close()
output.close()

