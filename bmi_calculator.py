#BMI_08函数课程内容
def fun_bmi(name,height,weight):
    '''功能：根据身高和体重计算BMI指数
       name：姓名
       height：身高，单位：米
       weight：体重，单位：千克
    '''
    print(name + '的身高：' + str(height) + '米，'+'体重：'+str(weight) +'千克')
    bmi = weight/(height*height)
    print(name + '的Bmi指数为：' + str(bmi))

    if bmi < 18.5:
        print('你的体重过轻，ono')
    if bmi >= 18.5 and bmi <24.9:
        print('你的体重在正常范围，good！')
    if bmi >= 24.9 and bmi <29.9:
        print('你的体重过重')
    if bmi>= 29.9:
        print('有点肥胖')
#测试函数fun_bmi实例
fun_bmi(name = 'happy',height = 1.56,weight = 56)
fun_bmi(name = 'unhappy',height = 1.64,weight = 50)