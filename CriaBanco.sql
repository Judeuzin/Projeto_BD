SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;

USE `mydb` ;

DROP TABLE IF EXISTS `mydb`.`Servidor`;
DROP TABLE IF EXISTS `mydb`.`ContaUsuario`;
DROP TABLE IF EXISTS  `mydb`.`Monstro`;
DROP TABLE IF EXISTS `mydb`.`Local`;
DROP TABLE IF EXISTS `mydb`.`Classe`;
DROP TABLE IF EXISTS  `mydb`.`Roupa`;
DROP TABLE IF EXISTS  `mydb`.`Arma`;
DROP TABLE IF EXISTS  `mydb`.`Personagem`;
DROP TABLE IF EXISTS  `mydb`.`Personagem_has_Roupa`;
DROP TABLE IF EXISTS  `mydb`.`Personagem_has_Arma`;

-- -----------------------------------------------------
-- Table `mydb`.`Servidor`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`Servidor` (
  `idServidor` INT NOT NULL AUTO_INCREMENT,
  `DataDeCriacao` DATETIME NOT NULL,
  `Nome` VARCHAR(45) NOT NULL,
  `NumeroDeJogadores` INT NOT NULL,
  `NumeroMaximoDeJogadores` INT NOT NULL,
  PRIMARY KEY (`idServidor`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`ContaUsuario`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`ContaUsuario` (
  `Login` VARCHAR(15) NOT NULL,
  `Senha` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Login`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Monstro`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`Monstro` (
  `idMonstro` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Nivel` INT NOT NULL,
  `Defesa` INT NOT NULL,
  `Ataque` INT NOT NULL,
  PRIMARY KEY (`idMonstro`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Local`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`Local` (
  `idLocal` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Nivel` INT NOT NULL,
  `Monstro_idMonstro` INT NOT NULL,
  PRIMARY KEY (`idLocal`),
  INDEX `fk_Local_Monstro1_idx` (`Monstro_idMonstro` ASC) VISIBLE,
  CONSTRAINT `fk_Local_Monstro1`
    FOREIGN KEY (`Monstro_idMonstro`)
    REFERENCES `mydb`.`Monstro` (`idMonstro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Classe`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`Classe` (
  `idClasse` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idClasse`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Roupa`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`Roupa` (
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
    REFERENCES `mydb`.`Classe` (`idClasse`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Arma`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`Arma` (
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
    REFERENCES `mydb`.`Classe` (`idClasse`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Personagem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Personagem` (
  `idPersonagem` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Nivel` INT NOT NULL,
  `Servidor_idServidor` INT NOT NULL,
  `ContaUsuario_Login` VARCHAR(15) NOT NULL,
  `ArmaEquipada_idArma` INT NOT NULL,
  `RoupaEquipada_idRoupa` INT NOT NULL,
  `Local_idLocal` INT NOT NULL,
  `Classe_idClasse` INT NOT NULL,
  PRIMARY KEY (`idPersonagem`, `Servidor_idServidor`, `ContaUsuario_Login`),
  INDEX `fk_Personagem_Servidor_idx` (`Servidor_idServidor` ASC) VISIBLE,
  INDEX `fk_Personagem_ContaUsuario1_idx` (`ContaUsuario_Login` ASC) VISIBLE,
  INDEX `fk_Personagem_Arma1_idx` (`ArmaEquipada_idArma` ASC) VISIBLE,
  INDEX `fk_Personagem_Roupa1_idx` (`RoupaEquipada_idRoupa` ASC) VISIBLE,
  INDEX `fk_Personagem_Local1_idx` (`Local_idLocal` ASC) VISIBLE,
  INDEX `fk_Personagem_Classe1_idx` (`Classe_idClasse` ASC) VISIBLE,
  CONSTRAINT `fk_Personagem_Servidor`
    FOREIGN KEY (`Servidor_idServidor`)
    REFERENCES `mydb`.`Servidor` (`idServidor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personagem_ContaUsuario1`
    FOREIGN KEY (`ContaUsuario_Login`)
    REFERENCES `mydb`.`ContaUsuario` (`Login`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personagem_Arma1`
    FOREIGN KEY (`ArmaEquipada_idArma`)
    REFERENCES `mydb`.`Arma` (`idArma`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personagem_Roupa1`
    FOREIGN KEY (`RoupaEquipada_idRoupa`)
    REFERENCES `mydb`.`Roupa` (`idRoupa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personagem_Local1`
    FOREIGN KEY (`Local_idLocal`)
    REFERENCES `mydb`.`Local` (`idLocal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personagem_Classe1`
    FOREIGN KEY (`Classe_idClasse`)
    REFERENCES `mydb`.`Classe` (`idClasse`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Personagem_has_Roupa`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`Personagem_has_Roupa` (
  `Personagem_idPersonagem` INT NOT NULL,
  `Personagem_Servidor_idServidor` INT NOT NULL,
  `Personagem_ContaUsuario_Login` VARCHAR(15) NOT NULL,
  `Roupa_idRoupa` INT NOT NULL,
  PRIMARY KEY (`Personagem_idPersonagem`, `Personagem_Servidor_idServidor`, `Personagem_ContaUsuario_Login`, `Roupa_idRoupa`),
  INDEX `fk_Personagem_has_Roupa_Roupa1_idx` (`Roupa_idRoupa` ASC) VISIBLE,
  INDEX `fk_Personagem_has_Roupa_Personagem1_idx` (`Personagem_idPersonagem` ASC, `Personagem_Servidor_idServidor` ASC, `Personagem_ContaUsuario_Login` ASC) VISIBLE,
  CONSTRAINT `fk_Personagem_has_Roupa_Personagem1`
    FOREIGN KEY (`Personagem_idPersonagem` , `Personagem_Servidor_idServidor` , `Personagem_ContaUsuario_Login`)
    REFERENCES `mydb`.`Personagem` (`idPersonagem` , `Servidor_idServidor` , `ContaUsuario_Login`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personagem_has_Roupa_Roupa1`
    FOREIGN KEY (`Roupa_idRoupa`)
    REFERENCES `mydb`.`Roupa` (`idRoupa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Personagem_has_Arma`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`Personagem_has_Arma` (
  `Personagem_idPersonagem` INT NOT NULL,
  `Personagem_Servidor_idServidor` INT NOT NULL,
  `Personagem_ContaUsuario_Login` VARCHAR(15) NOT NULL,
  `Arma_idArma` INT NOT NULL,
  PRIMARY KEY (`Personagem_idPersonagem`, `Personagem_Servidor_idServidor`, `Personagem_ContaUsuario_Login`, `Arma_idArma`),
  INDEX `fk_Personagem_has_Arma_Arma1_idx` (`Arma_idArma` ASC) VISIBLE,
  INDEX `fk_Personagem_has_Arma_Personagem1_idx` (`Personagem_idPersonagem` ASC, `Personagem_Servidor_idServidor` ASC, `Personagem_ContaUsuario_Login` ASC) VISIBLE,
  CONSTRAINT `fk_Personagem_has_Arma_Personagem1`
    FOREIGN KEY (`Personagem_idPersonagem` , `Personagem_Servidor_idServidor` , `Personagem_ContaUsuario_Login`)
    REFERENCES `mydb`.`Personagem` (`idPersonagem` , `Servidor_idServidor` , `ContaUsuario_Login`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personagem_has_Arma_Arma1`
    FOREIGN KEY (`Arma_idArma`)
    REFERENCES `mydb`.`Arma` (`idArma`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Monstro_has_Arma`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`Monstro_has_Arma` (
  `Monstro_idMonstro` INT NOT NULL,
  `Arma_idArma` INT NOT NULL,
  PRIMARY KEY (`Monstro_idMonstro`, `Arma_idArma`),
  INDEX `fk_Monstro_has_Arma_Arma1_idx` (`Arma_idArma` ASC) VISIBLE,
  INDEX `fk_Monstro_has_Arma_Monstro1_idx` (`Monstro_idMonstro` ASC) VISIBLE,
  CONSTRAINT `fk_Monstro_has_Arma_Monstro1`
    FOREIGN KEY (`Monstro_idMonstro`)
    REFERENCES `mydb`.`Monstro` (`idMonstro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Monstro_has_Arma_Arma1`
    FOREIGN KEY (`Arma_idArma`)
    REFERENCES `mydb`.`Arma` (`idArma`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Roupa_has_Monstro`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`Roupa_has_Monstro` (
  `Roupa_idRoupa` INT NOT NULL,
  `Monstro_idMonstro` INT NOT NULL,
  PRIMARY KEY (`Roupa_idRoupa`, `Monstro_idMonstro`),
  INDEX `fk_Roupa_has_Monstro_Monstro1_idx` (`Monstro_idMonstro` ASC) VISIBLE,
  INDEX `fk_Roupa_has_Monstro_Roupa1_idx` (`Roupa_idRoupa` ASC) VISIBLE,
  CONSTRAINT `fk_Roupa_has_Monstro_Roupa1`
    FOREIGN KEY (`Roupa_idRoupa`)
    REFERENCES `mydb`.`Roupa` (`idRoupa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Roupa_has_Monstro_Monstro1`
    FOREIGN KEY (`Monstro_idMonstro`)
    REFERENCES `mydb`.`Monstro` (`idMonstro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

INSERT INTO Servidor(DataDeCriacao,Nome,NumeroDeJogadores,NumeroMaximoDeJogadores) VALUES (SYSDATE(),'Thor',0,100);
INSERT INTO Servidor(DataDeCriacao,Nome,NumeroDeJogadores,NumeroMaximoDeJogadores) VALUES (SYSDATE(),'Valhalla',0,100);
INSERT INTO Servidor(DataDeCriacao,Nome,NumeroDeJogadores,NumeroMaximoDeJogadores) VALUES (SYSDATE(),'Asgard',0,100);
INSERT INTO Servidor(DataDeCriacao,Nome,NumeroDeJogadores,NumeroMaximoDeJogadores) VALUES (SYSDATE(),'Midgard',0,100);
INSERT INTO Servidor(DataDeCriacao,Nome,NumeroDeJogadores,NumeroMaximoDeJogadores) VALUES (SYSDATE(),'Niflheim',0,100);

INSERT INTO ContaUsuario(Login,Senha) VALUES ('Thor','Thor123');
INSERT INTO ContaUsuario(Login,Senha) VALUES ('Valhalla','Valhalla123');
INSERT INTO ContaUsuario(Login,Senha) VALUES ('Asgard','Asgard123');
INSERT INTO ContaUsuario(Login,Senha) VALUES ('Midgard','Midgard123');