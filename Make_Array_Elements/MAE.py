# # 파일 경로
# file_path = 'C:\\Users\\82104\\OneDrive\\바탕 화면\\test\\word1.txt'

# # 파일 열기
# with open(file_path, 'r', encoding='cp949', errors='ignore') as file:
#     # 각 줄을 읽어서 출력
#     for line in file:
#         print("\""+line.strip()+"\""+ ",", end="") 

file_path = 'C:\\Users\\82104\\OneDrive\\바탕 화면\\test\\word2.txt'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
    for line in file:
        # 공백을 제거하고 출력
        cleaned_line = line.replace(" ", "").strip()
        print("\"" + cleaned_line + "\"" + ",", end="")
