def verification(jour,mois,annee):

	jour = int(jour)

	mois = int(mois)

	annee = int(annee)

	if jour <= 0 or jour >31:
		return 0
	if mois <= 0 or mois >12 :
		return 0
	if  annee <= 0 or annee >=2023 :
		return 0
	
	if mois ==2:
		
		if (annee %4 == 0 and jour >29):
			return 0
		elif (annee%4!= 0 and jour >28):	
			return 0
	return 1

		
# def verification(jour,mois,annee):
# 	if jour <= 0 :
# 		return 0
# 	elif  jour > 31:
# 		return 0
# 	if mois <= 0 :
# 		return 0
# 	elif mois > 12:
# 		return 0
# 	if  annee < 1960 :
# 		return 0
# 	elif annee > 2023 :
# 		return 0
# 	elif mois == 2  :
# 		if (annee%4 == 0 and jour > 29):	
# 			return 0
# 		elif annee%4 !=0 and jour >28:
# 			return 0
# 	return 1 
# def  main():
# 	try :
# 		jour= int(input("Entrez le jour  : " ))
# 		mois = int(input("Entrez le mois : "))
# 		annee = int(input("Entrez l'année : "))
# 	except :
# 		print()
# 	else :
# 		while not verification(jour,mois,annee) :
# 			print("Invalide")
# 			try :
# 				jour= int(input("Entrez le jour  : " ))
# 				mois = int(input("Entrez le mois : "))
# 				annee = int(input("Entrez l'année : "))
# 			except :
# 				print("invalide")
# 		else :
# 			link =f"{jour}/{mois}/{annee}"
# 			print(link)
# if __name__ == '__main__':
# 	main()
