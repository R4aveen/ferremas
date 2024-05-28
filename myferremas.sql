-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-05-2024 a las 04:33:32
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
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(3, 'bodeguero'),
(2, 'cliente'),
(4, 'contador'),
(5, 'despachador'),
(1, 'vendedor');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add categoria producto', 7, 'add_categoriaproducto'),
(26, 'Can change categoria producto', 7, 'change_categoriaproducto'),
(27, 'Can delete categoria producto', 7, 'delete_categoriaproducto'),
(28, 'Can view categoria producto', 7, 'view_categoriaproducto'),
(29, 'Can add producto', 8, 'add_producto'),
(30, 'Can change producto', 8, 'change_producto'),
(31, 'Can delete producto', 8, 'delete_producto'),
(32, 'Can view producto', 8, 'view_producto'),
(33, 'Can add producto oferta', 9, 'add_productooferta'),
(34, 'Can change producto oferta', 9, 'change_productooferta'),
(35, 'Can delete producto oferta', 9, 'delete_productooferta'),
(36, 'Can view producto oferta', 9, 'view_productooferta'),
(37, 'Can add carrito', 10, 'add_carrito'),
(38, 'Can change carrito', 10, 'change_carrito'),
(39, 'Can delete carrito', 10, 'delete_carrito'),
(40, 'Can view carrito', 10, 'view_carrito'),
(41, 'Can add carrito item', 11, 'add_carritoitem'),
(42, 'Can change carrito item', 11, 'change_carritoitem'),
(43, 'Can delete carrito item', 11, 'delete_carritoitem'),
(44, 'Can view carrito item', 11, 'view_carritoitem'),
(45, 'Can add boleta', 12, 'add_boleta'),
(46, 'Can change boleta', 12, 'change_boleta'),
(47, 'Can delete boleta', 12, 'delete_boleta'),
(48, 'Can view boleta', 12, 'view_boleta'),
(49, 'Can add detalle boleta', 13, 'add_detalleboleta'),
(50, 'Can change detalle boleta', 13, 'change_detalleboleta'),
(51, 'Can delete detalle boleta', 13, 'delete_detalleboleta'),
(52, 'Can view detalle boleta', 13, 'view_detalleboleta'),
(53, 'Can add tipo producto', 14, 'add_tipoproducto'),
(54, 'Can change tipo producto', 14, 'change_tipoproducto'),
(55, 'Can delete tipo producto', 14, 'delete_tipoproducto'),
(56, 'Can view tipo producto', 14, 'view_tipoproducto'),
(57, 'Can add pedido', 15, 'add_pedido'),
(58, 'Can change pedido', 15, 'change_pedido'),
(59, 'Can delete pedido', 15, 'delete_pedido'),
(60, 'Can view pedido', 15, 'view_pedido'),
(61, 'Can add detalle pedido', 16, 'add_detallepedido'),
(62, 'Can change detalle pedido', 16, 'change_detallepedido'),
(63, 'Can delete detalle pedido', 16, 'delete_detallepedido'),
(64, 'Can view detalle pedido', 16, 'view_detallepedido');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$cpuv6oxHkF1oW4979usc5w$0Vg432ULYgKS7FVo/OR/l7Wx4T9yLc2o+8ZPWd2emv0=', '2024-05-28 02:03:01.486528', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2024-05-27 04:43:52.544346'),
(2, 'pbkdf2_sha256$720000$C61ZFvTNhih85fS9dOckLt$6rIoXbWCDZGB4WZZkzt+i1kOrX6TJ/zEbX2IqvhH8mA=', '2024-05-28 02:27:18.977689', 0, 'vendedor', '', '', '', 0, 1, '2024-05-27 05:06:28.000000'),
(3, 'pbkdf2_sha256$720000$bazaiXjtJNhoVyrsxQVxYc$zAHLUMIxofNqptlPn2GxFA8+OCfqs7Qo7deEpuvVoGs=', '2024-05-28 02:27:37.495259', 0, 'bodeguero', '', '', '', 0, 1, '2024-05-27 05:06:50.000000'),
(4, 'pbkdf2_sha256$720000$bXfmZK9FOZqxN7uYLIRG7r$9lC2fA2lbHu83HxiEGfIbVnIgz/mXUfcgxb6bxfLWYw=', NULL, 0, 'contador', '', '', '', 0, 1, '2024-05-27 05:07:03.000000'),
(5, 'pbkdf2_sha256$720000$SflIiPXB3u85EjcBNn5sC5$sTV6EF4W7zEvnKtRTW+Owhpwg1Dp6TYZ4rRV8k49woI=', '2024-05-28 02:27:57.731138', 0, 'despachador', '', '', '', 0, 1, '2024-05-27 05:09:18.000000'),
(6, 'pbkdf2_sha256$720000$kXlsJt1wGE6BzDwra2bfl6$bbvJWrT0V1vFvKJ1VC/YPwjX7UmwnoHRea06MtWLGgk=', '2024-05-28 02:04:29.146829', 0, 'cliente', '', '', 'car.pardo@duocuc.cl', 0, 1, '2024-05-27 23:21:24.000000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(3, 2, 1),
(1, 3, 3),
(2, 4, 4),
(4, 5, 5),
(5, 6, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-05-27 04:44:59.022813', '1', 'asdasd', 1, '[{\"added\": {}}]', 7, 1),
(2, '2024-05-27 04:45:04.854519', '1', 'asd', 1, '[{\"added\": {}}]', 14, 1),
(3, '2024-05-27 04:45:17.390481', '1', 'asdasd', 1, '[{\"added\": {}}]', 8, 1),
(4, '2024-05-27 04:45:38.542515', '1', 'asdasd', 3, '', 8, 1),
(5, '2024-05-27 04:45:45.237180', '1', 'asdasd', 3, '', 7, 1),
(6, '2024-05-27 04:45:55.227621', '1', 'asd', 3, '', 14, 1),
(7, '2024-05-27 05:05:40.084678', '1', 'vendedores', 1, '[{\"added\": {}}]', 3, 1),
(8, '2024-05-27 05:05:44.811929', '2', 'clientes', 1, '[{\"added\": {}}]', 3, 1),
(9, '2024-05-27 05:05:51.172691', '3', 'bodeguero', 1, '[{\"added\": {}}]', 3, 1),
(10, '2024-05-27 05:06:06.554667', '4', 'contador', 1, '[{\"added\": {}}]', 3, 1),
(11, '2024-05-27 05:06:31.011675', '2', 'vendedor', 1, '[{\"added\": {}}]', 4, 1),
(12, '2024-05-27 05:06:52.839779', '3', 'bodeguero', 1, '[{\"added\": {}}]', 4, 1),
(13, '2024-05-27 05:07:05.722772', '4', 'contador', 1, '[{\"added\": {}}]', 4, 1),
(14, '2024-05-27 05:07:24.740501', '3', 'bodeguero', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(15, '2024-05-27 05:07:36.617113', '4', 'contador', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(16, '2024-05-27 05:07:47.563693', '2', 'vendedor', 2, '[]', 4, 1),
(17, '2024-05-27 05:08:42.424078', '1', 'vendedor', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 3, 1),
(18, '2024-05-27 05:09:02.472689', '5', 'despachador', 1, '[{\"added\": {}}]', 3, 1),
(19, '2024-05-27 05:09:20.954938', '5', 'despachador', 1, '[{\"added\": {}}]', 4, 1),
(20, '2024-05-27 05:09:32.109652', '2', 'vendedor', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(21, '2024-05-27 05:09:55.291306', '5', 'despachador', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(22, '2024-05-27 23:21:03.052591', '2', 'cliente', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 3, 1),
(23, '2024-05-27 23:21:25.786795', '6', 'cliente', 1, '[{\"added\": {}}]', 4, 1),
(24, '2024-05-27 23:21:35.554419', '6', 'cliente', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(25, '2024-05-27 23:26:10.335783', '6', 'cliente', 2, '[{\"changed\": {\"fields\": [\"Email address\"]}}]', 4, 1),
(26, '2024-05-27 23:44:22.843268', '2', 'Pedido 2 - cliente - entregado', 3, '', 15, 1),
(27, '2024-05-27 23:47:23.327014', '4', 'Pedido 4 - cliente - pendiente de pago', 3, '', 15, 1),
(28, '2024-05-27 23:50:26.570104', '5', 'Pedido 5 - cliente - pendiente de pago', 3, '', 15, 1),
(29, '2024-05-27 23:57:03.572457', '7', 'Pedido 7 - cliente - pendiente de pago', 3, '', 15, 1),
(30, '2024-05-27 23:59:11.912585', '8', 'Pedido 8 - cliente - pendiente de pago', 3, '', 15, 1),
(31, '2024-05-28 00:02:40.978916', '9', 'Pedido 9 - cliente - pendiente de pago', 3, '', 15, 1),
(32, '2024-05-28 00:05:30.816906', '11', 'Pedido 11 - cliente - pendiente de pago', 3, '', 15, 1),
(33, '2024-05-28 00:13:42.751191', '12', 'Pedido 12 - cliente - preparando', 3, '', 15, 1),
(34, '2024-05-28 00:42:45.942392', '13', 'Pedido 13 - cliente - entregado', 3, '', 15, 1),
(35, '2024-05-28 00:47:22.696373', '14', 'Pedido 14 - cliente - aprobado', 3, '', 15, 1),
(36, '2024-05-28 02:03:09.187466', '18', 'Pedido 18 - cliente - aprobado', 3, '', 15, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(12, 'web_ferremas', 'boleta'),
(10, 'web_ferremas', 'carrito'),
(11, 'web_ferremas', 'carritoitem'),
(7, 'web_ferremas', 'categoriaproducto'),
(13, 'web_ferremas', 'detalleboleta'),
(16, 'web_ferremas', 'detallepedido'),
(15, 'web_ferremas', 'pedido'),
(8, 'web_ferremas', 'producto'),
(9, 'web_ferremas', 'productooferta'),
(14, 'web_ferremas', 'tipoproducto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-05-27 04:39:06.471726'),
(2, 'auth', '0001_initial', '2024-05-27 04:39:16.358843'),
(3, 'admin', '0001_initial', '2024-05-27 04:39:19.325508'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-05-27 04:39:19.379503'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-05-27 04:39:19.422558'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-05-27 04:39:20.354312'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-05-27 04:39:21.290030'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-05-27 04:39:21.543034'),
(9, 'auth', '0004_alter_user_username_opts', '2024-05-27 04:39:21.603027'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-05-27 04:39:22.412445'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-05-27 04:39:22.458478'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-05-27 04:39:22.540774'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-05-27 04:39:22.680769'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-05-27 04:39:22.824772'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-05-27 04:39:23.007771'),
(16, 'auth', '0011_update_proxy_permissions', '2024-05-27 04:39:23.065771'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-05-27 04:39:23.272774'),
(18, 'sessions', '0001_initial', '2024-05-27 04:39:23.980815'),
(19, 'web_ferremas', '0001_initial', '2024-05-27 04:39:26.554714'),
(20, 'web_ferremas', '0002_carrito_carritoitem', '2024-05-27 04:39:30.072673'),
(21, 'web_ferremas', '0003_boleta_detalleboleta', '2024-05-27 04:39:32.981517'),
(22, 'web_ferremas', '0004_tipoproducto_remove_producto_categoria_producto_tipo_and_more', '2024-05-27 04:39:42.732807'),
(23, 'web_ferremas', '0005_pedido_detallepedido', '2024-05-27 04:39:49.310552'),
(24, 'web_ferremas', '0006_boleta_usuario', '2024-05-27 04:39:51.547540'),
(25, 'web_ferremas', '0007_carrito_pedido_aprobado', '2024-05-27 04:39:51.917428'),
(26, 'web_ferremas', '0008_alter_pedido_estado', '2024-05-27 04:39:52.242982'),
(27, 'web_ferremas', '0010_auto_20240526_2335', '2024-05-27 04:39:52.324138'),
(28, 'web_ferremas', '0009_pedido_payment_token_alter_pedido_estado', '2024-05-27 04:39:52.629140'),
(29, 'web_ferremas', '0011_merge_20240526_2339', '2024-05-27 04:39:52.674134');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('260xgl0g2z66jteby4oy4qcbysgaxezu', '.eJxVjEEOgjAQRe_StWlCx4HWpXvP0Ez_TAQ1kFBYEe-uJCx0-997f3NZ1qXPa7U5D-oujt3pdyuCp4070IeM98ljGpd5KH5X_EGrv01qr-vh_h30UvtvLazRGlNiS9QFTaQSQ2pROAYIGOeGgVK0CRFExAVMhojUps7g3h_-HTig:1sBmZB:1TBntr8k-FgUE5if3RkEqtErqshD-EOvEehJkVJ49-A', '2024-06-11 02:27:57.787091'),
('kgv18sqgks4x01n8ewx1emqvobccehb0', '.eJxVjEEOwiAQRe_C2hCm7RRw6b5naGYGsFUDSWlXxrsbki50-997_61mOvZlPmrc5jWoq-rU5XdjkmfMDYQH5XvRUvK-raybok9a9VRCfN1O9-9gobq0GpAhdtwhGPEpSiIaDEpIxBKCtei9BWccuH6gES3EUQB71zNbTk59vv2WODA:1sBmBs:qWZ-WFrdY0csFhCWOiKkDyxj9tLTO5TRZNRva-nmedc', '2024-06-11 02:03:52.196139'),
('kz2o8wv5vhkt36uhliwm9x4oz72ga3lb', '.eJxVjEEOwiAQRe_C2hAHKjO4dO8ZCANTqRpISrsy3l2bdKHb_977LxXiupSwdpnDlNVZOXX43Timh9QN5Hust6ZTq8s8sd4UvdOury3L87K7fwcl9vKtiZNDAcjojyjWsTD6xGiBvPAAxBDJ2xGIEg3OMpuTAUwyymBsdur9AeNmN7w:1sBmCZ:gisRBwIn1SyspxaQVGQVs4ICsLJqUEg6uZBb50zx-gE', '2024-06-11 02:04:35.051558'),
('wjul9x0zqk8cu74nstfstc86nte0jb3w', '.eJxVjEEOgjAQRe_StWlCx4HWpXvP0Ez_TAQ1kFBYEe-uJCx0-997f3NZ1qXPa7U5D-oujt3pdyuCp4070IeM98ljGpd5KH5X_EGrv01qr-vh_h30UvtvLazRGlNiS9QFTaQSQ2pROAYIGOeGgVK0CRFExAVMhojUps7g3h_-HTig:1sBTBr:cognCiTAYJcb7xpyEfX4b3iPoCFtTvLW6UI8NxJY778', '2024-06-10 05:46:35.296113'),
('x5jxpwkbucgb39eebmrh2ojlznef9h03', '.eJxVjEEOwiAQRe_C2hCm7RRw6b5naGYGsFUDSWlXxrsbki50-997_61mOvZlPmrc5jWoq-rU5XdjkmfMDYQH5XvRUvK-raybok9a9VRCfN1O9-9gobq0GpAhdtwhGPEpSiIaDEpIxBKCtei9BWccuH6gES3EUQB71zNbTk59vv2WODA:1sBjd0:xLtUnlj7ffEd9E8RKb_XXZsKbbLJfePR8ydzMYqhpv4', '2024-06-10 23:19:42.916501');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `web_ferremas_boleta`
--

CREATE TABLE `web_ferremas_boleta` (
  `id` bigint(20) NOT NULL,
  `total` int(10) UNSIGNED NOT NULL CHECK (`total` >= 0),
  `fecha` datetime(6) NOT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `web_ferremas_boleta`
--


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `web_ferremas_carrito`
--

CREATE TABLE `web_ferremas_carrito` (
  `id` bigint(20) NOT NULL,
  `creado_en` datetime(6) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `pedido_aprobado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `web_ferremas_carrito`
--

INSERT INTO `web_ferremas_carrito` (`id`, `creado_en`, `usuario_id`, `pedido_aprobado`) VALUES
(1, '2024-05-27 05:04:00.836995', 1, 0),
(2, '2024-05-27 05:16:16.340684', 2, 0),
(3, '2024-05-27 23:22:14.797777', 6, 0),
(4, '2024-05-27 23:27:51.659281', 5, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `web_ferremas_carritoitem`
--

CREATE TABLE `web_ferremas_carritoitem` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(10) UNSIGNED NOT NULL CHECK (`cantidad` >= 0),
  `precio` decimal(10,2) NOT NULL,
  `carrito_id` bigint(20) NOT NULL,
  `producto_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `web_ferremas_categoriaproducto`
--

CREATE TABLE `web_ferremas_categoriaproducto` (
  `id` int(11) NOT NULL,
  `categoria` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `web_ferremas_categoriaproducto`
--

INSERT INTO `web_ferremas_categoriaproducto` (`id`, `categoria`) VALUES
(1, 'Puertas'),
(2, 'Herramientas'),
(3, 'Herramientas chicas'),
(4, 'Seguridad'),
(5, 'Sets'),
(6, 'Construcción');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `web_ferremas_detalleboleta`
--

CREATE TABLE `web_ferremas_detalleboleta` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(10) UNSIGNED NOT NULL CHECK (`cantidad` >= 0),
  `subtotal` int(10) UNSIGNED NOT NULL CHECK (`subtotal` >= 0),
  `boleta_id` bigint(20) NOT NULL,
  `producto_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `web_ferremas_detalleboleta`
--



-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `web_ferremas_detallepedido`
--

CREATE TABLE `web_ferremas_detallepedido` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(10) UNSIGNED NOT NULL CHECK (`cantidad` >= 0),
  `precio` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `producto_id` int(11) NOT NULL,
  `pedido_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `web_ferremas_pedido`
--

CREATE TABLE `web_ferremas_pedido` (
  `id` bigint(20) NOT NULL,
  `estado` varchar(20) NOT NULL,
  `creado_en` datetime(6) NOT NULL,
  `actualizado_en` datetime(6) NOT NULL,
  `direccion_envio` varchar(255) DEFAULT NULL,
  `metodo_pago` varchar(50) DEFAULT NULL,
  `carrito_id` bigint(20) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `payment_token` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
(1, 'Martillo', 100, 991, 'Martillo de construcción', 'productos/11.jpg', 0),
(2, 'Cincel', 100, 991, 'Cincel para albañilería', 'productos/400.webp', 0),
(3, 'Casco', 100, 994, 'casco azul', 'productos/4.jpg', 1),
(4, 'Set de alicates', 1000, 998, 'set de alicates todo tipos', 'productos/3.jpg', 1),
(5, 'Taladro', 1000, 997, 'taladro eléctrico inalámbrico', 'productos/5.jpg', 0),
(6, 'Sierra', 1000, 997, 'sierra electrica', 'productos/6.jpg', 0),
(7, 'Nivelador', 1000, 999, 'Nivelador laser', 'productos/1.jpg', 0),
(8, 'Huincha', 1000, 997, 'huincha de medir', 'productos/8.jpg', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `web_ferremas_productooferta`
--

CREATE TABLE `web_ferremas_productooferta` (
  `producto_id` int(11) NOT NULL,
  `precio_oferta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `web_ferremas_producto_categoria`
--

CREATE TABLE `web_ferremas_producto_categoria` (
  `id` bigint(20) NOT NULL,
  `producto_id` int(11) NOT NULL,
  `categoriaproducto_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `web_ferremas_producto_categoria`
--

INSERT INTO `web_ferremas_producto_categoria` (`id`, `producto_id`, `categoriaproducto_id`) VALUES
(1, 3, 2),
(2, 3, 3),
(3, 3, 4),
(4, 4, 2),
(5, 4, 3),
(6, 4, 5),
(7, 5, 2),
(8, 5, 6),
(9, 6, 2),
(10, 6, 6),
(11, 7, 2),
(12, 7, 3),
(13, 7, 6),
(14, 8, 2),
(15, 8, 3),
(16, 8, 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `web_ferremas_producto_tipo`
--

CREATE TABLE `web_ferremas_producto_tipo` (
  `id` bigint(20) NOT NULL,
  `producto_id` int(11) NOT NULL,
  `tipoproducto_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `web_ferremas_producto_tipo`
--

INSERT INTO `web_ferremas_producto_tipo` (`id`, `producto_id`, `tipoproducto_id`) VALUES
(1, 3, 1),
(2, 3, 2),
(3, 4, 3),
(4, 4, 4),
(5, 5, 2),
(6, 5, 5),
(7, 6, 6),
(8, 7, 1),
(9, 7, 2),
(10, 7, 4),
(11, 7, 6),
(12, 8, 1),
(13, 8, 2),
(14, 8, 4),
(15, 8, 5),
(16, 8, 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `web_ferremas_tipoproducto`
--

CREATE TABLE `web_ferremas_tipoproducto` (
  `id` int(11) NOT NULL,
  `tipo` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `web_ferremas_tipoproducto`
--

INSERT INTO `web_ferremas_tipoproducto` (`id`, `tipo`) VALUES
(1, 'albañileria'),
(2, 'carpinteria'),
(3, 'gafiteria'),
(4, 'otros'),
(5, 'electrico'),
(6, 'metalica');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `web_ferremas_boleta`
--
ALTER TABLE `web_ferremas_boleta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `web_ferremas_boleta_usuario_id_f45b4921_fk_auth_user_id` (`usuario_id`);

--
-- Indices de la tabla `web_ferremas_carrito`
--
ALTER TABLE `web_ferremas_carrito`
  ADD PRIMARY KEY (`id`),
  ADD KEY `web_ferremas_carrito_usuario_id_80fd5f92_fk_auth_user_id` (`usuario_id`);

--
-- Indices de la tabla `web_ferremas_carritoitem`
--
ALTER TABLE `web_ferremas_carritoitem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `web_ferremas_carrito_carrito_id_ca8dc819_fk_web_ferre` (`carrito_id`),
  ADD KEY `web_ferremas_carrito_producto_id_600f9564_fk_web_ferre` (`producto_id`);

--
-- Indices de la tabla `web_ferremas_categoriaproducto`
--
ALTER TABLE `web_ferremas_categoriaproducto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `web_ferremas_detalleboleta`
--
ALTER TABLE `web_ferremas_detalleboleta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `web_ferremas_detalle_boleta_id_f1c6f682_fk_web_ferre` (`boleta_id`),
  ADD KEY `web_ferremas_detalle_producto_id_d90252a0_fk_web_ferre` (`producto_id`);

--
-- Indices de la tabla `web_ferremas_detallepedido`
--
ALTER TABLE `web_ferremas_detallepedido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `web_ferremas_detalle_producto_id_17be69cc_fk_web_ferre` (`producto_id`),
  ADD KEY `web_ferremas_detalle_pedido_id_0040d00b_fk_web_ferre` (`pedido_id`);

--
-- Indices de la tabla `web_ferremas_pedido`
--
ALTER TABLE `web_ferremas_pedido`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `carrito_id` (`carrito_id`),
  ADD KEY `web_ferremas_pedido_usuario_id_d888a156_fk_auth_user_id` (`usuario_id`);

--
-- Indices de la tabla `web_ferremas_producto`
--
ALTER TABLE `web_ferremas_producto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `web_ferremas_productooferta`
--
ALTER TABLE `web_ferremas_productooferta`
  ADD PRIMARY KEY (`producto_id`);

--
-- Indices de la tabla `web_ferremas_producto_categoria`
--
ALTER TABLE `web_ferremas_producto_categoria`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `web_ferremas_producto_ca_producto_id_categoriapro_e6d82a90_uniq` (`producto_id`,`categoriaproducto_id`),
  ADD KEY `web_ferremas_product_categoriaproducto_id_6b989beb_fk_web_ferre` (`categoriaproducto_id`);

--
-- Indices de la tabla `web_ferremas_producto_tipo`
--
ALTER TABLE `web_ferremas_producto_tipo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `web_ferremas_producto_ti_producto_id_tipoproducto_c4e2e1f2_uniq` (`producto_id`,`tipoproducto_id`),
  ADD KEY `web_ferremas_product_tipoproducto_id_d3bfbc9a_fk_web_ferre` (`tipoproducto_id`);

--
-- Indices de la tabla `web_ferremas_tipoproducto`
--
ALTER TABLE `web_ferremas_tipoproducto`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `web_ferremas_boleta`
--
ALTER TABLE `web_ferremas_boleta`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `web_ferremas_carrito`
--
ALTER TABLE `web_ferremas_carrito`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `web_ferremas_carritoitem`
--
ALTER TABLE `web_ferremas_carritoitem`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `web_ferremas_categoriaproducto`
--
ALTER TABLE `web_ferremas_categoriaproducto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `web_ferremas_detalleboleta`
--
ALTER TABLE `web_ferremas_detalleboleta`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `web_ferremas_detallepedido`
--
ALTER TABLE `web_ferremas_detallepedido`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de la tabla `web_ferremas_pedido`
--
ALTER TABLE `web_ferremas_pedido`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `web_ferremas_producto`
--
ALTER TABLE `web_ferremas_producto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `web_ferremas_producto_categoria`
--
ALTER TABLE `web_ferremas_producto_categoria`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `web_ferremas_producto_tipo`
--
ALTER TABLE `web_ferremas_producto_tipo`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `web_ferremas_tipoproducto`
--
ALTER TABLE `web_ferremas_tipoproducto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `web_ferremas_boleta`
--
ALTER TABLE `web_ferremas_boleta`
  ADD CONSTRAINT `web_ferremas_boleta_usuario_id_f45b4921_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `web_ferremas_carrito`
--
ALTER TABLE `web_ferremas_carrito`
  ADD CONSTRAINT `web_ferremas_carrito_usuario_id_80fd5f92_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `web_ferremas_carritoitem`
--
ALTER TABLE `web_ferremas_carritoitem`
  ADD CONSTRAINT `web_ferremas_carrito_carrito_id_ca8dc819_fk_web_ferre` FOREIGN KEY (`carrito_id`) REFERENCES `web_ferremas_carrito` (`id`),
  ADD CONSTRAINT `web_ferremas_carrito_producto_id_600f9564_fk_web_ferre` FOREIGN KEY (`producto_id`) REFERENCES `web_ferremas_producto` (`id`);

--
-- Filtros para la tabla `web_ferremas_detalleboleta`
--
ALTER TABLE `web_ferremas_detalleboleta`
  ADD CONSTRAINT `web_ferremas_detalle_boleta_id_f1c6f682_fk_web_ferre` FOREIGN KEY (`boleta_id`) REFERENCES `web_ferremas_boleta` (`id`),
  ADD CONSTRAINT `web_ferremas_detalle_producto_id_d90252a0_fk_web_ferre` FOREIGN KEY (`producto_id`) REFERENCES `web_ferremas_producto` (`id`);

--
-- Filtros para la tabla `web_ferremas_detallepedido`
--
ALTER TABLE `web_ferremas_detallepedido`
  ADD CONSTRAINT `web_ferremas_detalle_pedido_id_0040d00b_fk_web_ferre` FOREIGN KEY (`pedido_id`) REFERENCES `web_ferremas_pedido` (`id`),
  ADD CONSTRAINT `web_ferremas_detalle_producto_id_17be69cc_fk_web_ferre` FOREIGN KEY (`producto_id`) REFERENCES `web_ferremas_producto` (`id`);

--
-- Filtros para la tabla `web_ferremas_pedido`
--
ALTER TABLE `web_ferremas_pedido`
  ADD CONSTRAINT `web_ferremas_pedido_carrito_id_52d92486_fk_web_ferre` FOREIGN KEY (`carrito_id`) REFERENCES `web_ferremas_carrito` (`id`),
  ADD CONSTRAINT `web_ferremas_pedido_usuario_id_d888a156_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `web_ferremas_productooferta`
--
ALTER TABLE `web_ferremas_productooferta`
  ADD CONSTRAINT `web_ferremas_product_producto_id_4d8f3cd4_fk_web_ferre` FOREIGN KEY (`producto_id`) REFERENCES `web_ferremas_producto` (`id`);

--
-- Filtros para la tabla `web_ferremas_producto_categoria`
--
ALTER TABLE `web_ferremas_producto_categoria`
  ADD CONSTRAINT `web_ferremas_product_categoriaproducto_id_6b989beb_fk_web_ferre` FOREIGN KEY (`categoriaproducto_id`) REFERENCES `web_ferremas_categoriaproducto` (`id`),
  ADD CONSTRAINT `web_ferremas_product_producto_id_e5d16f9f_fk_web_ferre` FOREIGN KEY (`producto_id`) REFERENCES `web_ferremas_producto` (`id`);

--
-- Filtros para la tabla `web_ferremas_producto_tipo`
--
ALTER TABLE `web_ferremas_producto_tipo`
  ADD CONSTRAINT `web_ferremas_product_producto_id_e5f50cf8_fk_web_ferre` FOREIGN KEY (`producto_id`) REFERENCES `web_ferremas_producto` (`id`),
  ADD CONSTRAINT `web_ferremas_product_tipoproducto_id_d3bfbc9a_fk_web_ferre` FOREIGN KEY (`tipoproducto_id`) REFERENCES `web_ferremas_tipoproducto` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
