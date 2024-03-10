-- database_setup.sql

-- Create table to store best open source projects
CREATE TABLE best_projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    stargazers_count INT NOT NULL,
    description TEXT,
    html_url VARCHAR(255) NOT NULL
);

-- Create table to store user specific needs
CREATE TABLE user_needs (
    id SERIAL PRIMARY KEY,
    need VARCHAR(255) NOT NULL
);

-- Sample data for user_needs table
INSERT INTO user_needs (need) VALUES ('your specific need here');
