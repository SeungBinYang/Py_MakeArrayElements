# # 파일 경로
# 예시 file_path = 'C:\\Users\\Username\\OneDrive\\바탕 화면\\test\\word1.txt'

# # 파일 열기
# with open(file_path, 'r', encoding='cp949', errors='ignore') as file:
#     # 각 줄을 읽어서 출력
#     for line in file:
#         print("\""+line.strip()+"\""+ ",", end="") 

file_path = 'C:\\Users\\***\\***\\***\\***\\word2.txt' # txt 파일 경로에 맞게 지정 

with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
    for line in file:
        # 공백을 제거하고 출력
        cleaned_line = line.replace(" ", "").strip()
        print("\"" + cleaned_line + "\"" + ",", end="")
