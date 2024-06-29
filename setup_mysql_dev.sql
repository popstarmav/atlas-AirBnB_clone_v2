-- Db for dev

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTSs 'hbnb_dev'@'localhost' IDENTIFIED BY hbnb_dev_pwd;
GRANT ALL PRIVILEGES ON hbnb_dev_db TO 'hbnb_dev'@'localhost';
GRANT SELECT PRIVILEGES ON performance_schema;
FLUSH PRIVILEGES;
