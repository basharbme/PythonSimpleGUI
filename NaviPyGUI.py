from Tkinter import *
import tkFont
import time


largeFont= ("Verdana", 20)
smallFont= ("Verdana", 12)
miniFont=("Verdana",8)


class NaviPyApp(Tk):

    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        Tk.wm_title(self, "NaviPy Client")
        
        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        
        label = Label(self, text="Welcome to NaviPyGUI.", font=largeFont)
        label.pack(pady=10,padx=10)
        
        description_label = Label(self, text="Manually select buttons below to navigate.", font=smallFont)
        description_label.pack(pady=0,padx=10)
        
        button = Button(self, text="Nav to Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack(expand=YES)

        button2 = Button(self, text="Nav to Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(expand=YES)


class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Welcome to Page One.", font=largeFont)
        label.pack(pady=10,padx=10)

        description_label = Label(self, text="Manually select buttons below to trigger action.", font=smallFont)
        description_label.pack(pady=0,padx=10)

        button1 = Button(self, text="ButtonOne",
                           command=lambda: actionSelect("ButtonOne") )
        button1.pack(pady=(10,0),padx=10)
        
        button2 = Button(self, text="ButtonTwo",
                            command=lambda: actionSelect("ButtonTwo"))
        button2.pack(pady=0,padx=10)
        
        button3 = Button(self, text="ButtonThree",
                            command=lambda: actionSelect("ButtonThree"))
        button3.pack(pady=0,padx=10)
        
        button4 = Button(self, text="ButtonFour",
                            command=lambda: actionSelect("ButtonFour"))
        button4.pack(pady=(0,10),padx=10)

        label2 = Button(self, text="actionView.", font=miniFont,
                            command=lambda: toggle("#51E49A"))
        label2.pack(pady=10,padx=10)
        
        homeButton = Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        homeButton.pack()

        autonButton = Button(self, text="Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        autonButton.pack()

        def actionSelect(name):
            label2.config(text=name+' selected')
            #print(name+' selected')

        def toggle(color):
            getColor = label2.cget("highlightbackground")
            if  getColor==color:
                label2.config(highlightbackground="white")
            else:
                label2.config(highlightbackground=color)
            #print("color toggled")

class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Welcome to Page Two.", font=largeFont)
        label.pack(pady=10,padx=10)
        
        #prepare objects for display
        iC = itemCollection()
        listCategories = list(iC.categoryOne + iC.categoryTwo + iC.categoryThree)
        listCategories.sort()

        #config list for display
        displayList = Listbox(self)
        for item in listCategories:
            displayList.insert(END, item)
        displayList.bind("<Double-Button-1>", self.OnDouble)
        displayList.pack(fill=BOTH, expand=YES,pady=(0,0),padx=(5,5))
        
        #config scrollbar to displayed list
        scroll = Scrollbar(displayList)
        scroll.pack(side=RIGHT, fill=Y, expand=NO)
        scroll.configure(command=displayList.yview)

        displayList.configure(yscrollcommand=scroll.set)
            
        homeButton = Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        homeButton.pack(side=LEFT,pady=(10,5),padx=(5,0))

        manualButton = Button(self,
                              text="Manual Mode",
                              command=lambda: controller.show_frame(PageOne))
        manualButton.pack(side=RIGHT,pady=(10,5),padx=(0,5))
        
    def OnDouble(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        sel = selection[0]
        
        #print('selection:', selection,'int: ',sel,'name: %s' % value)
        return self.makeSelection(sel)

    def makeSelection(self, argument):
        #print('the selection: ',argument)
        cf=combinationFunctions()
        if argument == 0:
            return cf.actionOne(argument)
        elif argument == 1:
            return cf.actionTwo(argument)
        else:
            return cf.actionThree(argument)
    
class combinationFunctions():
    
    def actionOne(self, num):
        print('action 1 selection at index '+str(num))
    
    def actionTwo(sel, num):
        print('action 2, selection at index '+str(num))

    def actionThree(self, num):
        print('action 3, selection at index '+str(num))

class itemCollection():
    categoryOne = ["First","First","First","First","First","First","First","First"]
    categoryTwo = ["Second","Second","Second","Second","Second","Second","Second","Second"]
    categoryThree = ["Third","Third","Third","Third","Third","Third","Third","Third",]
        
app = NaviPyApp()
app.mainloop()
