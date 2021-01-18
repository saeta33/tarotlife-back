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
  `score` int DEFAULT NULL,
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

