import pickle
with open("./usb_codes.pkl", "rb") as f:
    usb_codes=pickle.load(f)

lines=["","","",""]
pos=0

for l in open("newkeystrokes.txt", "r").readlines(): 
    code=int(l[6:8],16) 
    if code==0: 
        continue 
    if code==0x51 or code==0x28: 
        pos+=1 
        continue 
    if code==0x52: 
        pos-=1 
        continue 
    if int(l[0:2],16)==2: 
        lines[pos]+=usb_codes[code][1] 
    else: 
        lines[pos]+=usb_codes[code][0]

str_=[line for line in lines if "<" in line or ">" in line][0]
strnew_=[""]
pos=-1

for c in str_:
    if c is "<":
        pos-=1
        continue
    elif c is ">":
        pos+=1
        continue
    else:
        rightpart=strnew_[pos:]
        leftpart=strnew_[:pos]
        leftpart+=c
        strnew_=leftpart + rightpart

print("".join(strnew_))
