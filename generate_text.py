'''
采用随机算法生成语句 -V1.1版
++++++++++++++++++++++

考虑到机器学习的文本量需要非常
大才能实现较精准的自然语言输出
所以暂时采用此法来生成日志内容



++++++++++++++++++++++

'''

import random


today_lst = ['数据分析','测试新功能','整理计划','查数据','数据分析','运营数据分析',
             '加班','数据分析','数据分析','查数据','查数据'
    ]
tmr_lst = ['继续没做完的','调整状态','查数据','补完未完成的','新的学习计划','新的学习计划',
           '新工作内容','爬虫','考虑加班','保持专注不被干扰'
    ]
exp_lst = ['还不错','空气差','需要休息了','加油','加油','加油','还不错'
    ]
emoji_lst = ['[耶]','[赞]','[拍手]','[困]','[白眼]','[思考]','','','','','','','','',
             '','','','',
    ]


def today():
    num = random.randint(1,3)
    
    return (','.join(list(set(random.sample(today_lst,num)))))

def tmr():
    num = random.randint(1,4)
    
    return (','.join(list(set(random.sample(tmr_lst,num)))))

def exp():
    num = random.randint(1,2)
    exp_content = list(set(random.sample(exp_lst,num)))
    exp_content.append(random.choice(emoji_lst))
    if exp_content[-1] == '':
        return (','.join(exp_content[:-1]))
    else:
        return (','.join(exp_content))
