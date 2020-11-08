-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 08, 2020 at 08:41 AM
-- Server version: 10.1.8-MariaDB
-- PHP Version: 5.6.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `school_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `bugs`
--

CREATE TABLE `bugs` (
  `bugID` int(11) NOT NULL,
  `content` char(255) NOT NULL,
  `raised_by` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bugs`
--

INSERT INTO `bugs` (`bugID`, `content`, `raised_by`) VALUES
(1, 'This the first bug of sinotech international.This is expected to be solved by the mid of october', 'SQ9K'),
(2, 'Pushed via push_bug', 'OH2N'),
(3, 'This the second bug from my account please solve it', 'OH2N');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `employeeID` int(11) NOT NULL,
  `name` char(50) NOT NULL,
  `password` varchar(220) NOT NULL,
  `code` varchar(8) NOT NULL,
  `dept` char(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`employeeID`, `name`, `password`, `code`, `dept`) VALUES
(1, 'Sarthak Chauhan', '$2b$12$R.CgX/ExO.6X01Q/rzMBouIkrt4Trohqn6K1xuJlw44.LFvI9SzBe', 'OH2N', 'development'),
(2, 'Shivansh Goel', '$2b$12$I6ZiOY/rFtz9OPHOyxU9TOb8yXs0ouwGMP2fg8pLhQTus9nm9g04.', 'SQ9K', 'production'),
(3, 'Parvesh Saini', '$2b$12$SdJfNHn83WGGT7oZr6Zm.uPtuWiM5nuDj7CaNvZtBvDAiUAylwVH2', 'FG7J', 'development'),
(4, 'Devanshu Chandella', '$2b$12$0w2MRbhf3Sn7BqgdG1BFAOJdMwKHuef7ifyBGUKpNFVUmr9airGyK', 'FJ6K', 'production'),
(5, 'Toyesh Gupta', '$2b$12$QtkOADffonotiIV3hj8f6emFmIpHxujrgA7Z1d4TvXSJi4Vlvbni6', 'QO4V', 'Dm for fun');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bugs`
--
ALTER TABLE `bugs`
  ADD PRIMARY KEY (`bugID`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`employeeID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bugs`
--
ALTER TABLE `bugs`
  MODIFY `bugID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `employeeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
