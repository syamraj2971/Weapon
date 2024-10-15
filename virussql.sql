/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 10.4.25-MariaDB : Database - videoeliha
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`videoeliha` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `videoeliha`;

/*Table structure for table `emergency` */

DROP TABLE IF EXISTS `emergency`;

CREATE TABLE `emergency` (
  `emergency_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `emergency` varchar(100) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`emergency_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `emergency` */

insert  into `emergency`(`emergency_id`,`user_id`,`emergency`,`latitude`,`longitude`,`status`) values 
(1,1,'ddhf','356765274.46768','353246452156.653','sendsms'),
(2,2,'fjjj','9.976324','76.2862094',NULL),
(3,1,'fjjj','9.9763209','76.2862024','sendsms'),
(4,1,'Weaponn/Violenecedetect','0','0','sendsms'),
(5,1,'Weaponn/Violenecedetect','0','0','sendsms');

/*Table structure for table `images` */

DROP TABLE IF EXISTS `images`;

CREATE TABLE `images` (
  `img_id` int(10) NOT NULL AUTO_INCREMENT,
  `images` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`img_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `images` */

insert  into `images`(`img_id`,`images`) values 
(1,'static/video30a53483-0547-451f-8c45-9cc2e13f9c6b5e8da860a7c3a578a27dabbf431e43ca.png');

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `latitude` varchar(1000) DEFAULT NULL,
  `longitude` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `location` */

insert  into `location`(`location_id`,`user_id`,`latitude`,`longitude`) values 
(6,1,'9.9762938','76.2862323');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'hai','hai','user'),
(5,'hai','hai','police'),
(4,'police','police','police');

/*Table structure for table `police` */

DROP TABLE IF EXISTS `police`;

CREATE TABLE `police` (
  `police_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`police_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `police` */

insert  into `police`(`police_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,4,'user','qwerty','02345678907','student@gmail.com','kerala'),
(2,5,'users','qwertys','ekm','8281940635','ern@gamil.com');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `request` varchar(1000) DEFAULT NULL,
  `video_audio` varchar(1000) DEFAULT NULL,
  `out` varchar(1000) DEFAULT NULL,
  `status` varchar(1000) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`request_id`,`user_id`,`request`,`video_audio`,`out`,`status`,`type`) values 
(1,1,'request','dsgrdgersgterstes','20','pending',NULL),
(2,1,'haah','static/videoaab00f3d-2206-40ed-825e-e6f7622493a1abc.wav','0','pending','Audio'),
(3,1,'haah','static/video13bf8e19-b76d-4d94-a282-1a3c2da79e9babc.wav','0','pending','Audio'),
(4,1,'haah','static/video35da8ccc-a5db-4e00-9a4b-7fdd856f28baabc.wav','0','pending','Audio'),
(5,1,'haah','static/videobe3e5699-9178-4db1-a7d7-082901231b98abc.wav','0','pending','Audio'),
(6,1,'haah','static/video8055edf3-552c-4965-aa33-4605262bcd79abc.wav','0','pending','Audio'),
(7,1,'haah','static/videoce4e6d90-09a8-45bc-9798-d161efa6b939abc.wav','0','pending','Audio'),
(8,1,'haah','static/videodfb4a212-4081-4679-89b4-eafa44ff1c92abc.wav','0','pending','Audio'),
(9,1,'haah','static/video21f42827-2071-4cc5-89c6-b3d6e91dcb47abc.wav','0','pending','Audio'),
(10,1,'haah','static/video3b7265f9-a0e9-40db-810a-d0963c5320c0abc.wav','0','pending','Audio'),
(11,1,'haah','static/video3e557aa3-a4ba-4940-9091-7a9a252e87aaabc.wav','0','pending','Audio'),
(12,1,'haah','static/video7f224567-35a2-4672-8857-46b874a16cf3abc.wav','0','pending','Audio'),
(13,1,'haah','static/video91c3a398-f075-4ee4-9619-1ec184e118f1abc.wav','0','pending','Audio'),
(14,1,'haah','static/video47adc128-b052-4cff-ba1a-68f60b9b1728abc.wav','0','pending','Audio'),
(15,1,'haah','static/video7595f736-f139-4df3-9f32-3b9efb5add33abc.wav','0','pending','Audio'),
(16,1,'haah','static/video45311852-5de2-4e9b-8b21-5bafb972024eabc.wav','0','pending','Audio'),
(17,1,'haah','static/video14117c42-c7c8-4ffb-a63b-1c493200e8dfabc.wav','0','pending','Audio'),
(18,1,'haah','static/video88919cbb-af50-4686-9fb2-d09f6876816eabc.wav','0','pending','Audio'),
(19,1,'haah','static/video3df41e0e-9777-4ccc-a4a8-110a97e063afabc.wav','0','pending','Audio'),
(20,1,'Name','static/video4d5568fc-37ee-45c7-bcd4-2c1f766aedc6abc.mp4','0','pending','Video'),
(21,1,'Name','static/video662103c8-c65f-43ad-a294-15e3c97ffe36abc.mp4','0','pending','Video');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,2,'Renuka Kamath','Renuka Kamath','ekm','1234567891','renukakamath2@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
