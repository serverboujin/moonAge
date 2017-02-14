# -*- coding: utf-8 -*-

import datetime

today = datetime.date.today()
y = today.year
m = today.month
d = today.day

def moonAge():
    cM = [None, 0, 2, 0, 2, 2, 4, 5, 6, 7, 8, 9, 10]
    moon = ((( y-11 ) % 19) * 11 + cM[m] + d) % 30
    while moon > 30:
        moon = moon - 30

    return moon

def moonName():
    moonName = [None, '新月', '二日月', '三日月', None, None,
        None, '上弦の月', '上弦の月', None, None, None,
        None, '十三夜', '小望月（こもちづき）', '十五夜', '十六夜（いざよい）', '十七夜（じゅうしちや）', '居待月（いまちづき）',
        '寝待月（ねまちづき）', '更待月（ふけまちづき）', None, '下弦の月', '二十三夜', None,
        None, '二十六夜', None, None, '晦（つごもり）', '三十日（みそか）']
    return (moonName[moonAge()])

if __name__ == '__main__':
    dd = [1,2,3,7,8,13,14,15,16,17,18,19,20,22,23,26,29,30]

    print ("月齢をお知らせするPythonプログラムです")
    print ("今日の月齢を表示(0)／任意の日付の月齢を表示(1)")
    start = int(input ("0 / 1 >> "))

    if start == 0:
        print ("\n今日の月齢はおよそ %s です。" % moonAge())
        if d in dd:
            print ("%s です！" % moonName())
    elif start == 1:
        y = int(input ("年？>> "))
        m = int(input ("月？>> "))
        d = int(input ("日？>> "))
        print ("\n今日の月齢はおよそ %s です。" % moonAge())
        if d in dd:
            print ("%s です！" % moonName())

    fin = input ("\n\n終了します。何かキーを押してください…")
