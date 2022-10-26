from PySimpleGUI import *

layout =[
    [Text('0', key_=_'input')],

    [ReadFormButton('1'), ReadFormButton('2'), ReadFormButton('3'), ReadFormButton('+')],
    
    [ReadFormButton('4'), ReadFormButton('5'), ReadFormButton('6'), ReadFormButton('-')],
    
    [ReadFormButton('7'), ReadFormButton('8'), ReadFormButton('9'), ReadFormButton('*')],
    
    [ReadFormButton('0'), ReadFormButton('.'), ReadFormButton('='), ReadFormButton('/')],
    
    windows = FlexForm('Calculator')
    
    
    windows.Layout(layout)
    while True:
        button, values = windows.Read()
        if button is None:
            break
        print(button, values)
    windows.Close()
    
    if buttin == 'Exit' or button is None:
    windows.close()
    
    result = 0
    
    
          
 