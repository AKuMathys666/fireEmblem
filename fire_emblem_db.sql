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
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=latin1;

-- Export de données de la table fire_emblem_db.personnage : ~49 rows (environ)
/*!40000 ALTER TABLE `personnage` DISABLE KEYS */;
INSERT INTO `personnage` (`id`, `nom`, `type_deplacement`, `hp`, `atk`, `vit`, `def`, `res`, `portee`, `type_attaque`, `couleur`, `image`) VALUES
	(1, 'Abel', 'Cavalier', 39, 41, 27, 25, 25, 1, 'Physique', 'Bleu', 'img\\Characters\\Abel\\BtlFace - Copie.png'),
	(2, 'Alfonse', 'Infanterie', 43, 51, 25, 32, 22, 1, 'Physique', 'Rouge', 'img\\Characters\\Alfonse\\BtlFace - Copie.png'),
	(3, 'Alm', 'Infanterie', 45, 49, 30, 28, 22, 1, 'Physique', 'Rouge', 'img\\Characters\\Alm\\BtlFace - Copie.png'),
	(4, 'Amelia', 'Tank', 47, 48, 34, 35, 23, 1, 'Physique', 'Vert', 'img\\Characters\\Amelia\\BtlFace - Copie.png'),
	(5, 'Anna', 'Infanterie', 41, 45, 38, 22, 28, 1, 'Physique', 'Vert', 'img\\Characters\\Anna\\BtlFace - Copie.png'),
	(6, 'Arthur', 'Infanterie', 43, 45, 29, 30, 24, 1, 'Physique', 'Vert', 'img\\Characters\\Arthur\\BtlFace - Copie.png'),
	(7, 'Athena', 'Infanterie', 36, 44, 38, 27, 24, 1, 'Physique', 'Rouge', 'img\\Characters\\Athena\\BtlFace - Copie.png'),
	(8, 'Azura', 'Infanterie', 36, 43, 33, 21, 28, 1, 'Physique', 'Bleu', 'img\\Characters\\Azura\\BtlFace - Copie.png'),
	(9, 'Azura - Performing', 'Infanterie', 35, 48, 34, 20, 28, 1, 'Physique', 'Vert', 'img\\Characters\\Azura - Dancer\\BtlFace - Copie.png'),
	(10, 'Azama', 'Infanterie', 43, 31, 26, 32, 25, 2, 'Magique', 'Gris', 'img\\Characters\\Azama\\BtlFace - Copie.png'),
	(11, 'Barst', 'Infanterie', 46, 41, 27, 30, 17, 1, 'Physique', 'Vert', 'img\\Characters\\Barst\\BtlFace - Copie.png'),
	(12, 'Bartre', 'Infanterie', 49, 48, 25, 33, 13, 1, 'Physique', 'Vert', 'img\\Characters\\Bartre\\BtlFace - Copie.png'),
	(13, 'Berkut', 'Cavalier', 43, 48, 22, 31, 24, 1, 'Physique', 'Bleu', 'img\\Characters\\Berkut\\BtlFace - Copie.png'),
	(14, 'Beruka', 'Flier', 46, 40, 23, 37, 22, 1, 'Physique', 'Vert', 'img\\Characters\\Beruka\\BtlFace - Copie.png'),
	(15, 'Black Knight', 'Tank', 48, 50, 34, 35, 18, 1, 'Physique', 'Rouge', 'img\\Characters\\Black Knight\\BtlFace - Copie.png'),
	(16, 'Boey', 'Infanterie', 43, 39, 27, 32, 18, 2, 'Magique', 'Vert', 'img\\Characters\\Boey\\BtlFace - Copie.png'),
	(17, 'Caeda', 'Flier', 36, 43, 32, 24, 34, 1, 'Physique', 'Rouge', 'img\\Characters\\Caeda\\BtlFace - Copie.png'),
	(18, 'Caeda-Bride', 'Infanterie', 33, 41, 37, 19, 30, 2, 'Magique', 'Bleu', 'img\\Characters\\Caeda - Bride\\BtlFace - Copie.png'),
	(19, 'Cain', 'Cavalier', 42, 40, 27, 27, 21, 1, 'Physique', 'Rouge', 'img\\Characters\\Cain\\BtlFace - Copie.png'),
	(20, 'Camilla', 'Flier', 37, 38, 27, 28, 31, 1, 'Physique', 'Vert', 'img\\Characters\\Camilla\\BtlFace - Copie.png'),
	(21, 'Camilla - Spring', 'Flier', 39, 46, 28, 30, 19, 2, 'Magique', 'Vert', 'img\\Characters\\Camilla - Spring\\BtlFace - Copie.png'),
	(22, 'Camus', 'Cavalier', 42, 48, 33, 31, 17, 1, 'Physique', 'Bleu', 'img\\Characters\\Camus\\BtlFace - Copie.png'),
	(23, 'Catria', 'Flier', 39, 42, 34, 29, 25, 1, 'Physique', 'Bleu', 'img\\Characters\\Catria\\BtlFace - Copie.png'),
	(24, 'Cecilia', 'Cavalier', 36, 43, 25, 22, 29, 2, 'Magique', 'Vert', 'img\\Characters\\Cecilia\\BtlFace - Copie.png'),
	(25, 'Celica', 'Infanterie', 39, 46, 33, 22, 22, 2, 'Magique', 'Rouge', 'img\\Characters\\Celica\\BtlFace - Copie.png'),
	(26, 'Charlotte - Bride', 'Infanterie', 46, 36, 32, 24, 19, 1, 'Physique', 'Bleu', 'img\\Characters\\Charlotte - Bride\\BtlFace - Copie.png'),
	(27, 'Cherche', 'Flier', 46, 50, 25, 32, 16, 1, 'Physique', 'Vert', 'img\\Characters\\Cherche\\BtlFace - Copie.png'),
	(28, 'Chrom', 'Infanterie', 47, 53, 25, 31, 17, 1, 'Physique', 'Rouge', 'img\\Characters\\Chrom\\BtlFace - Copie.png'),
	(29, 'Chrom - Spring', 'Infanterie', 43, 48, 32, 28, 20, 1, 'Physique', 'Vert', 'img\\Characters\\Chrom - Spring\\BtlFace - Copie.png'),
	(30, 'Clair', 'Flier', 37, 41, 36, 24, 33, 1, 'Physique', 'Bleu', 'img\\Characters\\Clair\\BtlFace - Copie.png'),
	(31, 'Clarine', 'Cavalier', 35, 35, 33, 22, 29, 2, 'Magique', 'Gris', 'img\\Characters\\Clarine\\BtlFace - Copie.png'),
	(32, 'Clarisse', 'Infanterie', 37, 42, 34, 25, 20, 2, 'Physique', 'Gris', 'img\\Characters\\Clarisse\\BtlFace - Copie.png'),
	(33, 'Clive', 'Cavalier', 46, 33, 25, 32, 19, 1, 'Physique', 'Bleu', 'img\\Characters\\Clive\\BtlFace - Copie.png'),
	(34, 'Cordelia', 'Flier', 40, 35, 30, 22, 25, 1, 'Physique', 'Bleu', 'img\\Characters\\Cordelia\\BtlFace - Copie.png'),
	(35, 'Cordelia - Bride', 'Infanterie', 36, 47, 35, 19, 22, 2, 'Physique', 'Gris', 'img\\Characters\\Cordelia - Bride\\BtlFace - Copie.png'),
	(36, 'Corrifn F', 'Infanterie', 41, 40, 34, 34, 21, 1, 'Magique', 'Bleu', 'img\\Characters\\Corrin F\\BtlFace - Copie.png'),
	(37, 'Corrin F - Summer', 'Flier', 34, 44, 34, 22, 26, 2, 'Magique', 'Bleu', 'img\\Characters\\Corrin F - Summer\\BtlFace - Copie.png'),
	(38, 'Delthea', 'Infanterie', 33, 50, 34, 13, 31, 2, 'Magique', 'Bleu', 'img\\Characters\\Delthea\\BtlFace - Copie.png'),
	(39, 'Donnel', 'Infanterie', 43, 43, 24, 32, 23, 1, 'Physique', 'Bleu', 'img\\Characters\\Donnel\\BtlFace - Copie.png'),
	(40, 'Draug', 'Tank', 50, 38, 27, 39, 18, 1, 'Physique', 'Rouge', 'img\\Characters\\Draug\\BtlFace - Copie.png'),
	(41, 'Effie', 'Tank', 50, 55, 22, 33, 23, 1, 'Physique', 'Bleu', 'img\\Characters\\Effie\\BtlFace - Copie.png'),
	(42, 'Eirika', 'Infanterie', 42, 42, 35, 26, 28, 1, 'Physique', 'Rouge', 'img\\Characters\\Eirika\\BtlFace - Copie.png'),
	(43, 'Eldigan', 'Cavalier', 45, 32, 24, 34, 19, 1, 'Physique', 'Rouge', 'img\\Characters\\Eldigan\\BtlFace - Copie.png'),
	(44, 'Elincia', 'Flier', 35, 45, 36, 24, 27, 1, 'Physique', 'Rouge', 'img\\Characters\\Elincia\\BtlFace - Copie.png'),
	(45, 'Elise', 'Cavalier', 30, 42, 32, 19, 32, 2, 'Magique', 'Gris', 'img\\Characters\\Elise\\BtlFace - Copie.png'),
	(46, 'Elise - Summer', 'Infanterie', 34, 51, 34, 18, 25, 2, 'Magique', 'Vert', 'img\\Characters\\Elise - Summer\\BtlFace - Copie.png'),
	(47, 'Eliwood', 'Cavalier', 39, 47, 30, 23, 32, 1, 'Physique', 'Rouge', 'img\\Characters\\Eliwood\\BtlFace - Copie.png'),
	(48, 'Ephraim', 'Infanterie', 45, 47, 25, 32, 20, 1, 'Physique', 'Bleu', 'img\\Characters\\Ephraim\\BtlFace - Copie.png'),
	(49, 'Est', 'Flier', 36, 47, 30, 24, 32, 1, 'Physique', 'Bleu', 'img\\Characters\\Est\\BtlFace - Copie.png');
/*!40000 ALTER TABLE `personnage` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
