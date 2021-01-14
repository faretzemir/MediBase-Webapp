-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2021 at 07:27 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clinic`
--

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `pat_id` varchar(10) NOT NULL,
  `pat_name` varchar(50) NOT NULL,
  `pat_gender` varchar(10) NOT NULL,
  `pat_dob` date NOT NULL,
  `pat_age` int(11) NOT NULL,
  `pat_contact` varchar(10) NOT NULL,
  `pat_ic` varchar(15) NOT NULL,
  `past_visit` date NOT NULL,
  `fut_visit` date NOT NULL,
  `past_med` varchar(20) NOT NULL,
  `med_dosage` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`pat_id`, `pat_name`, `pat_gender`, `pat_dob`, `pat_age`, `pat_contact`, `pat_ic`, `past_visit`, `fut_visit`, `past_med`, `med_dosage`) VALUES
('PA10001', 'Faretz', 'Male', '1999-05-02', 21, '0197592599', '990502015479', '2019-08-16', '2021-01-27', 'Cocaine', 10),
('PA10002', 'Eilham Hakimie', 'Male', '1998-04-21', 22, '0197283746', '900504016738', '2019-08-16', '2021-10-22', 'Omeperazole', 25),
('PA10003', 'Pang Jie Xin', 'Male', '1999-08-16', 21, '0102221582', '990816018374', '2020-07-09', '0000-00-00', 'Adderall', 20),
('PA10004', 'Kenny G', 'Male', '1966-07-08', 30, '+860238458', '660708057283', '2020-09-22', '2021-10-22', 'Keppra XR', 45),
('PA10005', 'Nadhirah Balqis', 'Female', '2000-07-09', 21, '0126397867', '000709011234', '2020-07-09', '2021-01-27', 'Forteo', 12);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
