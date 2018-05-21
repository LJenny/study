# 명령행에서 인수 전달하기
import sys

print(sys.argv)

#sys.exit() # 강제로 스크립트 종료

# 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f) # data를 그대로 파일에 저장
f.close()

# 딕셔너리 객체 상태 그대로 불러옴
f = open("test.txt", 'rb')
data2 = pickle.load(f)
print(data2)
f.close()

# 내 시스템의 환경 변수값을 알고 싶을 때
import os
#print(os.environ['PATH'])
# 현재 디렉토리의 위치 변경
#os.chdir("C:\WINDOWS")
# 시스템 명령어 호출
os.system("ls")

#파일복사
import shutil
shutil.copy("test.txt", "test_cp.txt")


