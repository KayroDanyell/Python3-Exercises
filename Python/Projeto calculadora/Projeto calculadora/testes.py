import tkinter

#def main():
#    root = make_root()


#if __name__ == '__main__':
#    main()

#class Tk():
#   def __init__(self,master=None):
 #       self.__init__(self,master)
  #      self.msg = Label(self, text="Hello World")
   #     self.msg.pack()
    #    self.bye = Button(self, text="Bye", command=self.quit)
     #   self.bye.pack()
      #  self.pack()

#x = App()
#mainloop()
def window(title,back='#fff'):
    tk = tkinter.Tk()
    tk.title(title)
    tk.config(bg= back)
    return tk
def make_label(testo,):
    tk = tkinter.Tk()
    tk.label(window(),text=testo,master=False)
    tk.config(padx=10,bg='#fff')
    return tk
def execute():
    win = window('testando',back='#fff')
    #bot = make_label('butao')
    win.mainloop()

execute()