-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: alokar
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cargos`
--

DROP TABLE IF EXISTS `cargos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cargos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargos`
--

LOCK TABLES `cargos` WRITE;
/*!40000 ALTER TABLE `cargos` DISABLE KEYS */;
INSERT INTO `cargos` VALUES (1,'Manager'),(2,'Analista');
/*!40000 ALTER TABLE `cargos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionarios`
--

DROP TABLE IF EXISTS `funcionarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nomeCompleto` varchar(100) NOT NULL,
  `custoHora` decimal(10,0) NOT NULL,
  `quantProjetos` int NOT NULL,
  `disponibilidade` varchar(45) NOT NULL,
  `custoHora_overtime` varchar(45) DEFAULT NULL,
  `cargo_id` int NOT NULL,
  PRIMARY KEY (`id`,`cargo_id`),
  KEY `fk_funcionarios_cargo1_idx` (`cargo_id`),
  CONSTRAINT `fk_funcionarios_cargo1` FOREIGN KEY (`cargo_id`) REFERENCES `cargos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionarios`
--

LOCK TABLES `funcionarios` WRITE;
/*!40000 ALTER TABLE `funcionarios` DISABLE KEYS */;
INSERT INTO `funcionarios` VALUES (1,'Junior Silva',10,2,'Disponível','20',2),(2,'Joana Santos',20,3,'Indisponível','40',1),(3,'Ana Maria',30,2,'Disponível','60',2),(4,'Carlos Eduardo',36,1,'Indisponível','50',1),(5,'Paula Fortunato',20,3,'Indisponível','40',1),(6,'João Paulo',25,2,'Disponível','50',2),(7,'Rafael Ferreira',30,1,'Disponível','60',1),(8,'Vitória Santos',30,2,'Indisponível','60',1),(9,'Luiz Tomaz',15,1,'Disponível','30',2),(10,'Juliane Felix',35,2,'Dispnível','70',1),(11,'Rennan Pereira',30,1,'Disponível','60',1);
/*!40000 ALTER TABLE `funcionarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionarios_habilidades`
--

DROP TABLE IF EXISTS `funcionarios_habilidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionarios_habilidades` (
  `funcionarios_id` int NOT NULL,
  `habilidades_id` int NOT NULL,
  `tempoExperiencia` int NOT NULL,
  PRIMARY KEY (`funcionarios_id`,`habilidades_id`),
  KEY `fk_funcionários_has_habilidades_habilidades1_idx` (`habilidades_id`),
  KEY `fk_funcionários_has_habilidades_funcionários_idx` (`funcionarios_id`),
  CONSTRAINT `fk_funcionários_has_habilidades_funcionários` FOREIGN KEY (`funcionarios_id`) REFERENCES `funcionarios` (`id`),
  CONSTRAINT `fk_funcionários_has_habilidades_habilidades1` FOREIGN KEY (`habilidades_id`) REFERENCES `habilidades` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionarios_habilidades`
--

LOCK TABLES `funcionarios_habilidades` WRITE;
/*!40000 ALTER TABLE `funcionarios_habilidades` DISABLE KEYS */;
INSERT INTO `funcionarios_habilidades` VALUES (1,1,20),(2,2,30);
/*!40000 ALTER TABLE `funcionarios_habilidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionarios_projetos`
--

DROP TABLE IF EXISTS `funcionarios_projetos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionarios_projetos` (
  `funcionarios_id` int NOT NULL,
  `projetos_id` int NOT NULL,
  `overtime` int DEFAULT NULL,
  `funcao` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`funcionarios_id`,`projetos_id`),
  KEY `fk_funcionarios_has_projetos_projetos1_idx` (`projetos_id`),
  KEY `fk_funcionarios_has_projetos_funcionarios1_idx` (`funcionarios_id`),
  CONSTRAINT `fk_funcionarios_has_projetos_funcionarios1` FOREIGN KEY (`funcionarios_id`) REFERENCES `funcionarios` (`id`),
  CONSTRAINT `fk_funcionarios_has_projetos_projetos1` FOREIGN KEY (`projetos_id`) REFERENCES `projetos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionarios_projetos`
--

LOCK TABLES `funcionarios_projetos` WRITE;
/*!40000 ALTER TABLE `funcionarios_projetos` DISABLE KEYS */;
/*!40000 ALTER TABLE `funcionarios_projetos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `habilidades`
--

DROP TABLE IF EXISTS `habilidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `habilidades` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `habilidades`
--

LOCK TABLES `habilidades` WRITE;
/*!40000 ALTER TABLE `habilidades` DISABLE KEYS */;
INSERT INTO `habilidades` VALUES (1,'Python'),(2,'C#'),(3,'Angular'),(4,'PHP'),(5,'SQL Server'),(6,'Power BI'),(7,'Scrum');
/*!40000 ALTER TABLE `habilidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projetos`
--

DROP TABLE IF EXISTS `projetos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projetos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `custoPrevisto` float DEFAULT NULL,
  `area` varchar(45) DEFAULT NULL,
  `descricao` varchar(500) DEFAULT NULL,
  `otherCost` float DEFAULT NULL,
  `hardware` float DEFAULT NULL,
  `licenca` float DEFAULT NULL,
  `duracao` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `seatCharge` float DEFAULT NULL,
  `nomeEmpresa` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projetos`
--

LOCK TABLES `projetos` WRITE;
/*!40000 ALTER TABLE `projetos` DISABLE KEYS */;
INSERT INTO `projetos` VALUES (3,'Alokar',30000,'T.I','ZUltrices eros in cursus turpis. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. Cras adipiscing enim eu turpis. Tellus at urna condimentum mattis pellentesque.',10000,5000,5000,'Long Term','Incompleto',2000,'Accentureiros'),(4,'+ Saúde',20000,'Saúde','Ultrices eros in cursus turpis. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. Cras adipiscing enim eu turpis. Tellus at urna condimentum mattis pellentesque.',10000,5000,5000,'Short Term','Completo',2000,'Y'),(5,'Contigo',42000,'T.I','Ultrices eros in cursus turpis. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. Cras adipiscing enim eu turpis. Tellus at urna condimentum mattis pellentesque.',1000,5000,5000,'Long Term','Incompleto',3000,'Accenture'),(6,'Quick Results',35000,'T.I','Ultrices eros in cursus turpis. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. Cras adipiscing enim eu turpis. Tellus at urna condimentum mattis pellentesque.',1000,5000,5000,'Short Term','Incompleto',3000,'Accenture'),(7,'Porto Digital',70000,'T.I','Ultrices eros in cursus turpis. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. Cras adipiscing enim eu turpis. Tellus at urna condimentum mattis pellentesque.',1000,5000,5000,'Short Term','Incompleto',3000,'Accenture'),(8,'Senac',54000,'Educação','Ultrices eros in cursus turpis. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. Cras adipiscing enim eu turpis. Tellus at urna condimentum mattis pellentesque.',1000,5000,5000,'Long Term','Incompleto',3000,'Accenture'),(9,'Senai',48000,'Educação','Ultrices eros in cursus turpis. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. Cras adipiscing enim eu turpis. Tellus at urna condimentum mattis pellentesque.',1000,5000,5000,'Long Term','Incompleto',3000,'Accenture'),(10,'TopTab',10000,'T.I','Ultrices eros in cursus turpis. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. Cras adipiscing enim eu turpis. Tellus at urna condimentum mattis pellentesque.',1000,5000,5000,'Short Term','Incompleto',3000,'Accenture'),(11,'Buzzify',37000,'T.I','Ultrices eros in cursus turpis. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. Cras adipiscing enim eu turpis. Tellus at urna condimentum mattis pellentesque.',1000,5000,5000,'Long Term','Incompleto',3000,'Accenture'),(12,'Brightbook',28000,'Educação','Ultrices eros in cursus turpis. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. Cras adipiscing enim eu turpis. Tellus at urna condimentum mattis pellentesque.',1000,5000,5000,'Long Term','Incompleto',3000,'Accenture'),(31,'BlankSteuvin',500,'T.I','Ultrices eros in cursus turpis. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. Cras adipiscing enim eu turpis. Tellus at urna condimentum mattis pellentesque.',40123,12312,400,'Long Term','',5005,'Tecnologias Novas'),(35,'Projeto Z',30000,'Saúde','ZZZZZZZZZZZZZZZZ',10000,5000,5000,'Long Term','Incompleto',2000,'Z');
/*!40000 ALTER TABLE `projetos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projetos_habilidades`
--

DROP TABLE IF EXISTS `projetos_habilidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projetos_habilidades` (
  `projetos_id` int NOT NULL,
  `habilidades_id` int NOT NULL,
  PRIMARY KEY (`projetos_id`,`habilidades_id`),
  KEY `fk_projetos_has_habilidades_habilidades1_idx` (`habilidades_id`),
  KEY `fk_projetos_has_habilidades_projetos1_idx` (`projetos_id`),
  CONSTRAINT `fk_projetos_has_habilidades_habilidades1` FOREIGN KEY (`habilidades_id`) REFERENCES `habilidades` (`id`),
  CONSTRAINT `fk_projetos_has_habilidades_projetos1` FOREIGN KEY (`projetos_id`) REFERENCES `projetos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projetos_habilidades`
--

LOCK TABLES `projetos_habilidades` WRITE;
/*!40000 ALTER TABLE `projetos_habilidades` DISABLE KEYS */;
/*!40000 ALTER TABLE `projetos_habilidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `senha` varchar(250) DEFAULT NULL,
  `funcionarios_id` int NOT NULL,
  `funcionarios_cargo_id` int NOT NULL,
  PRIMARY KEY (`id`,`funcionarios_id`,`funcionarios_cargo_id`),
  KEY `fk_usuarios_funcionarios1_idx` (`funcionarios_id`,`funcionarios_cargo_id`),
  CONSTRAINT `fk_usuarios_funcionarios1` FOREIGN KEY (`funcionarios_id`, `funcionarios_cargo_id`) REFERENCES `funcionarios` (`id`, `cargo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'alokar'
--

--
-- Dumping routines for database 'alokar'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-08 10:35:36
