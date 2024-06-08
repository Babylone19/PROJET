
from magasinier import menu_magasinier

from vendeur  import  menu_vendeur

from datetime import datetime , time 

from controle_num  import controle_num

from table_create import table

from verifcationDate import verification


#Fonction qui permet de quitter et revenir a chaque fois sur la page principale

def quitter(matricule,conn):


	retour = input("Voulez vous revenir ou quitter ( 'o- pour revenir et n- pour quitter') : ")

	while retour not in ('o','n'):

		print("Erreur ")

		retour = input("Voulez vous revenir ou quitter ( 'o- pour revenir et n- pour quitter')")

	if retour =='o':

		menu_gerant(matricule,conn)
		
	else:

		print("#################### VOUS ÊTES DECONNECTER ##########")



#Fonction qui permet de fixer le prix de vente des produits s'il ne sont pas encore fixer

def fixer_prix (matricule,conn):

	constante=True

	while constante :

		cur=conn.cursor()

		cur.execute("select numero,libelle_produit,quantite_prod ,categorie_prod, poids_prod from PRODUITS where prix_vente_prod = %s ",(0,))

		

		produi_pv= cur.fetchall()

		if produi_pv :

			colonne_produit =["NUMERO","NOM DU PRODUIT","QUANTITE STOCK","CATEGORIE","POIDS"]

			table_prod_pv =table(colonne_produit,produi_pv)

			print()

			print()

			print(" LES PRODUITS SANS PRIX DE VENTE ")

			print()

			print()

			print(table_prod_pv)


			print()

			print()

			

			num_prod =input("Entrez le numero du produit concerner : " )

			while not num_prod.isdigit():

				print(" Erreur de saisi !!!")

				num_prod =input("Entrez le numero du produit concerner : " )

			if num_prod :

				cur.execute("select id_prod from PRODUITS where numero =%s",(num_prod,))

				variable=cur.fetchone()

				if variable:

					variable_pv =input(" Entrez le prix de vente : ")

					while not variable_pv.isdigit():

						print("ERREUR LE PRIX DE VENTE DOIT ETRE UN ENTIER")

						variable_pv =input(" Entrez le prix de vente : ")

					variable_pv =int(variable_pv)

					while variable_pv <=0 :

						print("Le prix de vente ne doit pas inferieur ou egale a zero ")

						variable_pv =input(" Entrez le prix de vente : ")

					variable_pv=int(variable_pv)

					cur.execute("update produits set prix_vente_prod =%s where id_prod =%s",(variable_pv,variable,))

					conn.commit()

					print(" Le prix de vente a ete bien fixer ")

					constante =input(" voulez vous continuez !(1-oui et 2-non) : ")

					while constante not in("1","2"):

						print("Erreur d'entree !! ")

						constante =input(" voulez vous continuez !(1-oui et 2-non) : ")

					if constante == "1":

						constante=True

					else:

						constante=False
				else:

					print(" Aucun produit associe a ce numero !!")

					print()

					fixer_prix(matricule,conn)

			else:
			
				print(" Aucun numero entree !! ")

				print()

				fixer_prix(matricule,conn)

		else:
			print()

			print(" AUCUN PRODUIT SANS PRIX DE VENTE ")

			print()

			print()


			menu_gerant(matricule,conn)



#Fonction qui permet de consulter les entree et sorties des operations


def consulter_journal(matricule,conn):

	cur=conn.cursor()

	print("1 -AFFICHER LES PRODUITS DONT LA QUANTITE STOCK EST INFERIEUR A UNE QUANTIE DONNEE ")

	print("2- AFFICHER LES CLIENTS DONT LE MONTANT TOTAL DE LA COMMANDE EST SUPEIREUR A UN MONTANT DONNEE ET A UNE PERIODE DONNEE ")

	variable_choix = input(" £££££ Entrez votre choix entre (1 ou 2 ) ££££ :  ")

	while variable_choix not in ("1","2"):

		print("Errreur de saisi ")

		variable_choix = input(" £££££ Entrez votre choix entre (1 ou 2 ) ££££ :  ")


	if variable_choix=="1":

		qtn = input(" Entrez UNE VALEUR DONNEE :   ")

		while not qtn.isdigit():

			print(" Erreur de saisi ")

			qtn = input(" Entrez UNE VALEUR DONNEE :   ")

		qtn= int(qtn)

		cur.execute("select * from PRODUITS where quantite_prod < %s ",(qtn,))

		

		qnt_retour = cur.fetchall()

		if qnt_retour :

			colone_qnt=["NUMERO","IDENTIFIANT","NOM PRODUIT","QUANTITE ","PRIX VENTE","CATEGORIE","POIDS"]

			table_qnt= table(colone_qnt,qnt_retour)

			print()

			print()

			print(f"PRODUITS DONT LA QUANTITE EST INFERIEUR A : {qtn}  *************** ")

			print()

			print()

			print(table_qnt)

			print()

			print()

			quitter(matricule,conn)

		else:

			print("AUCUN PRODUIT DONT LA QUANTITE EST INFERIEUR A LA QUANTITE DONNEE")

			print()

			quitter(matricule,conn)

	else:

		


		mnt = input("Entrez un montant  donnee : ")

		while not mnt.isdigit() :

			print("Entrez des chiffres  ")

			mnt = input("Entrez un montant  donnee : ")

		mnt= int(mnt)

		
		jour_commande_1 =input("Entrez la date du jour de la commande du client  : ")

		while jour_commande_1.isdigit() == False :

			print("$$$Erreur le jour de la commande  commence de 1 à 31$$$")

			jour_commande_1 =input("Entrez la date du jour de la commande du client  : ")
			
		mois_1 = input("Entrez le mois de la commande du client en chiffre : ")

		while mois_1.isdigit()==False :

			print("Erreur le mois commence de 1 et ce limite à 12 ")

			mois_1 = input("Entrez corectement le mois de la commande  du client : ")

			
		
		annee_commande_1 =input("Entrez l'année de la commande du client  du client :  ")

		while annee_commande_1.isdigit()==False :

			print("$$$L'annee doit être des chiffres$$$")

			annee_commande_1 =input("Entrez l'année de la commande  du client :  ")

		
		while not  verification(jour_commande_1,mois_1,annee_commande_1):

			print("$$$Erreur de saisi $$$$")

			jour_commande_1 =input("Entrez la date du jour de la commande du client  : ")

			mois_1 = input("Entrez corectement le mois de la commande  du client : ")

			annee_commande_1 =input("Entrez l'année de la commande  du client :  ")



		link_1 =f"{jour_commande_1}/{mois_1}/{annee_commande_1}"


		print("*** ENTREZ LA SECONDE INTERVALLE ***")

		jour_commande_2 =input("Entrez la date du jour de la commande  du client  : ")

		while jour_commande_2.isdigit() == False :

			print("$$$Erreur le jour de la commande  commence de 1 à 31$$$")

			jour_commande_2 = input("Entrez le jour de la commande  du client ")

			
		mois_2 = input("Entrez le mois de la commande  du client en chiffre : ")

		while mois_2.isdigit()==False :

			print("Erreur le mois commence de 1 et ce limite à 12 ")

			mois_2 = input("Entrez corectement le mois de la commande  du client : ")

			
		
		annee_commande_2 =input("Entrez l'année de la commande  du client :  ")

		while annee_commande_2.isdigit()==False :

			print("$$$L'annee doit être des chiffres$$$")

			annee_commande_2 =input("Entrez l'année de la commande  du client :  ")

		
		while not  verification(jour_commande_2,mois_2,annee_commande_2):

			print("$$$Erreur de saisi $$$$")

			jour_commande_2 =input("Entrez la date du jour de la commande  du client  : ")

			mois_2 = input("Entrez corectement le mois de la commande  du client : ")

			annee_commande_2 =input("Entrez l'année de  la commande  du client :  ")



		link_2 =f"{jour_commande_2}/{mois_2}/{annee_commande_2}"

		print()

		print()

		print()

		cur.execute("select c.id_clt ,c.nom_clt , sum(co.montant_commande) from  clients c , ligne_commande l ,commandes co where c.id_clt=co.id_clt and l.id_comd = co.id_comd and date_comd between %s and %s group by c.id_clt  having sum(co.montant_commande)> %s  ",(link_1,link_2,mnt,))

		


		montant_comd = cur.fetchall()

		if montant_comd :

			colone_comd = ["NUMERO","NOM CLIENTS","MONTANT TOTAL"]

			table_comd = table(colone_comd,montant_comd)

			print()

			print()

			print("£££££   LES CLIENTS   £££££")

			print()

			print()


			print(table_comd)

			print()

			print()


		else : 

			print(" Pas de clients ")

			print()

			quitter(matricule,conn)

		



#Fonction d'affichage de menu auquel un gerant est affronter pour faire ses operations



def menu_gerant(matricule,conn):  

	cur=conn.cursor()

	cur.execute("select libelle_produit,categorie_prod,poids_prod from PRODUITS where prix_vente_prod = %s ",(0,))

	conn.commit()

	resultat_produit = cur.fetchall()

	if resultat_produit :

		colone= ["NOM PRODUIT","CATEGORIE","POIDS"]

		table_produit = table(colone,resultat_produit)


		print()

		print()

		print("LES PRODUITS DONT LE PRIX DE VENTE N'EST PAS FIXER ")

		print()

		print()

		print(table_produit)

		print()

		print()

	else:
		print("TOUT VOS PRODUITS ONT UN PRIX DE VENTE FIXER ")

		print()

	print("   ***********************VOUS ÊTES CONNECTER EN TANT QUE GERANT**********************  ")
	print("___________________________________________________________________________________________________")
	print("|                  BIENVENUE SUR LA PAGE DE LA BOUTIQUE                                            |")
	print("|                                                                                                  |")

	print("|                1 -FAIRE AUTRE CHOSE QUE LE VOTRE                                                 |")
	print()
	print("|                2-FIXER PRIX DE VENTE                                                             |")
	print()
	print("|                3-CONSULTER LE JOURNAL DES EVENEMENTS                                             |")
	print()
	print("|                4-QUITTER OU REVENIR                                                              |")

	print()
	print("___________________________________________________________________________________________________")

	print()

	choix_1 = input(" Entrez le numero de l'instruction qui repond à votre besoin : ")

	if choix_1.isdigit()==False :

		print (" Erreur de saisi entrez que des chiffres 1 !!!!!") 

		choix_1 = input(" Entrez le numero de l'instruction qui repond à votre besoin : ")


	while  choix_1 not in ('1','2','3','4') :

		print (" Erreur de saisi entrez que des chiffres 1 !!!!!") 

		choix_1 = input(" Entrez le numero de l'instruction qui repond à votre besoin : ")

	if choix_1 == '1':

		print()

		print("1- FAIRE L'ACTION DU MAGASINIER   ")

		print()

		print("2- FAIRE L'ACTION DU VENDEUR  ")

		print()

		choix_2 = input(" Entrez le numero de l'instruction qui repond à votre besoin : ")

		if choix_1.isdigit()==False :

			print(" Erreur de saisi entrez que des chiffres 1 !!!!!")

			choix_2 = input(" Entrez le numero de l'instruction qui repond à votre besoin : ")

		while  choix_2 not in ('1','2') :

			print (" Erreur de saisi entrez que des chiffres 1 !!!!!") 

			choix_2 = input(" Entrez le numero de l'instruction qui repond à votre besoin : ")

		if choix_2  =='1':

			menu_magasinier(matricule,conn)

			print()

			quitter(matricule,conn)
		else :

			menu_vendeur(matricule,conn)

			print()

			quitter(matricule,conn)



	elif choix_1 == '2':

		fixer_prix(matricule,conn)

		print()
		
		quitter(matricule,conn)

	elif choix_1 == '3':
		
		consulter_journal(matricule,conn)

		print()

		quitter(matricule,conn)

	else :

		quitter(matricule,conn)


	



#menu_gerant()
