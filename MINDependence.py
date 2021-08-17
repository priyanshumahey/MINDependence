import tkinter
import tkinter.font as tkFont
import time
from cortex import Cortex
from train import Train
import requests


#Init
name = "MINDependence"
window = tkinter.Tk()
window.geometry('1280x720')
window.title(name)


#Font Styles
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
fontStyle30 = tkFont.Font(family="Lucida Grande", size=30)
fontStylehead = tkFont.Font(family="Lucida Grande", size=40)
fontBigHead = tkFont.Font(family='Lucida Grande', size=50)
fontInput2 = tkFont.Font(family='Lucida Grande', size=17)
fontInput = tkFont.Font(family='Lucida Grande', size=15)
fontStyle1 = tkFont.Font(family="Lucida Grande", size=13)


#Mental Commands
Command1 = {
    'action': '',
    'power' : '',
    'output':''
    }

Command2 = {
    'action': '',
    'power' : '',
    'output':''
    }

Command3 = {
    'action': '',
    'power' : '',
    'output':''
    }

Command4 = {
    'action': '',
    'power' : '',
    'output':''
    }

Command5 = {
    'action': '',
    'power' : '',
    'output':''
    }

ch_com1_str = tkinter.StringVar()
ch_com2_str = tkinter.StringVar()
ch_com3_str = tkinter.StringVar()
ch_com4_str = tkinter.StringVar()
ch_com5_str = tkinter.StringVar()

out1_str = tkinter.StringVar()
out2_str = tkinter.StringVar()
out3_str = tkinter.StringVar()
out4_str = tkinter.StringVar()
out5_str = tkinter.StringVar()


#Commands
def loginNow():
    print(username.get())
    Title.destroy()
    usernameLabel.destroy()
    loginButton.destroy()
    usernameEntry.destroy()
    page2()

def nextButtonCommand():
    nextButton.destroy()
    page2home.destroy()
    Introduction.pack()
    Introduction.place(x=100 , y=100)
    Introduction2.pack()
    Introduction2.place(x=100 , y=140)
    Introduction3.pack()
    Introduction3.place(x=100 , y=180)
    Introduction4.pack()
    Introduction4.place(x=100 , y=220)
    Introduction5.pack()
    Introduction5.place(x=100 , y=260)
    Introduction6.pack()
    Introduction6.place(x=100 , y=300)
    Introduction7.pack()
    Introduction7.place(x=100 , y=340)
    nextButton2.pack()
    nextButton2.place(y=400, x=580, width=200, height=40)

def nextButton2Command():
    Introduction.destroy()
    Introduction2.destroy()
    Introduction3.destroy()
    Introduction4.destroy()
    Introduction5.destroy()
    Introduction6.destroy()
    Introduction7.destroy()
    nextButton2.destroy()
    myCanvas.pack()
    myCanvas.place(y=0, x=0)
    Page2Head.pack()
    Page2Head.place(y=40, x=300)
    startButton.pack()
    startButton.place(y=550, x=120, height=100, width=200,)
    configureButton.pack()
    configureButton.place(y=550, x=960, height=100, width=200)

def back2page2Com():
    page2()
    nextButtonCommand()
    nextButton2Command()
    back2page2Button.destroy()
    configureCommandsButton.destroy()
    configureOutputsButton.destroy()
    out1t.destroy() 
    out2t.destroy() 
    out3t.destroy() 
    out4t.destroy() 
    out5t.destroy()
    Out1Label.destroy()
    Out2Label.destroy()
    Out3Label.destroy()
    Out4Label.destroy()
    Out5Label.destroy()
    Com1t.destroy()
    Com2t.destroy() 
    Com3t.destroy() 
    Com4t.destroy() 
    Com5t.destroy()
    Com1Label.destroy()
    Com2Label.destroy()
    Com3Label.destroy()
    Com4Label.destroy()
    Com5Label.destroy()
    commandTitle.destroy()
    OutTitle.destroy()

def StartCommand():
    Page2Head.destroy()
    startButton.destroy()
    configureButton.destroy()
    myCanvas.destroy()
    startpage()


def configureCommand():
    Page2Head.destroy()
    startButton.destroy()
    configureButton.destroy()
    myCanvas.destroy()
    configpage()

def changeCommandsCommand():
    back2page2Button.destroy()
    configureCommandsButton.destroy()
    configureOutputsButton.destroy()
    out1t.destroy() 
    out2t.destroy() 
    out3t.destroy() 
    out4t.destroy() 
    out5t.destroy()
    Out1Label.destroy()
    Out2Label.destroy()
    Out3Label.destroy()
    Out4Label.destroy()
    Out5Label.destroy()
    Com1t.destroy()
    Com2t.destroy() 
    Com3t.destroy() 
    Com4t.destroy() 
    Com5t.destroy()
    Com1Label.destroy()
    Com2Label.destroy()
    Com3Label.destroy()
    Com4Label.destroy()
    Com5Label.destroy()
    commandTitle.destroy()
    OutTitle.destroy()
    configcommandspage()


def changeOutputsCommand():
    back2page2Button.destroy()
    configureCommandsButton.destroy()
    configureOutputsButton.destroy()
    out1t.destroy() 
    out2t.destroy() 
    out3t.destroy() 
    out4t.destroy() 
    out5t.destroy()
    Out1Label.destroy()
    Out2Label.destroy()
    Out3Label.destroy()
    Out4Label.destroy()
    Out5Label.destroy()
    Com1t.destroy()
    Com2t.destroy() 
    Com3t.destroy() 
    Com4t.destroy() 
    Com5t.destroy()
    Com1Label.destroy()
    Com2Label.destroy()
    Com3Label.destroy()
    Com4Label.destroy()
    Com5Label.destroy()
    commandTitle.destroy()
    OutTitle.destroy()
    configoutputspage()

def ChangeNow():
    Command1['action'] = str(ch_com1_str.get())
    Command2['action'] = str(ch_com2_str.get())
    Command3['action'] = str(ch_com3_str.get())
    Command4['action'] = str(ch_com4_str.get())
    Command5['action'] = str(ch_com5_str.get())


def ChangeNowOuputs():
    Command1['output'] = str(out1_str.get())
    Command2['output'] = str(out2_str.get())
    Command3['output'] = str(out3_str.get())
    Command4['output'] = str(out4_str.get())
    Command5['output'] = str(out5_str.get())

def ChangeNow2():
    print(Command1)
    print(Command2)
    print(Command3)
    print(Command4)
    print(Command5)



def toconfigfromcommandconfig():
    ch_com1Label.destroy()
    ch_com1Entry.destroy() 
    ch_com2Label.destroy() 
    ch_com2Entry.destroy() 
    ch_com3Label.destroy()
    ch_com3Entry.destroy() 
    ch_com4Label.destroy() 
    ch_com4Entry.destroy() 
    ch_com5Label.destroy() 
    ch_com5Entry.destroy()
    ChangeCommandButton.destroy()
    #ChangeCommandButton2.destroy()
    ChangeCommandButton3.destroy()
    CommandInfo.destroy() 
    CommandInfo2.destroy() 
    CommandInfo3.destroy() 
    CommandInfo4.destroy()
    configpage()

def toconfigfromoutputconfig():
    out1Label.destroy() 
    out1Entry.destroy()  
    out2Label.destroy()  
    out2Entry.destroy()  
    out3Label.destroy()  
    out3Entry.destroy()  
    out4Label.destroy()  
    out5Label.destroy()  
    out4Entry.destroy()  
    out5Entry.destroy() 
    ChangeOuputButton.destroy()  
    ChangeOutputButton3.destroy() 
    OutInfo.destroy()
    OutInfo2.destroy() 
    OutInfo3.destroy()
    OutInfo4.destroy() 
    configpage()

def send_state(s):
    url = 'http://127.0.0.1:5000/setState'
    state_info = {'state': s}
    x = requests.post(url, params=state_info)

def tohomefromstart():
    deletestartpageButton.destroy()
    showstatusLabel.destroy()
    startButton.destroy()

    page2()
    nextButtonCommand()
    nextButton2Command()








    
#Page 1 will be a username page
def page1():
    global username, Title, usernameLabel, usernameEntry, loginButton
    Title = tkinter.Label(window, text="MINDependence", font=fontStylehead)
    Title.pack()
    Title.place(y=180, x=480)

    usernameLabel = tkinter.Label(window, text="Enter Username:", font=fontStyle)
    usernameLabel.pack()
    usernameLabel.place(y=300, x=580)


    
    username = tkinter.StringVar()

    usernameEntry = tkinter.Entry(window, textvariable=username, font=fontStyle)
    usernameEntry.pack()
    usernameEntry.place(y=350, x=580, width=200, height=40)


    loginButton = tkinter.Button(window, text="Login", command=loginNow, bg='white')
    loginButton.pack()
    loginButton.place(y=400, x=580, width=200, height=40)





#Page 2 will be the main home page

def page2():
    global page2home, nextButton, Introduction, Introduction2, Introduction3, Introduction4, Introduction5, Introduction6, Introduction7, nextButton2, myCanvas, Page2Head
    global startButton, configureButton
    
    page2home = tkinter.Label(window, text='Welcome ' +str(username.get()) + '!', font=fontStyle)
    page2home.pack()
    page2home.place(y=300, x=580)

    nextButton =  tkinter.Button(window, text="Continue", command=nextButtonCommand, bg='white')
    nextButton.pack()
    nextButton.place(y=400, x=580, width=200, height=40)

    Introduction = tkinter.Label(window, text='Welcome to ' + name + '. This app helps those with disabilities to take control of their lives.', font=fontStyle)
    Introduction2 = tkinter.Label(window, text='This app is designed to give users full control of their emotiv headset and quickly control', font=fontStyle)
    Introduction3 = tkinter.Label(window, text='everything around them. Built off of Virtual Brainwear, the user is able to customize outputs', font=fontStyle)
    Introduction4 = tkinter.Label(window, text='for certain brainwaves. The commands are currently using Mental Commands in Virtual', font=fontStyle)
    Introduction5 = tkinter.Label(window, text='Brainwear. In the future, users will be required to train the app and it will then listen to', font=fontStyle)
    Introduction6 = tkinter.Label(window, text='their choosen inputs. In the meantime, the user can only select from pretrainerd inputs.', font=fontStyle)
    Introduction7 = tkinter.Label(window, text='Then, the user will be able to choose what response they want the brainwave to produce.', font=fontStyle)

    nextButton2 =  tkinter.Button(window, text="Continue ->", command=nextButton2Command, bg='white')
    
    myCanvas = tkinter.Canvas(window, bg="white", height=140, width=1280)
    Page2Head = tkinter.Label(window, bg="white", text=name, font=fontBigHead)

    startButton = tkinter.Button(window, text="Start",  command=StartCommand, bg='white')
    configureButton = tkinter.Button(window, text="Configure", command=configureCommand, bg='white')




#Page 3 is the config page
def configpage():
    global back2page2Button, commandTitle, Com1Label, Com2Label, Com3Label, Com4Label, Com5Label
    global com1, com2, com3, com4, com5, OutTitle
    global Com1t, Com2t, Com3t, Com4t, Com5t

    back2page2Button = tkinter.Button(window, text="Go Back",  command=back2page2Com, bg='red')
    back2page2Button.pack()
    back2page2Button.place(y=30, x=30, width='100', height='50')

    commandTitle = tkinter.Label(window, text='Mental Commands', font=fontStyle)
    commandTitle.pack()
    commandTitle.place(x=415, y=40)

    Com1Label = tkinter.Label(window, text='Command 1:', font=fontInput2)
    Com2Label = tkinter.Label(window, text='Command 2:', font=fontInput2)
    Com3Label = tkinter.Label(window, text='Command 3:', font=fontInput2)
    Com4Label = tkinter.Label(window, text='Command 4:', font=fontInput2)
    Com5Label = tkinter.Label(window, text='Command 5:', font=fontInput2)

    comlabels=[160, 210, 260, 310, 360]
    Com1Label.place(x=190, y=comlabels[0])
    Com2Label.place(x=190,y=comlabels[1])
    Com3Label.place(x=190,y=comlabels[2])
    Com4Label.place(x=190,y=comlabels[3])
    Com5Label.place(x=190,y=comlabels[4])

    com1 = str(Command1['action'])
    com2 = str(Command2['action'])
    com3 = str(Command3['action'])
    com4 = str(Command4['action'])
    com5 = str(Command5['action'])

    Com1t = tkinter.Label(window, text=com1, font=fontInput2, bg='white')
    Com2t = tkinter.Label(window, text=com2, font=fontInput2, bg='white')
    Com3t = tkinter.Label(window, text=com3, font=fontInput2, bg='white')
    Com4t = tkinter.Label(window, text=com4, font=fontInput2, bg='white')
    Com5t = tkinter.Label(window, text=com5, font=fontInput2, bg='white')

    Com1t.place(x=415, y=comlabels[0])
    Com2t.place(x=415, y=comlabels[1])
    Com3t.place(x=415, y=comlabels[2])
    Com4t.place(x=415, y=comlabels[3])
    Com5t.place(x=415, y=comlabels[4])

    OutTitle = tkinter.Label(window, text='Outputs', font=fontStyle)
    OutTitle.pack()
    OutTitle.place(x=890, y=40)

    global Out1Label, Out2Label, Out3Label, Out4Label, Out5Label

    Out1Label = tkinter.Label(window, text='Ouput 1:', font=fontInput2)
    Out2Label = tkinter.Label(window, text='Output 2:', font=fontInput2)
    Out3Label = tkinter.Label(window, text='Output 3:', font=fontInput2)
    Out4Label = tkinter.Label(window, text='Output 4:', font=fontInput2)
    Out5Label = tkinter.Label(window, text='Output 5:', font=fontInput2)

    Outlabels=[160, 210, 260, 310, 360]
    Out1Label.place(x=665, y=comlabels[0])
    Out2Label.place(x=665,y=comlabels[1])
    Out3Label.place(x=665,y=comlabels[2])
    Out4Label.place(x=665,y=comlabels[3])
    Out5Label.place(x=665,y=comlabels[4])

    global out1, out2, out3, out4, out5

    out1 = str(Command1['output'])
    out2 = str(Command2['output'])
    out3 = str(Command3['output'])
    out4 = str(Command4['output'])
    out5 = str(Command5['output'])

    global out1t, out2t, out3t, out4t, out5t

    out1t = tkinter.Label(window, text=out1, font=fontInput2, bg='white')
    out2t = tkinter.Label(window, text=out2, font=fontInput2, bg='white')
    out3t = tkinter.Label(window, text=out3, font=fontInput2, bg='white')
    out4t = tkinter.Label(window, text=out4, font=fontInput2, bg='white')
    out5t = tkinter.Label(window, text=out5, font=fontInput2, bg='white')

    out1t.place(x=890, y=comlabels[0])
    out2t.place(x=890, y=comlabels[1])
    out3t.place(x=890, y=comlabels[2])
    out4t.place(x=890, y=comlabels[3])
    out5t.place(x=890, y=comlabels[4])

    global configureCommandsButton, configureOutputsButton

    configureCommandsButton = tkinter.Button(window, text="Change Commands", bg='white', command=changeCommandsCommand)
    configureCommandsButton.place(x=415, y=550,width='150', height='75')
    configureOutputsButton = tkinter.Button(window, text="Change Ouputs", bg='white', command=changeOutputsCommand)
    configureOutputsButton.place(x=890, y=550, width='150', height='75')

def configcommandspage():
    global ch_com1Label, ch_com1Entry, ch_com2Label, ch_com2Entry, ch_com3Label
    global ch_com3Entry, ch_com4Label, ch_com4Entry, ch_com5Label, ch_com5Entry
    global ChangeCommandButton, ChangeCommandButton2, ChangeCommandButton3
    
    #y
    command_change_loc = [70, 90, 145, 165, 220, 240, 295, 315, 370, 390]

    #x
    command_change_loc_x = 150
    ch_com1Label = tkinter.Label(window, text="Command 1:", font=fontStyle1)
    ch_com1Label.pack()
    ch_com1Label.place(y=command_change_loc[0], x=command_change_loc_x)


    ch_com1Entry = tkinter.Entry(window, textvariable=ch_com1_str, font=fontInput )
    ch_com1Entry.pack()
    ch_com1Entry.place(y=command_change_loc[1], x=command_change_loc_x, width=190, height=50)

    ch_com2Label = tkinter.Label(window, text="Command 2:", font=fontStyle1)
    ch_com2Label.pack()
    ch_com2Label.place(y=command_change_loc[2], x=command_change_loc_x)

    ch_com2Entry = tkinter.Entry(window, textvariable=ch_com2_str, font=fontInput )
    ch_com2Entry.pack()
    ch_com2Entry.place(y=command_change_loc[3], x=command_change_loc_x, width=190, height=50)


    ch_com3Label = tkinter.Label(window, text="Command 3:", font=fontStyle1)
    ch_com3Label.pack()
    ch_com3Label.place(y=command_change_loc[4], x=command_change_loc_x)


    ch_com3Entry = tkinter.Entry(window, textvariable=ch_com3_str, font=fontInput )
    ch_com3Entry.pack()
    ch_com3Entry.place(y=command_change_loc[5], x=command_change_loc_x, width=190, height=50)

    ch_com4Label = tkinter.Label(window, text="Command 4:", font=fontStyle1)
    ch_com4Label.pack()
    ch_com4Label.place(y=command_change_loc[6], x=command_change_loc_x)

    ch_com4Entry = tkinter.Entry(window, textvariable=ch_com4_str, font=fontInput )
    ch_com4Entry.pack()
    ch_com4Entry.place(y=command_change_loc[7], x=command_change_loc_x, width=190, height=50)

    ch_com5Label = tkinter.Label(window, text="Command 5:", font=fontStyle1)
    ch_com5Label.pack()
    ch_com5Label.place(y=command_change_loc[8], x=command_change_loc_x)

    ch_com5Entry = tkinter.Entry(window, textvariable=ch_com5_str, font=fontInput )
    ch_com5Entry.pack()
    ch_com5Entry.place(y=command_change_loc[9], x=command_change_loc_x, width=190, height=50)

    ChangeCommandButton = tkinter.Button(window, text="Save Commands", command=ChangeNow, bg='white')
    ChangeCommandButton.pack()
    ChangeCommandButton.place(y=460, x=command_change_loc_x, width=190, height=50)

    #ChangeCommandButton2 = tkinter.Button(window, text="Print", command=ChangeNow2, bg='white')
    #ChangeCommandButton2.pack()
    #ChangeCommandButton2.place(y=515, x=command_change_loc_x, width=190, height=50)

    ChangeCommandButton3 = tkinter.Button(window, text="Go Back", command=toconfigfromcommandconfig, bg='red')
    ChangeCommandButton3.pack()
    ChangeCommandButton3.place(y=30, x=30, width='100', height='50')

    global CommandInfo, CommandInfo2, CommandInfo3, CommandInfo4 
    CommandInfo = tkinter.Label(window, text='Since this is a demo version, it only uses a few commands. The possible commands are:', font=fontInput)
    CommandInfo.place(x=400, y=100)
    CommandInfo2 = tkinter.Label(window, text='neutral      pull      push      lift      drop      left      right', font=fontInput)
    CommandInfo2.place(x=400, y=130)
    CommandInfo3 = tkinter.Label(window, text="In the commands section, choose which command you'd like to use. Then in outputs, you", font=fontInput)
    CommandInfo3.place(x=400, y=160)
    CommandInfo4 = tkinter.Label(window, text="can choose the corresponding outputs you'd like", font=fontInput)
    CommandInfo4.place(x=400, y=190)


def configoutputspage():
    global out1Label, out1Entry, out2Label, out2Entry, out3Label, out3Entry, out4Label, out5Label, out4Entry, out5Entry,ChangeOuputButton, ChangeOutputButton3

    
    #y
    ouput_change_loc = [70, 90, 145, 165, 220, 240, 295, 315, 370, 390]

    #x
    ouput_change_loc_x = 150

    out1Label = tkinter.Label(window, text='Ouput 1:', font=fontStyle1)
    out1Label.pack()
    out1Label.place(y=ouput_change_loc[0], x=ouput_change_loc_x)

    out1Entry = tkinter.Entry(window, textvariable=out1_str, font=fontInput )
    out1Entry.pack()
    out1Entry.place(y=ouput_change_loc[1], x=ouput_change_loc_x, width=190, height=50)

    out2Label = tkinter.Label(window, text='Ouput 2:', font=fontStyle1)
    out2Label.pack()
    out2Label.place(y=ouput_change_loc[2], x=ouput_change_loc_x)

    out2Entry = tkinter.Entry(window, textvariable=out2_str, font=fontInput )
    out2Entry.pack()
    out2Entry.place(y=ouput_change_loc[3], x=ouput_change_loc_x, width=190, height=50)

    out3Label = tkinter.Label(window, text='Ouput 3:', font=fontStyle1)
    out3Label.pack()
    out3Label.place(y=ouput_change_loc[4], x=ouput_change_loc_x)

    out3Entry = tkinter.Entry(window, textvariable=out3_str, font=fontInput )
    out3Entry.pack()
    out3Entry.place(y=ouput_change_loc[5], x=ouput_change_loc_x, width=190, height=50)

    out4Label = tkinter.Label(window, text='Ouput 4:', font=fontStyle1)
    out4Label.pack()
    out4Label.place(y=ouput_change_loc[6], x=ouput_change_loc_x)

    out4Entry = tkinter.Entry(window, textvariable=out4_str, font=fontInput )
    out4Entry.pack()
    out4Entry.place(y=ouput_change_loc[7], x=ouput_change_loc_x, width=190, height=50)

    out5Label = tkinter.Label(window, text='Ouput 5:', font=fontStyle1)
    out5Label.pack()
    out5Label.place(y=ouput_change_loc[8], x=ouput_change_loc_x)

    out5Entry = tkinter.Entry(window, textvariable=out5_str, font=fontInput )
    out5Entry.pack()
    out5Entry.place(y=ouput_change_loc[9], x=ouput_change_loc_x, width=190, height=50)



    ChangeOuputButton = tkinter.Button(window, text="Save Ouputs", command=ChangeNowOuputs, bg='white')
    ChangeOuputButton.pack()
    ChangeOuputButton.place(y=460, x=ouput_change_loc_x, width=190, height=50)

    #ChangeCommandButton2 = tkinter.Button(window, text="Print", command=ChangeNow2, bg='white')
    #ChangeCommandButton2.pack()
    #ChangeCommandButton2.place(y=515, x=ouput_change_loc_x, width=190, height=50)

    ChangeOutputButton3 = tkinter.Button(window, text="Go Back", command=toconfigfromoutputconfig, bg='red')
    ChangeOutputButton3.pack()
    ChangeOutputButton3.place(y=30, x=30, width='100', height='50')


    global OutInfo, OutInfo2, OutInfo3, OutInfo4 
    OutInfo = tkinter.Label(window, text='This demo uses a website that changes colours instead to for demo purposes.', font=fontInput)
    OutInfo.place(x=400, y=100)
    OutInfo2 = tkinter.Label(window, text='The code currently supports most colours. Inputs should be similiar to the following:', font=fontInput)
    OutInfo2.place(x=400, y=130)
    OutInfo3 = tkinter.Label(window, text="#ff6346      blue      red      green      #ff6fff      	LightCoral      #DFFF00", font=fontInput)
    OutInfo3.place(x=400, y=160)
    OutInfo4 = tkinter.Label(window, text="can choose the corresponding outputs you'd like", font=fontInput)
    OutInfo4.place(x=400, y=190)
    



def startpage():
    global profile_name, t, j, emotiv_request, deletestartpageButton, showstatusLabel
    # name of training profile
    profile_name = 'testprofile345'



    # Init Train
    t=Train()

    # Do prepare steps
    t.do_prepare_steps() 

    # subscribe sys stream to receive Training Event
    t.subscribe_data(['sys'])

    # load existed profile or create a new profile
    t.load_profile(profile_name)
    

    deletestartpageButton = tkinter.Button(window, text='Go back', command=tohomefromstart, bg='red')
    deletestartpageButton.pack()
    deletestartpageButton.place(y=30, x=30, width='100', height='50')

    
    

    showstatusLabel = tkinter.Label(window, text='WARNING: This window will freeze for a bit while running. Make sure that \n you have setup configurations first. If you have not, go back and do so. \n Once set up, feel free to make changes in Virtual Brainwear', font=fontInput)
    showstatusLabel.place(x=400, y=190)
    global startButton
    """
    while 1:
        j =t.live(profile_name)
        if str(j[0]['action']).lower() == Command1['action']:
            send_state(Command1['output'])
            print(Command1['output'])
        if str(j[0]['action']).lower() == Command2['action']:
            send_state(Command2['output'])
            print(Command2['output'])
        if str(j[0]['action']).lower() == Command3['action']:
            send_state(Command3['output'])
            print(Command3['output'])
        if str(j[0]['action']).lower() == Command4['action']:
            send_state(Command4['output'])
            print(Command4['output'])
        if str(j[0]['action']).lower() == Command5['action']:
            send_state(Command5['output'])
            print(Command5['output'])
    
    #print(j[0]['action'])
    """
    """
        if str(j[0]['action']).lower() == Command1['action']:
            send_state(Command1['output'])
            print(Command1['output'])
        if str(j[0]['action']).lower() == Command2['action']:
            send_state(Command2['output'])
            print(Command2['output'])
        if str(j[0]['action']).lower() == Command3['action']:
            send_state(Command3['output'])
            print(Command3['output'])
        if str(j[0]['action']).lower() == Command4['action']:
            send_state(Command4['output'])
            print(Command4['output'])
        if str(j[0]['action']).lower() == Command5['action']:
            send_state(Command5['output'])
            print(Command5['output'])
    """



    startButton = tkinter.Button(window, text='Start', bg='white', command=run_this)
    startButton.place(x=415, y=550,width='150', height='75')


def run_this():
    # name of training profile
    profile_name = 'testprofile345'

    # number of training time for one action
    number_of_train = 1

    # Init Train
    t=Train()

    # Do prepare steps
    t.do_prepare_steps() 

    # subscribe sys stream to receive Training Event
    t.subscribe_data(['sys'])

    # load existed profile or create a new profile
    t.load_profile(profile_name)


    # Training neutral action
    training_action = 'neutral'
    #t.train_mc(profile_name, training_action, number_of_train)

    # # add active action

    # Training push action
    training_action = 'push'
    ##t.train_mc(profile_name, training_action, number_of_train)

    # unload profile
    t.unload_profile(profile_name)
    for i in range(500):
        j = t.live_looped(profile_name, 1)
        #print(j[0]['action'])
        if str(j[0]['action']).lower() == Command1['action']:
            send_state(Command1['output'])
            print(Command1['output'])
        if str(j[0]['action']).lower() == Command2['action']:
            send_state(Command2['output'])
            print(Command2['output'])
        if str(j[0]['action']).lower() == Command3['action']:
            send_state(Command3['output'])
            print(Command3['output'])
        if str(j[0]['action']).lower() == Command4['action']:
            send_state(Command4['output'])
            print(Command4['output'])
        if str(j[0]['action']).lower() == Command5['action']:
            send_state(Command5['output'])
            print(Command5['output'])

        """
        if str(j[0]['action']).lower() == "neutral":
            print('This is ' + j[0]['action'])
        if str(j[0]['action']).lower() == "push":
            print('This is ' + j[0]['action'])
        if str(j[0]['action']).lower() == "pull":
            print('This is ' + j[0]['action'])
        if str(j[0]['action']).lower() == "lift":
            print('This is ' + j[0]['action'])
        if str(j[0]['action']).lower() == "drop":
            print('This is ' + j[0]['action'])
        if str(j[0]['action']).lower() == "left":
            print('This is ' + j[0]['action'])
        if str(j[0]['action']).lower() == "right":
            print('This is ' + j[0]['action'])
        if str(j[0]['action']).lower() == "rotateleft":
            print('This is ' + j[0]['action'])
        if str(j[0]['action']).lower() == "rotateright":
            print('This is ' + j[0]['action'])
        if str(j[0]['action']).lower() == "rotateclockwise":
            print('This is ' + j[0]['action'])
        if str(j[0]['action']).lower() == "rotatecounterclockwise":
            print('This is ' + j[0]['action'])
        if str(j[0]['action']).lower() == "rotateforwards":
            print('This is ' + j[0]['action'])
        if str(j[0]['action']).lower() == "rotatereverse":
            print('This is ' + j[0]['action'])
        if str(j[0]['action']).lower() == "disappear":
            print('This is ' + j[0]['action'])
        """









page1()


window.mainloop()