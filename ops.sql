-- MySQL dump 10.13  Distrib 5.5.35, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: ops
-- ------------------------------------------------------
-- Server version	5.5.35-0ubuntu0.12.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `zc_comment`
--

DROP TABLE IF EXISTS `zc_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zc_comment` (
  `coid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `mid` int(11) NOT NULL,
  `uname` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT 'ÐÕÃû',
  `commentinfo` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT '±¸×¢',
  `commenttime` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`coid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='±¸×¢±í';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zc_comment`
--

LOCK TABLES `zc_comment` WRITE;
/*!40000 ALTER TABLE `zc_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `zc_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zc_contact`
--

DROP TABLE IF EXISTS `zc_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zc_contact` (
  `ccid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `cname` text COLLATE utf8_unicode_ci NOT NULL COMMENT 'Ãû×Ö',
  `cinfo` text COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`ccid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='ÁªÏµÈËÐÅÏ¢';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zc_contact`
--

LOCK TABLES `zc_contact` WRITE;
/*!40000 ALTER TABLE `zc_contact` DISABLE KEYS */;
INSERT INTO `zc_contact` VALUES (0,'李晴天','01234567890'),(1,'lee','01234567890'),(4,'jia','1111111');
/*!40000 ALTER TABLE `zc_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zc_idc`
--

DROP TABLE IF EXISTS `zc_idc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zc_idc` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `idcname` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `contact` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(11) COLLATE utf8_unicode_ci NOT NULL COMMENT 'number',
  `comments` text COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zc_idc`
--

LOCK TABLES `zc_idc` WRITE;
/*!40000 ALTER TABLE `zc_idc` DISABLE KEYS */;
INSERT INTO `zc_idc` VALUES (2,'移动','李晴天','12345678900','丰台移动机房'),(4,'皂君庙','','0',''),(5,'土城','','0','土城联通机房'),(6,'北显','','0','北显联通机房'),(7,'华为','lee','0','好机房');
/*!40000 ALTER TABLE `zc_idc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zc_machine`
--

DROP TABLE IF EXISTS `zc_machine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zc_machine` (
  `mid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL COMMENT 'machine room',
  `serverip` text COLLATE utf8_unicode_ci NOT NULL,
  `publicip` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `stype` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT 'server type',
  `sn` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT 'serial number',
  `os` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT 'operating system',
  `service` tinyint(4) NOT NULL COMMENT 'service name',
  `mstatus` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `memsize` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `disksize` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `cpunum` char(8) COLLATE utf8_unicode_ci NOT NULL COMMENT 'cpu',
  `serverrack` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT 'server rack',
  `comment` text COLLATE utf8_unicode_ci COMMENT 'comment',
  `createtime` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'machine create time',
  `modifytime` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'machine modify time',
  `ccid` int(10) unsigned NOT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zc_machine`
--

LOCK TABLES `zc_machine` WRITE;
/*!40000 ALTER TABLE `zc_machine` DISABLE KEYS */;
INSERT INTO `zc_machine` VALUES (1,2,'1.1.1.188','222.222.222.222','','','',12,'在线','10G','','','','这台机器不错','2014-04-14 11:13:18','2014-04-20 13:09:04',0),(2,3,'2.2.2.2','111.111.111.111','','','redhat5.7',10,'在线','8G','100G','4','','','2014-04-14 11:14:08','2014-04-20 14:25:17',0),(3,2,'3.3.3.3','','','','',10,'空闲','','','','','','2014-04-14 17:32:05','2014-04-20 12:39:34',0),(4,2,'4.4.4.4','','','','',10,'空闲','','','','','','2014-04-15 10:24:40',NULL,0),(5,2,'5.5.5.5','','','','',10,'空闲','','','','','','2014-04-15 10:24:54',NULL,0),(6,4,'1.2.2.2','','','','',20,'空闲','','','','','','2014-04-15 10:25:03','2014-04-20 14:25:26',0),(7,4,'1.2.3.3','','','','',10,'空闲','','','','','','2014-04-15 10:25:12','2014-04-20 14:27:16',0),(8,2,'4.4.4.5','','','','',10,'空闲','','','','','','2014-04-15 10:25:21',NULL,0),(9,2,'6.6.6.6','','','','',10,'空闲','','','','','','2014-04-15 10:25:28','2014-04-20 12:29:56',0),(10,2,'1.2.3.1','','','','',10,'空闲','','','','','','2014-04-15 10:25:34',NULL,0),(11,5,'1.1.1.7','','','','',10,'空闲','','','','','','2014-04-15 10:25:42','2014-04-20 14:25:36',0),(12,2,'2.2.2.1','','','','',16,'空闲','','','','','','2014-04-15 10:26:04','2014-04-20 12:02:14',0),(13,7,'3.2.2.1','','','','',10,'空闲','','','','','','2014-04-15 10:26:12','2014-04-21 10:14:06',0),(14,2,'2.3.5.1','','','','',10,'空闲','','','','','','2014-04-15 10:26:19','2014-04-20 12:43:21',0),(16,6,'8.8.8.9','','','','',10,'空闲','','','','','','2014-04-20 12:01:39','2014-04-20 14:25:45',0),(17,2,'8.9.9.9','','','','',10,'空闲','','','','','','2014-04-20 12:41:43',NULL,0);
/*!40000 ALTER TABLE `zc_machine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zc_role`
--

DROP TABLE IF EXISTS `zc_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zc_role` (
  `id` smallint(6) unsigned NOT NULL AUTO_INCREMENT,
  `rolename` varchar(20) CHARACTER SET utf8 NOT NULL,
  `status` tinyint(1) unsigned DEFAULT NULL,
  `remark` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `status` (`status`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zc_role`
--

LOCK TABLES `zc_role` WRITE;
/*!40000 ALTER TABLE `zc_role` DISABLE KEYS */;
INSERT INTO `zc_role` VALUES (1,'administrator',1,NULL),(2,'guest',1,NULL);
/*!40000 ALTER TABLE `zc_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zc_service`
--

DROP TABLE IF EXISTS `zc_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zc_service` (
  `sid` tinyint(4) NOT NULL AUTO_INCREMENT,
  `sname` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT 'ÒµÎñÃû',
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zc_service`
--

LOCK TABLES `zc_service` WRITE;
/*!40000 ALTER TABLE `zc_service` DISABLE KEYS */;
INSERT INTO `zc_service` VALUES (10,'奥运'),(11,'空闲'),(12,'其他'),(13,'uc'),(14,'mued'),(15,'宿主机'),(16,'live'),(17,'ucweb'),(18,'百度合作'),(19,'积分商城'),(20,'数据中心'),(21,'阅读'),(22,'直播'),(24,'search'),(25,'数据挖掘'),(27,'春风社'),(28,'minisite'),(30,'游戏平台'),(31,'小说和起始页'),(33,'微博wap'),(36,'汽车'),(37,'微博DC'),(38,'新小说'),(39,'多屏互动项目'),(40,'手搜push系统'),(42,'腾讯合作');
/*!40000 ALTER TABLE `zc_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zc_user`
--

DROP TABLE IF EXISTS `zc_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zc_user` (
  `uid` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `username` varchar(20) CHARACTER SET latin1 NOT NULL,
  `userpassword` varchar(250) CHARACTER SET latin1 NOT NULL,
  `email` varchar(50) CHARACTER SET latin1 NOT NULL,
  `createtime` int(11) NOT NULL,
  `lastlogintime` int(11) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='ÓÃ»§±í';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zc_user`
--

LOCK TABLES `zc_user` WRITE;
/*!40000 ALTER TABLE `zc_user` DISABLE KEYS */;
INSERT INTO `zc_user` VALUES (1,1,'admin','21232f297a57a5a743894a0e4a801fc3','no19860616@yahoo.com.cn',1325649180,1325652138);
/*!40000 ALTER TABLE `zc_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-04-21 11:26:30
