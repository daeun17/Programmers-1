def solution(babbling):
    answer = 0
    bab = [11,22,33,44]
    
    for i in range(0,len(babbling),1) :
        babbling[i] = babbling[i].replace('aya','1')
        babbling[i] = babbling[i].replace('ye','2')
        babbling[i] = babbling[i].replace('woo','3')
        babbling[i] = babbling[i].replace('ma','4')
        babbling[i] = babbling[i].replace('11','x')
        babbling[i] = babbling[i].replace('22','x')
        babbling[i] = babbling[i].replace('33','x')
        babbling[i] = babbling[i].replace('44','x')
        babbling[i] = babbling[i].replace('1','-')
        babbling[i] = babbling[i].replace('2','-')
        babbling[i] = babbling[i].replace('3','-')
        babbling[i] = babbling[i].replace('4','-')
        babbling[i] = babbling[i].replace('-','')
        if babbling[i] == '':
            answer += 1
    
    print(babbling)
    return answer