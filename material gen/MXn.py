M = ['Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn']
X = ['O','S','Se','Te','Po','Lv']
for m in range(len(M)):
    for x in range(len(X)):
        for i in range (1,10):
            print(f'{M[m]}{X[x]}{i}')
