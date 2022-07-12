sub_dict = {"north Auck": "4 Hiome Pl",
"south Auck": "49 wiri",
"west Auck": "4 Henderson",
"east Auck": "4 Howick "
            }



ask_sub=input("Whats your suburb")
for k,v in sub_dict.items():
    if k == ask_sub:
        print (v)

mynestlist=[['a',1],['b',2],['c',3]]
amt = int(input("Enter amount"))
for i in range(len(mynestlist)):
   # for j in range(len(mynestlist[i])):
        if amt>= mynestlist[i][1] :
            print(mynestlist[i][0])