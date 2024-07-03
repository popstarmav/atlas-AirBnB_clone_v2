-- Setup Db for dev

-- Check if the database 'hbnb_dev_db' exists, and create it if it doesn't
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Check if the user 'hbnb_dev' exists on 'localhost', and create it with a password if it doesn't
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the database 'hbnb_dev_db' to the user 'hbnb_dev'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant the user 'hbnb_dev' the privilege to perform SELECT operations on the 'performance_schema' database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply the changes made by the GRANT statements
FLUSH PRIVILEGES;

