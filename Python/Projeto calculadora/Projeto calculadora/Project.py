import tkinter as tk

def make_root():
    root = tk.Tk()
    root.title('Calculator')
    root.config(padx=25, pady=20, background='#fff')
    return root

def make_label(root):
    label = tk.label(
        root, text = 'Cudecurioso',
        anchor = 'e', justify = 'right', background = '#fff'
    )
    label.grid(row=0,column=0,columnspan=5)
    return label


def main():
    root = make_root()
    root.mainloop()

x = {'Matrix':22, 'Joege':345, 'Luana': 678}
for c,v in x.items():
    print(c)
    print(v)

