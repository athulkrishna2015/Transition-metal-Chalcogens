M = ['Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn']
X = ['O','S','Se','Te','Po','Lv']
for m in range(len(M)):
    for x0 in range(len(X)):
        for x1 in range(len(X)):
            for i0 in range (1,10):
                for i1 in range(1,10):
                    if x0 != x1:
                        print(f'{M[m]}{X[x0]}{i0}{X[x1]}{i1}')    