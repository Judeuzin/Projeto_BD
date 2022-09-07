insert into monstro_has_arma 
Select idMonstro, idArma from monstro, arma 
where arma.nivel = monstro.nivel or arma.nivel = monstro.nivel+1