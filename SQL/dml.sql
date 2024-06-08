insert into FOURNISSEURS(Nom_Four,Telephone_Four,Email_Four,Adresse_Four) values('tchakala',90200014,'bary_1@gmail.com','didaoure');

insert into FOURNISSEURS(Nom_Four,Telephone_Four,Email_Four,Adresse_Four) values('tchabou',99210014,'ibrahim@gmail.com','didaoure1');

insert into FOURNISSEURS(Nom_Four,Telephone_Four,Email_Four,Adresse_Four) values('alhassani',90200000,'bary@gmail.com','didaoure3');





insert into CLIENTS(Nom_Clt,prenom_clt,Date_Naissance_Clt,Telephone_Clt,Adresse_Clt) values('sankara','alone','13/04/2023',70909838,'kamp');


insert into CLIENTS(Nom_Clt,prenom_clt,Date_Naissance_Clt,Telephone_Clt,Adresse_Clt) values('akoh','john','25/12/1999',90919137,'kpangalam');


insert into EMPLOYES(Nom_Emp,Prenom_Emp,Date_Naissance_Emp,Telephone_Emp,Adresse_Emp,Email_Emp,Date_Arrivee_Emp,Statut_Emp) values('traore','aimane','06/9/1890','90541288','zamb','aimane@gmail.com','15/06/2009','Magasinier');


Insert into EMPLOYES(Nom_Emp,Prenom_Emp,Date_Naissance_Emp,Telephone_Emp,Adresse_Emp,Email_Emp,Date_Arrivee_Emp,Statut_Emp) values('bataya','crepin','27/11/2001','90572274','salimde','crepin@gmail.com','20/08/2010','Gerant');

insert into EMPLOYES(Nom_Emp,Prenom_Emp,Date_Naissance_Emp,Telephone_Emp,Adresse_Emp,Email_Emp,Date_Arrivee_Emp,Statut_Emp) values('farid','bako','27/11/2001','90472274','salimde','crepin_1@gmail.com','20/08/2010','Vendeur');




insert into APPROVISIONNEMENTS(Date_App,Id_Four,Id_Emp ) values('22/03/2000','FOUR3','EMP1');
insert into APPROVISIONNEMENTS(Date_App,Id_Four,Id_Emp ) values('18/06/2014','FOUR3','EMP1'); 
insert into APPROVISIONNEMENTS(Date_App,Id_Four,Id_Emp ) values('31/01/1950','FOUR3','EMP1'); 

insert into
 PRODUITS(Libelle_Produit,Quantite_Prod ,Prix_Vente_Prod,Categorie_Prod , Poids_Prod) values('lait',15,50,'vivalait','6g');
insert into PRODUITS(Libelle_Produit,Quantite_Prod ,Prix_Vente_Prod,Categorie_Prod , Poids_Prod) values('tomate',10,300,'jumbo','5kg'); 
insert into PRODUITS(Libelle_Produit,Quantite_Prod ,Prix_Vente_Prod,Categorie_Prod , Poids_Prod) values('mouchoir',5,500,'lotus','5g');
insert into PRODUITS(Libelle_Produit,Quantite_Prod ,Categorie_Prod , Poids_Prod) values('mouchoir',5,'dodus','5g');

insert into LIGNE_APPROVISIONNEMENTS(Id_App,Id_Prod,Prix_Achat,Quantite_Fournit) values('APPR2','PROD1',1500,40000);
insert into LIGNE_APPROVISIONNEMENTS(Id_App,Id_Prod,Prix_Achat,Quantite_Fournit) values('APPR1','PROD3',2000,15);
insert into LIGNE_APPROVISIONNEMENTS(Id_App,Id_Prod,Prix_Achat,Quantite_Fournit) values('APPR3','PROD2',100,5);

insert into COMMANDES(Date_Comd,Id_Clt,Id_Emp) values('22/03/2000','saal1','EMP1');

insert into LIGNE_COMMANDE(Quantite_Commande,Prix_Vente,Id_Prod,Id_Comd) values(5,50,'PROD3', 'COMM1');



---insert into COMMANDES(Date_Comd,Id_Clt,montant_commande) values('18/06/2014','CLT98',15000);
---insert into COMMANDES(Date_Comd,Id_Clt,montant_commande) values('31/01/1950','CLT100',2000);











