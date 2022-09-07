use projetobd
DELIMITER $$
DROP PROCEDURE IF EXISTS busca_drops_monstro $$
CREATE PROCEDURE busca_drops_monstro (IN idL INT, IN idP INT, IN tipo_drop int, OUT drop_monstro INT)
BEGIN

set @drop_a = 1;
set @drop_r = 1;
set @randomize = 0;

CALL busca_classe_jogador(idP, @idC);

select idArma into @drop_a from arma a 
inner join monstro_has_arma ma 
on a.idArma = ma.Arma_idArma 
and Classe_idClasse = @idC
and Monstro_idMonstro = idL
order by rand() 
limit 1;

select idRoupa into @drop_r from roupa r 
inner join roupa_has_monstro rm 
on r.idRoupa = rm.Roupa_idRoupa
and Classe_idClasse = @idC
and Monstro_idMonstro = idL
order by rand() 
limit 1;

select if(tipo_drop = 0, @drop_a, @drop_r) into drop_monstro;
END $$
DELIMITER ;

call busca_drops_monstro(1, 2, 1, @dm);
select @dm;