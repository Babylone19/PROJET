def controle_num(variable):
    if (variable.startswith('9') and variable[1] in ['0','1','2','3','6','7','8','9'] ) or (variable.startswith('7') and variable[1] in ['0','1','9']) :
        if len(variable) ==8:
            return 1
        else :
            return 0
    else :
        return 0

"""
def vv():
    try:
        telephone = input("Entrez le numero : ")
    except:
        print("invalide")
    else :
        while not foncto(telephone):
            print("invall")
            try:
                telephone = input("Entrez le numero : ")
            except:
                print("invalide")
        else :
            telephone = int(telephone)
            print(telephone)
            print(type(telephone))


vv()
"""
