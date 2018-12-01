# -*- coding: utf-8 -*-
'''
Created on 2018年1月5日

@author: ls
'''

import os
import datetime
import shelve
import sys
    
    
if not os.path.exists('fee.db.dat'):
    print('初始化fee.db')
    with shelve.open('fee.db') as db:
        db['electron'] = [186]
        db['water'] = [657]

def totalRent(electriThis, waterThis, property_fee = 97.5, coef_Electron = 0.68, coef_water = 3.8, base = 1800):
    '''
    waterUse = [this month, last month]
    electriUse = [this month, last month]
    # 基本房租
    base = 1800
    
    # 电费系数
    coef_Electron = 0.68
    
    # 水费系数
    coef_water = 3.8
    
    # 物业费
    property_fee = 97.5
    '''
    with shelve.open('fee.db') as db:
        electriLast = db['electron'][-1]
        waterLast = db['water'][-1]
        
    
    water_fee = (waterThis - waterLast) * coef_water
    electri_fee = (electriThis - electriLast) * coef_Electron
    
    total = base + electri_fee + water_fee + property_fee

    print('实际电费：', electri_fee)
    print('实际水费：', water_fee)
    print('\n\n')
    
    print('----时间： ',datetime.datetime.now())
    print('\n')
    print("----基本：", base, "元")
    print('\n')
    print("----电费：(%s - %s) X %s = %.3f 元" %(electriThis, electriLast, coef_Electron, electri_fee))
    print('\n')
    print("----水费：(00%s - 00%s) X %s = %.3f 元" %(waterThis, waterLast, coef_water, water_fee))
    print('\n')
    print("----物业费：", property_fee, "元")
    print('\n')
    print("----合计：%s + %.3f + %.3f + %s = %.3f 元\n" % (base, electri_fee, water_fee, property_fee, total))
    print('\n')
    
    filePath = os.path.join(os.getcwd(),'log\\'+str(datetime.datetime.now()).replace(' ','-').replace(':','-')+'.log')
    with open(filePath, 'w') as f:
        f.write('----时间：  ' + str(datetime.datetime.now())+'------------------------------------------\n')
        f.write('\n')
        f.write("----基本：" + str(base) + " 元\n")
        f.write('\n')
        f.write("----电费：(%s - %s) X %s = %.3f 元\n" %(electriThis, electriLast, coef_Electron, electri_fee))
        f.write('\n')
        f.write("----水费：(00%s - 00%s) X %s = %.3f 元\n" %(waterThis, waterLast, coef_water, water_fee))
        f.write('\n')
        f.write("----物业费：" + str(property_fee) + " 元\n")
        f.write('\n')
        f.write("----合计：%s + %.3f + %.3f + %s = %.3f 元\n" % (base, electri_fee, water_fee, property_fee, total))
        f.write('\n')
        
    print('\n')
    print('日志路径：', filePath, '\n')

if __name__ == '__main__':
#     ini = input("是否打印默认输出？[y/n/enter]:\n")
#     if ini == 'y':
#         waterUse = 658
#         electriUse = 347.47
#         totalRent(electriUse, waterUse)
#          
#     if len(ini) == 0:
    script_path = os.path.split(os.path.abspath(sys.argv[0]))[0]
    print("script_path: %s" % script_path)
    electriThis = float(input('输入这个月的电表度数：\n'))
    waterThis = float(input('输入这个月的水表度数：\n'))
    print('\n')
    
    totalRent(electriThis, waterThis)
    
    save = input("是否保存这个月的数据,输入是'y'保存，按回车不保存\n")
    shelve_db_path = os.path.join(script_path, 'fee.db')
    if len(save) != 0:
        with shelve.open(shelve_db_path) as db:
            db['electron'] = db['electron'] + [electriThis]
            db['water'] = db['water'] + [waterThis]

    with shelve.open(shelve_db_path) as db:
        print('electron:', db['electron'])
        print('water:', db['water'])
        print('\n\n\n')

    
    
