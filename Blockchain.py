from hashlib import sha256
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox,simpledialog
import json


class Block:
    def __init__(self, PrevBlockHash, BlockIndex, Tx, TimeStamp):
        self.PrevBlockHash = PrevBlockHash
        self.BlockIndex = BlockIndex
        self.Tx = Tx
        self.TimeStamp = TimeStamp

    def getHash(self):
        # self.__dict__ นำข้อมูลใน __init__ มาทำเป็น Dictionary
        # json.dumps แปลงเป็น string
        return sha256(json.dumps(self.__dict__).encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.unconfirmTx = []
        self.chain = []
        self.createGenesis()

    def createGenesis(self):
        Genesis = Block("0", 0, [
            {
                "Match": "Manchester City : Brighton & Hove Albion",
                "Score": "1:0",
                "Date": datetime(2021, 1, 13).strftime("%d %B %Y")
            },
            {
                "Match": "Tottenham Hotspur : Fulham",
                "Score": "1:1",
                "Date": datetime(2021, 1, 13).strftime("%d %B %Y")
            }], str(datetime.now()))

        self.chain.append(Genesis)

    @property
    def lastBlock(self):
        return self.chain[-1]

    def addTx(self, transaction):
        self.unconfirmTx.append(transaction)

    def CreateBlock(self):
        if (len(self.unconfirmTx) == 0):
            print(len(self.unconfirmTx))
            return False
        BlockIndex = len(self.chain)
        NewBlock = Block(self.lastBlock.getHash(), BlockIndex,
                         self.unconfirmTx, str(datetime.now()))
        self.chain.append(NewBlock)
        self.unconfirmTx = []
        return True


FirstBlockchain = Blockchain()  # Create First Chain

# Block1
TxBlock1 = [
    {
        "Match": "Arsenal : Crystal Palace",
        "Score": "0:0",
        "Date": datetime(2021, 1, 14).strftime("%d %B %Y")
    }
]
for data in TxBlock1:
    FirstBlockchain.addTx(data)
FirstBlockchain.CreateBlock()

# Block2
TxBlock2 = [
    {
        "Match": "Wolverhampton Wanderers : West Bromwich Albion",
        "Score": "2:3",
        "Date": datetime(2021, 1, 16).strftime("%d %B %Y")
    },
    {
        "Match": "Leeds United : Brighton & Hove Albion",
        "Score": "0:1",
        "Date": datetime(2021, 1, 16).strftime("%d %B %Y")
    },
    {
        "Match": "West Ham United : Burnley",
        "Score": "1:0",
        "Date": datetime(2021, 1, 16).strftime("%d %B %Y")
    },
    {
        "Match": "Fulham : Chelsea",
        "Score": "0:1",
        "Date": datetime(2021, 1, 16).strftime("%d %B %Y")
    },
    {
        "Match": "Leicester City : Southampton",
        "Score": "2:0",
        "Date": datetime(2021, 1, 16).strftime("%d %B %Y")
    }
]
for data in TxBlock2:
    FirstBlockchain.addTx(data)
FirstBlockchain.CreateBlock()

# Block3
TxBlock3 = [
    {
        "Match": "Sheffield United : Tottenham Hotspur",
        "Score": "1:3",
        "Date": datetime(2021, 1, 17).strftime("%d %B %Y")
    },
    {
        "Match": "Liverpool : Manchester United",
        "Score": "0:0",
        "Date": datetime(2021, 1, 17).strftime("%d %B %Y")
    },
    {
        "Match": "Manchester City : Crystal Palace",
        "Score": "4:0",
        "Date": datetime(2021, 1, 17).strftime("%d %B %Y")
    }
]
for data in TxBlock3:
    FirstBlockchain.addTx(data)
FirstBlockchain.CreateBlock()

# Block4
TxBlock4 = [
    {
        "Match": "Arsenal : Crystal Palace",
        "Score": "2:0",
        "Date": datetime(2021, 1, 18).strftime("%d %B %Y")
    }
]
for data in TxBlock4:
    FirstBlockchain.addTx(data)
FirstBlockchain.CreateBlock()

# Block5
TxBlock5 = [
    {
        "Match": "Wolverhampton Wanderers : West Bromwich Albion",
        "Score": "0:3",
        "Date": datetime(2021, 1, 19).strftime("%d %B %Y")
    },
    {
        "Match": "Leeds United : Brighton & Hove Albion",
        "Score": "1:1",
        "Date": datetime(2021, 1, 19).strftime("%d %B %Y")
    },
    {
        "Match": "West Ham United : Burnley",
        "Score": "1:2",
        "Date": datetime(2021, 1, 19).strftime("%d %B %Y")
    },
    {
        "Match": "Fulham : Chelsea",
        "Score": "3:1",
        "Date": datetime(2021, 1, 19).strftime("%d %B %Y")
    },
    {
        "Match": "Leicester City : Southampton",
        "Score": "2:2",
        "Date": datetime(2021, 1, 19).strftime("%d %B %Y")
    }
]
for data in TxBlock5:
    FirstBlockchain.addTx(data)
FirstBlockchain.CreateBlock()

# Block6
TxBlock6 = [
    {
        "Match": "Sheffield United : Tottenham Hotspur",
        "Score": "4:3",
        "Date": datetime(2021, 1, 20).strftime("%d %B %Y")
    },
    {
        "Match": "Liverpool : Manchester United",
        "Score": "2:0",
        "Date": datetime(2021, 1, 20).strftime("%d %B %Y")
    },
    {
        "Match": "Manchester City : Crystal Palace",
        "Score": "2:1",
        "Date": datetime(2021, 1, 20).strftime("%d %B %Y")
    }
]
for data in TxBlock6:
    FirstBlockchain.addTx(data)
FirstBlockchain.CreateBlock()

# Block7
TxBlock7 = [
    {
        "Match": "Arsenal : Crystal Palace",
        "Score": "0:3",
        "Date": datetime(2021, 1, 21).strftime("%d %B %Y")
    }
]
for data in TxBlock7:
    FirstBlockchain.addTx(data)
FirstBlockchain.CreateBlock()

# Block8
TxBlock8 = [
    {
        "Match": "Wolverhampton Wanderers : West Bromwich Albion",
        "Score": "4:3",
        "Date": datetime(2021, 1, 22).strftime("%d %B %Y")
    },
    {
        "Match": "Leeds United : Brighton & Hove Albion",
        "Score": "2:1",
        "Date": datetime(2021, 1, 22).strftime("%d %B %Y")
    },
]
for data in TxBlock8:
    FirstBlockchain.addTx(data)
FirstBlockchain.CreateBlock()

# Block9
TxBlock9 = [
    {
        "Match": "Sheffield United : Tottenham Hotspur",
        "Score": "2:3",
        "Date": datetime(2021, 1, 23).strftime("%d %B %Y")
    },
    {
        "Match": "Liverpool : Manchester United",
        "Score": "0:0",
        "Date": datetime(2021, 1, 23).strftime("%d %B %Y")
    },
    {
        "Match": "Manchester City : Crystal Palace",
        "Score": "2:3",
        "Date": datetime(2021, 1, 23).strftime("%d %B %Y")
    }
]
for data in TxBlock9:
    FirstBlockchain.addTx(data)

FirstBlockchain.CreateBlock()



for x in FirstBlockchain.chain:
    print("-----------------------------")
    print("Block Index = ", x.BlockIndex)
    print("Block Hash = ", x.getHash())
    print("Prev Hash = ", x.PrevBlockHash)
    print("TimeStamp = ", x.TimeStamp)
    print("Transactions")
    for t in x.Tx:
        print("     Match = ", t["Match"])
        print("     Score = ", t["Score"])
        print("     Date = ", t["Date"])
        print("")


win = tk.Tk()

# Add a title
win.title("Python GUI")

tabControl = ttk.Notebook(win)          # Create Tab Control

addBlock = ttk.Frame(tabControl)            # Create a tab
tabControl.add(addBlock, text='Add Block')      # Add the tab

dataVerifi = ttk.Frame(tabControl)            # Add a second tab
# Make second tab visible
tabControl.add(dataVerifi, text='Data Verification')


tabControl.pack(expand=1, fill="both")  # Pack to make visible

# LabelFrame using addBlock as the parent
mighty = ttk.LabelFrame(addBlock, text=' Add Transaction ')
mighty.grid(column=0, row=0, padx=8, pady=8)

# Modify adding a Label using mighty as the parent instead of win
a_label = ttk.Label(mighty, text="ใส่ชื่อทีมที่มีการแข่ง :")
a_label.grid(column=0, row=0, sticky='W')

# Modified Button Click Function




# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=20, textvariable=name)
name_entered.grid(column=0, row=1, sticky='e')               # align left/West

split = ttk.Label(mighty, text="              vs ")
split.grid(column=1, row=1, sticky='WE')

name2 = tk.StringVar()
name_entered2 = ttk.Entry(mighty, width=20, textvariable=name2)
name_entered2.grid(column=2, row=1, sticky='W')


s_label = ttk.Label(mighty, text="ใส่ผลการแข่งขัน :")
s_label.grid(column=0, row=2, sticky='W')

score1 = tk.StringVar()
s1_entered = ttk.Entry(mighty, width=15, textvariable=score1)
s1_entered.grid(column=0, row=3, sticky='E')               # align left/West

split = ttk.Label(mighty, text="               : ")
split.grid(column=1, row=3, sticky='WE')

score2 = tk.StringVar()
s2_entered2 = ttk.Entry(mighty, width=15, textvariable=score2)
s2_entered2.grid(column=2, row=3, sticky='W')

# ---------------------------------------------------------------
d_label = ttk.Label(mighty, text="วัน-เดือน-ปี ที่แข่ง :")
d_label.grid(column=0, row=4, sticky='W')

date = tk.StringVar()
date_entered = ttk.Entry(mighty, width=15, textvariable=date)
date_entered.grid(column=0, row=5, sticky='W')

def addNewTransaction():
    scr.delete("1.0","end")
    newdate = date.get().split("/")
    newTx = {
        "Match": name.get()+" : "+name2.get(),
        "Score": score1.get()+" : "+score2.get(),
        "Date": datetime(int(newdate[2]), int(newdate[1]), int(newdate[0])).strftime("%d %B %Y")
    }
    FirstBlockchain.addTx(newTx)
    s=""
    for data in FirstBlockchain.unconfirmTx:
        s = s + "{\n     Match = " + data["Match"] + "\n" + "     Score = " + data["Score"] + "\n     Date = " + data["Date"] + "\n}"
        print(s)
    scr.insert(tk.INSERT, s)
    



action = ttk.Button(mighty, text="Add Transaction",command=addNewTransaction)
action.grid(column=1, row=6)

tx = ttk.LabelFrame(addBlock, text="Unconfirm Transaction")
tx.grid(column=1, row=0, padx=8, pady=8)

scrol_w = 80
scrol_h = 8
scr = scrolledtext.ScrolledText(tx, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=0, sticky='WE', columnspan=3)
n=[]
for i in FirstBlockchain.chain:
        n.append(i.BlockIndex)
def create():
    scr.delete("1.0","end")
    print(FirstBlockchain.CreateBlock())
    n=[]
    for i in FirstBlockchain.chain:
        n.append(i.BlockIndex)
action = ttk.Button(tx, text="Add Block", command=create)
action.grid(column=0, row=1,sticky='WE')

btn = ttk.LabelFrame(addBlock, text=None)
btn.grid(column=0, row=1, padx=8, pady=8)


ttk.Label(btn, text="Choose a block index:").grid(column=0, row=0)
number2 = tk.StringVar()
number2_chosen = ttk.Combobox(btn, width=12, textvariable=number2, state='readonly')

number2_chosen['values'] = n
number2_chosen.grid(column=0, row=1)
number2_chosen.current(0)

def showBlock():
    srcShow.delete("1.0","end")
    c=""
    data = FirstBlockchain.chain[int(number2.get())]
    c = c + "{\nBlock Index = "+ str(data.BlockIndex) + "\n" + "Block Hash = "+ data.getHash() + "\nPrev Hash = "+ data.PrevBlockHash + "\nTimeStamp = "+ str(data.TimeStamp) +"Transactions \n"
    for t in data.Tx:
        c = c + "\n     Match = " + t["Match"] + "\n" + "     Score = " + t["Score"] + "\n     Date = " + t["Date"] + "\n\n"
    c = c + "}\n--------------------------------------\n"
    srcShow.insert(tk.INSERT, c)

show = ttk.Button(btn, text="Show Block", command=showBlock)
show.grid(column=0, row=2,sticky='WE')
tx = ttk.LabelFrame(addBlock, text="Unconfirm Transaction")
tx.grid(column=1, row=0, padx=8, pady=8)

showBlock = ttk.LabelFrame(addBlock, text="Show Block")
showBlock.grid(column=1, row=1, padx=8, pady=8)

srcShow = scrolledtext.ScrolledText(showBlock, width=scrol_w, height=scrol_h, wrap=tk.WORD)
srcShow.grid(column=1, row=0, sticky='WE', columnspan=3)
# Adding a Button
#action = ttk.Button(mighty, text="Click Me!", command=click_me)
#action.grid(column=2, row=1)

#ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
#number = tk.StringVar()
#number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
#number_chosen['values'] = (1, 2, 4, 42, 100)
#number_chosen.grid(column=1, row=1)
# number_chosen.current(0)


# Tab Control 2 refactoring  ---------------------------------------------------------
# We are creating a container frame to hold all other widgets -- Tab2

allChain = ttk.LabelFrame(dataVerifi, text="All Chain")
allChain.grid(column=0, row=0, padx=8, pady=8)

scrol2_w = 80
scrol2_h = 15
lchain = scrolledtext.ScrolledText(allChain, width=scrol2_w, height=scrol2_h, wrap=tk.WORD)
lchain.grid(column=0, row=5, sticky='WE', columnspan=3)
c=""
for data in FirstBlockchain.chain:
    c = c + "{\nBlock Index = "+ str(data.BlockIndex) + "\n" + "Block Hash = "+ data.getHash() + "\nPrev Hash = "+ data.PrevBlockHash + "\nTimeStamp = "+ str(data.TimeStamp) +"Transactions \n"
    for t in data.Tx:
        c = c + "\n     Match = " + t["Match"] + "\n" + "     Score = " + t["Score"] + "\n     Date = " + t["Date"] + "\n\n"
    c = c + "}\n--------------------------------------\n"
lchain.insert(tk.INSERT, c)
# Exit GUI cleanly

def checkChain():
    lchain.delete("1.0","end")
    c=""
    for data in FirstBlockchain.chain:
        c = c + "{\nBlock Index = "+ str(data.BlockIndex) + "\n" + "Block Hash = "+ data.getHash() + "\nPrev Hash = "+ data.PrevBlockHash + "\nTimeStamp = "+ str(data.TimeStamp) +"Transactions \n"
        for t in data.Tx:
            c = c + "\n     Match = " + t["Match"] + "\n" + "     Score = " + t["Score"] + "\n     Date = " + t["Date"] + "\n\n"
        c = c + "}\n--------------------------------------\n"
    lchain.insert(tk.INSERT, c)
    ch = True
    bedit = ""
    chain = FirstBlockchain.chain
    for i in range(len(FirstBlockchain.chain)-1):
        print(chain[i].getHash()+"     "+chain[i+1].PrevBlockHash)
        if (chain[i].getHash()==chain[i+1].PrevBlockHash):
            ch = True
        else:
            ch = False
            bedit = "Block index "+str(i)+" was edit!!! \n" + "Hash Value change from \""+chain[i+1].PrevBlockHash+" \nTo\n "+chain[i].getHash()
            break
    if ch:
        messagebox.showinfo("Report","All blockchain are verify")
    else:
        messagebox.showinfo("Report",bedit)
    for i in FirstBlockchain.chain:
        n.append(i.BlockIndex)

check = ttk.Button(dataVerifi, text="Data Verification",command=checkChain)
check.grid(column=1, row=0)

editSl = ttk.LabelFrame(dataVerifi, text="Select")
editSl.grid(column=0, row=1, padx=8, pady=8)

ttk.Label(editSl, text="Choose a block index:").grid(column=0, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(editSl, width=12, textvariable=number, state='readonly')

number_chosen['values'] = n
number_chosen.grid(column=0, row=1)
number_chosen.current(0)



editLabel = ttk.LabelFrame(editSl, text=' Edit ')
editLabel.grid(column=0, row=2, padx=8, pady=8)

# Modify adding a Label using mighty as the parent instead of win
teaml = ttk.Label(editLabel, text="ใส่ชื่อทีมที่มีการแข่ง :")
teaml.grid(column=1, row=0, sticky='W')


# Adding a Textbox Entry widget
nameE1 = tk.StringVar()
nameE1_entered = ttk.Entry(editLabel, width=20, textvariable=nameE1)
nameE1_entered.grid(column=0, row=1, sticky='e')               # align left/West

split = ttk.Label(editLabel, text="              vs ")
split.grid(column=1, row=1, sticky='WE')

nameE2 = tk.StringVar()
name_entered2 = ttk.Entry(editLabel, width=20, textvariable=nameE2)
name_entered2.grid(column=2, row=1, sticky='W')


s_label = ttk.Label(editLabel, text="ใส่ผลการแข่งขัน :")
s_label.grid(column=0, row=2, sticky='W')

scoreE1 = tk.StringVar()
se1_entered = ttk.Entry(editLabel, width=15, textvariable=scoreE1)
se1_entered.grid(column=0, row=3, sticky='E')               # align left/West

split = ttk.Label(editLabel, text="               : ")
split.grid(column=1, row=3, sticky='WE')

scoreE2 = tk.StringVar()
s2_entered2 = ttk.Entry(editLabel, width=15, textvariable=scoreE2)
s2_entered2.grid(column=2, row=3, sticky='W')

# ---------------------------------------------------------------
d_label = ttk.Label(editLabel, text="วัน-เดือน-ปี ที่แข่ง :")
d_label.grid(column=0, row=4, sticky='W')

dateE = tk.StringVar()
dateE_entered = ttk.Entry(editLabel, width=15, textvariable=dateE)
dateE_entered.grid(column=0, row=5, sticky='W')

def editChain():
    bl = FirstBlockchain.chain[int(number.get())]
    bl.Tx[0]["Match"] = nameE1.get() +" : " +nameE2.get()
    bl.Tx[0]["Score"] = scoreE1.get() +" : "+scoreE2.get()
    bl.Tx[0]["Date"] = dateE.get()

editTx = ttk.Button(editSl, text="Edit",command=editChain)
editTx.grid(column=0, row=3)

def _quit():
    win.quit()
    win.destroy()
    exit()


name_entered.focus()      # Place cursor into name Entry
# ======================
# Start GUI
# ======================
win.mainloop()
