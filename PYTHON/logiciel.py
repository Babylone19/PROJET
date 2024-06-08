from magasinier import  menu_magasinier

from gerant import  menu_gerant
	
from vendeur  import  menu_vendeur

#from quitter import main
import psycopg2

conn=psycopg2.connect("dbname=projet_fin_d_annee")

cur=conn.cursor()

#Fonction qui determine les fonctionnalités d'un acteur apres qu'il ce soit loger

def  logiciel(conn):
	print("_______________________________________________________________________________________________________________________________________________________________")
	print("|                                                                                                                                                             |")
	print("|***********************************************************************LOGIN*********************************************************************************|")
	print("|_____________________________________________________________________________________________________________________________________________________________|")
	
	print()
	nombre_essai = 0

	while nombre_essai < 3 :

		val_1 = input ("ENTREZ VOTRE STATUT : ").upper()

		while not val_1.isalpha() and val_1.isdigit():

			print("Erreur de saisi votre format doit être des lettres et des chiffres ")

			val_1 = input ("ENTREZ VOTRE STATUT : ").upper()

		mot_pass = input("Entrez votre mot de passe : ")

		while not mot_pass.isalpha() and mot_pass.isdigit():


			print("Erreur de saisi votre format doit être des lettres et des chiffres ")

			mot_pass = input("Entrez votre mot de passe : ")

		cur.execute("select statut_emp from employes where matricule =%s and mot_pass =%s",(val_1 ,mot_pass,))

		retour_select = cur.fetchone() 


		if retour_select :


			retour_select= retour_select[0]


			#print(retour_select)


			if retour_select =="Magasinier" :

				print()

				menu_magasinier(val_1,conn)

			elif retour_select =="Vendeur":

				print()

				menu_vendeur(val_1,conn)

			elif retour_select =="Gerant":

				print()

				menu_gerant(val_1,conn)

			print("quitter ou revenir  à la page de la boutique (o ,ou,n )")

			print()
			
			choix = input("Entrez votre choix : ").lower()

			
			while  choix not in ('o' ,'n'):


				print("*****Erreur****")


				choix = input("Entrez votre choix : ").lower()

			if choix == 'o' :

				print()

				logiciel(conn)

			else :

				print("*********VOUS ÊTES DECONNECTER DE LA PAGE ********")

		else :

			print("$$MATRICULE ou MOT DE PASSE INCORRECT$$$")

		
		nombre_essai += 1

		if nombre_essai == 3 :


			print("***** TROP DE TENTATIVE ******")

			print()

			choix = input("Voulez vous continuez  1 -si oui ou 2- si non ")

			while choix not in("1","2"):

				print("Erreur entrez correctement ")

				print()

				choix = input("Voulez vous continuez  1 -si oui ou 2- si non ")

			if choix =="1":

				print()

				logiciel(conn)

			else :

				print("****BONNE SUITE *****")

 
logiciel(conn)

conn.commit()
cur.close()
conn.close()
