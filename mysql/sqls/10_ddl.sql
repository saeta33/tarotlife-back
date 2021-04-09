set global local_infile = 1;

use tarot;

-- tarot.tarot_desc definition

CREATE TABLE `tarot_desc` (
  `seq` int DEFAULT NULL,
  `c_id` varchar(10) DEFAULT NULL,
  `p_id` varchar(10) DEFAULT NULL,
  `ans` varchar(10) DEFAULT NULL,
  `name` varchar(500) DEFAULT NULL,
  `name_ja` varchar(500) DEFAULT NULL,
  `m_id` varchar(10) DEFAULT NULL,
  `m_kbn` varchar(50) DEFAULT NULL,
  `keyword0` varchar(500) DEFAULT NULL,
  `keyword1` varchar(500) DEFAULT NULL,
  `keyword2` varchar(500) DEFAULT NULL,
  `keyword3` varchar(500) DEFAULT NULL,
  `keyword4` varchar(500) DEFAULT NULL,
  `keyword5` varchar(500) DEFAULT NULL,
  `desc` text,
  `﻿seq` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- tarot.user_score definition

CREATE TABLE `user_score` (
  `user_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `score` float DEFAULT NULL,
  `score_dt` datetime DEFAULT NULL,
  `game_id` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- tarot.users definition

CREATE TABLE `users` (
  `id` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `address` varchar(1000) DEFAULT NULL,
  `tel` varchar(100) DEFAULT NULL,
  `mail` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO tarot.users (id, name, address, tel, mail, pwd) VALUES('01', '名前１', '住所１', '080-111-1111', 'user01@mail.com', 'password');
INSERT INTO tarot.users (id, name, address, tel, mail, pwd) VALUES('02', '名前２', '住所２', '080-222-2222', 'user02@mail.com', 'password');

-- tarot.musers definition

CREATE TABLE `musers` (
  `id` int DEFAULT NULL,
  `postalcode` varchar(10) COLLATE utf8mb4_bin DEFAULT NULL,
  `add1` varchar(120) COLLATE utf8mb4_bin DEFAULT NULL,
  `add2` varchar(120) COLLATE utf8mb4_bin DEFAULT NULL,
  `name` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `furigana` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `password` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `usrtel` varchar(20) COLLATE utf8mb4_bin DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `birthtime` varchar(10) COLLATE utf8mb4_bin DEFAULT NULL,
  `birthplace` varchar(120) COLLATE utf8mb4_bin DEFAULT NULL,
  `usrmail` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `cardflg` tinyint DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `modified` datetime DEFAULT NULL,
  `updateid` int DEFAULT NULL,
  `mdivision_id` int DEFAULT NULL,
  `taboo_flg` tinyint DEFAULT NULL,
  `adminflg` tinyint DEFAULT NULL,
  `remarks` varchar(124) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- tarot.Ereadings definition

CREATE TABLE `Ereadings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `mreading_id` int DEFAULT NULL,
  `answer` varchar(1000) COLLATE utf8mb4_bin DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `modified` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;



-- tarot.Mclassification definition

CREATE TABLE `Mclassification` (
  `id` int NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `modified` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


-- tarot.Mcommentarys definition

CREATE TABLE `Mcommentarys` (
  `id` int DEFAULT NULL,
  `mfile_id` int DEFAULT NULL,
  `mktbn_id` int DEFAULT NULL,
  `tno` int DEFAULT NULL,
  `name` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `Japanese` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `explanation` varchar(120) COLLATE utf8mb4_bin DEFAULT NULL,
  `rexplanation` varchar(120) COLLATE utf8mb4_bin DEFAULT NULL,
  `keyword0` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `keyword1` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `keyword2` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `keyword3` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `keyword4` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `keyword5` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `keyword6` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `keyword7` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `keyword8` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `keyword9` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `rkeyword0` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `rkeyword1` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `rkeyword2` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `rkeyword3` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `rkeyword4` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `rkeyword5` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `rkeyword6` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `rkeyword7` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `rkeyword8` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `rkeyword9` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `modified` datetime DEFAULT NULL,
  `updateid` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


-- tarot.Mreadings definition

CREATE TABLE `Mreadings` (
  `id` int DEFAULT NULL,
  `mcoursename_id` int DEFAULT NULL,
  `mclassification_id` int DEFAULT NULL,
  `level_id` int DEFAULT NULL,
  `mspread_id` int NOT NULL,
  `title` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `question` varchar(1000) COLLATE utf8mb4_bin DEFAULT NULL,
  `correct_answer` varchar(1000) COLLATE utf8mb4_bin DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `modified` datetime DEFAULT NULL,
  `updateid` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


-- tarot.Mspreads definition

CREATE TABLE `Mspreads` (
  `id` int DEFAULT NULL,
  `name` varchar(40) COLLATE utf8mb4_bin DEFAULT NULL,
  `template` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `modified` datetime DEFAULT NULL,
  `updateid` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


-- tarot.Vreadings source

CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `tarot`.`Vreadings` AS
select
    `r`.`id` AS `id`,
    `r`.`mcoursename_id` AS `mcoursename_id`,
    `r`.`mclassification_id` AS `mclassification_id`,
    `r`.`level_id` AS `level_id`,
    `r`.`mspread_id` AS `mspread_id`,
    `r`.`title` AS `title`,
    `c`.`name` AS `cname`,
    `r`.`question` AS `question`,
    `r`.`correct_answer` AS `correct_answer`,
    `r`.`created` AS `created`,
    `r`.`modified` AS `modified`,
    `r`.`updateid` AS `updateid`,
    `s`.`template` AS `template`
from
    ((`tarot`.`Mreadings` `r`
join `tarot`.`Mclassification` `c` on
    ((`r`.`mclassification_id` = `c`.`id`)))
join `tarot`.`Mspreads` `s` on
    ((`r`.`mspread_id` = `s`.`id`)));

-- test users
	
INSERT INTO tarot.musers (id, password, usrmail) VALUES(1, 'password', 'user01@mail.com');
INSERT INTO tarot.musers (id, password, usrmail) VALUES(2, 'password', 'user02@mail.com');

-- categories

INSERT INTO tarot.Mclassification (id, name, created, modified) VALUES(1, '人間関係', '20210305', '20210305');
INSERT INTO tarot.Mclassification (id, name, created, modified) VALUES(2, '恋愛', '20210305', '20210305');
INSERT INTO tarot.Mclassification (id, name, created, modified) VALUES(3, '仕事', '20210305', '20210305');
INSERT INTO tarot.Mclassification (id, name, created, modified) VALUES(4, 'その他', '20210305', '20210305');
