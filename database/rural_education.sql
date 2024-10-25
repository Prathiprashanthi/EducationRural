-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 23, 2024 at 07:03 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rural_education`
--
CREATE DATABASE IF NOT EXISTS `rural_education` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `rural_education`;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=69 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
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
(25, 'Can add instructor reg model', 7, 'add_instructorregmodel'),
(26, 'Can change instructor reg model', 7, 'change_instructorregmodel'),
(27, 'Can delete instructor reg model', 7, 'delete_instructorregmodel'),
(28, 'Can view instructor reg model', 7, 'view_instructorregmodel'),
(29, 'Can add addcourse', 8, 'add_addcourse'),
(30, 'Can change addcourse', 8, 'change_addcourse'),
(31, 'Can delete addcourse', 8, 'delete_addcourse'),
(32, 'Can view addcourse', 8, 'view_addcourse'),
(33, 'Can add question', 9, 'add_question'),
(34, 'Can change question', 9, 'change_question'),
(35, 'Can delete question', 9, 'delete_question'),
(36, 'Can view question', 9, 'view_question'),
(37, 'Can add result model', 10, 'add_resultmodel'),
(38, 'Can change result model', 10, 'change_resultmodel'),
(39, 'Can delete result model', 10, 'delete_resultmodel'),
(40, 'Can view result model', 10, 'view_resultmodel'),
(41, 'Can add student reg model', 11, 'add_studentregmodel'),
(42, 'Can change student reg model', 11, 'change_studentregmodel'),
(43, 'Can delete student reg model', 11, 'delete_studentregmodel'),
(44, 'Can view student reg model', 11, 'view_studentregmodel'),
(45, 'Can add student feedback', 12, 'add_studentfeedback'),
(46, 'Can change student feedback', 12, 'change_studentfeedback'),
(47, 'Can delete student feedback', 12, 'delete_studentfeedback'),
(48, 'Can view student feedback', 12, 'view_studentfeedback'),
(49, 'Can add student courses', 13, 'add_studentcourses'),
(50, 'Can change student courses', 13, 'change_studentcourses'),
(51, 'Can delete student courses', 13, 'delete_studentcourses'),
(52, 'Can view student courses', 13, 'view_studentcourses'),
(53, 'Can add cart model', 14, 'add_cartmodel'),
(54, 'Can change cart model', 14, 'change_cartmodel'),
(55, 'Can delete cart model', 14, 'delete_cartmodel'),
(56, 'Can view cart model', 14, 'view_cartmodel'),
(57, 'Can add user test model', 15, 'add_usertestmodel'),
(58, 'Can change user test model', 15, 'change_usertestmodel'),
(59, 'Can delete user test model', 15, 'delete_usertestmodel'),
(60, 'Can view user test model', 15, 'view_usertestmodel'),
(61, 'Can add scholarship application', 16, 'add_scholarshipapplication'),
(62, 'Can change scholarship application', 16, 'change_scholarshipapplication'),
(63, 'Can delete scholarship application', 16, 'delete_scholarshipapplication'),
(64, 'Can view scholarship application', 16, 'view_scholarshipapplication'),
(65, 'Can add loan application', 17, 'add_loanapplication'),
(66, 'Can change loan application', 17, 'change_loanapplication'),
(67, 'Can delete loan application', 17, 'delete_loanapplication'),
(68, 'Can view loan application', 17, 'view_loanapplication');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `cart_details`
--

DROP TABLE IF EXISTS `cart_details`;
CREATE TABLE IF NOT EXISTS `cart_details` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cart_booking_id` int(11) NOT NULL,
  `cart_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cart_details_cart_booking_id_77c0b5d0` (`cart_booking_id`),
  KEY `cart_details_cart_user_id_98a1135a` (`cart_user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `courses_details`
--

DROP TABLE IF EXISTS `courses_details`;
CREATE TABLE IF NOT EXISTS `courses_details` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(255) NOT NULL,
  `course_image` varchar(100) NOT NULL,
  `course_category` varchar(100) NOT NULL,
  `course_language` varchar(100) NOT NULL,
  `video_url` varchar(200) NOT NULL,
  `duration_weeks` int(11) NOT NULL,
  `added_date` date DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'adminapp', 'instructorregmodel'),
(8, 'adminapp', 'addcourse'),
(9, 'adminapp', 'question'),
(10, 'userapp', 'resultmodel'),
(11, 'userapp', 'studentregmodel'),
(12, 'userapp', 'studentfeedback'),
(13, 'userapp', 'studentcourses'),
(14, 'userapp', 'cartmodel'),
(15, 'userapp', 'usertestmodel'),
(16, 'adminapp', 'scholarshipapplication'),
(17, 'adminapp', 'loanapplication');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-06-20 12:48:12.358464'),
(2, 'auth', '0001_initial', '2024-06-20 12:48:12.860845'),
(3, 'admin', '0001_initial', '2024-06-20 12:48:13.016708'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-06-20 12:48:13.016708'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-06-20 12:48:13.053369'),
(6, 'adminapp', '0001_initial', '2024-06-20 12:48:13.295819'),
(7, 'contenttypes', '0002_remove_content_type_name', '2024-06-20 12:48:13.451361'),
(8, 'auth', '0002_alter_permission_name_max_length', '2024-06-20 12:48:13.525432'),
(9, 'auth', '0003_alter_user_email_max_length', '2024-06-20 12:48:13.603564'),
(10, 'auth', '0004_alter_user_username_opts', '2024-06-20 12:48:13.620417'),
(11, 'auth', '0005_alter_user_last_login_null', '2024-06-20 12:48:13.675675'),
(12, 'auth', '0006_require_contenttypes_0002', '2024-06-20 12:48:13.683262'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2024-06-20 12:48:13.702903'),
(14, 'auth', '0008_alter_user_username_max_length', '2024-06-20 12:48:13.770200'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2024-06-20 12:48:13.867589'),
(16, 'auth', '0010_alter_group_name_max_length', '2024-06-20 12:48:13.953808'),
(17, 'auth', '0011_update_proxy_permissions', '2024-06-20 12:48:13.981861'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2024-06-20 12:48:14.070734'),
(19, 'sessions', '0001_initial', '2024-06-20 12:48:14.161120'),
(20, 'userapp', '0001_initial', '2024-06-20 12:48:14.570955'),
(21, 'userapp', '0002_remove_cartmodel_cart_booking_and_more', '2024-06-21 07:28:24.208380'),
(22, 'userapp', '0003_initial', '2024-06-21 07:29:32.345132'),
(23, 'adminapp', '0002_remove_addcourse_price', '2024-06-21 08:53:57.667155'),
(24, 'adminapp', '0003_remove_addcourse_instructor', '2024-06-21 11:00:35.907979'),
(25, 'adminapp', '0004_remove_addcourse_course_description', '2024-06-21 11:45:18.556643'),
(26, 'adminapp', '0005_remove_question_instructor', '2024-06-21 11:57:21.710396'),
(27, 'userapp', '0004_remove_cartmodel_cart_booking_and_more', '2024-06-21 12:04:17.295394'),
(28, 'adminapp', '0006_remove_question_course_delete_instructorregmodel_and_more', '2024-06-21 12:04:18.834580'),
(29, 'adminapp', '0007_initial', '2024-06-21 12:06:13.068317'),
(30, 'userapp', '0005_initial', '2024-06-21 12:06:13.388315'),
(31, 'adminapp', '0008_scholarshipapplication', '2024-06-21 13:16:43.829374'),
(32, 'adminapp', '0009_loanapplication', '2024-06-21 13:21:22.525476'),
(33, 'userapp', '0006_remove_cartmodel_cart_booking_and_more', '2024-06-22 04:26:48.411079'),
(34, 'adminapp', '0010_delete_addcourse_delete_instructorregmodel_and_more', '2024-06-22 04:26:48.431417'),
(35, 'adminapp', '0011_initial', '2024-06-22 04:27:19.939567'),
(36, 'userapp', '0007_initial', '2024-06-22 04:27:20.257707'),
(37, 'userapp', '0008_remove_cartmodel_cart_booking_and_more', '2024-06-22 12:40:51.835138'),
(38, 'adminapp', '0012_delete_addcourse_delete_instructorregmodel_and_more', '2024-06-22 12:40:51.835138'),
(39, 'adminapp', '0013_initial', '2024-06-22 12:41:33.383047'),
(40, 'userapp', '0009_initial', '2024-06-22 12:41:33.681888'),
(41, 'userapp', '0010_remove_cartmodel_cart_booking_and_more', '2024-06-22 14:47:24.465524'),
(42, 'adminapp', '0014_remove_question_course_delete_instructorregmodel_and_more', '2024-06-22 14:47:25.936180'),
(43, 'adminapp', '0015_initial', '2024-06-22 14:48:11.875798'),
(44, 'userapp', '0011_initial', '2024-06-22 14:48:12.243159'),
(45, 'userapp', '0012_remove_cartmodel_cart_booking_and_more', '2024-06-23 06:57:36.569816'),
(46, 'adminapp', '0016_delete_addcourse_delete_instructorregmodel_and_more', '2024-06-23 06:57:36.590046'),
(47, 'adminapp', '0017_initial', '2024-06-23 06:58:03.754196'),
(48, 'userapp', '0013_initial', '2024-06-23 06:58:04.056844');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0ij8zv2b6cupsltk45o0w7wzjmewdby4', 'eyJzdHVkZW50X2lkIjoxfQ:1sKsax:sK4SRqTW0JVS9tiFvguXy9rfXGMA2laYQm_eibGN3VA', '2024-07-06 04:43:23.496314'),
('m5f9ueoxvqbztxfwf3n00ga8usjvz72i', 'eyJzdHVkZW50X2lkX2FmdGVyX2xvZ2luIjoyfQ:1sKxNn:rc2PPhBY9wYBy3D3sZMnB82VdneaIjVJ5-pW4-UE-OM', '2024-07-06 09:50:07.219635'),
('ohyipjv75sa5c2eu0dllp26lqce2w1tg', '.eJxtkLFOw0AMhl_F8pwBOmZBIDEydWCg6OQkTnJwuVNtpxBVfXfcUIEEven82f7t30dUmzvOFmIXqDeWkMoQM9a3FbaJVEOmibHGDVaoc_PGrXn0mIcUdXQmrHMyxfrliPuZ1WLJLrYK_MTGn-euJxJZYKQDA0GKZokh0dScpTm5MvsSWT9YvHgkdd4WEU_84nuHUcOFY91TUj5Vf4Zv_g9_HskgKtjIcOmGvsgEpV_ZgaWBmNe_-kU4t1zDDrceB39g5TtnRRjYyxfYks3S0bLDu6sehsJXTTxcNfFaoRWjFCaSd7_ozekLb_ORwA:1sL1L5:XkUzH4BpDvLOjqKcFYjZBxpIMGpAvwTSHWGGYQHncMM', '2024-07-06 14:03:35.548714');

-- --------------------------------------------------------

--
-- Table structure for table `instructor_details`
--

DROP TABLE IF EXISTS `instructor_details`;
CREATE TABLE IF NOT EXISTS `instructor_details` (
  `instructor_id` int(11) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(55) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_number` bigint(20) DEFAULT NULL,
  `gender` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `status` varchar(100) DEFAULT NULL,
  `reg_date` date DEFAULT NULL,
  `address` varchar(255) NOT NULL,
  `otp` varchar(6) NOT NULL,
  `otp_status` varchar(15) NOT NULL,
  PRIMARY KEY (`instructor_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `loan`
--

DROP TABLE IF EXISTS `loan`;
CREATE TABLE IF NOT EXISTS `loan` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `eligibility` varchar(10) NOT NULL,
  `deadline` date NOT NULL,
  `link` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
CREATE TABLE IF NOT EXISTS `questions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `subject` varchar(50) NOT NULL,
  `question_text` longtext NOT NULL,
  `class_name` varchar(255) NOT NULL,
  `option_a` varchar(255) NOT NULL,
  `option_b` varchar(255) NOT NULL,
  `option_c` varchar(255) NOT NULL,
  `option_d` varchar(255) NOT NULL,
  `correct_answer` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `scholarship`
--

DROP TABLE IF EXISTS `scholarship`;
CREATE TABLE IF NOT EXISTS `scholarship` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `eligibility` varchar(10) NOT NULL,
  `deadline` date NOT NULL,
  `link` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `student_courses_details`
--

DROP TABLE IF EXISTS `student_courses_details`;
CREATE TABLE IF NOT EXISTS `student_courses_details` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `amount` int(11) NOT NULL,
  `payment_status` varchar(100) NOT NULL,
  `purchase_date` date DEFAULT NULL,
  `payment_id` varchar(200) NOT NULL,
  `order_id` varchar(200) NOT NULL,
  `course_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `student_courses_details_course_id_19b51a85` (`course_id`),
  KEY `student_courses_details_student_id_e541b9d6` (`student_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `student_details`
--

DROP TABLE IF EXISTS `student_details`;
CREATE TABLE IF NOT EXISTS `student_details` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone_number` bigint(20) NOT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL,
  `reg_date` date DEFAULT NULL,
  `address` varchar(255) NOT NULL,
  `otp` varchar(6) NOT NULL,
  `otp_status` varchar(15) NOT NULL,
  `class_selected` varchar(2) NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `student_feedback`
--

DROP TABLE IF EXISTS `student_feedback`;
CREATE TABLE IF NOT EXISTS `student_feedback` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(255) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `user_email` varchar(254) NOT NULL,
  `rating` int(11) NOT NULL,
  `additional_comments` longtext NOT NULL,
  `submitted_at` datetime(6) NOT NULL,
  `sentiment` varchar(20) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_feedback_student_id_d8d2dddf` (`student_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_feedback`
--

INSERT INTO `student_feedback` (`id`, `course_name`, `user_name`, `user_email`, `rating`, `additional_comments`, `submitted_at`, `sentiment`, `student_id`) VALUES
(1, 'First', 'ammullu', 'ammu@gmail.com', 5, 'very very good', '2024-06-23 06:58:20.538154', 'very positive', 1);

-- --------------------------------------------------------

--
-- Table structure for table `student_result_details`
--

DROP TABLE IF EXISTS `student_result_details`;
CREATE TABLE IF NOT EXISTS `student_result_details` (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `test_id` int(11) DEFAULT NULL,
  `test_name` varchar(155) NOT NULL,
  `question` varchar(155) NOT NULL,
  `useranswer` varchar(55) NOT NULL,
  `correctanswer` varchar(55) NOT NULL,
  `marks` int(11) NOT NULL,
  `result_date` date DEFAULT NULL,
  PRIMARY KEY (`result_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user_tests_details`
--

DROP TABLE IF EXISTS `user_tests_details`;
CREATE TABLE IF NOT EXISTS `user_tests_details` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `test_name` varchar(155) NOT NULL,
  `test_date` date NOT NULL,
  `test_marks` int(11) NOT NULL,
  `test_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `test_name` (`test_name`),
  KEY `User_tests_details_test_user_id_89c17f0d` (`test_user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
