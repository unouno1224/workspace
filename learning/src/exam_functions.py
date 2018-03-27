import openpyxl as xl
import math as mt

path = 'D:\\Python\\workspace\\learning\\xls\\'

def get_data_from_excel (file_name):
    """
    2018.03.26 by unouno
    desciption: 엑셀파일이름을 인풋으로 받아 첫 행은 key로 
                다음행 부터 딕셔너리 형태로 데이터를 저장하여 리스트를 만든 후 반환한다.
    usage)
        get_data_from_excel(file_name)
        ==> [
                {name:'name1', math:score1, literature:score1, science:score1},
                {name:'name2', math:score2, literature:score2, science:score2},
                ...
            ]
        Arguments:
            file_name {[string]} -- [엑셀로 읽을 파일 이름]

    """
    wb = xl.load_workbook(path+file_name)
    ws = wb.active
    g = ws.rows
    #첫 행은 key로
    cells = next(g)
    keys = []           #키 값 모음 리스트 
    student_datas =[]   #학생 데이터 딕셔너리 리스트
    for cell in cells:
        keys.append(cell.value)
    #학생 데이터에 값을 저장
    for row in g:
        dic = {k : c.value for k,c in zip(keys,row)}
        student_datas.append(dic)
    return keys,student_datas


def get_score_list(subject,dic_list):
    """[과목명, 학생데이터를 받아서 해당 과목 점수만 리스트로 반환]

    Arguments:
        subject {[string]} -- [과목명]
        dic_list {[list]} -- [과목,점수 데이터]

    Returns:
        [list] -- [해당 과목에 대한 점수만 추출하여 리스트로 반환]
    """
    scores=[]
    for score in dic_list:
        scores.append(score.get(subject))
    return scores

def get_average(scores):
    sum=0
    try:
        for score in scores:
            sum += score
        return round(sum/len(scores), 2)
    except:
        return '값 오류'
def get_variance(scores,avrg):
    var=0
    try:
        for score in scores:
            var+=(score-avrg)**2
        return round(var/len(scores),2)
    except:
        return '값 오류'
def get_std_dev(variance):
    try:
        return round(mt.sqrt(variance),2)
    except:
        return '값 오류'


