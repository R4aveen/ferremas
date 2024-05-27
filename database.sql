-- VACIAR O BORRAR LOS DATOS DE ESTAS TABLAS KJSAKSAS
-- primero pasar las imagenes al media/productos

-- PRODUCTOS
INSERT INTO `web_ferremas_producto` (`id`, `nombre`, `precio`, `stock`, `descripcion`, `imagen`, `en_oferta`) VALUES
(1, 'Martillo', 100, 997, 'Martillo de construcción', 'productos/11.jpg', 0),
(2, 'Cincel', 100, 1000, 'Cincel para albañilería', 'productos/400.webp', 0),
(3, 'Casco', 100, 998, 'casco azul', 'productos/4.jpg', 1),
(4, 'Set de alicates', 1000, 999, 'set de alicates todo tipos', 'productos/3.jpg', 1),
(5, 'Taladro', 1000, 1000, 'taladro eléctrico inalámbrico', 'productos/5.jpg', 0),
(6, 'Sierra', 1000, 999, 'sierra electrica', 'productos/6.jpg', 0),
(7, 'Nivelador', 1000, 1000, 'Nivelador laser', 'productos/1.jpg', 0),
(8, 'Huincha', 1000, 999, 'huincha de medir', 'productos/8.jpg', 0);

-- CATEGORIAS DE LOS PRODUCTOS
INSERT INTO `web_ferremas_categoriaproducto` (`id`, `categoria`) VALUES
(1, 'Puertas'),
(2, 'Herramientas'),
(3, 'Herramientas chicas'),
(4, 'Seguridad'),
(5, 'Sets'),
(6, 'Construcción');

-- ESTOS SON LOS TIPOS PRODUCTOS XD
INSERT INTO `web_ferremas_tipoproducto` (`id`, `tipo`) VALUES
(1, 'albañileria'),
(2, 'carpinteria'),
(3, 'gafiteria'),
(4, 'otros'),
(5, 'electrico'),
(6, 'metalica');

-- MUCHO A MUCHOS DE CATPROD A TIPPROD
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

-- AQUI LO MISMO PERO AL REVEZ SAJJSAS
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
