# 파일 읽기
file = open('./Input_Data/child/(POS)child_1.txt','r', encoding='utf8')
data = file.read()
print (data)
file.close()