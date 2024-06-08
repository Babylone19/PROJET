\c template1
drop database projet_fin_d_annee;
create database projet_fin_d_annee;
\c projet_fin_d_annee;
 
create sequence seq_four  start  1;
create sequence seq_mat_four start 10;


 
create table FOURNISSEURS (Id_Four  varchar default('FOUR'||  nextval('seq_four'))primary key ,Nom_Four varchar  not null  ,Telephone_Four varchar   ,Email_Four varchar ,Adresse_Four varchar ,matricule varchar default ('MAT'||nextval('seq_mat_four')));
 


create sequence seq_clt start  1;

create sequence seq_num_clt start 10;

 
create table CLIENTS (numero_cli varchar default nextval('seq_num_clt') ,Id_Clt varchar default('CLT') primary key , Nom_Clt varchar  not null,Prenom_clt varchar not null , Date_Naissance_Clt date ,Telephone_Clt varchar  ,Adresse_Clt varchar  ); 
 






create sequence seq_emp start  1;

create sequence seq_mat_emp start 1;


 
create table EMPLOYES (Id_Emp varchar default('EMP' || nextval('seq_emp')) primary key , Nom_Emp varchar   ,Prenom_Emp varchar    ,Date_Naissance_Emp date ,Telephone_Emp varchar  ,Adresse_Emp varchar ,Email_Emp varchar ,Date_Arrivee_Emp date ,Statut_Emp varchar  check (Statut_Emp in('Gerant','Vendeur','Magasinier')) ,mot_pass varchar unique   , matricule varchar  default('MAT' ||nextval('seq_mat_emp')) unique );
 


create sequence seq_comd  start  1;

create sequence seq_num_com start 10;


 
create table COMMANDES (numero_commande varchar default nextval('seq_num_com') ,Id_Comd varchar default ('COMM' ||nextval('seq_comd')) primary key,Date_Comd timestamp ,Id_Clt varchar REFERENCES CLIENTS(Id_Clt) on update cascade  on delete set null , montant_commande numeric,Id_Emp varchar references EMPLOYES(Id_Emp) on update cascade on delete set null);





create sequence seq_app  start  1;


 
create table APPROVISIONNEMENTS (Id_App varchar default ('APPR'|| nextval('seq_app'))primary key ,Date_App timestamp ,Id_Four varchar references FOURNISSEURS (Id_Four ) on update cascade  on delete set null, Id_Emp  varchar references EMPLOYES (Id_Emp) on update cascade on delete set null ,montant_app numeric   ); 
 


create sequence seq_prodt  start  1;

create sequence seq_numero start 10;
 
create table PRODUITS (numero  varchar default nextval('seq_numero') ,Id_Prod varchar default('PROD'||  nextval('seq_prodt')) primary key ,Libelle_Produit varchar ,Quantite_Prod numeric check(Quantite_Prod >= 0) ,Prix_Vente_Prod numeric default(0) check (Prix_Vente_Prod >=0) , Categorie_Prod varchar , Poids_Prod  varchar check(Poids_Prod  like '%kg'  or Poids_Prod like '%g' or Poids_Prod like '%lbs'  or Poids_Prod like '%lbs'  or  Poids_Prod like '%mg'));

create sequence seq_lig_app start 10;
 
create table LIGNE_APPROVISIONNEMENTS ( id_lig_app varchar primary key default('LIGA'|| nextval('seq_lig_app')) ,Id_App varchar references APPROVISIONNEMENTS (Id_App) on update cascade on delete set null ,Id_Prod varchar references PRODUITS (Id_Prod)   on update cascade on delete set null  ,Prix_Achat numeric ,Quantite_Fournit integer check (Quantite_Fournit >0),montant_ligne numeric   ); 
 
 

create sequence seq_ligne  start  1;


 
create table LIGNE_COMMANDE (Id_Ligne varchar default('LIGP'||  nextval('seq_ligne')) primary key ,Quantite_Commande numeric check (Quantite_Commande >0) not null  , Prix_Vente numeric not null,montant numeric   ,Id_Prod varchar references PRODUITS(Id_Prod) on update cascade on delete set null , Id_Comd varchar references COMMANDES(Id_Comd) on update cascade on delete set null); 
 



