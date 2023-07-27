DROP DATABASE IF EXISTS gpeDb;
CREATE DATABASE IF NOT EXISTS gpeDb;
CREATE USER 'gpeUser'@'%' IDENTIFIED BY 'JeSuIsLePaSsWordDeTeSt';
GRANT ALL PRIVILEGES ON *.* TO 'gpeUser'@'%' WITH GRANT OPTION;
flush privileges; 
USE gpeDb;

CREATE TABLE `user`
(
    `id`             INT NOT NULL AUTO_INCREMENT,
    `firstname`      VARCHAR(45) NOT NULL,
    `lastname`       VARCHAR(45) NOT NULL,
    `mail`           VARCHAR(150) NOT NULL,
    `age`            INT NOT NULL,
    `password`       VARCHAR(255) NOT NULL,
    `username`       VARCHAR(45) NOT NULL,
    `is_admin`       TINYINT(1) NOT NULL DEFAULT 0,
    `wins`           INT NOT NULL DEFAULT 0,
    `defeats`        INT NOT NULL DEFAULT 0,
    `line_coded`     INT NOT NULL DEFAULT 0,
    `experience`     INT NOT NULL DEFAULT 0,
    PRIMARY KEY (`id`)
);

CREATE TABLE `achievement`
(
    `id`          INT NOT NULL AUTO_INCREMENT,
    `name`        VARCHAR(45) NOT NULL,
    `xp_value`    SMALLINT NOT NULL DEFAULT 0,
    `description` TEXT NOT NULL,
    `metas`       TEXT NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `quest`
(
    `id`          INT NOT NULL AUTO_INCREMENT,
    `name`        VARCHAR(45) NOT NULL,
    `description` TEXT NOT NULL,
    `number`      SMALLINT NOT NULL,
    `difficulty`  TINYINT NOT NULL,
    `xp_value`    SMALLINT NOT NULL DEFAULT 0,
    PRIMARY KEY (`id`)
);

CREATE TABLE `user_achievements`
(
    `id`             INT NOT NULL AUTO_INCREMENT,
    `id_achievement` INT NOT NULL,
    `id_user`        INT NOT NULL,
    `done_at`        DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (`id`)
);

CREATE TABLE `user_quests`
(
    `id`       INT NOT NULL AUTO_INCREMENT,
    `id_quest` INT NOT NULL,
    `id_user`  INT NOT NULL,
    `status`   ENUM('done', 'in progress', 'failed') NOT NULL DEFAULT 'in progress',
    `code`     TEXT NOT NULL,
    `done_at`  DATETIME NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `download`
(
    `id`          INT NOT NULL AUTO_INCREMENT,
    `nb_download` INT NOT NULL,
    PRIMARY KEY (`id`)
);
