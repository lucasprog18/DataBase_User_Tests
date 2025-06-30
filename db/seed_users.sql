-- Initial seed for 'users' table
-- Run with: sqlite3 db/users.db < db/seed_users.sql

INSERT INTO users (name, email, cpf) VALUES 
  ('Alice Ferreira', 'alice@example.com', '111.111.111-11'),
  ('Bruno Costa', 'bruno@example.com', '222.222.222-22'),
  ('Camila Rocha', 'camila@example.com', '333.333.333-33'),
  ('Diego Almeida', 'diego@example.com', '444.444.444-44'),
  ('Evelyn Lima', 'evelyn@example.com', '555.555.555-55');
