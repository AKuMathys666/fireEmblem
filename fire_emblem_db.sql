-- --------------------------------------------------------
-- Hôte :                        127.0.0.1
-- Version du serveur:           10.1.28-MariaDB - mariadb.org binary distribution
-- SE du serveur:                Win32
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Export de la structure de la base pour fire_emblem_db
CREATE DATABASE IF NOT EXISTS `fire_emblem_db` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `fire_emblem_db`;

-- Export de la structure de la table fire_emblem_db. personnage
CREATE TABLE IF NOT EXISTS `personnage` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nom` varchar(32) NOT NULL,
  `type_deplacement` enum('Tank','Infanterie','Flier','Cavalier') NOT NULL,
  `hp` int(10) NOT NULL,
  `atk` int(10) NOT NULL,
  `vit` int(10) NOT NULL,
  `def` int(10) NOT NULL,
  `res` int(10) NOT NULL,
  `portee` int(10) NOT NULL,
  `type_attaque` enum('Magique','Physique') NOT NULL,
  `couleur` enum('Rouge','Bleu','Vert','Gris') NOT NULL,
  `image` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- Export de données de la table fire_emblem_db.personnage : ~8 rows (environ)
/*!40000 ALTER TABLE `personnage` DISABLE KEYS */;
INSERT INTO `personnage` (`id`, `nom`, `type_deplacement`, `hp`, `atk`, `vit`, `def`, `res`, `portee`, `type_attaque`, `couleur`, `image`) VALUES
	(1, 'Abel', 'Cavalier', 39, 33, 32, 25, 25, 1, 'Physique', 'Bleu', 'img\\Characters\\Abel\\BtlFace - Copie.png'),
	(2, 'Alfonse', 'Infanterie', 43, 35, 25, 32, 22, 1, 'Physique', 'Rouge', 'img\\Characters\\Alfonse\\BtlFace - Copie.png'),
	(3, 'Alm', 'Infanterie', 45, 33, 30, 28, 22, 1, 'Physique', 'Rouge', 'img\\Characters\\Alm\\BtlFace - Copie.png'),
	(4, 'Amelia', 'Tank', 47, 34, 34, 35, 23, 1, 'Physique', 'Vert', 'img\\Characters\\Amelia\\BtlFace - Copie.png'),
	(5, 'Anna', 'Infanterie', 41, 29, 38, 22, 28, 1, 'Physique', 'Vert', 'img\\Characters\\Anna\\BtlFace - Copie.png'),
	(6, 'Arthur', 'Infanterie', 43, 32, 29, 30, 24, 1, 'Physique', 'Vert', 'img\\Characters\\Arthur\\BtlFace - Copie.png'),
	(7, 'Athena', 'Infanterie', 36, 31, 38, 27, 24, 1, 'Physique', 'Rouge', 'img\\Characters\\Athena\\BtlFace - Copie.png'),
	(8, 'Azura', 'Infanterie', 36, 31, 33, 21, 28, 1, 'Physique', 'Bleu', 'img\\Characters\\Azura\\BtlFace - Copie.png');
/*!40000 ALTER TABLE `personnage` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
