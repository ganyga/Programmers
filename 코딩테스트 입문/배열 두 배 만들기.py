"""
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(numbers):
    answer = []
    for i in numbers:
        i = i * 2   # 이 부분을 제외하고 answer.append(i * 2) 이렇게 해도됨
        answer.append(i)
    return answer
# 파이썬은 들여쓰기가 매우 중요함
# return은 def 함수로 구현한 값을 반환하기 위한 것
# 함수를 쓰는 이유는 반환 되는 값을 재사용하기 위해(ex. 최대공약수 구하는 함수를 만들어서 여러 번 구할 때 사용)