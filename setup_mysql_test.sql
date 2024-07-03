-- CREATE THE DATABASE
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- CREATE THE USER
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

--  GRANT ALL PRIVILEGES ON THE DATABASE TO THE USER
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- GRANT SELECT ON performance_schema TO THE USER
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;