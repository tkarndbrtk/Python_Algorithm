rp = 0
op = 0
vp = 0
gp = 0
sp = 0
pup = 0
pip = 0
wp = 0
rn = 0
on = 0
vn = 0
gn = 0
sn = 0
pin = 0
pun = 0
wn = 0
lst = []
def Q1(a):
    global rp
    global op
    global vp
    global gp
    global sp
    global pup
    global pip
    global wp
    if a == 1:
        vp += 3.0
        op += 3.1
        pip +=2.8
    elif a ==2:
        gp += 2.2
        rp += 2.8

def Q2(a):
    global rp
    global op
    global vp
    global gp
    global sp
    global pup
    global pip
    global wp
    if a == 1:
        wp += 2.5
        pip += 2.9
    elif a == 2:
        sp += 3.3
        pup += 3

def Q3(a):
    global rp
    global op
    global vp
    global gp
    global sp
    global pup
    global pip
    global wp
    if a == 1:
        rp += 2.8
        pup += 3
        gp += 2.6
    elif a ==2:
        vp += 3.9
        op += 3.2
        pip += 2.8
        sp +=3.1

def Q4(a):
    global rp
    global op
    global vp
    global gp
    global sp
    global pup
    global pip
    global wp
    if a == 1:
        wp += 3.2
        vp += 2.6
    elif a ==2:
        sp += 2.8
        op += 3.1
        rp += 2.4
def Q5(a):
    global rp
    global op
    global vp
    global gp
    global sp
    global pup
    global pip
    global wp
    if a == 1:
        rp += 2.2
    elif a ==2:
        op += 3.4
        wp += 2.8
        pip += 2.8
        vp += 2.3

def Q6(a):
    global rp
    global op
    global vp
    global gp
    global sp
    global pup
    global pip
    global wp
    if a == 1:
        rp += 2.2
        gp += 3.5
        pup += 3
    elif a ==2:
        wp += 2.2
        pip += 2.1

def Q7(a):
    global rp
    global op
    global vp
    global gp
    global sp
    global pup
    global pip
    global wp
    if a == 1:
        gp += 3.3
    elif a == 2:
        wp += 2.1
        sp += 3.2
        pup += 3.5
count = 0
a_1 = 0
a_2 = 0
a_3 = 0
a_4 = 0
a_5 = 0
a_6 = 0
a_7 = 0
for i in range(128):
    a_1 = i % 2
    temp1 = i//2
    a_2 = temp1 % 2
    temp1 //=2
    a_3 = temp1 % 2
    temp1 //=2
    a_4 = temp1 % 2
    temp1 //=2
    a_5 = temp1 % 2
    temp1 //=2
    a_6 = temp1 % 2
    temp1 //=2
    a_7 = temp1 % 2
    Q1(a_1+1)
    Q2(a_2+1)
    Q3(a_3+1)
    Q4(a_4+1)
    Q5(a_5+1)
    Q6(a_6+1)
    Q7(a_7+1)
    lst = [rp, op, vp, gp, sp, pup, pip, wp]
    num = lst.index(max(lst))
    joongbok = lst.count(max(lst))
    if joongbok != 1:
        print(joongbok, lst)
    if num ==0:
        rn+=1
    elif num ==1:
        on+=1
    elif num ==2:
        vn+=1
    elif num ==3:
        gn+=1
    elif num ==4:
        sn+=1
    elif num ==5:
        pun+=1
    elif num ==6:
        pin+=1
    else:
        wn+=1
    rp=0
    op=0
    vp=0
    gp=0
    sp=0
    pup=0
    pip=0
    wp=0
    count+=1
print(rn, on, vn, gn, sn, pun, pin, wn)
''' 
// 마지막에 들어갈 내용
Q1(a_1)
Q2(a_2)
Q3(a_3)
Q4(a_4)
Q5(a_5)
Q6(a_6)
Q7(a_7)
lst = [rp, op, vp, gp, sp, pup, pip, wp]
print(lst)
rp=0
op=0
vp=0
gp=0
sp=0
pup=0
pip=0
wp=0
'''