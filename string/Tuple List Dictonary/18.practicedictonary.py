#TO update the values of keys
a={1:2,  "Sumit": "A coder"    ,   "Mobile":"IQOO"}
a["Mobile"]="Apple"                                       #method 1
(a.update({"Sumit":"A gamer"}))                           #method 2          
print(a)                                                #in both method values of keys are replaced so old values of the keys are no 
                                                                            #longer in dictonary

# to add the keys and values in dictonary

a["Pen"]="Doms"
(a.update({"Laptop":"Dell"}))
print(a)
sj={
    "butter":"Chicken", "home":"mathura"
}
a.update(sj)
print(a)