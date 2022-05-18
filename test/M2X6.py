#gp = array # + Oxidation states
gp4 = ['Sc', 'Y', 'La']   #1, 2, 3
gp5 = ['Ti', 'Zr', 'Hf']  #1, 2, 3, 4
gp6 = ['V', 'Nb', 'Ta']   #1, 2, 3, 4, 5
gp7 = ['Cr', 'Mo', 'W']   #1, 2, 3, 4, 5, 6
gp8 = ['Mn', 'Tc', 'Re']  #1, 2, 3, 4, 5, 6, 7
gp9 = ['Fe', 'Ru', 'Os']  #1, 2, 3, 4, 5, 6, 7
gp10 = ['Co', 'Rh', 'Ir'] #1, 2, 3, 4, 5
gp11 = ['Ni', 'Pd', 'Pt'] #1, 2, 3, 4    
gp12 = ['Cu', 'Ag', 'Au'] #1, 2, 3,  (4 Cu) (5 Au)
gp13 = ['Zn', 'Cd', 'Hg'] #1, 2

val1_2 = gp4+gp5+gp6+gp7+gp8+gp9+gp10+gp11+gp12+gp13
val3 = gp4+gp5+gp6+gp7+gp8+gp9+gp10+gp11+gp12
val4 = gp5+gp6+gp7+gp8+gp9+gp10+gp11+['Cu']
val5 = gp6+gp7+gp8+gp9+gp10+['Au']
val6 = gp7+gp8+gp9
val7 = gp8+gp9

chal = ['O','S','Se','Te'] #+2

#MX2
for i in range(len(val6)):
    for j in range(len(chal)):
       print(f'{val6[i]}{chal[j]}3')
l = 6
#M2Xn0Yn1
for i in range(len(val6)):
    for j0 in range(len(chal)):
        for j1 in range(j0+1, len(chal)):
            # if j0 != j1:
                for n0 in range(1,l):
                    for n1 in range(1,l):
                        if n0+n1 ==l:
                            if n0 == 2:
                                print(f'{val6[i]}{chal[j0]}{n0}{chal[j1]}4')
                            elif n1 == 2:
                                print(f'{val6[i]}{chal[j0]}2{n0}{chal[j1]}') 
                            else:
                                print(f'{val6[i]}2{chal[j0]}{n0}{chal[j1]}{n1}')
                            # else :
                            #     print(f'{val5[i]}{chal[j0]}{chal[j1]}')


#M2Xn0Yn1Zn2
for i in range(len(val6)):
    for j0 in range(len(chal)):
        for j1 in range(j0+1, len(chal)):
            for j2 in range(j1+1, len(chal)):
                for n0 in range(1,l):
                    for n1 in range(1,l):
                        for n2 in range(1,l):                
                            # if (j0 != j1) and (j0 != j2) and (j1 != j2):
                                if n0+n1+n2 == l:
                                    if n0 == 2:
                                        print(f'{val6[i]}{chal[j0]}{chal[j1]}{chal[j2]}')
                                    else:
                                        print(f'{val6[i]}2{chal[j0]}{n0}{chal[j1]}{n1}{chal[j2]}{n2}')
#M2XYZA
for i in range(len(val6)):
    for j0 in range(len(chal)):
        for j1 in range(j0+1, len(chal)):
            for j2 in range(j1+1, len(chal)):
                for j3 in range(j2+1, len(chal)):
                    for n0 in range(1,l):
                        for n1 in range(1,l):
                            for n2 in range(1,l):
                                for n3 in range(1,l):
                                    # if (j0 != j1) and (j0 != j2) and (j0 != j3) and (j1 != j2) and (j1 != j3) and (j2 != j3):
                                        if n0+n1+n2+n3 == l:
                                            print(f'{val6[i]}2{chal[j0]}{n0}{chal[j1]}{n1}{chal[j2]}{n2}{chal[j3]}{n3}')

#M2X5
for i in range(len(val6)):
    for j0 in range(len(chal)):
        for j1 in range(j0+1, len(chal)):
            for j2 in range(j1+1, len(chal)):
                for j3 in range(j2+1, len(chal)):
                    # for j4 in range(len(chal)):
                        for n0 in range(1,l):
                            for n1 in range(1,l):
                                for n2 in range(1,l):
                                    for n3 in range(1,l):
                        #                 for n4 in range(6):
                                            # if (j0 != j1) and (j0 != j2) and (j0 != j3) and (j0 != j4) and (j1 != j2) and (j1 != j3) and (j1 != j4) and (j2 != j3) and (j2 != j4) and (j3 != j4):
                                                if n0+n1+n2+n3 == l:
                                                    # if (n0 and n1 and n2 and n3) != 2:
                                                    print(f'{val6[i]}2{chal[j0]}{n0}{chal[j1]}{n1}{chal[j2]}{n2}{chal[j3]}{n3}')
                                                    # else :
                                                    #     print(f'{val5[i]}{chal[j0]}{chal[j1]}{chal[j2]}{chal[j3]}')


#M2X6
for i in range(len(val6)):
    for j0 in range(len(chal)):
        for j1 in range(j0+1, len(chal)):
            for j2 in range(j1+1, len(chal)):
                for j3 in range(j2+1, len(chal)):
                    # for j4 in range(len(chal)):
                    #     for j5 in range(len(chal)):
                            for n0 in range(1,l):
                                for n1 in range(1,l):
                                    for n2 in range(1,l):
                                        for n3 in range(1,l):
                                            # for n4 in range(1,l):
                                            #     for n5 in range(1,l):
                                                    # if (j0 != j1) and (j0 != j2) and (j0 != j3) and (j0 != j4) and (j0 != j5) and (j1 != j2) and (j1 != j3) and (j1 != j4) and (j1 != j5) and (j2 != j3) and (j2 != j4) and (j2 != j5) and (j3 != j4) and (j3 != j5) and (j4 != j5):
                                                        if n0+n1+n2+n3 == l:
                                                            print(f'{val6[i]}2{chal[j0]}{n0}{chal[j1]}{n1}{chal[j2]}{n2}{chal[j3]}{n3}')


# M2X7
# for i in range(len(val7)):
#     for j0 in range(len(chal)):
#         for j1 in range(j0+1, len(chal)):
#             for j2 in range(j1+1, len(chal)):
#                 for j3 in range(j2+1, len(chal)):
#                     # for j4 in range(len(chal)):
#                     #     for j5 in range(len(chal)):
#                     #         for j6 in range(len(chal)):
#                                 for n0 in range(1,l):
#                                     for n1 in range(1,l):
#                                         for n2 in range(1,l):
#                                             for n3 in range(1,l):
#                                                 # for n4 in range(8):
#                                                 #     for n5 in range(8):
#                                                 #         for n6 in range(8):
#                                                             # if (j0 != j1) and (j0 != j2) and (j0 != j3) and (j0 != j4) and (j0 != j5) and (j0 != j6) and (j1 != j2) and (j1 != j3) and (j1 != j4) and (j1 != j5) and (j1 != j6) and (j2 != j3) and (j2 != j4) and (j2 != j5) and (j2 != j6) and (j3 != j4) and (j3 != j5) and (j3 != j6) and (j4 != j5) and (j4 != j6) and (j5 != j6):
#                                                                 if n0+n1+n2+n3 == 7:
#                                                                     print(f'{val7[i]}2{chal[j0]}{n0}{chal[j1]}{n1}{chal[j2]}{n2}{chal[j3]}{n3}')
