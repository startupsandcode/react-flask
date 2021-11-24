CREATE TABLE `revoked_tokens` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `token` varchar(256) DEFAULT NULL,
  `expiration` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;