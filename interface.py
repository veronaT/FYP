from tkinter import *
from tkinter.filedialog import askopenfilename
import os

import batteries
import ent


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
        self.__title_label.config(font=("Comic Sans MS", 18))
        #self.__title_label.pack(fill=X)
        self.__title_label.place(x=0, y=0, width=1280, height=25)


        #Input Title Label
        self.__input_label_frame = LabelFrame(self.master, text="Data File Input")
        self.__input_label_frame.config(font=("Comic Sans MS", 14))
        self.__input_label_frame.propagate(0)
        self.__input_label_frame.place(x=20, y=30, width=1240, height=75)

        #Input
        self.__file_input_label = Label(self.__input_label_frame, text='Input File Address or Select File')
        self.__file_input_label.config(font=("Comic Sans MS", 12))
        self.__file_input_label.place(x=10, y=5, height=25)

        #Input Box
        self.__file_name = StringVar()
        self.__file_input_entry = Entry(self.__input_label_frame, textvariable=self.__file_name)
        self.__file_input_entry.place(x=230, y=5, width=840, height=25)

        #File Select
        self.__file_select_button = Button(self.__input_label_frame, text='Select File', command=self.file_select)
        self.__file_select_button.config(font=("Comic Sans MS", 10))
        self.__file_select_button.place(x=1080, y=5, width=100, height=25)



        #Randomness Test Label
        self.__test_selection_label_frame = LabelFrame(self.master, text="Randomness Testing", padx=5, pady=5)
        self.__test_selection_label_frame.config(font=("Comic Sans MS", 14))

        self.__test_selection_label_frame.place(x=20, y=135, width=1240, height=400)

        self.__test_type = ['01. Entropy', '02. Chi Squared', '03. Mean', '04. Monte-Carlo-Pi', '05. Serial-Correlation', '06. Monobits', '07. Runs Test', '08. Long Runs', '09. Continuous Run', '10. Birthday Spacing Test', '11. Poker Test']

        self.__test_type_label = Label(self.__test_selection_label_frame, text='Test Type', borderwidth=2, relief="groove")
        self.__test_type_label.place(x=10, y=5, width=350, height=25)

        self.__p_value_label = Label(self.__test_selection_label_frame, text='P-Value', borderwidth=2, relief="groove")
        self.__p_value_label.place(x=365, y=5, width=500, height=25)

        self.__result_label = Label(self.__test_selection_label_frame, text='Result', borderwidth=2, relief="groove")
        self.__result_label.place(x=870, y=5, width=350, height=25)

        self.__chb_var = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),
                          IntVar(), IntVar(), IntVar()]

        self.__entropy = Label(self.__test_selection_label_frame, text=self.__test_type[0])

        #entropy
        self.__entropy.place(x=10, y=35)
        self.__entropy_p_value = StringVar()
        self.__entropy_p_value_entry = Entry(self.__test_selection_label_frame, textvariable=self.__entropy_p_value)
        self.__entropy_p_value_entry.config(state=DISABLED)
        self.__entropy_p_value_entry.place(x=365, y=35, width=500, height=25)
        self.__entropy_result = StringVar()
        self.__entropy_result_entry = Entry(self.__test_selection_label_frame, textvariable=self.__entropy_result)
        self.__entropy_result_entry.config(state=DISABLED)
        self.__entropy_result_entry.place(x=870, y=35, width=350, height=25)
        
        #Chi Squared
        self.__chiSqaure = Label(self.__test_selection_label_frame, text=self.__test_type[1])
        self.__chiSqaure.place(x=10, y=65)
        self.__chiSqaure_p_value = StringVar()
        self.__chiSqaure_p_value_entry = Entry(self.__test_selection_label_frame, textvariable=self.__chiSqaure_p_value)
        self.__chiSqaure_p_value_entry.config(state=DISABLED)
        self.__chiSqaure_p_value_entry.place(x=365, y=65, width=500, height=25)
        self.__chiSqaure_result = StringVar()
        self.__chiSqaure_result_entry = Entry(self.__test_selection_label_frame, textvariable=self.__chiSqaure_result)
        self.__chiSqaure_result_entry.config(state=DISABLED)
        self.__chiSqaure_result_entry.place(x=870, y=65, width=350, height=25)
        
        #pochisq
        self.__pochisq = Label(self.__test_selection_label_frame, text=self.__test_type[2])
        self.__pochisq.place(x=10, y=95)
        self.__pochisq_p_value = StringVar()
        self.__pochisq_p_value_entry = Entry(self.__test_selection_label_frame, textvariable=self.__pochisq_p_value)
        self.__pochisq_p_value_entry.config(state=DISABLED)
        self.__pochisq_p_value_entry.place(x=365, y=95, width=500, height=25)
        self.__pochisq_result = StringVar()
        self.__pochisq_result_entry = Entry(self.__test_selection_label_frame, textvariable=self.__pochisq_result)
        self.__pochisq_result_entry.config(state=DISABLED)
        self.__pochisq_result_entry.place(x=870, y=95, width=350, height=25)
        
        #Monte-Carlo
        self.__monteCarlo = Label(self.__test_selection_label_frame, text=self.__test_type[3])
        self.__monteCarlo.place(x=10, y=125)
        self.__monteCarlo_p_value = StringVar()
        self.__monteCarlo_p_value_entry = Entry(self.__test_selection_label_frame, textvariable=self.__monteCarlo_p_value)
        self.__monteCarlo_p_value_entry.config(state=DISABLED)
        self.__monteCarlo_p_value_entry.place(x=365, y=125, width=500, height=25)
        self.__monteCarlo_result = StringVar()
        self.__monteCarlo_result_entry = Entry(self.__test_selection_label_frame, textvariable=self.__monteCarlo_result)
        self.__monteCarlo_result_entry.config(state=DISABLED)
        self.__monteCarlo_result_entry.place(x=870, y=125, width=350, height=25)
        
        #Serial Correlation
        self.__correlation = Label(self.__test_selection_label_frame, text=self.__test_type[4])
        self.__correlation.place(x=10, y=155)
        self.__correlation_p_value = StringVar()
        self.__correlation_p_value_entry = Entry(self.__test_selection_label_frame, textvariable=self.__correlation_p_value)
        self.__correlation_p_value_entry.config(state=DISABLED)
        self.__correlation_p_value_entry.place(x=365, y=155, width=500, height=25)
        self.__correlation_result = StringVar()
        self.__correlation_result_entry = Entry(self.__test_selection_label_frame, textvariable=self.__correlation_result)
        self.__correlation_result_entry.config(state=DISABLED)
        self.__correlation_result_entry.place(x=870, y=155, width=350, height=25)

        #Mono bits
        self.__monobits = Label(self.__test_selection_label_frame, text=self.__test_type[5])
        self.__monobits.place(x=10, y=185)
        self.__monobits_p_value = StringVar()
        self.__monobits_p_value_entry = Entry(self.__test_selection_label_frame, textvariable=self.__monobits_p_value)
        self.__monobits_p_value_entry.config(state=DISABLED)
        self.__monobits_p_value_entry.place(x=365, y=185, width=500, height=25)
        self.__monobits_result = StringVar()
        self.__monobits_result_entry = Entry(self.__test_selection_label_frame, textvariable=self.__monobits_result)
        self.__monobits_result_entry.config(state=DISABLED)
        self.__monobits_result_entry.place(x=870, y=185, width=350, height=25)
        
        #run
        self.__run = Label(self.__test_selection_label_frame, text=self.__test_type[6])
        self.__run.place(x=10, y=215)
        self.__run_p_value = StringVar()
        self.__run_p_value_entry = Entry(self.__test_selection_label_frame, textvariable=self.__run_p_value)
        self.__run_p_value_entry.config(state=DISABLED)
        self.__run_p_value_entry.place(x=365, y=215, width=500, height=25)
        self.__run_result = StringVar()
        self.__run_result_entry = Entry(self.__test_selection_label_frame, textvariable=self.__run_result)
        self.__run_result_entry.config(state=DISABLED)
        self.__run_result_entry.place(x=870, y=215, width=350, height=25)
        
        #longruns
        self.__longRun = Label(self.__test_selection_label_frame, text=self.__test_type[7])
        self.__longRun.place(x=10, y=245)
        self.__longRun_p_value = StringVar()
        self.__longRun_p_value_entry = Entry(self.__test_selection_label_frame, textvariable=self.__longRun_p_value)
        self.__longRun_p_value_entry.config(state=DISABLED)
        self.__longRun_p_value_entry.place(x=365, y=245, width=500, height=25)
        self.__longRun_result = StringVar()
        self.__longRun_result_entry = Entry(self.__test_selection_label_frame, textvariable=self.__longRun_result)
        self.__longRun_result_entry.config(state=DISABLED)
        self.__longRun_result_entry.place(x=870, y=245, width=350, height=25)
        
        #contRun
        self.__contRun = Label(self.__test_selection_label_frame, text=self.__test_type[8])
        self.__contRun.place(x=10, y=275)

        self.__contRun_result = StringVar()
        self.__contRun_result_entry = Entry(self.__test_selection_label_frame, textvariable=self.__contRun_result)
        self.__contRun_result_entry.config(state=DISABLED)
        self.__contRun_result_entry.place(x=870, y=275, width=350, height=25)
        
        #birthday Spacing test
        self.__birthday = Label(self.__test_selection_label_frame, text=self.__test_type[9])
        self.__birthday.place(x=10, y=305)
        self.__birthday_p_value = StringVar()
        self.__birthday_p_value_entry = Entry(self.__test_selection_label_frame, textvariable=self.__birthday_p_value)
        self.__birthday_p_value_entry.config(state=DISABLED)
        self.__birthday_p_value_entry.place(x=365, y=305, width=500, height=25)
        self.__birthday_result = StringVar()
        self.__birthday_result_entry = Entry(self.__test_selection_label_frame, textvariable=self.__birthday_result)
        self.__birthday_result_entry.config(state=DISABLED)
        self.__birthday_result_entry.place(x=870, y=305, width=350, height=25)
        
        #Poker test
        self.__poker = Label(self.__test_selection_label_frame, text=self.__test_type[10])
        self.__poker.place(x=10, y=335)
        self.__poker_p_value = StringVar()
        self.__poker_p_value_entry = Entry(self.__test_selection_label_frame, textvariable=self.__poker_p_value)
        self.__poker_p_value_entry.config(state=DISABLED)
        self.__poker_p_value_entry.place(x=365, y=335, width=500, height=25)
        self.__poker_result = StringVar()
        self.__poker_result_entry = Entry(self.__test_selection_label_frame, textvariable=self.__poker_result)
        self.__poker_result_entry.config(state=DISABLED)
        self.__poker_result_entry.place(x=870, y=335, width=350, height=25)

        #run tests button
        self.__execute_button = Button(self.master, text='Execute Test', command=self.execute)
        self.__execute_button.config(font=("Comic Sans MS", 10))
        self.__execute_button.place(x=20, y=550, width=100, height=30)

        #save to file button
        self.__save_button = Button(self.master, text='Save to File', command=self.save)
        self.__save_button.config(font=("Comic Sans MS", 10))
        self.__save_button.place(x=125, y=550, width=100, height=30)


        #reset button
        self.__reset_button = Button(self.master, text='Reset', command=self.reset)
        self.__reset_button.config(font=("Comic Sans MS", 10))
        self.__reset_button.place(x=230, y=550, width=100, height=30)

    def file_select(self):
        print('File Select')
        file_name = askopenfilename(initialdir=os.getcwd(), title="Choose a file.")
        load = False
        print(self.__file_name)
        if file_name:
            self.__file_name.set(file_name)

    def execute(self):

        #returning ent results
        result = batteries.ent(self.__file_name.get())
        self.__entropy_p_value.set(result[0])
        #if result[0]

        self.__chiSqaure_p_value.set(result[1])

        self.__correlation_p_value.set(result[2])

        self.__pochisq_p_value.set(result[3])

        self.__monteCarlo_p_value.set(result[4])

        #returning fips results
        r, c = batteries.fips(self.__file_name.get())

        self.__monobits_p_value.set(c[0])
        if r[0] is True:
            self.__monobits_result.set("Passed: Random")
        else:
            self.__monobits_result.set("Failed: Not Random")
            
        self.__run_p_value.set(c[2])
        if r[2] is True:
            self.__run_result.set("Passed: Random")
        else:
            self.__run_result.set("Failed: Not Random")

        self.__longRun_p_value.set(c[3])
        if r[3] is True:
            self.__longRun_result.set("Passed: Random")
        else:
            self.__longRun_result.set("Failed: Not Random")

        if r[4] is True:
            self.__contRun_result.set("Passed: Random")
        else:
            self.__contRun_result.set("Failed: Not Random")

        self.__poker_p_value.set(c[1])
        if r[1] is True:
            self.__poker_result.set("Passed: Random")
        else:
            self.__poker_result.set("Failed: Not Random")

    def save(self):
        print()

    def reset(self):
        print()

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