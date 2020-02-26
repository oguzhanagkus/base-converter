from tkinter import *

def convert(v, b):
    temp_array = []

    while(v > b-1):
        temp_1 = v // b
        temp_2 = v % b

        if(b > 10):
            temp_array.append(f"({temp_2})")

        else:
            temp_array.append(str(temp_2))

        v = temp_1

    if(b > 10):
        temp_array.append(f"({temp_1})")

    else:
        temp_array.append(str(temp_1))

    temp_array. reverse()
    answer = "".join(temp_array)

    return answer

def calculate():
    if(value.get().isdigit() == False or base.get().isdigit() == False):
        result.config(text = "Values should be positive integer.", font = "calibri 15 bold")

    else:
        v = int(value.get())
        b = int(base.get())

        if(v < b):
            result.config(text = "Value should be bigger than base.", font = "calibri 15 bold")

        else:
            if(b <= 1):
                result.config(text= "Base should be bigger than 1.", font = "calibri 15 bold")

            else:
                answer = convert(v, b)
                result.config(text = answer, font = "calibri 15 bold")

window = Tk()
window.tk_setPalette("#D24D57")
window.geometry("450x250+250+250")
window.title("Base Converter")

get_value = Label(window, pady = 10)
get_value.config(text = "Value in base 10", font = "calibri 12 bold")
get_value.pack()

value = Entry(window, font = "calibri 12 bold")
value.pack()

get_base = Label(window, pady = 10)
get_base.config(text = "Base you want to convert", font = "calibri 12 bold")
get_base.pack()

base = Entry(window, font = "calibri 12 bold")
base.pack()

blank = Label(window)
blank.pack()

button = Button(window)
button.config(text = "Convert", font = "calibri 12 bold", command = calculate)
button.pack()

result = Label(window, pady = 15)
result.config(text = "")
result.pack()

window.mainloop()
