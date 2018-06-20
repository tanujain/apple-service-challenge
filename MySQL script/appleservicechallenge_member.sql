-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: appleservicechallenge
-- ------------------------------------------------------
-- Server version	5.7.15-log

-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member` (
  `idMember` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `password` char(100) NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`idMember`),
  UNIQUE KEY `idMember_UNIQUE` (`idMember`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (13,'LG0D26','$pbkdf2-sha256$29000$wvif856T0poTYsyZE8LYmw$Xdi1DciziJ4d.mdytoIka4QOTqzOAMBBMFBKuUN2Bec','LG0D26@gmail.com'),(14,'13JHPA','$pbkdf2-sha256$29000$GgPAuJcy5hzjHGNsbe19bw$MxI9I6ClGemS74mLYhScbu.f9d/Mg9t/ylLrXYD0y5U','13JHPA@gmail.com'),(15,'349QL1','$pbkdf2-sha256$29000$oTRmjFHqHeOc894bQ8iZkw$EPKpLLPNdwvbgF6k//In48Na48ek5vGkb7JPYwNI7oc','349QL1@gmail.com'),(16,'WKFOC0','$pbkdf2-sha256$29000$n5PSmrO29n7PmTOmNAbAWA$VBN7onZK8vOB/k.RZt7RsTubNOpCy8LGRVTBbZTz5gI','WKFOC0@gmail.com'),(17,'RX8VZI','$pbkdf2-sha256$29000$iRGCkFKKkVLqHcN4r1XKuQ$76sKfVJxaUlo9mCjRl108DIwJJq17HDqY3LkQe2oIig','RX8VZI@gmail.com'),(18,'43F986','$pbkdf2-sha256$29000$xZiz9n4PYSzFuJeydg4hpA$aIKLs52aGozcOY2GTHD.5OSovXn38l7nrZia7hwjlcA','43F986@gmail.com'),(19,'OAN0I3','$pbkdf2-sha256$29000$AuAcg/A.x9ibk9Jay7l3Lg$4ljezA15FCcAaGc0MP.s7yUi5hOjhtSZPeTwL4POz7E','OAN0I3@gmail.com'),(20,'E2IA9V','$pbkdf2-sha256$29000$tlaqtbY2BuBcay1lbI1RKg$bWvnsGCbgQ9thLEue4Zy66mzoTl692SBacigaMhtksw','E2IA9V@gmail.com');


-- Dump completed on 2018-06-18 22:59:14
