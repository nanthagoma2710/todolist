-- Create the todo_list_db database
CREATE DATABASE todolist;

-- Use the todo_list_db database
USE todolist;

-- Create the tasks table
CREATE TABLE IF NOT EXISTS todo (
  id INT AUTO_INCREMENT,
  task VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

--     To-Do List:
-- 1. Wake up at 6:00 AM
-- 2. Exercise (30 minutes)
-- 3. Shower and get dressed
-- 4. Have breakfast
-- 5. Check and respond to important emails