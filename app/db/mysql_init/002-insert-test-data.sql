-- CREATE DATABASE IF NOT EXISTS test_database;
-- USE test_database;

-- DROP TABLE IF EXISTS `staff`;
-- DROP TABLE IF EXISTS `staff_job`;

SET character_set_client = utf8;
SET character_set_connection = utf8;

INSERT INTO staff VALUES 
(1, 'user1', '鈴木', 'raM7IbozF4Awk',1,0),
(2, 'user2', '田中', 'pass2',0,0),
(3, 'user3', '田中削除', 'pass3',0,1);

INSERT INTO staff_job VALUES 
(1,1),
(1,2);

