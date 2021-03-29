from tkinter import *
from tkinter.messagebox import *
from webbrowser import open
from Calculate import run_line

text = ''
identval = dict()


def MainWindow(event=None):

    def output(result):
        global text
        txtresult.configure(state=NORMAL)
        text = str(result)
        txtresult.insert('end', result)
        txtresult.insert('end', '\n')
        txtresult.configure(state=DISABLED)

    def execute(events=None):
        global identval
        s = etycode.get()
        etycode.delete(0, 'end')
        identval = run_line(s, output)
        txtcode.configure(state=NORMAL)
        txtcode.insert('end', s)
        txtcode.insert('end', '\n')
        txtcode.configure(state=DISABLED)

    def copylast(events=None):
        global text
        pop = Tk()
        pop.title('Last Result to be copied')
        pop.geometry('300x150')
        ent = Entry(pop)
        ent.insert('end', text)
        ent.config(relief=FLAT, state='readonly')
        ent.pack(anchor=CENTER, fill=BOTH)
        pop.mainloop()

    def close(events=None):
        window.quit()
        window.destroy()

    def cut(events=None):
        etycode.event_generate("<<Cut>>")

    def copy(events=None):
        etycode.event_generate("<<Copy>>")

    def paste(events=None):
        etycode.event_generate("<<Paste>>")

    def varview():

        def varpack():
            for key in identval:
                txtiden.configure(state=NORMAL)
                txtiden.insert('end', str(key))
                txtiden.insert('end', '\n')
                txtiden.configure(state=DISABLED)
                txtval.configure(state=NORMAL)
                txtval.insert('end', str(identval[key]))
                txtval.insert('end', '\n')
                txtval.configure(state=DISABLED)

        var = Tk()
        var.title('List of Variables Declared')
        var.geometry('1200x600')
        fl = Frame(var)
        fr = Frame(var)
        fl.pack(side=LEFT, expand=YES)
        fr.pack(side=RIGHT, expand=YES)
        lbliden = Label(fl, anchor=NW, text='Identifiers: ', padx=10, pady=10)
        lbliden.pack()
        lblval = Label(fr, anchor=NW, text='Values: ', padx=10, pady=10)
        lblval.pack()
        txtiden = Text(fl, height=300, state=DISABLED)
        txtval = Text(fr, height=300, state=DISABLED)
        txtiden.pack(side=LEFT, fill=Y, padx=10, pady=10)
        txtval.pack(side=LEFT, fill=Y, padx=10, pady=10)
        sbiden = Scrollbar(fl)
        sbval = Scrollbar(fr)
        sbiden.pack(side=RIGHT, fill=Y)
        sbval.pack(side=RIGHT, fill=Y)
        varpack()
        var.mainloop()

    def showhelp():
        open("Language_Description.html")

    def upload():
        open("https://github.com/Benzene-gugugu/Mini-CAS-Calculator/issues/new")

    window = Tk()
    window.title('Python Computer Algebra System Calculator')
    window.geometry('1200x600')
    window.resizable(FALSE, FALSE)

    frame_b = Frame(window)
    frame_b.pack(side=BOTTOM, fill=X)
    btncopy = Button(frame_b, text='Copy Last Result', command=copylast)
    btncopy.pack(side=RIGHT, anchor=SE, padx=10, pady=10)
    btnexec = Button(frame_b, text='Execute', command=execute)
    btnexec.pack(side=RIGHT, anchor=SE, padx=10, pady=10)
    etycode = Entry(frame_b)
    etycode.bind('<Return>', execute)
    etycode.focus()
    etycode.pack(side=BOTTOM, anchor=S, fill=X, padx=10, pady=10)

    frame_l = Frame(window)
    frame_r = Frame(window)
    frame_l.pack(side=LEFT, expand=YES)
    frame_r.pack(side=RIGHT, expand=YES)
    lblcode = Label(frame_l, anchor=NW, text='History Code: ', padx=10, pady=10)
    lblcode.pack()
    lblresult = Label(frame_r, anchor=NW, text='History Result: ', padx=10, pady=10)
    lblresult.pack()
    txtcode = Text(frame_l, height=300, state=DISABLED)
    txtresult = Text(frame_r, height=300, state=DISABLED)
    txtcode.pack(side=LEFT, fill=Y, padx=10, pady=10)
    txtresult.pack(side=LEFT, fill=Y, padx=10, pady=10)
    sbcode = Scrollbar(frame_l)
    sbresult = Scrollbar(frame_r)
    sbcode.pack(side=RIGHT, fill=Y)
    sbresult.pack(side=RIGHT, fill=Y)

    menubar = Menu(window)

    filemenu = Menu(menubar, tearoff=FALSE)
    filemenu.add_command(label='New', command=MainWindow, accelerator='Ctrl+N')
    window.bind_all('<Control-n>', MainWindow)
    filemenu.add_separator()
    filemenu.add_command(label='Quit', command=close, accelerator='Ctrl+Q')
    window.bind_all('<Control-q>', close)
    menubar.add_cascade(label='File', menu=filemenu)

    editmenu = Menu(menubar, tearoff=FALSE)
    editmenu.add_command(label='Cut', command=cut, accelerator='Ctrl+X')
    etycode.bind("<Control-x>", cut)
    editmenu.add_command(label='Copy', command=copy, accelerator='Ctrl+C')
    etycode.bind("<Control-c>", copy)
    editmenu.add_command(label='Paste', command=paste, accelerator='Ctrl+V')
    etycode.bind("<Control-v>", paste)
    menubar.add_cascade(label='Edit', menu=editmenu)

    viewmenu = Menu(menubar, tearoff=FALSE)
    viewmenu.add_command(label='Show Variable View', command=varview)
    menubar.add_cascade(label='View', menu=viewmenu)

    helpmenu = Menu(menubar, tearoff=FALSE)
    helpmenu.add_command(label='Input Help', command=showhelp)
    helpmenu.add_separator()
    helpmenu.add_command(label='Upload Bug/Suggestions', command=upload)
    menubar.add_cascade(label='Help', menu=helpmenu)

    window.configure(menu=menubar)

    window.mainloop()


if __name__ == '__main__':
    MainWindow()
