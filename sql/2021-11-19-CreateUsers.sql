CREATE TABLE `user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `username` char(64) NOT NULL DEFAULT '',
  `email` char(120) NOT NULL DEFAULT '',
  `password` char(128) DEFAULT NULL,
  `is_active` smallint NOT NULL DEFAULT '1',
  `last_updated` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
