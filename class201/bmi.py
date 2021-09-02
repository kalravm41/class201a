from tkinter import *   

window = Tk()
window.title('BMI Calculator')
window.geometry('400x400')

headingLabel = Label(window,text='BMI Calculator',fg='black', bg='red', font=('Calibri', 20), bd=5)
headingLabel.place(x=50, y=20)

nameLabel = Label(window, text='Your Name', fg='black', bg='green', font=('Calibri', 14), bd=1)
nameLabel.place(x=20, y=90)
username = Entry(window, text='', bd=2, width=22)
username.place(x=150, y=92)

heightLabel = Label(window, text='Your Height (in cm)', fg='black', bg='green', font=('Calibri', 14), bd=1)
heightLabel.place(x=20, y=130)
Height = Entry(window, text='', bd=2, width=22)
Height.place(x=150, y=132)

weightLabel = Label(window, text='Your Weight (in kg)', fg='black', bg='green', font=('Calibri', 14), bd=1)
weightLabel.place(x=20, y=170)
Weight = Entry(window, text='', bd=2, width=22)
Weight.place(x=150, y=172)

resultFrame = LabelFrame(window, text='Result', bg='red', font=('Calibri', 14), fg='black')
resultFrame.pack()
resultFrame.place(x=20, y=20)

def calculateBMI():
    weight= int(Weight.get())
    height= int(Height.get())

    bmi1= weight/(height**2)
    bmi= round(bmi1,1) 

    name= username.get()
    message= ''

    if bmi <= 18.5:
        message= 'You Are Under Weight'

    elif bmi > 18.5 and bmi <= 24.9:
        message= 'Is In Normal Range'

    elif bmi >= 25 and bmi <= 29.9:
        message = 'You Are Overweight'

    elif bmi > 30:
        message = 'You Are Obest'

    else:
        message= 'Something Went Wrong'

    outPutMessage = Label(resultFrame, text=name+','+'your BMI is'+str(bmi)+message, bg='yellow', font=('Calibri', 18), width=12, fg='black') 
    outPutMessage.pack()
    outPutMessage.place(x=20, y=40)           

calculateButton = Button(window, text='CALCULATE', command=calculateBMI, font=('Calibri', 20), bd=5, bg='purple') 
calculateButton.place(x=20, y=250)  

window.mainloop()
