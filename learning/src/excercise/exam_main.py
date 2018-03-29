import os
from exam_functions import *

if __name__ == "__main__":
    print (os.getcwd())
    os.chdir(path)
    print (os.getcwd())
    keys, student_datas = get_data_from_excel('exam.xlsx')
    #수학점수만 계산
    # math_scores = get_score_list('science',student_datas)
    # avrg = get_average(math_scores)
    # variance = get_variance(math_scores,avrg)
    # std_dev = get_std_dev(variance)
       
    # print ('평균: {}, 분산: {}, 표준편차: {}'.format(avrg,variance,std_dev))
    #전체 점수 모두 계산
    results={}
    for title in keys :
        if title != 'name':
            scores=get_score_list(title,student_datas)
            avrg = get_average(scores)
            var = get_variance(scores,avrg)
            std_dev = get_std_dev(var)
            results[title]=[avrg,var,std_dev]
        else:
            results[title]=['평균','분산','표준편차']
        print (title + '|'+ '|'.join(map(str,results[title])))
        # print ("|".join(results[title]))
        
    print (keys)
    # x = {k: v for k, v in dict.fromkeys(keys).items()}
    print (dict.fromkeys(keys))