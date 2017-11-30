-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Client :  127.0.0.1
-- Généré le :  Ven 01 Décembre 2017 à 00:23
-- Version du serveur :  5.6.17
-- Version de PHP :  5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `fire_emblem_db`
--
CREATE DATABASE IF NOT EXISTS `fire_emblem_db` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `fire_emblem_db`;

-- --------------------------------------------------------

--
-- Structure de la table `personnage`
--

CREATE TABLE IF NOT EXISTS `personnage` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nom` varchar(32) NOT NULL,
  `type_deplacement` varchar(32) NOT NULL,
  `hp` int(10) NOT NULL,
  `atk` int(10) NOT NULL,
  `vit` int(10) NOT NULL,
  `def` int(10) NOT NULL,
  `res` int(10) NOT NULL,
  `porte` int(10) NOT NULL,
  `type_attack` tinyint(1) NOT NULL,
  `couleur` varchar(32) NOT NULL,
  `image` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `arme` (`porte`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Contenu de la table `personnage`
--

INSERT INTO `personnage` (`id`, `nom`, `type_deplacement`, `hp`, `atk`, `vit`, `def`, `res`, `porte`, `type_attack`, `couleur`, `image`) VALUES
(1, 'Nom1', 'tank', 44, 40, 28, 27, 18, 2, 1, 'red', 'img\\Characters\\Azura - Dancer/BtlFace - Copie.png'),
(2, 'Nom2', 'flier', 38, 41, 40, 20, 30, 2, 0, '', 'img\\Characters\\Azura - Dancer/BtlFace - Copie.png'),
(3, 'Nom3', 'infanterie', 41, 43, 30, 29, 20, 1, 0, '', 'img\\Characters\\Azura - Dancer/BtlFace - Copie.png'),
(4, 'Nom4', 'infanterie', 37, 35, 25, 25, 40, 1, 0, '', 'img\\Characters\\Azura - Dancer/BtlFace - Copie.png'),
(5, 'Nom5', 'infanterie', 50, 45, 32, 18, 22, 1, 0, '', 'img\\Characters\\Athena\\BtlFace - Copie.png'),
(6, 'Nom6', 'cavalier', 36, 38, 36, 25, 28, 1, 0, '', 'img\\Characters\\Athena\\BtlFace - Copie.png'),
(7, 'Nom7', 'cavalier', 47, 36, 25, 23, 30, 2, 1, '', 'img\\Characters\\Athena\\BtlFace - Copie.png'),
(8, 'Nom8', 'flier', 42, 52, 18, 38, 17, 1, 1, '', 'img\\Characters\\Athena\\BtlFace - Copie.png');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
