DROP DATABASE IF EXISTS gpeDb;
CREATE DATABASE IF NOT EXISTS gpeDb;
USE gpeDb;


CREATE TABLE 'user'
(
    'id'             integer NOT NULL AUTO_INCREMENT ,
    'firstname'      varchar(45) NOT NULL ,
    'lastname'       varchar(45) NOT NULL ,
    'mail'           varchar(150) NOT NULL ,
    'age'            integer NOT NULL ,
    'password'       varchar(255) NOT NULL ,
    'username'       varchar(45) NOT NULL ,
    'is_admin'       boolean NOT NULL DEFAULT 0,
    'time_played'    time NOT NULL DEFAULT 0,
    'wins'           integer NOT NULL DEFAULT 0,
    'defeats'        integer NOT NULL DEFAULT 0,
    'line_coded'     integer NOT NULL DEFAULT 0,
    'last_connexion' time NOT NULL DEFAULT 0,
    'experience'     integer NOT NULL DEFAULT 0,
    'created_at'     datetime NOT NULL  DEFAULT NOW(),
    'updated_at'     datetime NOT NULL DEFAULT NOW(),

    PRIMARY KEY ('id')
);


CREATE TABLE 'achievement'
(
    'id'          integer NOT NULL AUTO_INCREMENT ,
    'name'        varchar(45) NOT NULL ,
    'xp_value'    smallint NOT NULL DEFAULT 0,
    'description' text NOT NULL ,
    'metas'       text NOT NULL ,

    PRIMARY KEY ('id')
);

CREATE TABLE 'quest'
(
    'id'          integer NOT NULL AUTO_INCREMENT ,
    'name'        varchar(45) NOT NULL ,
    'description' text NOT NULL ,
    'number'      smallint NOT NULL ,
    'difficulty'  tinyint NOT NULL ,
    'xp_value'    smallint NOT NULL DEFAULT 0,

    PRIMARY KEY ('id')
);

CREATE TABLE 'user_achievements'
(
 'id'             integer NOT NULL AUTO_INCREMENT ,
 'id_achievement' integer NOT NULL ,
 'id_user'        integer NOT NULL ,
 'done_at'        datetime NOT NULL DEFAULT NOW(),

    PRIMARY KEY ('id')
);

CREATE TABLE 'user_quests'
(
    'id_quest' integer NOT NULL ,
    'id_user'  integer NOT NULL ,
    'status'   enum('done', 'in progress', 'failed') NOT NULL DEFAULT 'in progress',
    'code'     text NOT NULL ,
    'done_at'  datetime NOT NULL ,

    KEY 'FK_1' ('id_quest'),
    CONSTRAINT 'FK_2' FOREIGN KEY 'FK_1' ('id_quest') REFERENCES 'quest' ('id'),
    KEY 'FK_2' ('id_user'),
    CONSTRAINT 'FK_3' FOREIGN KEY 'FK_2' ('id_user') REFERENCES 'user' ('id')
);

CREATE TABLE 'download'
(
    'id' integer NOT NULL AUTO_INCREMENT ,
    'nb_download' integer NOT NULL ,

    PRIMARY KEY ('id')
);