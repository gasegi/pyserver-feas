-- CREATE DATABASE IF NOT EXISTS test_database;
-- USE test_database;

---- drop ----
DROP TABLE IF EXISTS `staff`;
DROP TABLE IF EXISTS `staff_job`;

---- create ----
CREATE TABLE IF NOT EXISTS `staff`
(
 `staff_id`             INT(11) AUTO_INCREMENT NOT NULL,
 `staff_number`         VARCHAR(10) NOT NULL,
 `staff_name`           VARCHAR(64) NOT NULL,
 `password`             VARCHAR(255) NOT NULL,
 `admin_flag`           INT(1) NOT NULL,
 `delete_flag`          INT(1) NOT NULL,
    PRIMARY KEY (`staff_id`)
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE IF NOT EXISTS `staff_job`
(
 `staff_id`             INT(11) NOT NULL,
 `job_id`               INT(11) NOT NULL,
    PRIMARY KEY (`staff_id`, `job_id`)
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
