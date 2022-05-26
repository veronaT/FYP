from tkinter import *
from tkinter.filedialog import askopenfilename
import os


class GUI(Frame):

    # Constructor
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()


    def init_window(self):

        # Title Label
        frame_title = 'A Minimal Set of Statistical Tests for RNG and PRNGs'
        self.__title_label = Label(self.master, text=frame_title)
        self.__title_label.config(font=("Times New Roman", 18))
        #self.__title_label.pack(fill=X)
        self.__title_label.place(x=0, y=0, width=1280, height=25)


        #Input Title Label
        self.__input_label_frame = LabelFrame(self.master, text="Data File Input")
        self.__input_label_frame.config(font=("Times New Roman", 14))
        self.__input_label_frame.propagate(0)
        self.__input_label_frame.place(x=20, y=30, width=1240, height=75)

        #Input
        self.__file_input_label = Label(self.__input_label_frame, text='Input File Address or Select File')
        self.__file_input_label.config(font=("Times New Roman", 12))
        self.__file_input_label.place(x=10, y=5, height=25)

        #Input Box
        self.__file_name = StringVar()
        self.__file_input_entry = Entry(self.__input_label_frame, textvariable=self.__file_name)
        self.__file_input_entry.place(x=230, y=5, width=840, height=25)

        #File Select
        self.__file_select_button = Button(self.__input_label_frame, text='Select File', command=self.file_select)
        self.__file_select_button.config(font=("Times New Roman", 10))
        self.__file_select_button.place(x=1080, y=5, width=100, height=25)



        #Randomness Test Label
        self.__test_selection_label_frame = LabelFrame(self.master, text="Randomness Testing", padx=5, pady=5)
        self.__test_selection_label_frame.config(font=("Times New Roman", 14))

        self.__test_selection_label_frame.place(x=20, y=135, width=1240, height=380)

        self.__test_type = ['01. Entropy', '02. Chi Squared', '03. Mean', '04. Monte-Carlo-Pi', '05. Serial-Correlation', '06. Monobits', '07. Runs Test', '08. Long Runs', '09. Continuous Run', '10. Birthday Spacing Test', '11. Poker Test']

        self.__test_type_label = Label(self.__test_selection_label_frame, text='Test Type', borderwidth=2, relief="groove")
        self.__test_type_label.place(x=10, y=5, width=350, height=25)

        self.__p_value_label = Label(self.__test_selection_label_frame, text='P-Value', borderwidth=2, relief="groove")
        self.__p_value_label.place(x=365, y=5, width=500, height=25)

        self.__result_label = Label(self.__test_selection_label_frame, text='Result', borderwidth=2, relief="groove")
        self.__result_label.place(x=870, y=5, width=350, height=25)

        self.__chb_var = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),
                          IntVar(), IntVar(), IntVar()]

    def file_select(self):
        print('File Select')
        file_name = askopenfilename(initialdir=os.getcwd(), title="Choose a file.")
        load = False
        print(self.__file_name)
        if file_name:
            self.__file_name.set(file_name)

    def exit(self):
        exit(0)


if __name__ == '__main__':
    root = Tk()
    root.resizable(0,0)
    root.geometry("%dx%d+0+0" % (1280, 600))
    title = 'Minimal set of Tests for Testing Randomness'
    root.title(title)
    app = GUI(root)
    app.focus_displayof()
    app.mainloop()