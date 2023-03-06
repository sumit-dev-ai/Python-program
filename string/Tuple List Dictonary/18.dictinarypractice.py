#WAP to create dictonary which takes hindi words from user and provides translation of those words
dict={"Pankha":"Fan",
"Roti":"bread",
"kursi":"Chair"
}
print("Search from options ",list(dict.keys()))
s=input("Enter your word in hindi :")
print("MEaning of your word is\t",dict.get(s))
print("MEaning of your word is\t",dict[s])