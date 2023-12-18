"""
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 
최빈값이 여러 개면 -1을 return 합니다.
"""

from collections import Counter # collections 모듈의 Counter 클래스

def solution(array): # array : [1,2,3,3,3,4]
    count = Counter(array) 
    # Counter : dict 형태로 요소의 빈도수를 알려줌
    # Counter({"1":1, "2":1, "3":3, "4":1} )
    
    ## 최빈값 구하기
    mode_values = []
    for key, value in count.items(): # items():딕셔너리에 있는 키와 값들의 쌍을 얻을 수 있음
        if value == max(count.values()): # max value와 value값이 같으면 key를 append 
            mode_values.append(key)
    
    # 리스트 컨프리헨션
    # mode_values = [key for key, value in count.items() if value == max_count]
    
    ## 최빈값 return
    if len(mode_values) == 1: # 최빈값이 한 개면 [0]번째 값을 출력
        return mode_values[0]
    else:                     # 최빈 값이 여러 개거나 전혀 없으면 -1을 출력
        return -1