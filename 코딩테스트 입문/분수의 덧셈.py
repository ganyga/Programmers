"""
첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
"""

# 기약분수 : 분모와 분자의 공약수가 1뿐인 분수, 분모와 분자를 그들의 최대공약수로 나누면 기약분수가 됨
# 수학 함수 모듈 math
import math

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    # 최대 공약수 함수 math.gcd()
    gcd = math.gcd(numer, denom)
    answer = [numer/gcd, denom/gcd]
    return answer
