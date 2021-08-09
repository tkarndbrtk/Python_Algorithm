rp = 0
op = 0
vp = 0
gp = 0
sp = 0
pup = 0
pip = 0
wp = 0
lst = []

for Q1 in range(1,3):
    if Q1 == 1:
        vp += 3
        op += 3

    elif Q1 ==2:
        rp += 3
        gp += 2

    for Q2 in range(1,3):
        if Q2 == 1:
            rp += 3
            wp += 3
        elif Q2 == 2:
            op += 3
            sp += 3
            gp += 3
            pup += 3

        for Q3 in range(1,3):
            if Q3 == 1:
                rp += 3
                pup += 3
                gp += 4
            elif Q3 ==2:
                vp += 3
                op += 3
                pip += 3

            for Q4 in range(1,3):
                if Q4 == 1:
                    gp += 4
                    rp += 3
                    pup += 3
                elif Q4 ==2:
                    sp += 3
                    pip += 3
                    op += 3
                    rp += 3 

                for Q5 in range(1,3):
                    if Q5 == 1:
                        rp += 2
                        pup += 3
                    elif Q5 ==2:
                        op += 3
                        sp += 3
                        wp += 3
                        pip += 2
                        vp += 2

                    for Q6 in range(1,3):
                        if Q6 == 1:
                            rp += 3
                            gp += 3
                            pup += 3
                            sp += 3
                        elif Q6 ==2:
                            op += 3
                            wp += 3
                            pip += 3

                        for Q7 in range(1,3):
                            if Q7 == 1:
                                gp += 4
                                wp += 2
                            elif Q7 ==2:
                                sp += 3
                                pup += 4
                            lst = [rp, op, vp, gp, sp, pup, pip, wp]
                            print(lst)
        rp = 0
        op = 0
        vp = 0
        gp = 0
        sp = 0
        pup = 0
        pip = 0
        wp = 0
                    


