#!/usr/bin/python3
#-*-coding: utf-8-*-
'''
MIT License

Copyright (c) 2018 Susliakov Vitalii Vladimirovich

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''
'''
    The latest version is always on the
    https://github.com/polsksu/pyCalc
'''

'''
    Imports of libs
    Импорт библиотек
'''
from sys import version_info
import decimal as dec
if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk

'''
    Main part
    Основной код
'''
class pyCalc:

    '''
        Count of numerals atfer point
        Кол-во знаков после запятой
    '''
    dec.getcontext().prec = 16

    '''
        Func that include equal and arithmetic buttons
        Функция, включающая в себя кнопки равно и арифметических действий
    '''
    def arithmetic(self,sigh=''):
        try:
            if self.secondaryAreaVar.get() != '':
                if sigh != self.secondaryAreaVar.get()[-1]:
                    if self.secondaryAreaVar.get()[-1] == '+':
                        self.arithmetic('+')
                    elif self.secondaryAreaVar.get()[-1] == '-':
                        self.arithmetic('-')
                    elif self.secondaryAreaVar.get()[-1] == '*':
                        self.arithmetic('*')
                    elif self.secondaryAreaVar.get()[-1] == '/':
                        self.arithmetic('/')

                if (self.primaryArea.get()).find('.') != -1 or (self.secondaryAreaVar.get()).find('.') != -1:
                    if self.primaryArea.get() != '0':
                        if sigh == '+':
                            self.secondaryAreaVar.set(str(dec.Decimal(self.secondaryAreaVar.get()[:-2]) + dec.Decimal(self.primaryArea.get())))
                        elif sigh == '-':
                            self.secondaryAreaVar.set(str(dec.Decimal(self.secondaryAreaVar.get()[:-2]) - dec.Decimal(self.primaryArea.get())))
                        elif sigh == '*':
                            self.secondaryAreaVar.set(str(dec.Decimal(self.secondaryAreaVar.get()[:-2]) * dec.Decimal(self.primaryArea.get())))
                        elif sigh == '/':
                            self.secondaryAreaVar.set(str(dec.Decimal(self.secondaryAreaVar.get()[:-2]) / dec.Decimal(self.primaryArea.get())))
                    else:
                        self.secondaryAreaVar.set(self.secondaryAreaVar.get()[:-2])

                    self.secondaryAreaVar.set(self.secondaryAreaVar.get() + ' ' + sigh)
                    self.primaryArea.delete(0,'end')
                    self.primaryArea.insert(0,'0')

                else:
                    if self.primaryArea.get() != '0':
                        if sigh == '+':
                            self.secondaryAreaVar.set(str(int(self.secondaryAreaVar.get()[:-2]) + int(self.primaryArea.get())))
                        elif sigh == '-':
                            self.secondaryAreaVar.set(str(int(self.secondaryAreaVar.get()[:-2]) - int(self.primaryArea.get())))
                        elif sigh == '*':
                            self.secondaryAreaVar.set(str(int(self.secondaryAreaVar.get()[:-2]) * int(self.primaryArea.get())))
                        elif sigh == '/':
                            self.secondaryAreaVar.set(str(int(self.secondaryAreaVar.get()[:-2]) / int(self.primaryArea.get())))
                    else:
                        self.secondaryAreaVar.set(self.secondaryAreaVar.get()[:-2])
                    self.secondaryAreaVar.set(self.secondaryAreaVar.get() + ' ' + sigh)
                    self.primaryArea.delete(0,'end')
                    self.primaryArea.insert(0,'0')
            else:
                self.secondaryAreaVar.set(self.primaryArea.get() + ' ' + sigh)
                self.primaryArea.delete(0,'end')
                self.primaryArea.insert(0,'0')
        except Exception:
            self.secondaryAreaVar.set('')
            self.primaryArea.delete(0,'end')
            self.primaryArea.insert(0,'An error was occured!')

    def equals(self):
        try:
            if (self.primaryArea.get()).find('.') != -1 or (self.secondaryAreaVar.get()).find('.') != -1:

                if self.secondaryAreaVar.get() != '':
                    if self.secondaryAreaVar.get()[-1] == '+':
                        result = str(dec.Decimal(self.secondaryAreaVar.get()[:-2]) + dec.Decimal(self.primaryArea.get()))
                    elif self.secondaryAreaVar.get()[-1] == '-':
                        result = str(dec.Decimal(self.secondaryAreaVar.get()[:-2]) - dec.Decimal(self.primaryArea.get()))
                    elif self.secondaryAreaVar.get()[-1] == '*':
                        result = str(dec.Decimal(self.secondaryAreaVar.get()[:-2]) * dec.Decimal(self.primaryArea.get()))
                    elif self.secondaryAreaVar.get()[-1] == '/':
                        result = str(dec.Decimal(self.secondaryAreaVar.get()[:-2]) / dec.Decimal(self.primaryArea.get()))

                    self.secondaryAreaVar.set('')
                    self.primaryArea.delete(0,'end')
                    self.primaryArea.insert(0,result)

            else:

                if self.secondaryAreaVar.get() != '':
                    if self.secondaryAreaVar.get()[-1] == '+':
                        result = str(int(self.secondaryAreaVar.get()[:-2]) + int(self.primaryArea.get()))
                    elif self.secondaryAreaVar.get()[-1] == '-':
                        result = str(int(self.secondaryAreaVar.get()[:-2]) - int(self.primaryArea.get()))
                    elif self.secondaryAreaVar.get()[-1] == '*':
                        result = str(int(self.secondaryAreaVar.get()[:-2]) * int(self.primaryArea.get()))
                    elif self.secondaryAreaVar.get()[-1] == '/':
                        result = str(int(self.secondaryAreaVar.get()[:-2]) / int(self.primaryArea.get()))

                    self.secondaryAreaVar.set('')
                    self.primaryArea.delete(0,'end')
                    self.primaryArea.insert(0,result)
        except Exception:
            self.secondaryAreaVar.set('')
            self.primaryArea.delete(0,'end')
            self.primaryArea.insert(0,'An error was occured!')


    '''
        Func that clear input panel by numeric
        Функция, очищающая панель ввода по символу
    '''
    def delete1(self):
        self.primaryArea.delete(len(self.primaryArea.get()) - 1)
        if self.primaryArea.get() == '':
            self.primaryArea.insert(0,'0')

    '''
        Func that clear all panels
        Функция, очищающая панели
    '''
    def deleteAll(self, arg):
        self.primaryArea.delete(0,'end')
        self.primaryArea.insert(0,'0')
        if arg == 'C':
           self.secondaryAreaVar.set('')

    '''
        Func that input point for float number
        Функция, которая вводит точку для числа с плавающей точкой(!)
    '''
    def point(self):
        if not '.' in self.primaryArea.get():
            self.primaryArea.insert('end','.')

    '''
        Func that input numeric in the input panel
        Функция, которая вводит цифру в панель ввода
    '''
    def numkey(self, number):
        if self.primaryArea.get() == '0':
            self.primaryArea.delete(0,'end')
        self.primaryArea.insert('end',number)

    ''' 
        Primary func
        Основная функция
    '''
    def __init__(self, master):

        '''
            Change of standart "tk" window title
            Замена заголовка окна
        '''
        master.title('pyCalc')

        '''
            Ban of change the window's size
            Запрет на изменение размера окна
        '''
        master.resizable(width=False, height=False)

        '''
            Generation of input panel
            Генерация панели ввода
        '''
        self.primaryArea = tk.Entry(master,justify='right',relief='flat',font='sans-serif 12',width=20)
        self.primaryArea.grid(row=1,column=0,columnspan=4,sticky='wens')
        self.primaryArea.insert(0,'0')

        ''' 
            Generation of panel with previous calculate
            Генерация панели предыдущих вычислений
        '''
        self.secondaryAreaVar = tk.StringVar()
        self.secondaryArea = tk.Label(master,anchor='e',font='sans-serif 8',bg='white',fg='#686868',width=20,textvariable=self.secondaryAreaVar)
        self.secondaryArea.grid(row=0,column=0,columnspan=4,sticky='wens')

        self.debugAreaVar = tk.StringVar()
        self.debugArea = tk.Label(master,anchor='e',font='sans-serif 8',bg='white',fg='#686868',width=20,textvariable=self.debugAreaVar)
        self.debugArea.grid(row=7,column=0,columnspan=4,sticky='wens')   

        ''' 
            Button generation 
            Генерация кнопок
        '''
        tk.Button(master,text='=',font='sans-serif 16',width=2,justify='center',command=lambda:self.equals()).grid(row=2,column=3,sticky='wens')
        tk.Button(master,text='+',font='sans-serif 16',width=2,justify='center',command=lambda:self.arithmetic('+')).grid(row=3,column=3,sticky='wens')
        tk.Button(master,text='-',font='sans-serif 16',width=2,justify='center',command=lambda:self.arithmetic('-')).grid(row=4,column=3,sticky='wens')
        tk.Button(master,text='*',font='sans-serif 16',width=2,justify='center',command=lambda:self.arithmetic('*')).grid(row=5,column=3,sticky='wens')
        tk.Button(master,text='/',font='sans-serif 16',width=2,justify='center',command=lambda:self.arithmetic('/')).grid(row=6,column=3,sticky='wens')
        tk.Button(master,text='←',font='sans-serif 16',width=2,justify='center',command=lambda:self.delete1()).grid(row=2,column=0,sticky='wens')
        tk.Button(master,text='C',font='sans-serif 16',width=2,justify='center',command=lambda:self.deleteAll('C')).grid(row=2,column=1,sticky='wens')
        tk.Button(master,text='CE',font='sans-serif 16',width=2,justify='center',command=lambda:self.deleteAll('CE')).grid(row=2,column=2,sticky='wens')
        tk.Button(master,text='0',font='sans-serif 16',width=4,justify='center',command=lambda:self.numkey('0')).grid(row=6,column=0,columnspan=2,sticky='wens')
        tk.Button(master,text='1',font='sans-serif 16',width=2,justify='center',command=lambda:self.numkey('1')).grid(row=5,column=0,sticky='wens')
        tk.Button(master,text='2',font='sans-serif 16',width=2,justify='center',command=lambda:self.numkey('2')).grid(row=5,column=1,sticky='wens')
        tk.Button(master,text='3',font='sans-serif 16',width=2,justify='center',command=lambda:self.numkey('3')).grid(row=5,column=2,sticky='wens')
        tk.Button(master,text='4',font='sans-serif 16',width=2,justify='center',command=lambda:self.numkey('4')).grid(row=4,column=0,sticky='wens')
        tk.Button(master,text='5',font='sans-serif 16',width=2,justify='center',command=lambda:self.numkey('5')).grid(row=4,column=1,sticky='wens')
        tk.Button(master,text='6',font='sans-serif 16',width=2,justify='center',command=lambda:self.numkey('6')).grid(row=4,column=2,sticky='wens')
        tk.Button(master,text='7',font='sans-serif 16',width=2,justify='center',command=lambda:self.numkey('7')).grid(row=3,column=0,sticky='wens')
        tk.Button(master,text='8',font='sans-serif 16',width=2,justify='center',command=lambda:self.numkey('8')).grid(row=3,column=1,sticky='wens')
        tk.Button(master,text='9',font='sans-serif 16',width=2,justify='center',command=lambda:self.numkey('9')).grid(row=3,column=2,sticky='wens')
        tk.Button(master,text='.',font='sans-serif 16',width=2,justify='center',command=lambda:self.point()).grid(row=6,column=2,sticky='wens')

if __name__ == '__main__':
    root = tk.Tk()       
    app = pyCalc(root)   # Object initialization
                         # Инициализация объекта
    root.mainloop()      
