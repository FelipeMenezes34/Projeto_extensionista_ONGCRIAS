-- Execute como administrador (root) UMA vez. As tabelas são criadas pelo Django (migrate).
CREATE DATABASE IF NOT EXISTS ong_crias CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Usuário exclusivo do site, com acesso só a este banco (nunca use o root no site).
CREATE USER IF NOT EXISTS 'crias_app'@'localhost' IDENTIFIED BY 'TROQUE_ESTA_SENHA';
GRANT ALL PRIVILEGES ON ong_crias.* TO 'crias_app'@'localhost';
FLUSH PRIVILEGES;
