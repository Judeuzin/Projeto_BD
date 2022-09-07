insert into roupa_has_monstro
Select idRoupa,idMonstro from monstro, roupa
where roupa.nivel = monstro.nivel or roupa.nivel = monstro.nivel+1