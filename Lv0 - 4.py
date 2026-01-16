### TL;DR : shutil 모듈 활용하기


# 빈칸 넣기

# import ______

# _____.____("c:/doit/a.txt", "c:/temp/a.txt.bak")  # 파일 복사
# _____.____("c:/doit/a.txt", "c:/temp/a.txt")  # 파일 이동





# ->





import shutil

shutil.copy("c:/doit/a.txt", "c:/temp/a.txt.bak")  # 파일 복사
shutil.move("c:/doit/a.txt", "c:/temp/a.txt")  # 파일 이동