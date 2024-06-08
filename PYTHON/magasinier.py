
from datetime import datetime , time 

from controle_num  import controle_num

from table_create import table


#Fonction qui permet de cree le produit si le produit n'existe pas dans notre base de donne


def cree_produit(conn):

	cur=conn.cursor()


	nom_prod = input("ENTREZ LE NOM DU PRODUIT : ").lower()

	while not nom_prod.isalpha() and nom_prod.isdigit():

		print("Erreur de saisi")

		nom_prod = input("ENTREZ LE NOM DU PRODUIT : ").lower()

	print()

	categorie= input("ENTREZ LA CATEGORIE : ").upper()

	while not categorie.isalpha() and categorie.isdigit():

		print("Erreur de saisi")

		categorie= input("ENTREZ LA CATEGORIE : ").upper()

	print()

	poids = input("ENTREZ LE POIDS : ")

	while not poids.isalpha() and poids.isdigit():

		print("Erreur de saisi")

		poids = input("ENTREZ LE POIDS : ")


	prix_vente = 0

	quantite_prod = 0

	cur.execute("insert into PRODUITS (libelle_produit,quantite_prod,prix_vente_prod,categorie_prod,poids_prod) values(%s,%s,%s,%s,%s)",(nom_prod,quantite_prod,prix_vente,categorie,poids,))

	conn.commit()

	cur.execute("select Id_Prod from PRODUITS where categorie_prod = %s and poids_prod = %s ", (categorie, poids))

	retour_id_prod = cur.fetchone()

	retour_id_prod = retour_id_prod[0]

	

	return retour_id_prod


#Fonction qui permet de quitter et revenir a chaque fois sur le menu


def quitter(matricule,conn):


	retour = input("Voulez vous revenir ou quitter ( 'o- pour revenir et n- pour quitter') : ").lower()

	while retour not in ('o','n'):

		print("Erreur ")

		retour = input("Voulez vous revenir ou quitter ( 'o- pour revenir et n- pour quitter')").lower()

	if retour =='o':

		menu_magasinier(matricule,conn)
		
	else:

		print("####################VOUS ÊTES DECONNECTER##########")



#Fonction qui permet de cree le fournisseur si le fournisseur n'est encore cree


def creation_fournisseur(conn):

	cur=conn.cursor()

	nom_fournisseur=input("saisir le nom du fournisseur :").upper()

	while nom_fournisseur.isalpha() ==False :

		print("Erreur entrez que des lettres !!!!")

		nom_fournisseur=input("saisir le nom du fournisseur :").upper()

	print()

	telephone=input("veillez saisir le telephone du fournisseur:")
	
	while telephone.isdigit() == False :
		
		print("Erreur entrez que des chiffres !!!!")
		
		telephone=input("veillez saisir le telephone du fournisseur :")
	
	while not controle_num(telephone) :
		
		print("Erreur entrez que des chiffres  ******!!!!")
		
		telephone=input("veillez saisir le telephone du fournisseur :")

	print()
	
	email=input("saisisez  l' email du fournisseur  :")
	
	while not email.isalpha() and email.isdigit():
	
		print("Erreur entrez que des lettres accompagner des chiffres si vous voulez  !!!!")
		
		email=input("saisisez  l' email du fournisseur  :")
	
	print()

	adresse=input("saisir l adresse du fournisseur :") 
	
	while not  adresse.isalpha()  and adresse.isdigit(): 
	
		print("Erreur entrez que des lettres accompagner des chiffres si vous voulez  !!!!")
		
		adresse=input("saisir l adresse du fournisseur :") 
	
	
	cur.execute("insert into FOURNISSEURS(Nom_Four,Telephone_Four,Email_Four,Adresse_Four) values(%s,%s,%s, %s)",(nom_fournisseur,telephone,email,adresse))

	conn.commit()

	cur.execute("select matricule from FOURNISSEURS where Nom_Four =%s",(nom_fournisseur,))

	

	retour_select=cur.fetchone()

	retour_select_1= retour_select[0]
	
	return retour_select 
	
#creation_fournisseur()


#Fonction qui permet de recuperer l'identifiant du fournisseur apres la creation du fournisseur


def recup_id_fourn(conn):

	cur=conn.cursor()

	recheche_four = input("Recherche du  fournisseur :  ").lower()

	

	v = "select nom_four, telephone_four, email_four,adresse_four,matricule from FOURNISSEURS where Nom_Four ilike %s or Telephone_Four ::text ilike %s or Email_Four :: text ilike %s or adresse_four ilike %s or matricule ilike %s  "

	cur.execute(v ,(f'%{recheche_four}%',f'%{recheche_four}%',f'%{recheche_four}%',f'%{recheche_four}%',f'%{recheche_four}%',))

	

	resultat_four = cur.fetchall()

	if resultat_four:

		colonne_four= ["NOM" ,"TELEPHONE","EMAIL","ADRESSE","MATRICULE"]

		retour_table_four = table(colonne_four,resultat_four)

		print()

		print("LES FOURNISSEURS ")

		print()
		print()

		print(retour_table_four)

		print()
		print()



		nom_fourn = input("veuillez saisir le numero matricule du fournisseur  : ").upper()
		
		while not  nom_fourn.isalpha() and nom_fourn.isdigit() :
		
			print("ERREUR !!!!!")
			
			nom_fourn= input("veuillez saisir le numero matricule du fournisseur  : ").upper()
			
		
		cur.execute("select Id_Four from FOURNISSEURS where matricule = %s ",(nom_fourn,))

		
		

		solut =cur.fetchone()

		if solut :

			print("*****FOURNISSEUR TROUVER ******")

			return solut

		else :

			print("*** AUCUN FOURNISSEUR AVEC CE NUMERO ***")

			rep = input(" 1 - Pour effectuer la recherche  2- Pour creer le fournisseur ")

			while rep not in ("1","2"):

				print("ERREUR !!!!!")

				rep = input(" 1 - Pour effectuer la recherche  2- Pour creer le fournisseur ")

			if rep.lower()=="1" :

				recup_id_fourn(conn)
				
			else :

				enregistrer=creation_fournisseur(conn)	
		
				cur.execute("select Id_Four from FOURNISSEURS  where matricule =%s",(enregistrer,))
			
				

				solut=cur.fetchone()
		
				if solut:
			
					solut = solut[0]
			
					print("***********Le fournisseur à  été bien créer ************")
		
					#print(solut)
			
				return solut



	else :

		print(" PAS DE FOURNISSEUR ")

		print()

		enregistrer=creation_fournisseur(conn)	
		
		cur.execute("select Id_Four from FOURNISSEURS  where matricule =%s",(enregistrer,))
			
		

		solut=cur.fetchone()
		
		if solut:
			
			solut = solut[0]
			
			print("***********Le fournisseur à  été bien créer ************")
		
			#print(solut)
			
		return solut 




def recup_id_emp(matricule,conn):#Fonction qui permet de recuperer l'identifiant de l'acteur connecter

	cur=conn.cursor()

	nom_emp=matricule

	cur.execute("select Id_Emp from EMPLOYES where matricule=%s",(nom_emp,))

	

	result=cur.fetchone()
	
	if result :
		
		result = result[0]	
		 
		
	#print (result)
	
	return result
	
	
#recup_id_emp()


def insert_into_app(matricule,conn):

	cur=conn.cursor()

	result=recup_id_emp(matricule,conn)

	print()

	solut=recup_id_fourn(conn)

	print()

	ap = datetime.now().date()
	
	date_ap = str(ap)
	
	heure_ap = datetime.now().time().strftime('%H:%M:%S')
	
	link = date_ap +" "+heure_ap
	
	cur.execute("insert into approvisionnements (date_app, id_four , id_emp) values (%s,%s,%s)",(link  , solut,result))

	conn.commit()

	cur.execute("select Id_App from APPROVISIONNEMENTS where date_app = %s", (link,))

	
	print()

	retour_id_app = cur.fetchone()

	retour_id_app = retour_id_app[0]

	return retour_id_app # Fonction qui permet d'alimenter la table approvisionnement a chaque fois qu'il y a action d'approvisionnement


	


#insert_into_app()	
	








def recuperation_id_prod(conn): #Fonction permet de recuperer l'identifient du produit concerner lors de l'approvisionnement  et appel la fonction qui permet de creer le produit au cas ou le produit n'existe pas

	cur=conn.cursor()


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

		solution= cree_produit(conn)
		
		return solution

	print()

	reponse_produit= input("£££ Entrez le numero du produit £££ : ")

	while not reponse_produit.isdigit()  :

		print("£££££ Erreur de saisi £££££")

		reponse_produit= input("£££ Entrez le numero du produit £££ : ")

	cur.execute("select id_prod from PRODUITS where numero = %s",(reponse_produit,))

	

	solution = cur.fetchone()

	if solution :

		print("****Le produit existe *****")

		#print(solution)

		solution = solution [0]

		return solution

	else:

		print("le produits n'existe pas ")

		print()

		retour = input("Voluez vous creer le produit  repondez par 1 - si oui ou 2 -si non :  ")

		while retour not in ("1","2"):

			print("Entrez bien votre choix ")

			retour = input("Voluez vous creer le produit  repondez par 1 - si oui ou 2 -si non :  ")

		if retour =="1" :

			print()

			solution = cree_produit(conn)

			print("****LE PRODUIT EST CREER *****")

			return solution


		else :


			print("***Sans le produit pas d'approvissionnement *****")

			print()

			menu_magasinier(matricule,conn)

	





def  ajouter_produit(matricule,conn): #Fonction qui permet de prendre les information lier au produit concerner et d'augmenter ca quantite en stock apres validation

	cur=conn.cursor()

	montant_app= []

	app_tab =[]

	stock={}

	factur=[]


	
	id_app_1=insert_into_app(matricule,conn)

	print()

	const=True

	while const:

		id_app=id_app_1

		produit = recuperation_id_prod(conn)

		print()
		
		prix_achat=input("veuillez saisir le prix achat du produit que voulez vous ajouter:!")

		while  not prix_achat.isdigit():

			print("******Erreur le prix ne peut pas être egale à 0 et doit être des chiffres ******") 

			prix_achat=input("veuillez saisir le prix achat du produit que voulez vous ajouter:!")

		#prix_achat = int(prix_achat)
		
		while  prix_achat <= "0":

			print("******Erreur le prix ne peut pas être egale à 0 et doit être des chiffres ******") 

			prix_achat=input("veuillez saisir le prix achat du produit que voulez vous ajouter:!")

		prix_achat=int(prix_achat)

		print()

		quantite=input("veuillez saisir la quantite fournit du produit:")

		while not quantite.isdigit() :

			print("******Erreur la quantite  ne peut pas être egale à 0 et doit être des chiffres ******")

			quantite=input("veuillez saisir la quantite du produit:")

		#quantite = int(quantite)

		while quantite <= "0" :

			print("******Erreur la quantite  ne peut pas être egale à 0 et doit être des chiffres ******")

			quantite=input("veuillez saisir la quantite du produit:")

		quantite = int(quantite)

		print()

		#Cette partie permet de verifier ci le produit a ete repeter deux fois ou non si oui on remplacer la quantiter par la nouvelle si non on passe

		constat= None

		for index , ligne in enumerate(app_tab):

			quantite_veri ,prix_vt,id_produit = ligne 

			if produit == (id_produit):

				constat = index

				break

		if constat is not None:

			quantite_veri= quantite

			app_tab[constat]=(quantite_veri, prix_vt,id_produit)

			

		else:


			app_tab.append((quantite,prix_achat,produit))

		total = prix_achat * quantite

		montant_app.append(total)

		#Cette partie apres recuperation de id du produit on recherche le nom lier a ce produit que nous allons ajouter a un dictionnaire

		cur.execute("select libelle_produit from PRODUITS where id_prod =%s",(produit,))

		nomp=cur.fetchone()

		nomp=nomp[0]


		#on verifi si le nom est deja dans le dictionnaire si oui on lui donne comme valeur la quantite et le prix achat

		if nomp in stock:

			

			stock[nomp]=(quantite,prix_achat)

		else:

			#si non on l'ajoute comme avec comme comme valeur la quantite et le prix achat

			stock[nomp]=(quantite,prix_achat)



		const = input(" Voulez vous continuez (-oui et - non: ")

		while const not in ("oui","non"):

			print("££££ Erreur ££££")

			const = input(" Voulez vous continuez (oui et - non: ")

		if const.lower() != "oui":

			const = False

			#on parcours le dictionnaire pour ajouter les données contenu a une liste qui va nous servir pour la facturation apres approvisionnement

			for  nom_prod ,info in stock.items():

				qunt=info[0]

				prix_v=info[1]

				factur.append((nom_prod,qunt,prix_v))


			col=["NOM PRODUIT ","QUANTITE","PRIX ACHAT "]

			tabl_fa=table(col,factur)

			print()

			print()

			print(tabl_fa)

			print()	

			#on fait la somme du tableau qui contient les montants de chaques produits

			mnt_f = sum(montant_app)

			print(f" **** LE MONTANT TOTAL DE L'APPROVISIONNEMENT EST : {mnt_f} *****")

			print()

			print()

			#La partie qui concerne la validation de l'	approvisionnement

			confirmation = input("VALIDER  L'APPROVISIONNEMENT ? ( 1 - oui et 2 - non ) ?  ")

			while confirmation not in ("1","2"):

				print("£££££ Erreur de syntaxe £££££")

				confirmation = input("Valider L'APPROVISIONNEMENT ? ( 1 - oui et 2 - non ) ?  ")

			if confirmation =="1":

				if app_tab :

					print(app_tab)

					#on parcours le tableau qui contient les informations necessaire pour alimenter la base

					for produit_red in app_tab :

						quantite_1,prix_achat_1,produit_1 = produit_red


						cur.execute("insert into LIGNE_APPROVISIONNEMENTS (id_app,id_prod,prix_achat, quantite_fournit) values(%s,%s,%s,%s)", (id_app, produit_1,prix_achat_1,quantite_1,))

						conn.commit()

						print()

					print("*****APPROVISIONNEMENTS REUSSI*****")

					

				else: 

					print("££££ UNE ERREUR £££££")

					print()

					ajouter_produit(matricule,conn)

			else: 

				print("££££ APPROVISIONNEMENTS ANNULEE £££")

				print()

				menu_magasinier(matricule,conn)
		else:

			const= True

	



#ajouter_produit()

def inventaire_stock(matricule,conn): #Fonction qui permet de faire l'inventaire du stock

	cur=conn.cursor()

	cur.execute("select * from APPROVISIONNEMENTS ")

	

	retour_inv = cur.fetchall()

	colonne =["NUMERO DE L'APPROVISIONNEMENT","DATE APPROVISIONNEMENTS","LE NUMERO DU FOURNISSEURS","NUMERO DE L'EMPLOYER","MONTANT_TOTAL"]

	retour_table_1 = table(colonne,retour_inv)

	cur.execute("select * from LIGNE_APPROVISIONNEMENTS")

	

	retour_inv_1=cur.fetchall()

	colonne_1 =["NUMERO DE LA LIGNE APPROVISIONNEMENT ","NUMERO APPROVISIONNEMENTS","NUMERO DU PRODUIT","LE PRIX DE L'ACHAT","LA QUANTITE FOURNIT","MONTANT" ]

	retour_table_2 =table(colonne_1,retour_inv_1)

	cur.execute("select  id_prod,libelle_produit ,quantite_prod,categorie_prod,poids_prod  from PRODUITS")

	

	retour_inv_2 = cur.fetchall()

	colonne_2 =["NUMERO DU PRODUIT","NOM DU PRODUIT","QUANTITE DU PRODUIT","CATEGORIE DU PRODUIT","POIDS DU PRODUIT"]

	retour_table_3 = table(colonne_2,retour_inv_2)

	print()

	print()

	print("APPROVISIONNEMENTS")

	print()

	print()

	print(retour_table_1)

	print()

	print()

	print("LIGNE_APPROVISIONNEMENTS")

	print()

	print()

	print(retour_table_2)

	print()

	print()

	print("PRODUITS")

	print()

	print()

	print(retour_table_3)

	print()

	print()

	#print(retour_inv_2)

	
	
	

	#return retour_table_2,retour_table_3,retour_table_3


def menu_magasinier(matricule,conn) : #Fonction qui affiche le menu du magasinier

	cur=conn.cursor()

	print("   ***********************VOUS ÊTES CONNECTER EN TANT QUE MAGASINIER**********************  ")
	print("___________________________________________________________________________________________________")
	print("|                  BIENVENUE SUR LA PAGE DE LA BOUTIQUE                                            |")
	print("|                                                                                                 |")
	
	print("|         1-FAIRE L'APPROVISIONNEMENT                                                             |")
	print()
	print("|         2-FAIRE L'INVENTAIRE DU STOCK                                                           |")
	print()
	print("|         3-QUITTER OU REVENIR                                                                    |")
	print()
	print("___________________________________________________________________________________________________")

	reponse = input("Entrez le numero de l'instruction qui repond à votre besoin : " )

	if reponse.isdigit()== False :

		print ("Erreur de saisi entrez que des chiffres 1 !!!!!")

		reponse = input("Entrez le numero de l'instruction qui repond à votre besoin : " )

	while reponse not in ('1','2','3') :

		print("Erreur de saisi entrez que des chiffres 1 !!!!!")

		print()
		reponse = input("Entrez le numero de l'instruction qui repond à votre besoin : " )
	

			
	if reponse == '1' :

		print()

		print()

		ajouter_produit(matricule,conn) 

		print()

		print()

		quitter(matricule,conn)

	elif reponse =='2' :

		print()

		print()

		inventaire_stock(matricule,conn)

		print()

		print()


		quitter(matricule,conn)

	else :

		print()

		print()

		quitter(matricule,conn) # Fonction menu magasinier qui  permet de voir les differantes taches possible que nous pouvons faire

		print()

		print()
#menu_magasinier()


