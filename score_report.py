#成绩统计_定义函数内容
def get_level(score):
    '''功能：接收一个分数，返回它对应的等级
       score：分数，单位：分，范围 0~100
    '''
    if score >= 90:
        return '优秀'
    if score >= 80:
        return '良好'
    if score >= 70:
        return '中等'
    if score >= 60:
        return '及格'
    return '不及格'

def average(scores):
    '''功能：接收一个成绩列表，返回平均分
       scores：成绩列表，列表中的每个元素都是一个分数
    '''
    total = 0
    for s in scores:
        total = total + s
    return total / len(scores)

#---------------调用函数---------------
scores = [88, 95, 62, 74, 59]
for s in scores:
    print(s, '分：', get_level(s))
print('平均分：', average(scores))
