create or replace function identifiant_client()

returns trigger as

$$
declare

	nom_clt clients.nom_clt%type;

	prenom clients.prenom_clt%type;

	sequence varchar := nextval('seq_clt');

	concatene clients.id_clt%type;

	nom_final varchar;

	clt clients%rowtype;

begin 
	
	select *  into clt from clients where id_clt = new.id_clt;

	nom_clt := clt.nom_clt;

	prenom := clt.prenom_clt;

	nom_final :=substring(nom_clt from 1 for 2)|| substring(prenom from 1 for 2) || sequence ;

	update clients set  id_clt = nom_final where id_clt= new.id_clt;

	return new;
end;
$$
language plpgsql;

create trigger clt_identif after insert on clients 

for each row execute procedure identifiant_client();










create or replace function mot_de_pass()
returns trigger as
$$
declare
	nom_user EMPLOYES.Nom_Emp%type;
	Statut_user EMPLOYES.Statut_Emp%type;
	empl EMPLOYES%rowtype;
	code EMPLOYES.mot_pass%type;
	num_user varchar;

begin 
	select * into empl from EMPLOYES where Id_Emp = new.Id_Emp ;

	nom_user := empl.Nom_Emp;
	Statut_user := empl.Statut_Emp;
	num_user := empl.Telephone_Emp;
	code := substring(nom_user from 1 for 2 ) || substring(Statut_user from 1 for 2 ) || substring(num_user from 1 for 3);
	update EMPLOYES set mot_pass = code  where Id_Emp = new.Id_Emp;
	return new ;
end;
$$
language plpgsql ;


create trigger code_automatique after insert on EMPLOYES
for each row execute procedure mot_de_pass(); 






create or replace function montant_ligne()

returns trigger as 
$$
declare
	somme_total LIGNE_APPROVISIONNEMENTS.montant_ligne%type;

	solde PRODUITS.Quantite_Prod%type;
begin

	if (TG_OP ='INSERT') then 
	
		update LIGNE_APPROVISIONNEMENTS set montant_ligne =  new.prix_achat * new.Quantite_fournit where LIGNE_APPROVISIONNEMENTS.id_lig_app = new.id_lig_app;


		select sum(montant_ligne) into somme_total  from ligne_approvisionnements l  where l.id_app = new.id_app;

		update approvisionnements set montant_app = somme_total where id_app = new.id_app;

		select Quantite_Prod into solde from PRODUITS where Id_Prod = new.Id_Prod;

		update PRODUITS set Quantite_Prod = solde + new.Quantite_Fournit where Id_Prod = new.Id_Prod ;
	

		return new;
	end if;
end;
$$
language plpgsql;

create trigger mis_montant_ligne after insert  on LIGNE_APPROVISIONNEMENTS

for each row execute procedure montant_ligne();




create or replace function mise_à_jour_prod()
returns trigger as
$$
declare
	somme commandes.montant_commande%type;
begin 
	
	if (TG_OP ='INSERT') then 
	
		update PRODUITS set Quantite_Prod = Quantite_Prod - new.Quantite_Commande where PRODUITS.Id_Prod = new.Id_Prod;

		update LIGNE_COMMANDE set montant = new.Quantite_Commande * new.prix_vente where LIGNE_COMMANDE.id_ligne = new.id_ligne;

		select sum(montant) into somme from LIGNE_COMMANDE L where L.id_comd = new.id_comd;

		update commandes set montant_commande = somme  where id_comd= new.id_comd;

		return new;

	end if;
end;
$$
language plpgsql;

create trigger mise_à_jour_qt_prod after insert on LIGNE_COMMANDE
for each row execute procedure mise_à_jour_prod();






create table prix_vente_1_audit(laDate timestamp not null , iDuser text not null , ancienId_Prod text not null,nouveauId_Prod text not null  ,ancienPrix_Vente integer , nouveauPrix_Vente integer);


create or replace function processus_prix_vente_audit() returns trigger as 

$$
begin
	insert into prix_vente_1_audit(laDate ,iDuser,ancienId_Prod ,nouveauId_Prod,ancienPrix_Vente, nouveauPrix_Vente)
	values (now(),user,old.Id_Prod , new.Id_Prod ,old.Prix_Vente_Prod ,new.Prix_Vente_Prod );
	return new;
end;
$$
language plpgsql ;


create trigger prix_vente_audit_1 before update on PRODUITS
for each row execute procedure processus_prix_vente_audit();


create table client_audit_2(laDate timestamp not null , iDuser text not null , ancienId_Clt text not null, ancienTelephone_Clt varchar,ancien_nom  text,ancien_prenom text ,ancienne_adresse text ,ancienne_date date );


create or replace function processus_client_2_audit() returns trigger as 

$$
begin
	insert into client_audit_1(laDate ,iDuser ,nouveauId_Clt, ancienId_Clt ,ancienTelephone_Clt,ancien_nom,ancien_prenom,ancienne_adresse,ancienne_date)

	values (now(),user,  new.Id_Clt ,old.Id_Clt  ,old.Telephone_Clt,old.nom_clt ,old.prenom_clt,old.Adresse_Clt,old.Date_Naissance_Clt );
	return new;
end;
$$
language plpgsql ;


create trigger client_2_audit  before delete on CLIENTS
for each row execute procedure processus_client_2_audit();
	
	



























	
	

	
	
	
	
	


