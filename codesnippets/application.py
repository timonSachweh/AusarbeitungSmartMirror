class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        (*\vdots*)
        self.generalInformation.grid(row=0, column=0, rowspan=1, columnspan=1, sticky="nsw")
        self.todayTodosFrame.grid(row=0, column=1, rowspan=1, columnspan=1, sticky="nse")
        self.newsBlockFrame.grid(row=1, column=0, rowspan=1, columnspan=2, sticky="nsew")

if __name__ == "__main__":
    root = Toplevel()
    root.title("Smart Mirror")
    application = Application(root)
    root.mainloop()

