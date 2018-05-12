print(abs(-3))

# 반복 가능한 자료형 x를 입력 인수로 받으며, 이 x가 몯 ㅜ참이면 True, 거짓이 하나라도 있으면 False를 리턴
print(all([1, 2, 3, 0]))

# x 중 하나라도 참이 있을 경우 True, x가 모두 거짓일 때에만 Faluse를 기턴
print(any([1,2,3,0]))
print(any([0, ""]))

# 아스키 코드값을 입력받아 그 코드에 해당하는 문자를 출력
print(chr(65))

# 객체 자체적으로 가지고 있는 변수나 함수를 보여줌
# 리스트
print(dir([1,2,3]))
# 딕셔너리
print(dir({'1', 'a'}))

# a를 b로 나눈 몫과 나머지를 튜플 형태로 리턴
print(divmod(7, 3))
print(divmod(2,1))
print(divmod(1.3, 0.2))

# 리스트, 튜플, 문자열을 입력받아 인덱스 값을 포함하는 enumerate 객체 리턴
for i, name in enumerate(['body', 'foo', 'bar']):
	print(i, name)

# 실행가능한 문자열을 입력으로 받아 문자열을 실행한 결과값 리턴
print(eval('1+2'))
eval('print(eval("divmod(4,3)"))')

# 두번째 인수인 반복가능한 자료형 요소들이 첫번째 인수인 함수에 입력되었을 때 리턴값이 참인 것만 묶어서 돌려줌
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, 5, 6])))

# 정수값을 입력받아 16진수로 변환하여 리턴
print(hex(10))
