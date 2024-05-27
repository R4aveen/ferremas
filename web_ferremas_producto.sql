-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-05-2024 a las 07:41:12
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `myferremas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `web_ferremas_producto`
--

CREATE TABLE `web_ferremas_producto` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `precio` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  `descripcion` longtext NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `en_oferta` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `web_ferremas_producto`
--

INSERT INTO `web_ferremas_producto` (`id`, `nombre`, `precio`, `stock`, `descripcion`, `imagen`, `en_oferta`) VALUES
(1, 'Martillo', 100, 995, 'Martillo de construcción', 'productos/11.jpg', 0),
(2, 'Cincel', 100, 1000, 'Cincel para albañilería', 'productos/400.webp', 0),
(3, 'Casco', 100, 998, 'casco azul', 'productos/4.jpg', 1),
(4, 'Set de alicates', 1000, 999, 'set de alicates todo tipos', 'productos/3.jpg', 1),
(5, 'Taladro', 1000, 1000, 'taladro eléctrico inalámbrico', 'productos/5.jpg', 0),
(6, 'Sierra', 1000, 999, 'sierra electrica', 'productos/6.jpg', 0),
(7, 'Nivelador', 1000, 1000, 'Nivelador laser', 'productos/1.jpg', 0),
(8, 'Huincha', 1000, 999, 'huincha de medir', 'productos/8.jpg', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `web_ferremas_producto`
--
ALTER TABLE `web_ferremas_producto`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `web_ferremas_producto`
--
ALTER TABLE `web_ferremas_producto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
