-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema foodies_db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `foodies_db` ;

-- -----------------------------------------------------
-- Schema foodies_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `foodies_db` DEFAULT CHARACTER SET utf8 ;
USE `foodies_db` ;

-- -----------------------------------------------------
-- Table `foodies_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `foodies_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foodies_db`.`restaurants`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `foodies_db`.`restaurants` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `location` VARCHAR(100) NOT NULL,
  `reason` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_restaurants_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_restaurants_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `foodies_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foodies_db`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `foodies_db`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `sender_id` INT NOT NULL,
  `receiver_id` INT NOT NULL,
  `restaurant_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_users_idx` (`sender_id` ASC) VISIBLE,
  INDEX `fk_messages_users1_idx` (`receiver_id` ASC) VISIBLE,
  INDEX `fk_messages_restaurants1_idx` (`restaurant_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_users`
    FOREIGN KEY (`sender_id`)
    REFERENCES `foodies_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_messages_users1`
    FOREIGN KEY (`receiver_id`)
    REFERENCES `foodies_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_messages_restaurants1`
    FOREIGN KEY (`restaurant_id`)
    REFERENCES `foodies_db`.`restaurants` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foodies_db`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `foodies_db`.`favorites` (
  `user_id` INT NOT NULL,
  `restaurant_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `restaurant_id`),
  INDEX `fk_users_has_restaurants_restaurants1_idx` (`restaurant_id` ASC) VISIBLE,
  INDEX `fk_users_has_restaurants_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_restaurants_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `foodies_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_restaurants_restaurants1`
    FOREIGN KEY (`restaurant_id`)
    REFERENCES `foodies_db`.`restaurants` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
