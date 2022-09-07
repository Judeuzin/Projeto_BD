use projetobd
DELIMITER //
CREATE PROCEDURE busca_classe_jogador(in IdP INT, out idC INT)
BEGIN

select Classe_idClasse into idC from personagem
where idPersonagem = IdP;

END //
DELIMITER ;

SET @Id_personagem = 2;
CALL busca_classe_jogador(@Id_Personagem, @id_Classe);
select @id_Classe;