// Gmsh project created on Fri Feb 19 18:32:14 2021
//+
Point(1) = {1000, 0, 0, 1.0};
//+
Point(2) = {1000, 1000, 0, 1.0};
//+
Point(3) = {238.8947, 1642.715, 0, 1.0};
//+
Point(4) = {-681.0657, 1239.1713, 0, 1.0};
//+
Point(5) = {-1557.4245, 757.5124, 0, 1.0};
//+
Point(6) = {-1994.8995, -141.6759, 0, 1.0};
//+
Point(7) = {-1924.0589, -1139.1635, 0, 1.0};
//+
Point(8) = {-1414.1909, -1999.4162, 0, 1.0};
//+
Point(9) = {-597.5837, -2576.6099, 0, 1.0};
//+
Point(10) = {376.4934, -2802.8266, 0, 1.0};
//+
Point(11) = {1367.6487, -2670.1194, 0, 1.0};
//+
Point(12) = {2257.555, -2213.976, 0, 1.0};
//+
Point(13) = {2957.4675, -1499.7474, 0, 1.0};
//+
Point(14) = {3410.2061, -608.1041, 0, 1.0};
//+
Point(15) = {3585.2909, 376.4493, 0, 1.0};
//+
Line(1) = {1 ,2};
//+
Line(2) = {2 ,3};
//+
Line(3) = {3 ,4};
//+
Line(4) = {4 ,5};
//+
Line(5) = {5 ,6};
//+
Line(6) = {6 ,7};
//+
Line(7) = {7 ,8};
//+
Line(8) = {8 ,9};
//+
Line(9) = {9 ,10};
//+
Line(10) = {10 ,11};
//+
Line(11) = {11 ,12};
//+
Line(12) = {12 ,13};
//+
Line(13) = {13 ,14};
//+
Line(14) = {14 ,15};
//+
Line(15) = {15, 1};
//+
Line Loop(16) = {15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14};
//+
Plane Surface(17) = {16};
//+
Physical Surface(18) = {17};
