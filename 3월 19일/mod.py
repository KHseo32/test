# 평균값 함수 mean()
def mean(*_values) :
    sum_values = 0
    cnt = 0
    for val in _values:
        sum_values += val
        cnt += 1
    result = sum_values / cnt
    return result