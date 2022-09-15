SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `ProjetoBD` DEFAULT CHARACTER SET utf8 ;
USE `ProjetoBD` ;

DROP TABLE IF EXISTS `ProjetoBD`.`Servidor`;
DROP TABLE IF EXISTS `ProjetoBD`.`ContaUsuario`;
DROP TABLE IF EXISTS  `ProjetoBD`.`Monstro`;
DROP TABLE IF EXISTS `ProjetoBD`.`Local`;
DROP TABLE IF EXISTS `ProjetoBD`.`Classe`;
DROP TABLE IF EXISTS  `ProjetoBD`.`Roupa`;
DROP TABLE IF EXISTS  `ProjetoBD`.`Arma`;
DROP TABLE IF EXISTS  `ProjetoBD`.`Personagem`;
DROP TABLE IF EXISTS  `ProjetoBD`.`Personagem_has_Roupa`;
DROP TABLE IF EXISTS  `ProjetoBD`.`Personagem_has_Arma`;
DROP TABLE IF EXISTS `ProjetoBD`.`Monstro_has_Arma`;
DROP TABLE IF EXISTS `ProjetoBD`.`Roupa_has_Monstro`;

-- -----------------------------------------------------
-- Table `ProjetoBD`.`Servidor`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `ProjetoBD`.`Servidor` (
  `NomeServidor` VARCHAR(45) NOT NULL,
  `DataDeCriacao` DATETIME NOT NULL,
  `NumeroDeJogadores` INT NOT NULL,
  `NumeroMaximoDeJogadores` INT NOT NULL,
  PRIMARY KEY (`NomeServidor`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ProjetoBD`.`ContaUsuario`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `ProjetoBD`.`ContaUsuario` (
  `Login` VARCHAR(15) NOT NULL,
  `Senha` VARCHAR(45) NOT NULL,
  `Telefone` VARCHAR(10) NOT NULL,
  `Email` VARCHAR(25) NOT NULL,
  `Endereço` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Login`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ProjetoBD`.`Monstro`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `ProjetoBD`.`Monstro` (
  `idMonstro` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Nivel` INT NOT NULL,
  `Defesa` INT NOT NULL,
  `Ataque` INT NOT NULL,
  PRIMARY KEY (`idMonstro`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ProjetoBD`.`Local`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `ProjetoBD`.`Local` (
  `idLocal` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Nivel` INT NOT NULL,
  `Monstro_idMonstro` INT NOT NULL,
  PRIMARY KEY (`idLocal`),
  INDEX `fk_Local_Monstro1_idx` (`Monstro_idMonstro` ASC) VISIBLE,
  CONSTRAINT `fk_Local_Monstro1`
    FOREIGN KEY (`Monstro_idMonstro`)
    REFERENCES `ProjetoBD`.`Monstro` (`idMonstro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ProjetoBD`.`Classe`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `ProjetoBD`.`Classe` (
  `idClasse` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idClasse`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ProjetoBD`.`Roupa`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `ProjetoBD`.`Roupa` (
  `idRoupa` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Nivel` INT NOT NULL,
  `Defesa` INT NOT NULL,
  `Ataque` INT NOT NULL,
  `Classe_idClasse` INT NOT NULL,
  PRIMARY KEY (`idRoupa`),
  INDEX `fk_Roupa_Classe1_idx` (`Classe_idClasse` ASC) VISIBLE,
  CONSTRAINT `fk_Roupa_Classe1`
    FOREIGN KEY (`Classe_idClasse`)
    REFERENCES `ProjetoBD`.`Classe` (`idClasse`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ProjetoBD`.`Arma`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `ProjetoBD`.`Arma` (
  `idArma` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Nivel` INT NOT NULL,
  `Defesa` INT NOT NULL,
  `Ataque` INT NOT NULL,
  `Classe_idClasse` INT NOT NULL,
  PRIMARY KEY (`idArma`),
  INDEX `fk_Arma_Classe1_idx` (`Classe_idClasse` ASC) VISIBLE,
  CONSTRAINT `fk_Arma_Classe1`
    FOREIGN KEY (`Classe_idClasse`)
    REFERENCES `ProjetoBD`.`Classe` (`idClasse`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ProjetoBD`.`Personagem`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `ProjetoBD`.`Personagem` (
  `idPersonagem` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Nivel` INT NOT NULL,
  `Servidor_NomeServidor` VARCHAR(45) NOT NULL,
  `ContaUsuario_Login` VARCHAR(15) NOT NULL,
  `ArmaEquipada_idArma` INT NOT NULL,
  `RoupaEquipada_idRoupa` INT NOT NULL,
  `Local_idLocal` INT NOT NULL,
  `Classe_idClasse` INT NOT NULL,
  PRIMARY KEY (`idPersonagem`, `Servidor_NomeServidor`, `ContaUsuario_Login`),
  INDEX `fk_Personagem_Servidor_idx` (`Servidor_NomeServidor` ASC) VISIBLE,
  INDEX `fk_Personagem_ContaUsuario1_idx` (`ContaUsuario_Login` ASC) VISIBLE,
  INDEX `fk_Personagem_Arma1_idx` (`ArmaEquipada_idArma` ASC) VISIBLE,
  INDEX `fk_Personagem_Roupa1_idx` (`RoupaEquipada_idRoupa` ASC) VISIBLE,
  INDEX `fk_Personagem_Local1_idx` (`Local_idLocal` ASC) VISIBLE,
  INDEX `fk_Personagem_Classe1_idx` (`Classe_idClasse` ASC) VISIBLE,
  CONSTRAINT `fk_Personagem_Servidor`
    FOREIGN KEY (`Servidor_NomeServidor`)
    REFERENCES `ProjetoBD`.`Servidor` (`NomeServidor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personagem_ContaUsuario1`
    FOREIGN KEY (`ContaUsuario_Login`)
    REFERENCES `ProjetoBD`.`ContaUsuario` (`Login`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personagem_Arma1`
    FOREIGN KEY (`ArmaEquipada_idArma`)
    REFERENCES `ProjetoBD`.`Arma` (`idArma`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personagem_Roupa1`
    FOREIGN KEY (`RoupaEquipada_idRoupa`)
    REFERENCES `ProjetoBD`.`Roupa` (`idRoupa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personagem_Local1`
    FOREIGN KEY (`Local_idLocal`)
    REFERENCES `ProjetoBD`.`Local` (`idLocal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personagem_Classe1`
    FOREIGN KEY (`Classe_idClasse`)
    REFERENCES `ProjetoBD`.`Classe` (`idClasse`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ProjetoBD`.`Personagem_has_Roupa`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `ProjetoBD`.`Personagem_has_Roupa` (
  `Personagem_idPersonagem` INT NOT NULL,
  `Personagem_Servidor_NomeServidor` VARCHAR(45) NOT NULL,
  `Personagem_ContaUsuario_Login` VARCHAR(15) NOT NULL,
  `Roupa_idRoupa` INT NOT NULL,
  PRIMARY KEY (`Personagem_idPersonagem`, `Personagem_Servidor_NomeServidor`, `Personagem_ContaUsuario_Login`, `Roupa_idRoupa`),
  INDEX `fk_Personagem_has_Roupa_Roupa1_idx` (`Roupa_idRoupa` ASC) VISIBLE,
  INDEX `fk_Personagem_has_Roupa_Personagem1_idx` (`Personagem_idPersonagem` ASC, `Personagem_Servidor_NomeServidor` ASC, `Personagem_ContaUsuario_Login` ASC) VISIBLE,
  CONSTRAINT `fk_Personagem_has_Roupa_Personagem1`
    FOREIGN KEY (`Personagem_idPersonagem` , `Personagem_Servidor_NomeServidor` , `Personagem_ContaUsuario_Login`)
    REFERENCES `ProjetoBD`.`Personagem` (`idPersonagem` , `Servidor_NomeServidor` , `ContaUsuario_Login`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personagem_has_Roupa_Roupa1`
    FOREIGN KEY (`Roupa_idRoupa`)
    REFERENCES `ProjetoBD`.`Roupa` (`idRoupa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ProjetoBD`.`Personagem_has_Arma`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `ProjetoBD`.`Personagem_has_Arma` (
  `Personagem_idPersonagem` INT NOT NULL,
  `Personagem_Servidor_NomeServidor` VARCHAR(45) NOT NULL,
  `Personagem_ContaUsuario_Login` VARCHAR(15) NOT NULL,
  `Arma_idArma` INT NOT NULL,
  PRIMARY KEY (`Personagem_idPersonagem`, `Personagem_Servidor_NomeServidor`, `Personagem_ContaUsuario_Login`, `Arma_idArma`),
  INDEX `fk_Personagem_has_Arma_Arma1_idx` (`Arma_idArma` ASC) VISIBLE,
  INDEX `fk_Personagem_has_Arma_Personagem1_idx` (`Personagem_idPersonagem` ASC, `Personagem_Servidor_NomeServidor` ASC, `Personagem_ContaUsuario_Login` ASC) VISIBLE,
  CONSTRAINT `fk_Personagem_has_Arma_Personagem1`
    FOREIGN KEY (`Personagem_idPersonagem` , `Personagem_Servidor_NomeServidor` , `Personagem_ContaUsuario_Login`)
    REFERENCES `ProjetoBD`.`Personagem` (`idPersonagem` , `Servidor_NomeServidor` , `ContaUsuario_Login`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personagem_has_Arma_Arma1`
    FOREIGN KEY (`Arma_idArma`)
    REFERENCES `ProjetoBD`.`Arma` (`idArma`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ProjetoBD`.`Monstro_has_Arma`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `ProjetoBD`.`Monstro_has_Arma` (
  `Monstro_idMonstro` INT NOT NULL,
  `Arma_idArma` INT NOT NULL,
  PRIMARY KEY (`Monstro_idMonstro`, `Arma_idArma`),
  INDEX `fk_Monstro_has_Arma_Arma1_idx` (`Arma_idArma` ASC) VISIBLE,
  INDEX `fk_Monstro_has_Arma_Monstro1_idx` (`Monstro_idMonstro` ASC) VISIBLE,
  CONSTRAINT `fk_Monstro_has_Arma_Monstro1`
    FOREIGN KEY (`Monstro_idMonstro`)
    REFERENCES `ProjetoBD`.`Monstro` (`idMonstro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Monstro_has_Arma_Arma1`
    FOREIGN KEY (`Arma_idArma`)
    REFERENCES `ProjetoBD`.`Arma` (`idArma`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ProjetoBD`.`Roupa_has_Monstro`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `ProjetoBD`.`Roupa_has_Monstro` (
  `Roupa_idRoupa` INT NOT NULL,
  `Monstro_idMonstro` INT NOT NULL,
  PRIMARY KEY (`Roupa_idRoupa`, `Monstro_idMonstro`),
  INDEX `fk_Roupa_has_Monstro_Monstro1_idx` (`Monstro_idMonstro` ASC) VISIBLE,
  INDEX `fk_Roupa_has_Monstro_Roupa1_idx` (`Roupa_idRoupa` ASC) VISIBLE,
  CONSTRAINT `fk_Roupa_has_Monstro_Roupa1`
    FOREIGN KEY (`Roupa_idRoupa`)
    REFERENCES `ProjetoBD`.`Roupa` (`idRoupa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Roupa_has_Monstro_Monstro1`
    FOREIGN KEY (`Monstro_idMonstro`)
    REFERENCES `ProjetoBD`.`Monstro` (`idMonstro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Excluir depois que usarmos
-- -----------------------------------------------------

INSERT INTO ContaUsuario(Login,Senha,Telefone,Email,Endereço) VALUES ('Thor','Thor123','981283895','Thorzedes@gmail.com','Rua Asgard De Olinda');
INSERT INTO ContaUsuario(Login,Senha,Telefone,Email,Endereço) VALUES ('Valhalla','Valhalla123','981283895','Valhallazedes@gmail.com','Rua Ancestral De Olinda');
INSERT INTO ContaUsuario(Login,Senha,Telefone,Email,Endereço) VALUES ('Asgard','Asgard123','981213475','Asgardzedes@gmail.com','Rua Esquina De Olinda');
INSERT INTO ContaUsuario(Login,Senha,Telefone,Email,Endereço) VALUES ('Midgard','Midgard123','911882795','Midgardzedes@gmail.com','Rua Curva De Olinda');

INSERT INTO Servidor(NomeServidor,DataDeCriacao,NumeroDeJogadores,NumeroMaximoDeJogadores) VALUES ('Thor',SYSDATE(),0,100);
INSERT INTO Servidor(NomeServidor,DataDeCriacao,NumeroDeJogadores,NumeroMaximoDeJogadores) VALUES ('Valhalla',SYSDATE(),0,100);
INSERT INTO Servidor(NomeServidor,DataDeCriacao,NumeroDeJogadores,NumeroMaximoDeJogadores) VALUES ('Asgard',SYSDATE(),0,100);
INSERT INTO Servidor(NomeServidor,DataDeCriacao,NumeroDeJogadores,NumeroMaximoDeJogadores) VALUES ('Midgard',SYSDATE(),0,100);
INSERT INTO Servidor(NomeServidor,DataDeCriacao,NumeroDeJogadores,NumeroMaximoDeJogadores) VALUES ('Niflheim',SYSDATE(),0,100);

INSERT INTO Classe (Nome) VALUES ('Guerreiro');
INSERT INTO Classe (Nome) VALUES ('Mago');
INSERT INTO Classe (Nome) VALUES ('Ladrão');
INSERT INTO Classe (Nome) VALUES ('Artista Marcial');
INSERT INTO Classe (Nome) VALUES ('Barbaro');

INSERT INTO Monstro (Nome, Nivel, Defesa, Ataque) VALUES ("Slime", 1, 10, 8);
INSERT INTO Monstro (Nome, Nivel, Defesa, Ataque) VALUES ("Goblin", 2, 11, 15);
INSERT INTO Monstro (Nome, Nivel, Defesa, Ataque) VALUES ("Troll", 3, 20, 20);
INSERT INTO Monstro (Nome, Nivel, Defesa, Ataque) VALUES ("Orc", 4, 23, 30);
INSERT INTO Monstro (Nome, Nivel, Defesa, Ataque) VALUES ("Dragon", 5, 35, 45);

INSERT INTO Local (Nome, Nivel, Monstro_idMonstro) VALUES ("Bandopolis", 1, 1);
INSERT INTO Local (Nome, Nivel, Monstro_idMonstro) VALUES ("Piltover", 2, 2);
INSERT INTO Local (Nome, Nivel, Monstro_idMonstro) VALUES ("Zaun", 3, 3);
INSERT INTO Local (Nome, Nivel, Monstro_idMonstro) VALUES ("Noxus", 4, 4);
INSERT INTO Local (Nome, Nivel, Monstro_idMonstro) VALUES ("O Vazio", 5, 5);

INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Escudo de Potter", 1, 10, 8, 1);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Couraca de Pano", 2, 11, 15, 1);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Cota de Malha", 3, 20, 20, 1);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Egide da Legiao", 4, 23, 30, 1);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Armadura do Guerreiro", 5, 35, 45, 1);

INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Capa de Potter", 1, 10, 8, 2);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Pressagio do Gaviao", 2, 11, 15, 2);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Forca dos Elfos", 3, 20, 20, 2);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Mascara do Abismo", 4, 23, 30, 2);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Armadura do Arqueiro", 5, 35, 45, 2);

INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Manto de Potter", 1, 10, 8, 3);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Capa da Agilidade", 2, 11, 15, 3);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Colete Invisivel", 3, 20, 20, 3);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Couraca do Defunto", 4, 23, 30, 3);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Armadura do Assassino", 5, 35, 45, 3);

INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Terno de Potter", 1, 10, 8, 4);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Semblante da Natureza", 2, 11, 15, 4);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Abraco da Driade", 3, 20, 20, 4);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Medalhao de Ferro", 4, 23, 30, 4);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Armadura do Bardo", 5, 35, 45, 4);

INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Roupao de Potter", 1, 10, 8, 5);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Pensamentos de Lich", 2, 11, 15, 5);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Convergencia de Gandalf", 3, 20, 20, 5);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Cinturao da Magia", 4, 23, 30, 5);
INSERT INTO Roupa (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Armadura do Mago", 5, 35, 45, 5);

INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Espada de Potter", 1, 10, 8, 1);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Espada Longa", 2, 11, 15, 1);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Fulgor", 3, 20, 20, 1);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Lamina Sanguinaria", 4, 23, 30, 1);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Gume do Infinito", 5, 35, 40, 1);

INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Arco de Potter", 1, 10, 8, 2);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Arco Recurvo", 2, 11, 15, 2);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Furacao de Legolas", 3, 20, 20, 2);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Lembrete Mortal", 4, 23, 30, 2);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Mata Crakens", 5, 35, 40, 2);

INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Adaga de Potter", 1, 10, 8, 3);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Chamado do Assassino", 2, 11, 15, 3);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Dancarina Fantasma", 3, 20, 20, 3);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Limiar da Noite", 4, 23, 30, 3);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Garra do Espreitador", 5, 35, 40, 3);

INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Viola de Potter", 1, 10, 8, 4);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Saxofone Amplificador", 2, 11, 15, 4);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Redencao do Baixo", 3, 20, 20, 4);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Força do Triangulo", 4, 23, 30, 4);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Violino do Rancor", 5, 35, 40, 4);

INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Anel de Potter", 1, 10, 8, 5);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Varinha Explosiva", 2, 11, 15, 5);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Cajado do Vazio", 3, 20, 20, 5);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Capuz da Morte", 4, 23, 30, 5);
INSERT INTO Arma (Nome, Nivel, Defesa, Ataque, Classe_idClasse) VALUES ("Lembranças da Lorde Malevola", 5, 35, 40, 5);

INSERT INTO Roupa_has_Monstro 
SELECT idRoupa, idMonstro FROM Monstro, Roupa 
WHERE Roupa.Nivel = Monstro.Nivel OR Roupa.Nivel = Monstro.Nivel+1;

INSERT INTO Monstro_has_Arma 
SELECT idMonstro, idArma FROM Monstro, Arma 
WHERE Arma.Nivel = Monstro.Nivel OR Arma.Nivel = Monstro.Nivel+1;

grant insert, select, delete, update
on projetobd.monstro to 'root'@'localhost';

alter table monstro
add image longblob;

update monstro SET image = Load_file('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Slime.png') where Nivel = 1;
update monstro SET image = Load_file('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Goblin.png') where Nivel = 2;
update monstro SET image = Load_file('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Orc.png') where Nivel = 3;
update monstro SET image = Load_file('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Troll.png') where Nivel = 4;
update monstro SET image = Load_file('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Dragao.png') where Nivel = 5;

select min(idLocal) into @idL from Local;

SELECT idArma,idRoupa into @idA, @idR FROM Classe,Arma,Roupa WHERE Arma.Nivel = 1 
AND Roupa.Nivel = 1 AND Classe.idClasse = Arma.Classe_idClasse 
AND Classe.idClasse = Roupa.Classe_idClasse AND Classe.Nome = "Guerreiro";
INSERT INTO Personagem(Nome, Nivel, Servidor_NomeServidor, ContaUsuario_Login, ArmaEquipada_idArma, RoupaEquipada_idRoupa, Local_idLocal, Classe_idClasse) 
VALUES ("Olaf",1,"Asgard","Asgard",@idA,@idR,@idL,1);
Select idPersonagem into @idP from Personagem where Nome = "Olaf";
INSERT INTO personagem_has_arma VALUES (@idP,"Asgard","Asgard",@idA);
INSERT INTO personagem_has_roupa VALUES (@idP,"Asgard","Asgard",@idR);

SELECT idArma,idRoupa into @idA, @idR FROM Classe,Arma,Roupa WHERE Arma.Nivel = 1 
AND Roupa.Nivel = 1 AND Classe.idClasse = Arma.Classe_idClasse 
AND Classe.idClasse = Roupa.Classe_idClasse AND Classe.Nome = "Mago";
INSERT INTO Personagem(Nome, Nivel, Servidor_NomeServidor, ContaUsuario_Login, ArmaEquipada_idArma, RoupaEquipada_idRoupa, Local_idLocal, Classe_idClasse) 
VALUES ("Waterloop",1,"Asgard","Asgard",@idA,@idR,@idL,1);
Select idPersonagem into @idP from Personagem where Nome = "Waterloop";
INSERT INTO personagem_has_arma VALUES (@idP,"Asgard","Asgard",@idA);
INSERT INTO personagem_has_roupa VALUES (@idP,"Asgard","Asgard",@idR);


SELECT idArma,idRoupa into @idA, @idR FROM Classe,Arma,Roupa WHERE Arma.Nivel = 1 
AND Roupa.Nivel = 1 AND Classe.idClasse = Arma.Classe_idClasse 
AND Classe.idClasse = Roupa.Classe_idClasse AND Classe.Nome = "Ladrão";
INSERT INTO Personagem(Nome, Nivel, Servidor_NomeServidor, ContaUsuario_Login, ArmaEquipada_idArma, RoupaEquipada_idRoupa, Local_idLocal, Classe_idClasse) 
VALUES ("Sonica",1,"Asgard","Asgard",@idA,@idR,@idL,1);
Select idPersonagem into @idP from Personagem where Nome = "Sonica";
INSERT INTO personagem_has_arma VALUES (@idP,"Asgard","Asgard",@idA);
INSERT INTO personagem_has_roupa VALUES (@idP,"Asgard","Asgard",@idR);


SELECT idArma,idRoupa into @idA, @idR FROM Classe,Arma,Roupa WHERE Arma.Nivel = 1 
AND Roupa.Nivel = 1 AND Classe.idClasse = Arma.Classe_idClasse 
AND Classe.idClasse = Roupa.Classe_idClasse AND Classe.Nome = "Artista Marcial";
INSERT INTO Personagem(Nome, Nivel, Servidor_NomeServidor, ContaUsuario_Login, ArmaEquipada_idArma, RoupaEquipada_idRoupa, Local_idLocal, Classe_idClasse) 
VALUES ("Chantas",1,"Asgard","Asgard",@idA,@idR,@idL,1);
Select idPersonagem into @idP from Personagem where Nome = "Chantas";
INSERT INTO personagem_has_arma VALUES (@idP,"Asgard","Asgard",@idA);
INSERT INTO personagem_has_roupa VALUES (@idP,"Asgard","Asgard",@idR);

SELECT idArma,idRoupa into @idA, @idR FROM Classe,Arma,Roupa WHERE Arma.Nivel = 1 
AND Roupa.Nivel = 1 AND Classe.idClasse = Arma.Classe_idClasse 
AND Classe.idClasse = Roupa.Classe_idClasse AND Classe.Nome = "Barbaro";
INSERT INTO Personagem(Nome, Nivel, Servidor_NomeServidor, ContaUsuario_Login, ArmaEquipada_idArma, RoupaEquipada_idRoupa, Local_idLocal, Classe_idClasse) 
VALUES ("Malik",1,"Asgard","Asgard",@idA,@idR,@idL,1);
Select idPersonagem into @idP from Personagem where Nome = "Malik";
INSERT INTO personagem_has_arma VALUES (@idP,"Asgard","Asgard",@idA);
INSERT INTO personagem_has_roupa VALUES (@idP,"Asgard","Asgard",@idR);
UPDATE servidor set NumeroDeJogadores = 5 where NomeServidor = 'Asgard';

DELIMITER //
DROP VIEW IF EXISTS JogadoresRegistradores
CREATE VIEW JogadoresRegistradores AS
    SELECT 
      Personagem.Servidor_NomeServidor,Servidor.NumeroDeJogadores, Classe.Nome, COUNT(*) AS NumberOfPersonagens
    FROM 
      Personagem,Classe,Servidor
    WHERE
      Personagem.Classe_idClasse = Classe.idClasse AND Servidor.NomeServidor = Personagem.Servidor_NomeServidor
    GROUP BY
      Personagem.Servidor_NomeServidor, Personagem.Classe_idClasse
    ORDER BY
      Servidor.NumeroDeJogadores,Personagem.Servidor_NomeServidor, Classe.Nome;


DELIMITER $$
DROP PROCEDURE IF EXISTS busca_drops_monstro $$
CREATE PROCEDURE busca_drops_monstro (IN idP INT, IN tipo_drop int, OUT drop_monstro INT)
BEGIN

select Classe_idClasse, Local_idLocal into @classe, @local_ from Personagem where idPersonagem = idP;
select Monstro_idMonstro into @monstro from Local where idLocal = @local_;

select idArma into @drop_a from arma a 
inner join monstro_has_arma ma 
on a.idArma = ma.Arma_idArma 
and Classe_idClasse = @classe
and Monstro_idMonstro = @monstro
order by rand() 
limit 1;

select idRoupa into @drop_r from roupa r 
inner join roupa_has_monstro rm 
on r.idRoupa = rm.Roupa_idRoupa
and Classe_idClasse = @classe
and Monstro_idMonstro = @monstro
order by rand() 
limit 1;

select if(tipo_drop = 0, @drop_a, @drop_r) into drop_monstro;
END $$
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS busca_dados_inventario_arma //
CREATE PROCEDURE busca_dados_inventario_arma(in IdP INT, in IdA INT)
BEGIN

select Personagem_Servidor_NomeServidor,Personagem_ContaUsuario_Login into @Servidor, @Conta from personagem_has_arma
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

select Personagem_Servidor_NomeServidor,Personagem_ContaUsuario_Login into @Servidor, @Conta from personagem_has_roupa
where Personagem_idPersonagem = IdP;

insert into personagem_has_roupa values (IdP, @Servidor, @Conta, idR);

END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS insere_dados_inventario_arma //
CREATE PROCEDURE insere_dados_inventario_arma(in IdP INT, in IdA INT)
BEGIN

select distinct Personagem_Servidor_NomeServidor,Personagem_ContaUsuario_Login into @Servidor, @Conta from personagem_has_arma
where Personagem_idPersonagem = IdP;

insert into personagem_has_arma values (IdP, @Servidor, @Conta, idA);
commit;

END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS insere_dados_inventario_roupa //
CREATE PROCEDURE insere_dados_inventario_roupa(in IdP INT, in IdR INT)
BEGIN

set @Servidor = 0;
set @Conta = "";

select distinct Personagem_Servidor_NomeServidor,Personagem_ContaUsuario_Login into @Servidor, @Conta from personagem_has_roupa
where Personagem_idPersonagem = IdP;

insert into personagem_has_roupa values (IdP, @Servidor, @Conta, idR);
commit;

END //
DELIMITER ;
