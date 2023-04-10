def solution(name, yearning, photo):
    answer = []
    yearning = list(map(str,yearning))
    name_dict = dict(zip(name,yearning))
    #print(name_dict)
    
    
    for i in range(0,len(photo),1) :
        answer.append(0)
        #print(i)
        for j in photo[i] :
            if j in name :
                answer[i] += int(name_dict[j])

    return answer