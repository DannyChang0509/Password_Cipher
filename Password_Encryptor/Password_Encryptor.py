import tkinter as tk

window = tk.Tk()
window.title('Password_Encryptor')
window.geometry('500x300')

l = tk.Label(window, text = 'Password:')
l.place(x = 100, y = 10, anchor = 'n')

PWD = tk.StringVar()
e = tk.Entry(window, textvariable = PWD, width = 20, show = '*')
e.place(x = 250, y = 10, anchor = 'n')

def ShowPassword():
    if(SP.get() == 0):
        e.config(show = '*')
    else:
        e.config(show = '')

SP = tk.IntVar()
c = tk.Checkbutton(window, text = 'Show Password', variable = SP, onvalue = 1, offvalue = 0, command = ShowPassword)
c.place(x = 400, y = 10, anchor = 'n')

tk.Label(window, text = 'Encryption Strength:').place(x = 100, y = 55, anchor = 'n')
s = tk.Scale(window, from_= 1, to = 3, orient = tk.HORIZONTAL, length = 100, showvalue = 3, tickinterval = 1, resolution = 1)
s.place(x = 250, y = 40, anchor = 'n')

tk.Label(window, text = 'Entrypted Password:').place(x = 100, y = 150, anchor = 'n')

output = tk.Text(window, width = 20, height = 1)
output.place(x = 250, y = 150, anchor = 'n')

tk.Label(window, text = '設計:張詠翔').place(x = 495, y = 290, anchor = 'e')

def GO():
    P = PWD.get()
    New_PWD = list(str(P))
    S = int(s.get())
    if(S >= 1):
        tem1 = New_PWD.copy()
        a = 0
        b = -1
        for i in range(len(tem1)):
            if(i%2 == 0):
                New_PWD[i] = tem1[a]
                a += 1
            else:
                New_PWD[i] = tem1[b]
                b -= 1
    if(S >= 2):
        New_PWD.reverse()
    if(S >= 3):
        tem2 = New_PWD.copy()
        for i in range(len(tem2)):
            New_PWD[i] = chr(ord(tem2[i])+9)
    N_PWD = ""
    for i in range(len(New_PWD)):
        N_PWD += str(New_PWD[i])
    output.delete(1.0, "end")
    output.insert('insert', N_PWD)

b = tk.Button(window, text = 'Encrypt', width = 10, height = 1, command = GO)
b.place(x = 250, y = 100, anchor = 'n')

window.mainloop()