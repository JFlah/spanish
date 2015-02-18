# Spanish 21 8-deck

# Stand soft 17

from Tkinter import *

root=Tk()
root.title("Spanish 21 Payout Calculator")

# 21 Variation Payouts
# Following payouts apply with splits, DO NOT APPLY WITH DOUBLING

def _21():
    bet=float(betEntry.get())
    payout=bet

    payoutEntry.delete(1,END)
    payoutEntry.insert(1,payout)

def _5card():
    bet=float(betEntry.get())
    payout = bet*1.5
    
    payoutEntry.delete(1,END)
    payoutEntry.insert(1,payout)

def _6card():
    bet=float(betEntry.get())
    payout=bet*2.

    payoutEntry.delete(1,END)
    payoutEntry.insert(1,payout)

def _7cardplus():
    bet=float(betEntry.get())
    payout=bet*3.

    payoutEntry.delete(1,END)
    payoutEntry.insert(1,payout)

def _678777mixed():
    bet=float(betEntry.get())
    payout=bet*1.5
    
    payoutEntry.delete(1,END)
    payoutEntry.insert(1,payout)

def _678777same():
    bet=float(betEntry.get())
    payout=bet*2.

    payoutEntry.delete(1,END)
    payoutEntry.insert(1,payout)

    extrasEntry.delete(0,END)
    extrasEntry.insert(0,"If suited player 777 vs dealer 7, check super bonus")

def _678777spade():
    bet=float(betEntry.get())
    payout=bet*3.

    payoutEntry.delete(1, END)
    payoutEntry.insert(1, payout)

    extrasEntry.delete(0,END)
    extrasEntry.insert(0, "If suited player 777 vs dealer 7, check super bonus")

# SUPER BONUS $1000 under 25, $5000 over 25

# NEGATED BY DOUBLING AND SPLITTING, ALL OTHER PLAYERS PAID $50 ENVY BONUS

def suited777vs7():
    bet = float(betEntry.get())
    if bet<25:
        extrasEntry.delete(0,END)
        extrasEntry.insert(0, "$1000 bonus to player, $50 envy bonus to all else")
    else:
        extrasEntry.delete(0,END)
        extrasEntry.insert(0, "$5000 bonus to player, $50 envy bonus to all else")

# Match the Dealer

def match():
    bet=float(matchEntry.get())
    payout=bet*3.
    
    matchPayoutEntry.delete(1, END)
    matchPayoutEntry.insert(1, payout) 

def suitmatch():
    bet=float(matchEntry.get())
    payout=bet*12.
    
    matchPayoutEntry.delete(1, END)
    matchPayoutEntry.insert(1, payout)

def doublematch():
    bet=float(matchEntry.get())
    payout=bet*6.
    
    matchPayoutEntry.delete(1, END)
    matchPayoutEntry.insert(1, payout)

def doublesuit():
    bet=float(matchEntry.get())
    payout=bet*24.
    
    matchPayoutEntry.delete(1, END)
    matchPayoutEntry.insert(1, payout)

def matchsuitmatch():
    bet=float(matchEntry.get())
    payout=bet*15.
    
    matchPayoutEntry.delete(1, END)
    matchPayoutEntry.insert(1, payout)

def insurance():
    amt=float(insuranceEntry.get())

    payout=amt*2.

    insurancePayoutEntry.delete(1,END)
    insurancePayoutEntry.insert(1,payout)

insuranceButton = Button(root, text="Pay Insurnace", command=insurance)
insuranceButton.grid(row=0, column=0, sticky="WE")

_21Button = Button(root, text="Normal 21", command=_21)
_21Button.grid(row=0, column=4, sticky="WE")

_5cardButton = Button(root, text="5 Card 21 or BJ", command=_5card)
_5cardButton.grid(row=0, column=1, sticky="WE")

_6cardButton = Button(root, text="6 Card 21", command=_6card)
_6cardButton.grid(row=0, column=2, sticky="WE")

_7cardplusButton = Button(root, text="7+ Card 21", command=_7cardplus)
_7cardplusButton.grid(row=0, column=3, sticky="WE")

_678777mixedButton = Button(root, text="6-7-8/7-7-7 Mixed Suit 21", command=_678777mixed)
_678777mixedButton.grid(row=1, column=0, sticky="WE")

_678777sameButton = Button(root, text="6-7-8/7-7-7 Same Suit 21", command=_678777same)
_678777sameButton.grid(row=1, column=1, sticky="WE")

_678777spadeButton = Button(root, text="6-7-8/7-7-7 Spade Suit 21", command=_678777spade)
_678777spadeButton.grid(row=1, column=2, sticky="WE")

suited777vs7Button = Button(root, text="7-7-7 Same Suit 21 vs Dealer 7(Super Bonus)", command=suited777vs7)
suited777vs7Button.grid(row=1, column=3, sticky="WE")

matchButton = Button(root, text="Dealer Match", command=match)
matchButton.grid(row=2, column=0, sticky="WE")

suitmatchButton = Button(root, text="Dealer Suited Match", command=suitmatch)
suitmatchButton.grid(row=2, column=1, sticky="WE")

doublematchButton = Button(root, text="Double Dealer Match", command=doublematch)
doublematchButton.grid(row=2, column=2, sticky="WE")

doublesuitButton = Button(root, text="Double Dealer Suited Match", command=doublesuit)
doublesuitButton.grid(row=2, column=3, sticky="WE")

matchsuitmatchButton = Button(root, text="Dealer Match + Dealer Suited Match", command=matchsuitmatch)
matchsuitmatchButton.grid(row=2, column=4, sticky="WE")

# Entries and Labels

betButton = Label(root, text="Enter bet amount($):")
betButton.grid(row=3, column=0)

betEntry = Entry(root)
betEntry.grid(row=3, column=1)
betEntry.insert(0, "")


matchButton = Label(root, text="Enter match bet amount($):")
matchButton.grid(row=5, column=0)

matchEntry = Entry(root)
matchEntry.grid(row=5, column=1)
matchEntry.insert(0, "")


payoutButton = Label(root, text="Amount to be paid on bet($):")
payoutButton.grid(row=4, column=0)

payoutEntry = Entry(root)
payoutEntry.grid(row=4, column=1)
payoutEntry.insert(0, "$0.00")


matchpayoutButton = Label(root, text="Amount to be paid on match($):")
matchpayoutButton.grid(row=6, column=0)

matchPayoutEntry = Entry(root)
matchPayoutEntry.grid(row=6, column=1)
matchPayoutEntry.insert(0, "$0.00")


insuranceButton = Label(root, text="Enter insurance amount($):")
insuranceButton.grid(row=7,column=0)

insuranceEntry = Entry(root)
insuranceEntry.grid(row=7,column=1)
insuranceEntry.insert(0,"")


insurancePayoutButton = Label(root, text="Amount to be paid on insurance($):")
insurancePayoutButton.grid(row=8,column=0)

insurancePayoutEntry = Entry(root)
insurancePayoutEntry.grid(row=8,column=1)
insurancePayoutEntry.insert(0, "$0.00")


extrasButton = Label(root, text="Note bene:")
extrasButton.grid(row=9,column=0)

extrasEntry = Entry(root)
extrasEntry.grid(row=9, column=1, columnspan=4, sticky="WE")
extrasEntry.insert(0, "")

root.mainloop()
    

