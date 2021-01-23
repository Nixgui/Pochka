-- --------------------------------------------------------
-- Хост:                         127.0.0.1
-- Версия сервера:               8.0.22 - MySQL Community Server - GPL
-- Операционная система:         Win64
-- HeidiSQL Версия:              11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Дамп структуры базы данных pyclient
CREATE DATABASE IF NOT EXISTS `pyclient` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `pyclient`;

-- Дамп структуры для таблица pyclient.accounts
CREATE TABLE IF NOT EXISTS `accounts` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(255) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дамп данных таблицы pyclient.accounts: ~1 rows (приблизительно)
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` (`ID`, `Username`, `Password`) VALUES
	(1, 'Admin', 'Adminn');
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;

-- Дамп структуры для таблица pyclient.clients
CREATE TABLE IF NOT EXISTS `clients` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ClientName` varchar(255) DEFAULT NULL,
  `BeginData` datetime(4) DEFAULT NULL,
  `EndData` datetime(4) DEFAULT NULL,
  `Hairdresser` int DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  KEY `FK_clients_hairdresser` (`Hairdresser`),
  CONSTRAINT `FK_clients_hairdresser` FOREIGN KEY (`Hairdresser`) REFERENCES `hairdresser` (`ID`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дамп данных таблицы pyclient.clients: ~1 rows (приблизительно)
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` (`ID`, `ClientName`, `BeginData`, `EndData`, `Hairdresser`) VALUES
	(1, 'Nina', '2021-01-22 21:00:00.0000', '2021-01-22 22:47:44.0000', 1);
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;

-- Дамп структуры для таблица pyclient.hairdresser
CREATE TABLE IF NOT EXISTS `hairdresser` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `HairdresserName` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `HairdresserName` (`HairdresserName`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дамп данных таблицы pyclient.hairdresser: ~1 rows (приблизительно)
/*!40000 ALTER TABLE `hairdresser` DISABLE KEYS */;
INSERT INTO `hairdresser` (`ID`, `HairdresserName`) VALUES
	(1, 'Diana');
/*!40000 ALTER TABLE `hairdresser` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
