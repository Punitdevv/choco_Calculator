import  streamlit as choco

choco.title("CHOCO CALCULATOR ")
choco.header(" WELCOME IN CHOCO CALCULATOR ")
choco.subheader("HERE YOU CAN  (    MULTIPLY   DIVIDE  SUBTRACT     ADDON ) THE NUMBERS"    )



first= choco.number_input("enter first number")
operetor = choco.text_input("select operetor (+,-,*,/,) :,")
second = choco.number_input("enter second number")



if  operetor == "+":
    print=choco.text(first+second)
elif operetor == "-":
    print=choco.text(first-second)
elif operetor == "*":
    print=choco.text(first*second)
elif operetor == "/":
    print=choco.text(first/second)