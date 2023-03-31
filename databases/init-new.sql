CREATE TABLE `user`
(
 `id`         integer NOT NULL AUTO_INCREMENT ,
 `firstname`  varchar(45) NOT NULL ,
 `lastname`   varchar(45) NOT NULL ,
 `mail`       varchar(150) NOT NULL ,
 `age`        integer NOT NULL ,
 `password`   varchar(255) NOT NULL ,
 `username`   varchar(45) NOT NULL ,
 `created_at` datetime NOT NULL ,
 `updated_at` datetime NOT NULL ,

PRIMARY KEY (`id`)
);

CREATE TABLE `achievement`
(
 `id`          integer NOT NULL AUTO_INCREMENT ,
 `name`        varchar(45) NOT NULL ,
 `xp_value`    smallint NOT NULL ,
 `description` text NOT NULL ,
 `metas`       text NOT NULL COMMENT 'JSON permettant de mettre les informations nécessaires à l''acquisition de l''achievement sous forme de données' ,

PRIMARY KEY (`id`)
);

CREATE TABLE `quest`
(
 `id`          integer NOT NULL AUTO_INCREMENT ,
 `name`        varchar(45) NOT NULL ,
 `description` text NOT NULL ,
 `number`      smallint NOT NULL ,
 `difficulty`  tinyint NOT NULL ,
 `xp_value`    smallint NOT NULL ,

PRIMARY KEY (`id`)
);

CREATE TABLE `user_achievements`
(
 `id_achievement` integer NOT NULL ,
 `id_user`        integer NOT NULL ,
 `done_at`        datetime NOT NULL ,

KEY `FK_1` (`id_achievement`),
CONSTRAINT `FK_4` FOREIGN KEY `FK_1` (`id_achievement`) REFERENCES `achievement` (`id`),
KEY `FK_2` (`id_user`),
CONSTRAINT `FK_5` FOREIGN KEY `FK_2` (`id_user`) REFERENCES `user` (`id`)
);

CREATE TABLE `user_quests`
(
 `id_quest` integer NOT NULL ,
 `id_user`  integer NOT NULL ,
 `status`   enum('done', 'in progress', 'failed') NOT NULL ,
 `code`     text NOT NULL ,
 `done_at`  datetime NOT NULL ,

KEY `FK_1` (`id_quest`),
CONSTRAINT `FK_2` FOREIGN KEY `FK_1` (`id_quest`) REFERENCES `quest` (`id`),
KEY `FK_2` (`id_user`),
CONSTRAINT `FK_3` FOREIGN KEY `FK_2` (`id_user`) REFERENCES `user` (`id`)
);

CREATE TABLE `user_stats`
(
 `id`             integer NOT NULL AUTO_INCREMENT ,
 `id_user`        integer NOT NULL ,
 `time_played`    time NOT NULL ,
 `wins`           integer NOT NULL ,
 `defeats`        integer NOT NULL ,
 `line_coded`     integer NOT NULL ,
 `last_connexion` time NOT NULL ,
 `experience`     integer NOT NULL ,

PRIMARY KEY (`id`),
KEY `FK_2` (`id_user`),
CONSTRAINT `FK_1` FOREIGN KEY `FK_2` (`id_user`) REFERENCES `user` (`id`)
);