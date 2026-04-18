import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Rivals Proficiency Calculator')
root.geometry('300x300+50+50')
root.resizable(True, True)
root.attributes('-topmost', 1)



frame = ttk.Frame(root)

def runit(time, level, exp, wantlevel):
    templevel = level
    if level < 5:
        lvlexp = (templevel - 1) * 125
    elif level < 10:
        templevel -= 5
        lvlexp = (templevel * 240) + 500
    elif level < 15:
        templevel -= 10
        lvlexp = (templevel * 400) + 1700
    elif level < 20:
        templevel -= 15
        lvlexp = (templevel * 480) + 3700
    elif level < 50:
        templevel -= 20
        lvlexp = (templevel * 1600) + 6100
    else:
        templevel -= 50
        lvlexp = (templevel * 3100) + 54100
    totalexp = lvlexp + exp
    rate = time/totalexp

    if level < 20:
        prediction20 = rate * (6100 - totalexp)
        totalexp = 0
        multiplyer = 0
    else:
        prediction20 = 0
        totalexp -= 6100
        multiplyer = 2 / ((level / 5) - 3)

    if level < 70 & wantlevel == 70:
        prediction = (rate * (110000 - totalexp) / ((multiplyer/2) + 1)) + prediction20
    elif level < 65 & wantlevel == 65:
        prediction = (rate * (94500 - totalexp) / ((multiplyer/2) + 1)) + prediction20
    elif level < 60 & wantlevel == 60:
        prediction = (rate * (79000 - totalexp) / ((multiplyer/2) + 1)) + prediction20
    elif level < 55 & wantlevel == 55:
        prediction = (rate * (63500 - totalexp) / ((multiplyer/2) + 1)) + prediction20
    elif level < 50 & wantlevel == 50:
        prediction = (rate * (48000 - totalexp) / (multiplyer + 1)) + prediction20
    elif level < 45 & wantlevel == 45:
        prediction = (rate * (40000 - totalexp) / (multiplyer + 1)) + prediction20
    elif level < 40 & wantlevel == 40:
        prediction = (rate * (32000 - totalexp) / (multiplyer + 1)) + prediction20
    elif level < 35 & wantlevel == 35:
        prediction = (rate * (24000 - totalexp) / (multiplyer + 1)) + prediction20
    elif level < 30 & wantlevel == 30:
        prediction = (rate * (16000 - totalexp) / (multiplyer + 1)) + prediction20
    elif level < 25 & wantlevel == 25:
        prediction = (rate * (8000 - totalexp) / (multiplyer + 1)) + prediction20
    elif level < 20 & wantlevel == 20:
        prediction = prediction20
    else:
        prediction = 0
    output1.config(text="Time to level "+ str(wantlevel) +": "+ str(round(prediction,1)))


# place a label on the root window
header1 = ttk.Label(root, text="Enter Hours Played")
header1.pack(pady=3)

textInput1 = tk.DoubleVar()
textBox1 = ttk.Entry(root, textvariable=textInput1)
textBox1.pack()
textBox1.focus()

header2 = ttk.Label(root, text="Enter Level")
header2.pack(pady=3)

textInput2 = tk.IntVar()
textBox2 = ttk.Entry(root, textvariable=textInput2)
textBox2.pack()

header3 = ttk.Label(root, text="Enter Level EXP")
header3.pack(pady=3)

textInput3 = tk.IntVar()
textBox3 = ttk.Entry(root, textvariable=textInput3)
textBox3.pack()

header4 = ttk.Label(root, text="Enter Desired Level")
header4.pack(pady=3)
# spinbox
spinValue = tk.IntVar(value=70)
spinBox = ttk.Spinbox(
    root,
    from_=20,
    to=70,
    values=(20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70),
    textvariable=spinValue,
    wrap=False)

spinBox.pack()

Button1 = ttk.Button(root, text="Calculate", command=lambda: runit(textInput1.get(),
                                textInput2.get(), textInput3.get(), spinValue.get()))
Button1.pack(pady=5)

output1 = ttk.Label(frame)
output1.pack(pady=1)

frame.pack(padx=5, pady=5)
# keep the window displaying
root.mainloop()

