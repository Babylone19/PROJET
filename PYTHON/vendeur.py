
from datetime import datetime , time 

from verifcationDate import verification

from controle_num  import controle_num

from table_create import table



#Fonction qui permet la creation du client si le client n'exists pas encore dans la base

def creation_client (matricule,conn) :

	cur=conn.cursor()

	print("BIENVENU SUR LA PAGE D'ENREGISTREMENT D'UN CLIENT ")

	nom = input("Entrez le nom du client :  ")

	while not nom.isalpha() and nom.isdigit() :

		print("$$$Erreur de saisi entre des lettres ou des lettres suivies des chiffres$$$")

		nom = input("Entrez le nom du client :  ")

	print()

	prenom = input("Entrez le prenom du client : ")

	while not prenom.isalpha() and prenom.isdigit() :

		print("$$$Erreur de saisi entre des lettres ou des lettres suivies des chiffres$$$")

		prenom = input("Entrez le prenom du client : ")

	print()

	jour_naissance =input("Entrez la date du jour de naissance du client  : ")

	while jour_naissance.isdigit() == False :

		print("$$$Erreur le jour de naissance commence de 1 à 31$$$")

		jour_naissance = input("Entrez le jour de naissance du client ")

	print()

	mois = input("Entrez le mois de naissance du client en chiffre : ")

	while mois.isdigit()==False :

		print("Erreur le mois commence de 1 et ce limite à 12 ")

		mois = input("Entrez corectement le mois du client : ")

		
	print()

	annee_naissance =input("Entrez l'année de naissance du client :  ")

	while annee_naissance.isdigit()==False :

		print("$$$L'annee doit être des chiffres$$$")

		annee_naissance =input("Entrez l'année de naissance du client :  ")

	
	while not  verification(jour_naissance,mois,annee_naissance):

		print("$$$Erreur de saisi $$$$")

		jour_naissance =input("Entrez la date du jour de naissance du client  : ")

		print()

		mois = input("Entrez corectement le mois du client : ")

		print()

		annee_naissance =input("Entrez l'année de naissance du client :  ")



	link =f"{jour_naissance}/{mois}/{annee_naissance}"


	adresse = input("Entrez l'adresse du client  : ")

	while not adresse.isalpha() and adresse.isdigit() :

		print("$$$Erreur entrez que des lettres accompagner des chiffres si vous voulez  !!!!$$$")

		adresse = input("Entrez l'adresse du client  : ")

	print()

	telephone = input("Entrez le numero du client sans l'indicateur du pays : ")

	while telephone.isdigit() == False :

		print("$$$Erreur entrez que des chiffres !!!!$$$$")

		print()

		telephone = input("Entrez le numero du client sans l'indicateur du pays : ")

	while not controle_num(telephone) :


		print("*****Erreur de saisi du numero******!!!!")

		print()

		telephone = input("Entrez le numero du client sans l'indicateur du pays : ")

	telephone= str(telephone)

	cur.execute("insert into CLIENTS(Nom_Clt,Prenom_clt,Date_Naissance_Clt,Telephone_Clt,Adresse_Clt) values(%s,%s,%s, %s,%s)",(nom,prenom,link,telephone,adresse,))

	conn.commit()

	print("$$$$CREATION DU CLIENT REUSSI$$$")

	cur.execute("select Id_Clt from CLIENTS where date_naissance_clt = %s and Telephone_Clt = %s" ,(link , telephone,))

	

	retour_cur = cur.fetchone()

	if retour_cur :

		retour_cur = retour_cur[0]

	#print(retour_cur)

	

	return  retour_cur



	
#creation_client()


#Fonction qui permet de recuperer identifiant du client dans la table client


def recup_id_clt(matricule,conn):

	cur=conn.cursor()


	reponse_recherche = input("#### RECHERCHE DU CLIENT  ####:  ")

	select_query="select * from CLIENTS  where nom_clt ilike %s or telephone_clt ilike %s  or adresse_clt  ilike %s  or date_naissance_clt :: text ilike %s or  prenom_clt ilike %s "

	cur.execute(select_query,(f'%{reponse_recherche}%' ,f'%{reponse_recherche}%' , f'%{reponse_recherche}%' , f'%{reponse_recherche}%' , f'%{reponse_recherche}%'))

	retour_recherche = cur.fetchall()

	if retour_recherche:


		colonne_recherche =["NUMERO","IDENTIFIANT" , "NOM CLIENT" , "PRENOM CLIENT" ,"DATE NAISSANCE","NUMERO TELEPHONE", "ADRESSE"]

		retour_table_recherche = table(colonne_recherche , retour_recherche)

		print()

		print(retour_table_recherche)

		print()

		reponse_vendeur_3 = input("Entrez son numero  :  ")


		while not  reponse_vendeur_3.isdigit() :

			print("$$$ Le numero  est incorrect $$$$")

			reponse_vendeur_3 = input("Entrez son numero:  ")


		cur.execute("select Id_Clt from CLIENTS   where numero_cli =%s ",(reponse_vendeur_3,))

		
	
		retour_select = cur.fetchone()



		if retour_select :


			retour_select= retour_select[0]

			print(retour_select)

			print("$$$ NUMERO  TROUVER $$$")


			retour_select

			enregistrer_produit(matricule,retour_select,conn)

		else :

			print("*********Ce numero  n'existe pas dans notre base********")

			retour_select=recup_id_clt(matricule,conn)

			retour_select

			enregistrer_produit(matricule,retour_select,conn)
	
	else:
		print()

		a= input("Voulez vous recommencer(1-oui et 2- non) : ")

		while a not in("1","2"):

			print("Erreur de saisi")

			a= input("Voulez vous recommencer(1-oui et 2- non) : ")

		if a =="1":

			recup_id_clt(matricule,conn)



		else:

			print()

			creation_clt = creation_client(matricule,conn)

			print()

			enregistrer_produit(matricule,creation_clt,conn)


	#return retour_select   

		


#recup_id_clt(matricule)
#conn.close()



#Fonction qui permet de recuperer identifiant de l'acteur qui s'est loger pour la vente

def recup_id_emp(matricule,conn):

	cur=conn.cursor()
	
	
	cur.execute("select Id_Emp from EMPLOYES where matricule=%s",(matricule,))

	
	
	result=cur.fetchone()

	if result:

		result = result[0]
	#print(result)

	return result
	




def enregistrer_commande(matricule,num_clt,num_emp,conn):#Fonction qui permet d'enregistrer une commande

	cur=conn.cursor()

	ap = datetime.now().date()
	
	date_ap = str(ap)
	
	heure_ap = datetime.now().time().strftime('%H:%M:%S')
	
	date= date_ap +" "+heure_ap
	
	id_clt=num_clt

	while not id_clt:

		print("### ECHEC DE COMMANDE ###")

		print()

		answer = input("$$$ Voulez vous recommancer : (1 = oui ou 2 = non ) ?  ")

		while answer not in ("1","2"):

			print("### ERREUR DE SAISI ###")

			answer = input("$$$ Voulez vous recommancer : (1 = oui ou 2 = non ) ?  ")


		if answer == "1" :

			print()

			enregistrer_commande(matricule,num_clt)

		else : 

			print()

			menu_vendeur(matricule,conn)
	
	
		
		#nom_client=input("saisir le nom du client:")
		
	cur.execute("insert into COMMANDES(Date_Comd,Id_Clt,Id_Emp) values(%s,%s,%s)",(date,id_clt,num_emp,))

	conn.commit()

	cur.execute("select id_comd from commandes where Id_Clt = %s and date_comd = %s",(id_clt,date,))

	

	retour_comm = cur.fetchone()

	if retour_comm:

		retour_comm= retour_comm[0]

	return retour_comm





#Fonction qui permet afficher les listes des produits  pour voir combien il reste en stock

def afficher_liste_produit(matricule,conn):

	cur=conn.cursor()

	cur.execute("select id_prod,libelle_produit, quantite_prod from PRODUITS ")

	

	resultat_affiche =cur.fetchall()

	colonne_affiche= ["IDENTIFIANT DU PRODUIT","NOM DU PRODUIT","QUANTITE EN STOCK"]

	table_affiche = table(colonne_affiche,resultat_affiche)

	print()
	print()

	print("***** LISTES DES PRODUITS *****")

	print()
	print()

	print(table_affiche)

	print()
	print()



#afficher_liste_produit()
#conn.close()


#Fonction qui permet afficher les listes des produits commandes par un clients à une periode donnée


def afficher_liste_produits_commande(matricule,conn):

	cur=conn.cursor()


	


	retour=rechercher_commande_client_simple(conn) 
						
	print()


	jour_commande_1 =input("Entrez la date du jour de la commande du client  : ")

	while jour_commande_1.isdigit() == False :

		print("$$$Erreur le jour de la commande  commence de 1 à 31$$$")

		jour_commande_1 =input("Entrez la date du jour de la commande du client  : ")

	print()

	mois_1 = input("Entrez le mois de la commande du client en chiffre : ")

	while mois_1.isdigit()==False :

		print("Erreur le mois commence de 1 et ce limite à 12 ")

		mois_1 = input("Entrez corectement le mois de la commande  du client : ")

		
	print()


	annee_commande_1 =input("Entrez l'année de la commande du client  du client :  ")

	while annee_commande_1.isdigit()==False :

		print("$$$L'annee doit être des chiffres$$$")

		annee_commande_1 =input("Entrez l'année de la commande  du client :  ")

	
	while not  verification(jour_commande_1,mois_1,annee_commande_1):

		print("$$$Erreur de saisi $$$$")

		jour_commande_1 =input("Entrez la date du jour de la commande du client  : ")

		print()

		mois_1 = input("Entrez corectement le mois de la commande  du client : ")

		print()

		annee_commande_1 =input("Entrez l'année de la commande  du client :  ")



	link_1 =f"{jour_commande_1}/{mois_1}/{annee_commande_1}"

	print("*** ENTREZ LA SECONDE INTERVALLE ***")


	print()

	jour_commande_2 =input("Entrez la date du jour de la commande  du client  : ")

	while jour_commande_2.isdigit() == False :

		print("$$$Erreur le jour de la commande  commence de 1 à 31$$$")

		jour_commande_2 = input("Entrez le jour de la commande  du client ")

	print()

	mois_2 = input("Entrez le mois de la commande  du client en chiffre : ")

	while mois_2.isdigit()==False :

		print("Erreur le mois commence de 1 et ce limite à 12 ")

		mois_2 = input("Entrez corectement le mois de la commande  du client : ")

	print()
	
	annee_commande_2 =input("Entrez l'année de la commande  du client :  ")

	while annee_commande_2.isdigit()==False :

		print("$$$L'annee doit être des chiffres$$$")

		annee_commande_2 =input("Entrez l'année de la commande  du client :  ")

	
	while not  verification(jour_commande_2,mois_2,annee_commande_2):

		print("$$$Erreur de saisi $$$$")

		jour_commande_2 =input("Entrez la date du jour de la commande  du client  : ")

		print()

		mois_2 = input("Entrez corectement le mois de la commande  du client : ")

		print()

		annee_commande_2 =input("Entrez l'année de  la commande  du client :  ")



	link_2 =f"{jour_commande_2}/{mois_2}/{annee_commande_2}"


	
	
	cur.execute("select Nom_Clt,libelle_produit,Id_Emp,date_comd from commandes ,clients,ligne_commande,produits where produits.id_prod = ligne_produits.id_prod and commandes.id_comd = ligne_produits.id_comd and commandes.id_clt = clients.id_clt and commandes.id_clt = %s  and date_comd between %s and %s", (retour , link_1,link_2,))

	

	list_comm=cur.fetchall()

	if list_comm :

		colone_comm = ["NOM CLIENTS","NOM PRODUIT","IDENTIFIANT DU CLIENT","DATE COMMANDE"]

		tableau_comm = table(colone_comm,list_comm)
		
		#print(list_comm)

		print(tableau_comm)

	else:

		print("£$$$$ PAS DE COMMANDE EN CE JOUR £££££")

		print()

		quitter(matricule,conn)


		#return list_comm
	
#afficher_liste_produits_commande()
#conn.close()


#Fonction qui permet d'enregistrer les produits  qui constitues la commande


def enregistrer_produit(matricule,num_clt,conn):

	cur=conn.cursor()

	ap = datetime.now().date()
	
	date_ap = str(ap)
	
	heure_ap = datetime.now().time().strftime('%H:%M:%S')
	
	date= date_ap +" "+heure_ap

	tab_id={}

	produit_nom=[]

	produits_plus =[]

	montant =[]

	liste_verif = []
	
	stock_produits={}

	#recuperation de id,la quantite des produits en base pour alimenter un dictonnaire (chaque id et ca quantite
	cur.execute("select id_prod,quantite_prod from PRODUITS;")

	donne_stock = cur.fetchall()

	for tuple in donne_stock:

		cle_dict= tuple[0]

		valeur_dict=tuple[1]

		stock_produits[cle_dict]=valeur_dict
	

	constante = True 

	while constante :

		print()

		recherche_produit = input("RECHERCHE DU PRODUIT  :  ").lower()


		select_query_produit = "select numero,libelle_produit, quantite_prod,prix_vente_prod,categorie_prod,poids_prod from PRODUITS where  id_prod ilike %s or libelle_produit ilike %s or quantite_prod ::text ilike %s or prix_vente_prod ::text ilike %s or categorie_prod ilike %s or poids_prod ilike %s  "

		cur.execute(select_query_produit ,(f'%{recherche_produit}%',f'%{recherche_produit}%',f'%{recherche_produit}%',f'%{recherche_produit}%',f'%{recherche_produit}%',f'%{recherche_produit}%'))

		

		retour_recherche_produit = cur.fetchall()

		if retour_recherche_produit :


			colonne_produit= ["NUMERO DU PRODUIT","LE NOM PRODUIT","QUANTITE DU PRODUIT","PRIX VENTE ","CATEGORIE PRODUIT","POIDS DU PRODUIT"]

			table_produit = table(colonne_produit , retour_recherche_produit)

			print()
			print()

			print(" *** LES PRODUITS ****")

			print()

			print(table_produit)

		else:

			print("ˇˇˇPas de produit soyez plus claire ˇˇˇ")

			print()

			print("**** Tous les commandes ont été annulés *****")

			print()

			enregistrer_produit(matricule,num_clt,conn)


		print()

		reponse_produit= input("£££ Entrez le numero du produit £££ : ")

		while not reponse_produit.isdigit()  :

			print("£££££ Erreur de saisi £££££")

			print()

			reponse_produit= input("£££ Entrez le numero du produit £££ : ")

		cur.execute("select id_prod from PRODUITS where numero = %s",(reponse_produit,))

		

		retour_select_prod = cur.fetchone()

		if retour_select_prod :

			retour_select_prod = retour_select_prod[0]

			cur.execute("select prix_vente_prod from PRODUITS where id_prod = %s",(retour_select_prod,))

			

			retour_demande_1 = cur.fetchone()

			if retour_demande_1[0] > 0 :

				retour_demande_1 = retour_demande_1[0]

				demande_2 = input("Entrez la quantite voulu : ")

				while not demande_2.isdigit() and demande_2 ==  "0" :

					print("££££ Erreur de saisi ££££")

					print()

					demande_2 = input("Entrez la quantite voulu : ")

				demande_2= int(demande_2)

			
				#verification si le produit concerner ce trouve dans le dictionnaire

				if retour_select_prod in stock_produits :

					#verification si la quantite voulu est inferieur a la quantite en stock

					if demande_2 <= stock_produits[retour_select_prod]:

						#si oui on diminu la quantite du produit en question dans le dictionnaire

						stock_produits[retour_select_prod]-=demande_2

						

						total = demande_2 * retour_demande_1

						montant.append(total)

						cur.execute("select libelle_produit from PRODUITS where id_prod = %s ",(retour_select_prod,))

						reste_nom =cur.fetchone()

						reste_nom=reste_nom[0]


						#verification pour ne pas repeter le produit deux fois sur la facture et de remplacer ca quantite par la nouvelle si le produit a etre encore indexer

						if reste_nom in tab_id:

							



							tab_id[reste_nom]=(demande_2,retour_demande_1)

								

						else:

							#produits_commandes[nom]=(quantite,prix)
								
							tab_id[reste_nom]=(demande_2,retour_demande_1)

						# verification pour ne pas repeter le produit deux fois  et de remplacer ca quantite par la nouvelle si le produit a etre encore indexer

						constat= None

						for index , ligne in enumerate(produits_plus):

							quantite_veri ,prix_vt,id_produit = ligne 

							if retour_select_prod == (id_produit):

								constat = index

								break

						if constat is not None:

							quantite_veri = demande_2

							produits_plus[constat]=(quantite_veri ,prix_vt,id_produit)

							

						else :
							
							
							

							produits_plus.append((demande_2,retour_demande_1,retour_select_prod))


						constante = input("Voulez vous continuez ou non (oui - Pour contunier et non- Pour arreter )").lower()

						while constante not in ("oui","non"):

							print("Erreur de saisi")

							constante = input("Voulez vous continuez ou non (oui - Pour contunier et non- Pour arreter )").lower()

						if constante.lower() != "oui":

							constante =False

							mnt =sum(montant)
							#parcours du ditionnaire pour alimenter les données contenus dans une liste pour utiliser la lse pour en faire la facture

							for  nom_prod ,info in tab_id.items():

								qunt=info[0]

								prix_v=info[1]

								produit_nom.append((nom_prod,qunt,prix_v))


							print()

							print()

							col= ["NOM PRODUIT","QUANTITE","PRIX VENTE"]

							recu= table(col ,produit_nom)

							cur.execute("select Nom_Clt,prenom_clt,telephone_clt from CLIENTS where Id_Clt =%s",(num_clt,))

							no_clt=cur.fetchone()

							nom=no_clt[0]

							prenom = no_clt[1]

							tel=no_clt[2]

							print()

							print("                                ETS BABA TRAORE    ")

							print()

							print(f"LA DATE DE LA COMMANDE :  {date} ")

							print()

							print(f"					NOM DU CLIENT :  {nom} ")

							print()

							print(f"					PRENOM DU CLIENT :  {prenom}")

							print()

							print(f"					NUMERO DU CLIENT :  {tel}  ")


							print()

									
							print(															recu  )

							print()

							print()

							print(f"                                                   LE MONTANT A PAYER  :  {mnt}")

							print()

							print()
							#la partie pour la validation

							validation = input("£££ ok -Pour valider la COMMANDE et  non -Pour annuler la COMMANDE ")

							while validation not in ("ok","non"):

								print("££££ Erreur de saisi ££££")

								validation = input("£££ ok -Pour valider la COMMANDE et  non -Pour annuler la COMMANDE ")


							if validation.lower()=="ok":

								

								if produits_plus :

									#print(produits_plus)

									num_emp= recup_id_emp(matricule,conn)

									num_comm = enregistrer_commande(matricule,num_clt,num_emp,conn)

									for produit_red in produits_plus :

										quantite,prix,num_prod_1 = produit_red

										enregister_la_ligne_prod(quantite,prix,num_prod_1,num_comm,conn)

									#fact = facturation_simple(num_comm,conn)

									print()

									#print(fact)

									quitter(matricule,conn)

							elif validation.lower()=="non" :

								print(" COMMANDE ANNULEE ")

						else : 

							constante = True

					else:

						print("£££££ La quantite demandée est superieure à  celle contenue en base   £££££")



				else:

					print("££££  Stock insuffisant pour ce produit £££££")

					enregistrer_produit(matricule,num_clt,conn)

			else :

				print("££££ Le produit  ne peut être vendu car le prix de vente n'est pas encore fixer ££££££")

				enregistrer_produit(matricule,num_clt,conn)

		else :

			print("£££ LE NUMERO n'est pas lié à un produit £££££ ")

			choix_vend = input("ˇˇˇ Voulez vous recommencer où quitter ( 1 - Pour commencer ou 2 - Pour quitter) ˇˇˇ?  ")

			while choix_vend not in ("1" ,"2"):

				print("€€€€ Saisi non conforme €€€€")

				choix_vend = input("ˇˇˇ Voulez vous recommencer où quitter ( 1 - Pour commencer ou 2 - Pour quitter) ˇˇˇ?  ")

			if choix_vend =="1":

				print()

				enregistrer_produit(matricule,num_clt,conn)

			else :



				print()

				menu_vendeur(matricule,conn)

					


	











#Fonction qui permet de rechercher un client

def rechercher_commande_client_simple(conn):

	cur=conn.cursor()

	



	reponse_recherche = input("#### RECHERCHE DU  CLIENT ####:  ")

	
	
	select_query_aff_2 ="select numero_cli, nom_clt,prenom_clt,Date_Naissance_Clt,Telephone_Clt,adresse_clt from CLIENTS where nom_clt ilike %s or telephone_clt ilike %s  or adresse_clt  ilike %s or  date_naissance_clt :: text ilike %s or  prenom_clt ilike %s "

	

	cur.execute(select_query_aff_2,(f'%{reponse_recherche}%' ,f'%{reponse_recherche}%' , f'%{reponse_recherche}%'  , f'%{reponse_recherche}%' , f'%{reponse_recherche}%'))

	

	retour_select_aff_2 = cur.fetchall()

	if retour_select_aff_2 :


		colonne_recherche_aff_2 = ["IDENTIFIANT" , "NOM CLIENT" , "PRENOM CLIENT" ,"DATE NAISSANCE","NUMERO TELEPHONE", "ADRESSE"]

		retour_table_recherche_aff_2 = table(colonne_recherche_aff_2 , retour_select_aff_2)

		print()

		print("***** CLIENTS ******")

		print()

		print()

		print(retour_table_recherche_aff_2)

		print()

		print()




		reponse_vendeur_10 = input("Entrez son numero  :  ")


		while not reponse_vendeur_10.isdigit() :

			print("$$$ Le numero  est incorrect $$$$")

			print()

			reponse_vendeur_10 = input("Entrez son numero  :  ")

		print()

		choix_aff= input("le numero est il conforme a votre client : (1 = oui , 2 = non)  ?  ")

		while choix_aff not in ("1","2"):

			print("Entrez correctement la reponse : ")

			print()

			choix_aff= input("le numero est il conforme a votre client : (1 = oui , 2 = non)  ?  ")

		if choix_aff.lower()=="1":


			cur.execute("select Id_Clt from CLIENTS where  numero_cli =%s ",(reponse_vendeur_10,))

			
		
			retour_select_aff = cur.fetchone()



			if retour_select_aff :


				retour_select_aff= retour_select_aff[0]


				#print(retour_select_aff)

				print("$$$ NUMERO TROUVER $$$")


				return  retour_select_aff

			else :

				print("*********Ce numero  n'existe pas dans notre base********")

				print()

				rechercher_commande_client_simple(conn)
				

				

		elif choix_aff.lower()=="2":

			print()

			rechercher_commande_client_simple(conn)
				


			

	else:

		print("£££ Pas de clients ££££$")

		print()

		rechercher_commande_client_simple(conn)
		


		

	





		


		

	


#pour enregistrer les lignes de commande 

def enregister_la_ligne_prod(quantite_comm,prix_vente_prod,num_prod,num_com,conn):

	cur=conn.cursor()

	quantite_comm = int(quantite_comm)

	prix_vente_prod=int(prix_vente_prod)

	cur.execute("insert into ligne_commande (quantite_commande,prix_vente,id_prod,id_comd) values (%s,%s,%s,%s)",(quantite_comm,prix_vente_prod,num_prod,num_com,))

	conn.commit()

	
#facturation  pour faire la facture mais il n'est plus utiliser 


def facturation_simple(num_com,conn):


	cur=conn.cursor()

	print("£££££ LA COMMANDE ETE BIEN ENREGISTRER £££££")

	


	cur.execute("select libelle_produit,quantite_commande,prix_vente,montant from  PRODUITS P,ligne_commande L,commandes co where P.id_prod = L.id_prod and L.id_comd = co.id_comd and co.id_comd =%s ",(num_com,))

	facture_l = cur.fetchall()

	colonne_fact_l = ["NOM PRODUIT","QUANTITE ","PRIX VENTE","MONTANT"]

	table_fact_l= table(colonne_fact_l,facture_l)

	print()

	print(" LA FACTURE DE LA COMMANDE ")


	print()

	print(table_fact_l)


	cur.execute("select Nom_Clt,prenom_clt,telephone_clt,montant_commande,date_comd from clients c,commandes co where c.id_clt=co.id_clt  and co.id_comd= %s",(num_com,))


	facture = cur.fetchall()

	if facture:

		colone_facture =["NOM DU CLIENT","PRENOM DU CLIENT","NUMERO TELEPHONE","MONTANT TOTAL","DATE COMMANDE"]

		table_facture = table(colone_facture,facture)

	


		

		print(table_facture)
		

		print()


		print()




	#return table_facture










#Fonction qui permet de quitter et revenir a chaque fois sur la page principal


def quitter(matricule,conn):

	cur=conn.cursor()


	retour = input("Voulez vous revenir ou quitter ( 'o- pour revenir et n- pour quitter') : ").lower()

	while retour not in ('o','n'):

		print("Erreur ")

		retour = input("Voulez vous revenir ou quitter ( 'o- pour revenir et n- pour quitter')").lower()

	if retour =='o':

		menu_vendeur(matricule,conn)
		
		
	else:

		print("####################VOUS ÊTES DECONNECTER##########")


#Fonction d'affichage du menu vendeur auquelle le vendeur est appeler a faire


def menu_vendeur(matricule,conn):
	print("   ***********************VOUS ÊTES CONNECTER EN TANT QUE VENDEUR**********************  ")
	print("___________________________________________________________________________________________________")
	print("|                  BIENVENUE SUR LA PAGE DE LA BOUTIQUE                                            |")
	print("|                                                                                                  |")
	print("|         1 - ENREGISTRER UNE COMMMANDE                                                            |")
	print()
	print("|         2-AFFICHIER LES PRODUITS POUR VOIR COMBIEN IL RESTE EN STOCK                             |")
	print()
	print("|         3-AFFICHER LES PRODUITS COMMANDES A UNE PERIODE DONNEES                                  |")
	print()
	print("|         4- QUITTER OU REVENIR                                                                    |")
	print()
	print("___________________________________________________________________________________________________ ")

	print()

	choix = input("Entrez  le numero qui repond à votre besoin : ")

	if choix.isdigit() == False:

		print("Errreur entrez correctement les numero uniquement que des chiffres !!! ")

		print()

		choix = input("Entrez  le numero qui repond à votre besoin : ")

	while choix not in ('1','2','3','4') :

		print("Errreur entrez correctement les numero uniquement que des chiffres !!! ")

		print()

		choix = input("Entrez  le numero qui repond à votre besoin : ")

	if choix == '1':

		print()

		recup_id_clt(matricule,conn)

		print()

		quitter(matricule,conn)

	elif choix =='2':

		print()

		afficher_liste_produit(matricule,conn)

		print()

		quitter(matricule,conn)

	elif choix == '3':
		print()

		afficher_liste_produits_commande(matricule,conn)

		print()

		quitter(matricule,conn) 

	else :
		print()

		quitter(matricule,conn)
#menu_vendeur(matricule)
		
			
#menu_vendeur()
#conn.close()

