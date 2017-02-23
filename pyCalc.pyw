#!/usr/bin/python3
#-*-coding: utf-8-*-

'''
    This is a little text about OOP. So, I can't do it!
    Маленькое предисловие, я никогда до этого не программировал 
    объектно-ориентированно, поэтому контролируйте свои тряпки,
    летящие в меня.
'''

import tkinter as tk

class pyCalc:

    '''
        Func that include equal and arithmetic buttons
        Функция, включающая в себя кнопки равно и арифметических действий
    '''
    def equalsAndActions(self,sigh=''):
        try:
            if self.secondaryAreaVar.get() != '':
                if (self.primaryArea.get()).find('.') != -1 or (self.secondaryAreaVar.get()).find('.') != -1:
                    if sigh == '':
                        if self.secondaryAreaVar.get()[-1] == '+':
                            result = str(float(self.secondaryAreaVar.get()[:-2]) + float(self.primaryArea.get()))
                        elif self.secondaryAreaVar.get()[-1] == '-':
                            result = str(float(self.secondaryAreaVar.get()[:-2]) - float(self.primaryArea.get()))
                        elif self.secondaryAreaVar.get()[-1] == '*':
                            result = str(float(self.secondaryAreaVar.get()[:-2]) * float(self.primaryArea.get()))
                        elif self.secondaryAreaVar.get()[-1] == '/':
                            result = str(float(self.secondaryAreaVar.get()[:-2]) / float(self.primaryArea.get()))

                        self.secondaryAreaVar.set('')
                        self.primaryArea.delete(0,'end')
                        self.primaryArea.insert(0,result)
                    else:
                        if sigh == '+':
                            self.secondaryAreaVar.set(str(float(self.secondaryAreaVar.get()[:-2]) + float(self.primaryArea.get())))
                        elif sigh == '-':
                            self.secondaryAreaVar.set(str(float(self.secondaryAreaVar.get()[:-2]) - float(self.primaryArea.get())))
                        elif sigh == '*':
                            self.secondaryAreaVar.set(str(float(self.secondaryAreaVar.get()[:-2]) * float(self.primaryArea.get())))
                        elif sigh == '/':
                            self.secondaryAreaVar.set(str(float(self.secondaryAreaVar.get()[:-2]) / float(self.primaryArea.get())))
                        self.secondaryAreaVar.set(self.secondaryAreaVar.get() + ' ' + sigh)
                        self.primaryArea.delete(0,'end')
                        self.primaryArea.insert(0,'0')

                else:
                    if sigh == '':
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
                    else:
                        if sigh == '+':
                            self.secondaryAreaVar.set(str(int(self.secondaryAreaVar.get()[:-2]) + int(self.primaryArea.get())))
                        elif sigh == '-':
                            self.secondaryAreaVar.set(str(int(self.secondaryAreaVar.get()[:-2]) - int(self.primaryArea.get())))
                        elif sigh == '*':
                            self.secondaryAreaVar.set(str(int(self.secondaryAreaVar.get()[:-2]) * int(self.primaryArea.get())))
                        elif sigh == '/':
                            self.secondaryAreaVar.set(str(int(self.secondaryAreaVar.get()[:-2]) / int(self.primaryArea.get())))
                        self.secondaryAreaVar.set(self.secondaryAreaVar.get() + ' ' + sigh)
                        self.primaryArea.delete(0,'end')
                        self.primaryArea.insert(0,'0')
            else:
                if sigh != '':
                    self.secondaryAreaVar.set(self.primaryArea.get() + ' ' + sigh)
                    self.primaryArea.delete(0,'end')
                    self.primaryArea.insert(0,'0')
        except Exception:
            self.secondaryAreaVar.set('')
            self.primaryArea.delete(0,'end')
            self.primaryArea.insert(0,'An error was occured')

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
    def deleteAll(self):
        self.primaryArea.delete(0,'end')
        self.primaryArea.insert(0,'0')
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
        super(pyCalc, self).__init__()

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

        ''' 
            Button generation 
            Генерация кнопок
        '''
        tk.Button(master,text='=',font='sans-serif 16',width=4,justify='center',command=lambda:self.equalsAndActions()).grid(row=2,column=2,columnspan=2,sticky='wens')
        tk.Button(master,text='+',font='sans-serif 16',width=2,justify='center',command=lambda:self.equalsAndActions('+')).grid(row=3,column=3,sticky='wens')
        tk.Button(master,text='-',font='sans-serif 16',width=2,justify='center',command=lambda:self.equalsAndActions('-')).grid(row=4,column=3,sticky='wens')
        tk.Button(master,text='*',font='sans-serif 16',width=2,justify='center',command=lambda:self.equalsAndActions('*')).grid(row=5,column=3,sticky='wens')
        tk.Button(master,text='/',font='sans-serif 16',width=2,justify='center',command=lambda:self.equalsAndActions('/')).grid(row=6,column=3,sticky='wens')
        tk.Button(master,text='←',font='sans-serif 16',width=2,justify='center',command=lambda:self.delete1()).grid(row=2,column=0,sticky='wens')
        tk.Button(master,text='C',font='sans-serif 16',width=2,justify='center',command=lambda:self.deleteAll()).grid(row=2,column=1,sticky='wens')
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