CREATE DATABASE if not  EXISTS `db_banco`;
USE `db_banco`;


CREATE TABLE usuarios (
   id INT AUTO_INCREMENT PRIMARY KEY,
   email TEXT NOT NULL,
   senha TEXT NOT NULL
);

CREATE TABLE tarefas (
   id INT AUTO_INCREMENT PRIMARY KEY,
   usuario_id TEXT NOT NULL,
   titulo TEXT NOT NULL,
   conteudo TEXT NOT NULL
);

CREATE TABLE categorias (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome TEXT NOT NULL
);