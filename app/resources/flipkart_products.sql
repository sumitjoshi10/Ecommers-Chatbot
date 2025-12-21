-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 15, 2025 at 01:12 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flipkart_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_link` text DEFAULT NULL,
  `title` text DEFAULT NULL,
  `brand` text DEFAULT NULL,
  `marked_price` bigint(20) DEFAULT NULL,
  `price` bigint(20) DEFAULT NULL,
  `discount` double DEFAULT NULL,
  `avg_rating` double DEFAULT NULL,
  `total_ratings` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_link`, `title`, `brand`, `marked_price`, `price`, `discount`, `avg_rating`, `total_ratings`) VALUES
('https://www.flipkart.com/vokline-sports-shoes-trekking-shoes-running-shoes-gym-shoes-women-walking/p/itmd28f73dfdbae0?pid=SHOGKRMTUNRHHHTS&lid=LSTSHOGKRMTUNRHHHTSMN7MSF&marketplace=FLIPKART&q=sports+shoes+for+women&store=osp%2Fiko%2Fd20&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=en_8GmqGVIwV_DpDqu_eveSd_rVCPDIo7nlxkITbuJ9vtvc48TC3rHg8HOU-y7QlNOwKDtzulQRFeOyWxJeEA-F3Q%3D%3D&ppt=sp&ppn=sp&ssid=yflcq4c6xs0000001765654572635&qH=32e27b1148959538', 'Vokline Sports shoes,trekking shoes, Running shoes,gym shoes For Women Walking Shoes For Women', 'Vokline ', 999, 360, 0.63, 4.1, 147894),
('https://www.flipkart.com/footox-trendy-sports-running-shoes-women/p/itm11d596cf87fb0?pid=SHOH8WS75TTCW9UC&lid=LSTSHOH8WS75TTCW9UCYMTFDB&marketplace=FLIPKART&q=sports+shoes+for+women&store=osp%2Fiko%2Fd20&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=en_8GmqGVIwV_DpDqu_eveSd_rVCPDIo7nlxkITbuJ9vtsHdeiUWehjXT5L-ic1-gm-xwd5bGeyCEvqN-vUj5iZag%3D%3D&ppt=sp&ppn=sp&ssid=yflcq4c6xs0000001765654572635&qH=32e27b1148959538', 'Trendy Sports Running Shoes For Women', 'Footox ', 999, 380, 0.61, 3.8, 1108),
('https://www.flipkart.com/fabbmate-trendy-memory-foam-walking-running-shoes-women/p/itmc5814f4e2a802?pid=SHOGH3Y26FSPPRQT&lid=LSTSHOGH3Y26FSPPRQTDN10J5&marketplace=FLIPKART&q=sports+shoes+for+women&store=osp%2Fiko%2Fd20&spotlightTagId=default_BestsellerId_osp%2Fiko%2Fd20&srno=s_1_3&otracker=search&otracker1=search&fm=Search&iid=f8eb7981-9149-4649-ac1a-bab39b655a43.SHOGH3Y26FSPPRQT.SEARCH&ppt=sp&ppn=sp&ssid=yflcq4c6xs0000001765654572635&qH=32e27b1148959538', 'Fabbmate Trendy Memory Foam Walking Running Shoes For Women', 'Fabbmate ', 799, 339, 0.57, 4, 139036),
('https://www.flipkart.com/campus-terra-running-shoes-women/p/itm2b3ee00805260?pid=SHOHGKKBFTTFF2SZ&lid=LSTSHOHGKKBFTTFF2SZKNQHGO&marketplace=FLIPKART&q=sports+shoes+for+women&store=osp%2Fiko%2Fd20&srno=s_1_4&otracker=search&otracker1=search&fm=Search&iid=f8eb7981-9149-4649-ac1a-bab39b655a43.SHOHGKKBFTTFF2SZ.SEARCH&ppt=sp&ppn=sp&ssid=yflcq4c6xs0000001765654572635&qH=32e27b1148959538', 'TERRA Running Shoes For Women', 'CAMPUS ', 1999, 1999, NULL, NULL, NULL),
('https://www.flipkart.com/deals4you-sneakers-women/p/itm6dd0e5a6dc9f6?pid=SHOGRW7NPGUFMMBW&lid=LSTSHOGRW7NPGUFMMBWZHX9UN&marketplace=FLIPKART&q=sports+shoes+for+women&store=osp%2Fiko%2Fd20&srno=s_1_5&otracker=search&otracker1=search&fm=Search&iid=en_8GmqGVIwV_DpDqu_eveSd_rVCPDIo7nlxkITbuJ9vtv58wzY2voXg8yr5BClGhcWtrhXsq0PVWhQPoo8XYwnGA%3D%3D&ppt=sp&ppn=sp&ssid=yflcq4c6xs0000001765654572635&qH=32e27b1148959538', 'Sneakers For Women', 'Deals4you ', 1499, 423, 0.71, 4, 16860),
('https://www.flipkart.com/campus-spree-running-shoes-women/p/itmc1c9c99885647?pid=SHOHGKKBCNZJZXVH&lid=LSTSHOHGKKBCNZJZXVHDDR6F6&marketplace=FLIPKART&q=sports+shoes+for+women&store=osp%2Fiko%2Fd20&srno=s_1_7&otracker=search&otracker1=search&fm=Search&iid=f8eb7981-9149-4649-ac1a-bab39b655a43.SHOHGKKBCNZJZXVH.SEARCH&ppt=sp&ppn=sp&ssid=yflcq4c6xs0000001765654572635&qH=32e27b1148959538', 'SPREE Running Shoes For Women', 'CAMPUS ', 2499, 2499, NULL, NULL, NULL),
('https://www.flipkart.com/cropic-sneakers-women/p/itmd7fa4ff8ae853?pid=SHOHGJD5JZMFQ9RD&lid=LSTSHOHGJD5JZMFQ9RDX5YHSU&marketplace=FLIPKART&q=sports+shoes+for+women&store=osp%2Fiko%2Fd20&srno=s_1_8&otracker=search&otracker1=search&fm=Search&iid=f8eb7981-9149-4649-ac1a-bab39b655a43.SHOHGJD5JZMFQ9RD.SEARCH&ppt=sp&ppn=sp&ssid=yflcq4c6xs0000001765654572635&qH=32e27b1148959538', 'Sneakers For Women', 'cropic ', 1199, 540, 0.54, NULL, NULL),
('https://www.flipkart.com/rizta-training-gym-shoes-women/p/itmd97c562dd2837?pid=SHOHGH4VCDYFQGG6&lid=LSTSHOHGH4VCDYFQGG6TRZN8Q&marketplace=FLIPKART&q=sports+shoes+for+women&store=osp%2Fiko%2Fd20&srno=s_1_9&otracker=search&otracker1=search&fm=Search&iid=f8eb7981-9149-4649-ac1a-bab39b655a43.SHOHGH4VCDYFQGG6.SEARCH&ppt=sp&ppn=sp&ssid=yflcq4c6xs0000001765654572635&qH=32e27b1148959538', 'Training & Gym Shoes For Women', 'RIZTA ', 999, 370, 0.62, NULL, NULL),
('https://www.flipkart.com/fabbmate-casual-sports-shoes-white-sneakers-women-girls/p/itma5fcb289f70ae?pid=SHOHF5MMXVPJPFJZ&lid=LSTSHOHF5MMXVPJPFJZUOBPOX&marketplace=FLIPKART&q=sports+shoes+for+women&store=osp%2Fiko%2Fd20&srno=s_1_10&otracker=search&otracker1=search&fm=Search&iid=f8eb7981-9149-4649-ac1a-bab39b655a43.SHOHF5MMXVPJPFJZ.SEARCH&ppt=sp&ppn=sp&ssid=yflcq4c6xs0000001765654572635&qH=32e27b1148959538', 'Fabbmate Casual Sports shoes White Sneakers for Women Girls White Shoes Sneakers For Women', 'Fabbmate ', 999, 432, 0.56, 4, 16653);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
