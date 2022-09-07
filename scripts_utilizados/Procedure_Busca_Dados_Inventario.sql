DELIMITER //
DROP PROCEDURE IF EXISTS busca_dados_inventario_arma //
CREATE PROCEDURE busca_dados_inventario_arma(in IdP INT, in IdA INT)
BEGIN

select Personagem_Servidor_idServidor,Personagem_ContaUsuario_Login into @Servidor, @Conta from personagem_has_arma
where Personagem_idPersonagem = IdP;

insert into personagem_has_arma values (IdP, @Servidor, @Conta, idA);

END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS busca_dados_inventario_roupa //
CREATE PROCEDURE busca_dados_inventario_roupa(in IdP INT, in IdR INT)
BEGIN

set @Servidor = 0;
set @Conta = "";

select Personagem_Servidor_idServidor,Personagem_ContaUsuario_Login into @Servidor, @Conta from personagem_has_roupa
where Personagem_idPersonagem = IdP;

insert into personagem_has_roupa values (IdP, @Servidor, @Conta, idR);

END //
DELIMITER ;
