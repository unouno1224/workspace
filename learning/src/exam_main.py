import os
from exam_functions import *

if __name__ == "__main__":
    print (os.getcwd())
    os.chdir(path)
    print (os.getcwd())
    keys, student_datas = get_data_from_excel('exam.xlsx')
    math_scores = get_score_list('math',student_datas)
    avrg = get_average(math_scores)
    variance = get_variance(math_scores,avrg)
    std_dev = get_std_dev(variance)
   
    print ('평균: {}, 분산: {}, 표준편차: {}'.format(avrg,variance,std_dev))
    
