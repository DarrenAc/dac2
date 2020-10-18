# -*- coding: utf-8 -*-
import functions

#菜单栏展示
print("########################简易计算器########################")
print("     请选择运算：")
print("     1、相加")
print("     2、相减")
print("     3、相乘")
print("     4、相除")
print("########################  v1.0  ########################")


choice = int(input("请输入您的选择（1/2/3/4）"))

#判断选择是否正确
if choice != 1 and choice != 2 and choice !=3 and choice!= 4:
    print("您的选择有误，请重新选择！")
    choice = int(input("请输入您的选择（1/2/3/4）"))

num1 = int(input("请输入第一个数字: "))
num2 = int(input("请输入第二个数字: "))

if choice == 1:
    print(num1, "+", num2, "=", functions.add(num1, num2))

if choice == 2:
    print(num1, "-", num2, "=", functions.subtract(num1, num2))

if choice == 3:
    print(num1, "*", num2, "=", functions.multiply(num1, num2))

if choice == 4:
    if num2 == 0:
        print("除数不能为零！")
    else:
        print(num1, "/", num2, "=", functions.divide(num1, num2))
