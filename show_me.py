def column(matrix, i):
    return [row[i] for row in matrix]

# 파일읽기
answer = open("answer.txt", "r", encoding="utf-8")
output = open("output.txt", "r", encoding="utf-8")

M = [[0]*9 for i in range(9)]
output_line = output.read().split()

print(M)

count = 0

for start in range(0, len(output_line), 9):
    temp = output_line[start:start + 9]
    max_index = temp.index(max(temp))
    answer_index = int(answer.readline())
    print(max_index,answer_index)
    if max_index == answer_index:
        count +=1
    M[max_index][answer_index] += 1

print(count)
print(M)
precision_list = []
recall_list = []
for i in range(0, 9):
    print(M)
    precision = M[i][0:9]
    recall = column(M, i)
    success = M[i][i]

    if sum(precision) == 0:
        precision_list.insert(i,0)
    else :
        precision_list.insert(i, success / sum(precision))
    if sum(recall) == 0:
        recall_list.insert(i,0)
    else :
        recall_list.insert(i, success / sum(recall))


f1_macro = (2 * sum(precision_list) / 9 * sum(recall_list) / 9) / (sum(precision_list) / 9 + sum(recall_list) / 9)
TP = 0
FP = 0
FN = 0
for i in range(0, 9):
    TP += M[i][i]
    FP += sum(M[i][0:9])
    FN += sum(column(M, i))
FP = FP - TP
FN = FN - TP

precision_total = TP / (TP + FP)
recall_total = TP / (TP + FN)
f1_micro = (2 * precision_total * recall_total) / (precision_total + recall_total)

print(">> Performance")
print(" - Macro_F1 : ", f1_macro)
print("")

print(" - Total Prediction : ", precision_total)
print(" - Total Recall : ", recall_total)
print(" - Micro_F1 : ", f1_micro)


answer.close()
output.close()

