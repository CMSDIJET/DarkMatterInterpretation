TGraph2D *graph2d   = new TGraph2D(626);
TH2D *triangulation = new TH2D("triangulation","",1200,0,1200,400,0,400);


void Limit_Mx_MA_obs_0p25()
{
   static Int_t  colors[500];
   static Bool_t initialized = kFALSE;
   Double_t Red[3]    = { 1.00, 156./255., 112./255.};
   Double_t Green[3]  = { 1.00, 179./255., 96./255.};
   Double_t Blue[3]   = { 1.00, 201./255., 159./255.};
   Double_t Length[3] = { 0.00, 0.7, 1.00 };
   if(!initialized){
      Int_t FI = TColor::CreateGradientColorTable(3,Length,Red,Green,Blue,500);
      for (int i=0; i<500; i++) colors[i] = FI+i;
      initialized = kTRUE;
      
   }
   gStyle->SetPalette(500,colors);
   gStyle->SetNumberContours(500);
//=========Macro generated from canvas: c2/c2
//=========  (Fri Jul 29 22:32:33 2016) by ROOT version6.02/13
   TCanvas *c2 = new TCanvas("c2", "c2",0,0,700,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   c2->Range(0,0,1,1);
   c2->SetFillColor(0);
   c2->SetBorderMode(0);
   c2->SetBorderSize(2);
   c2->SetTickx(1);
   c2->SetTicky(1);
   c2->SetLeftMargin(0.16);
   c2->SetRightMargin(0.05);
   c2->SetTopMargin(0.05);
   c2->SetBottomMargin(0.13);
   c2->SetFrameFillStyle(0);
   c2->SetFrameBorderMode(0);
  
// ------------>Primitives in pad: t2
   TPad *t2 = new TPad("t2", "t2",0,0,1,1);
   t2->Draw();
   t2->cd();
   t2->Range(-286.25,-46.40244,1509.062,318.2317);
   t2->SetFillColor(0);
   t2->SetBorderMode(0);
   t2->SetBorderSize(2);
   t2->SetLogz();
   t2->SetTickx(1);
   t2->SetTicky(1);
   t2->SetLeftMargin(0.16);
   t2->SetRightMargin(0.2);
   t2->SetTopMargin(0.05);
   t2->SetBottomMargin(0.13);
   t2->SetFrameFillStyle(0);
   t2->SetFrameBorderMode(0);
   t2->SetFrameFillStyle(0);
   t2->SetFrameBorderMode(0);
   
   graph2d->SetName("Observed");
   graph2d->SetTitle("Graph2D");
   Observed->SetDirectory(0);
   graph2d->SetPoint(0,10,1,0.1550365);
   graph2d->SetPoint(1,20,1,0.1878744);
   graph2d->SetPoint(2,30,1,0.06831674);
   graph2d->SetPoint(3,40,1,0.09079003);
   graph2d->SetPoint(4,50,1,0.1148836);
   graph2d->SetPoint(5,60,1,0.1391284);
   graph2d->SetPoint(6,70,1,0.16041);
   graph2d->SetPoint(7,80,1,0.1817968);
   graph2d->SetPoint(8,90,1,0.2016623);
   graph2d->SetPoint(9,100,1,0.2242391);
   graph2d->SetPoint(10,125,1,0.2725985);
   graph2d->SetPoint(11,150,1,0.3308425);
   graph2d->SetPoint(12,175,1,0.3823018);
   graph2d->SetPoint(13,200,1,0.4519581);
   graph2d->SetPoint(14,225,1,0.4345642);
   graph2d->SetPoint(15,250,1,0.4955321);
   graph2d->SetPoint(16,275,1,0.549319);
   graph2d->SetPoint(17,300,1,0.6171352);
   graph2d->SetPoint(18,325,1,0.655426);
   graph2d->SetPoint(19,350,1,0.7348944);
   graph2d->SetPoint(20,400,1,0.8978583);
   graph2d->SetPoint(21,450,1,1.101614);
   graph2d->SetPoint(22,525,1,1.352933);
   graph2d->SetPoint(23,600,1,1.767774);
   graph2d->SetPoint(24,725,1,2.637775);
   graph2d->SetPoint(25,800,1,3.318633);
   graph2d->SetPoint(26,925,1,4.818757);
   graph2d->SetPoint(27,1000,1,5.907738);
   graph2d->SetPoint(28,1125,1,8.300253);
   graph2d->SetPoint(29,1200,1,9.997747);
   graph2d->SetPoint(30,14,2,0.06591056);
   graph2d->SetPoint(31,10,5,0.8901754);
   graph2d->SetPoint(32,20,5,0.1139005);
   graph2d->SetPoint(33,30,5,0.1060689);
   graph2d->SetPoint(34,40,5,0.1347392);
   graph2d->SetPoint(35,50,5,0.1685325);
   graph2d->SetPoint(36,60,5,0.1842112);
   graph2d->SetPoint(37,70,5,0.2157004);
   graph2d->SetPoint(38,80,5,0.244006);
   graph2d->SetPoint(39,90,5,0.2670575);
   graph2d->SetPoint(40,100,5,0.2975391);
   graph2d->SetPoint(41,125,5,0.2304854);
   graph2d->SetPoint(42,150,5,0.2730839);
   graph2d->SetPoint(43,175,5,0.319774);
   graph2d->SetPoint(44,200,5,0.3703644);
   graph2d->SetPoint(45,225,5,0.4427041);
   graph2d->SetPoint(46,250,5,0.5052721);
   graph2d->SetPoint(47,275,5,0.5631432);
   graph2d->SetPoint(48,300,5,0.644284);
   graph2d->SetPoint(49,325,5,0.5773288);
   graph2d->SetPoint(50,350,5,0.6510783);
   graph2d->SetPoint(51,400,5,0.8041935);
   graph2d->SetPoint(52,450,5,0.9915138);
   graph2d->SetPoint(53,525,5,1.325841);
   graph2d->SetPoint(54,600,5,1.718125);
   graph2d->SetPoint(55,725,5,2.604162);
   graph2d->SetPoint(56,800,5,3.276237);
   graph2d->SetPoint(57,925,5,4.707468);
   graph2d->SetPoint(58,1000,5,5.838211);
   graph2d->SetPoint(59,1125,5,8.192303);
   graph2d->SetPoint(60,5,7,3.050712);
   graph2d->SetPoint(61,10,10,4.424558);
   graph2d->SetPoint(62,20,10,1.756368);
   graph2d->SetPoint(63,30,10,0.1554444);
   graph2d->SetPoint(64,40,10,0.1618021);
   graph2d->SetPoint(65,50,10,0.178879);
   graph2d->SetPoint(66,60,10,0.1977686);
   graph2d->SetPoint(67,70,10,0.2252308);
   graph2d->SetPoint(68,80,10,0.2521608);
   graph2d->SetPoint(69,90,10,0.2747051);
   graph2d->SetPoint(70,100,10,0.3056583);
   graph2d->SetPoint(71,125,10,0.2325638);
   graph2d->SetPoint(72,150,10,0.2799592);
   graph2d->SetPoint(73,175,10,0.3208144);
   graph2d->SetPoint(74,200,10,0.3658309);
   graph2d->SetPoint(75,225,10,0.4535129);
   graph2d->SetPoint(76,250,10,0.5063178);
   graph2d->SetPoint(77,275,10,0.5726002);
   graph2d->SetPoint(78,300,10,0.6426683);
   graph2d->SetPoint(79,325,10,0.5842792);
   graph2d->SetPoint(80,350,10,0.6441335);
   graph2d->SetPoint(81,400,10,0.8111053);
   graph2d->SetPoint(82,450,10,0.9886265);
   graph2d->SetPoint(83,525,10,1.315192);
   graph2d->SetPoint(84,600,10,1.733666);
   graph2d->SetPoint(85,725,10,2.583196);
   graph2d->SetPoint(86,800,10,3.287338);
   graph2d->SetPoint(87,925,10,4.744592);
   graph2d->SetPoint(88,1000,10,5.839011);
   graph2d->SetPoint(89,1125,10,8.164978);
   graph2d->SetPoint(90,1200,10,9.967738);
   graph2d->SetPoint(91,34,12,0.1283757);
   graph2d->SetPoint(92,25,17,2.765287);
   graph2d->SetPoint(93,54,22,0.3272906);
   graph2d->SetPoint(94,10,25,5.760174);
   graph2d->SetPoint(95,20,25,5.46419);
   graph2d->SetPoint(96,30,25,4.951653);
   graph2d->SetPoint(97,40,25,4.114565);
   graph2d->SetPoint(98,50,25,2.302012);
   graph2d->SetPoint(99,60,25,0.4088915);
   graph2d->SetPoint(100,70,25,0.2846688);
   graph2d->SetPoint(101,80,25,0.260172);
   graph2d->SetPoint(102,90,25,0.2612752);
   graph2d->SetPoint(103,100,25,0.2331563);
   graph2d->SetPoint(104,125,25,0.2601882);
   graph2d->SetPoint(105,150,25,0.2992277);
   graph2d->SetPoint(106,175,25,0.3422745);
   graph2d->SetPoint(107,200,25,0.3780842);
   graph2d->SetPoint(108,225,25,0.4657096);
   graph2d->SetPoint(109,250,25,0.5218279);
   graph2d->SetPoint(110,275,25,0.587004);
   graph2d->SetPoint(111,300,25,0.6471545);
   graph2d->SetPoint(112,325,25,0.6215281);
   graph2d->SetPoint(113,350,25,0.6825289);
   graph2d->SetPoint(114,400,25,0.8512965);
   graph2d->SetPoint(115,450,25,1.053276);
   graph2d->SetPoint(116,525,25,1.350485);
   graph2d->SetPoint(117,600,25,1.776941);
   graph2d->SetPoint(118,725,25,2.649819);
   graph2d->SetPoint(119,800,25,3.350036);
   graph2d->SetPoint(120,925,25,4.865939);
   graph2d->SetPoint(121,1000,25,5.962074);
   graph2d->SetPoint(122,1125,25,8.348368);
   graph2d->SetPoint(123,1200,25,10.05416);
   graph2d->SetPoint(124,45,27,4.307295);
   graph2d->SetPoint(125,74,32,0.6122099);
   graph2d->SetPoint(126,65,37,5.998619);
   graph2d->SetPoint(127,94,42,0.9901784);
   graph2d->SetPoint(128,85,47,7.421244);
   graph2d->SetPoint(129,10,50,14.10034);
   graph2d->SetPoint(130,20,50,13.86653);
   graph2d->SetPoint(131,30,50,13.62328);
   graph2d->SetPoint(132,40,50,13.29626);
   graph2d->SetPoint(133,50,50,12.64322);
   graph2d->SetPoint(134,60,50,12.01607);
   graph2d->SetPoint(135,70,50,11.14874);
   graph2d->SetPoint(136,80,50,9.863505);
   graph2d->SetPoint(137,90,50,8.095895);
   graph2d->SetPoint(138,100,50,4.51309);
   graph2d->SetPoint(139,125,50,0.5882857);
   graph2d->SetPoint(140,150,50,0.4544187);
   graph2d->SetPoint(141,175,50,0.4321136);
   graph2d->SetPoint(142,200,50,0.4580628);
   graph2d->SetPoint(143,225,50,0.5257564);
   graph2d->SetPoint(144,250,50,0.5818104);
   graph2d->SetPoint(145,275,50,0.6371504);
   graph2d->SetPoint(146,300,50,0.6998674);
   graph2d->SetPoint(147,325,50,0.6652773);
   graph2d->SetPoint(148,350,50,0.7294897);
   graph2d->SetPoint(149,400,50,0.8929447);
   graph2d->SetPoint(150,450,50,1.069189);
   graph2d->SetPoint(151,525,50,1.331084);
   graph2d->SetPoint(152,600,50,1.713582);
   graph2d->SetPoint(153,725,50,2.714642);
   graph2d->SetPoint(154,800,50,3.383028);
   graph2d->SetPoint(155,925,50,4.865073);
   graph2d->SetPoint(156,1000,50,6.009266);
   graph2d->SetPoint(157,1125,50,8.325212);
   graph2d->SetPoint(158,1200,50,10.22929);
   graph2d->SetPoint(159,114,52,1.180375);
   graph2d->SetPoint(160,105,57,7.633655);
   graph2d->SetPoint(161,10,60,15.57853);
   graph2d->SetPoint(162,20,60,15.62649);
   graph2d->SetPoint(163,30,60,15.3702);
   graph2d->SetPoint(164,40,60,14.90389);
   graph2d->SetPoint(165,50,60,14.45342);
   graph2d->SetPoint(166,60,60,13.88302);
   graph2d->SetPoint(167,70,60,13.15772);
   graph2d->SetPoint(168,80,60,12.40599);
   graph2d->SetPoint(169,90,60,11.24319);
   graph2d->SetPoint(170,100,60,9.989577);
   graph2d->SetPoint(171,125,60,2.635183);
   graph2d->SetPoint(172,150,60,0.655824);
   graph2d->SetPoint(173,175,60,0.5136567);
   graph2d->SetPoint(174,200,60,0.5040663);
   graph2d->SetPoint(175,225,60,0.5393579);
   graph2d->SetPoint(176,250,60,0.5720322);
   graph2d->SetPoint(177,275,60,0.5990769);
   graph2d->SetPoint(178,300,60,0.6190434);
   graph2d->SetPoint(179,325,60,0.6884367);
   graph2d->SetPoint(180,350,60,0.7491434);
   graph2d->SetPoint(181,400,60,0.9045174);
   graph2d->SetPoint(182,450,60,1.095299);
   graph2d->SetPoint(183,525,60,1.356865);
   graph2d->SetPoint(184,600,60,1.775507);
   graph2d->SetPoint(185,725,60,2.697236);
   graph2d->SetPoint(186,800,60,3.407266);
   graph2d->SetPoint(187,925,60,4.893821);
   graph2d->SetPoint(188,1000,60,6.041026);
   graph2d->SetPoint(189,1125,60,8.469287);
   graph2d->SetPoint(190,1200,60,10.1882);
   graph2d->SetPoint(191,134,62,1.632729);
   graph2d->SetPoint(192,125,67,8.947279);
   graph2d->SetPoint(193,10,70,19.88547);
   graph2d->SetPoint(194,20,70,19.5983);
   graph2d->SetPoint(195,30,70,19.59362);
   graph2d->SetPoint(196,40,70,19.25348);
   graph2d->SetPoint(197,50,70,18.68008);
   graph2d->SetPoint(198,60,70,18.15377);
   graph2d->SetPoint(199,70,70,17.4278);
   graph2d->SetPoint(200,80,70,16.33534);
   graph2d->SetPoint(201,90,70,15.78925);
   graph2d->SetPoint(202,100,70,14.37975);
   graph2d->SetPoint(203,125,70,10.78754);
   graph2d->SetPoint(204,150,70,2.064349);
   graph2d->SetPoint(205,175,70,0.7826774);
   graph2d->SetPoint(206,200,70,0.6240375);
   graph2d->SetPoint(207,225,70,0.6204961);
   graph2d->SetPoint(208,250,70,0.62223);
   graph2d->SetPoint(209,275,70,0.6535521);
   graph2d->SetPoint(210,300,70,0.6633076);
   graph2d->SetPoint(211,325,70,0.7173847);
   graph2d->SetPoint(212,350,70,0.7784756);
   graph2d->SetPoint(213,400,70,0.9374479);
   graph2d->SetPoint(214,450,70,1.120886);
   graph2d->SetPoint(215,525,70,1.372124);
   graph2d->SetPoint(216,600,70,1.784029);
   graph2d->SetPoint(217,725,70,2.628886);
   graph2d->SetPoint(218,800,70,3.333098);
   graph2d->SetPoint(219,925,70,4.935683);
   graph2d->SetPoint(220,1000,70,6.04359);
   graph2d->SetPoint(221,1125,70,8.320676);
   graph2d->SetPoint(222,1200,70,10.25273);
   graph2d->SetPoint(223,154,72,2.214205);
   graph2d->SetPoint(224,145,77,10.5158);
   graph2d->SetPoint(225,10,80,24.39412);
   graph2d->SetPoint(226,20,80,24.36305);
   graph2d->SetPoint(227,30,80,24.29416);
   graph2d->SetPoint(228,40,80,23.74829);
   graph2d->SetPoint(229,50,80,23.71895);
   graph2d->SetPoint(230,60,80,22.90576);
   graph2d->SetPoint(231,70,80,22.26514);
   graph2d->SetPoint(232,80,80,21.2506);
   graph2d->SetPoint(233,90,80,20.32443);
   graph2d->SetPoint(234,100,80,19.36573);
   graph2d->SetPoint(235,125,80,16.29763);
   graph2d->SetPoint(236,150,80,11.47209);
   graph2d->SetPoint(237,175,80,1.891861);
   graph2d->SetPoint(238,200,80,0.9029901);
   graph2d->SetPoint(239,225,80,0.748862);
   graph2d->SetPoint(240,250,80,0.7186569);
   graph2d->SetPoint(241,275,80,0.7207941);
   graph2d->SetPoint(242,300,80,0.7159086);
   graph2d->SetPoint(243,325,80,0.7619343);
   graph2d->SetPoint(244,350,80,0.8338816);
   graph2d->SetPoint(245,400,80,0.9685478);
   graph2d->SetPoint(246,450,80,1.160609);
   graph2d->SetPoint(247,525,80,1.39826);
   graph2d->SetPoint(248,600,80,1.801397);
   graph2d->SetPoint(249,725,80,2.666203);
   graph2d->SetPoint(250,800,80,3.330186);
   graph2d->SetPoint(251,925,80,4.909697);
   graph2d->SetPoint(252,1000,80,6.063399);
   graph2d->SetPoint(253,1125,80,8.362786);
   graph2d->SetPoint(254,1200,80,10.1454);
   graph2d->SetPoint(255,174,82,2.813754);
   graph2d->SetPoint(256,165,87,12.13219);
   graph2d->SetPoint(257,10,90,29.2595);
   graph2d->SetPoint(258,20,90,29.90632);
   graph2d->SetPoint(259,30,90,29.90118);
   graph2d->SetPoint(260,40,90,29.44709);
   graph2d->SetPoint(261,50,90,28.76751);
   graph2d->SetPoint(262,60,90,28.32453);
   graph2d->SetPoint(263,70,90,27.43501);
   graph2d->SetPoint(264,80,90,27.01712);
   graph2d->SetPoint(265,90,90,26.0042);
   graph2d->SetPoint(266,100,90,24.75862);
   graph2d->SetPoint(267,125,90,21.82985);
   graph2d->SetPoint(268,150,90,17.96631);
   graph2d->SetPoint(269,175,90,11.2401);
   graph2d->SetPoint(270,200,90,1.912514);
   graph2d->SetPoint(271,225,90,1.082569);
   graph2d->SetPoint(272,250,90,0.885677);
   graph2d->SetPoint(273,275,90,0.8436423);
   graph2d->SetPoint(274,300,90,0.7913688);
   graph2d->SetPoint(275,325,90,0.8279495);
   graph2d->SetPoint(276,350,90,0.8658876);
   graph2d->SetPoint(277,400,90,1.015631);
   graph2d->SetPoint(278,450,90,1.185743);
   graph2d->SetPoint(279,525,90,1.433256);
   graph2d->SetPoint(280,600,90,1.837844);
   graph2d->SetPoint(281,725,90,2.690186);
   graph2d->SetPoint(282,800,90,3.414234);
   graph2d->SetPoint(283,925,90,4.752866);
   graph2d->SetPoint(284,1000,90,6.011768);
   graph2d->SetPoint(285,1125,90,8.420804);
   graph2d->SetPoint(286,1200,90,10.3117);
   graph2d->SetPoint(287,194,92,3.497843);
   graph2d->SetPoint(288,185,97,13.79142);
   graph2d->SetPoint(289,10,100,35.35856);
   graph2d->SetPoint(290,20,100,35.61178);
   graph2d->SetPoint(291,30,100,35.90743);
   graph2d->SetPoint(292,40,100,35.06672);
   graph2d->SetPoint(293,50,100,35.18319);
   graph2d->SetPoint(294,60,100,34.00482);
   graph2d->SetPoint(295,70,100,33.64884);
   graph2d->SetPoint(296,80,100,32.9546);
   graph2d->SetPoint(297,90,100,32.05371);
   graph2d->SetPoint(298,100,100,30.62065);
   graph2d->SetPoint(299,125,100,28.24512);
   graph2d->SetPoint(300,150,100,24.40437);
   graph2d->SetPoint(301,175,100,18.96286);
   graph2d->SetPoint(302,200,100,10.10372);
   graph2d->SetPoint(303,225,100,1.951726);
   graph2d->SetPoint(304,250,100,1.216704);
   graph2d->SetPoint(305,275,100,1.021745);
   graph2d->SetPoint(306,300,100,0.8981874);
   graph2d->SetPoint(307,325,100,0.9184889);
   graph2d->SetPoint(308,350,100,0.9368314);
   graph2d->SetPoint(309,400,100,1.081539);
   graph2d->SetPoint(310,450,100,1.245319);
   graph2d->SetPoint(311,525,100,1.467783);
   graph2d->SetPoint(312,600,100,1.836995);
   graph2d->SetPoint(313,725,100,2.723868);
   graph2d->SetPoint(314,800,100,3.417459);
   graph2d->SetPoint(315,925,100,4.855601);
   graph2d->SetPoint(316,1000,100,6.134316);
   graph2d->SetPoint(317,1125,100,8.452301);
   graph2d->SetPoint(318,1200,100,10.2243);
   graph2d->SetPoint(319,214,102,4.48168);
   graph2d->SetPoint(320,205,107,15.88632);
   graph2d->SetPoint(321,10,110,42.06936);
   graph2d->SetPoint(322,20,110,42.60458);
   graph2d->SetPoint(323,30,110,41.80578);
   graph2d->SetPoint(324,40,110,41.39664);
   graph2d->SetPoint(325,50,110,41.17243);
   graph2d->SetPoint(326,60,110,41.22452);
   graph2d->SetPoint(327,70,110,40.32797);
   graph2d->SetPoint(328,80,110,39.37074);
   graph2d->SetPoint(329,90,110,38.91745);
   graph2d->SetPoint(330,100,110,37.95872);
   graph2d->SetPoint(331,125,110,35.33101);
   graph2d->SetPoint(332,150,110,31.05633);
   graph2d->SetPoint(333,175,110,26.1085);
   graph2d->SetPoint(334,200,110,20.00655);
   graph2d->SetPoint(335,225,110,7.755237);
   graph2d->SetPoint(336,250,110,2.086252);
   graph2d->SetPoint(337,275,110,1.368153);
   graph2d->SetPoint(338,300,110,1.096957);
   graph2d->SetPoint(339,325,110,1.049779);
   graph2d->SetPoint(340,350,110,1.031397);
   graph2d->SetPoint(341,400,110,1.12919);
   graph2d->SetPoint(342,450,110,1.299817);
   graph2d->SetPoint(343,525,110,1.526334);
   graph2d->SetPoint(344,600,110,1.91342);
   graph2d->SetPoint(345,725,110,2.794109);
   graph2d->SetPoint(346,800,110,3.457284);
   graph2d->SetPoint(347,925,110,4.939829);
   graph2d->SetPoint(348,1000,110,6.184924);
   graph2d->SetPoint(349,1125,110,8.539737);
   graph2d->SetPoint(350,1200,110,10.35508);
   graph2d->SetPoint(351,234,112,5.32611);
   graph2d->SetPoint(352,225,117,18.02489);
   graph2d->SetPoint(353,254,122,6.281843);
   graph2d->SetPoint(354,10,125,53.61415);
   graph2d->SetPoint(355,20,125,54.59857);
   graph2d->SetPoint(356,30,125,53.79099);
   graph2d->SetPoint(357,40,125,53.52124);
   graph2d->SetPoint(358,50,125,52.97757);
   graph2d->SetPoint(359,60,125,52.57774);
   graph2d->SetPoint(360,70,125,51.89835);
   graph2d->SetPoint(361,80,125,51.59224);
   graph2d->SetPoint(362,90,125,50.42805);
   graph2d->SetPoint(363,100,125,49.65497);
   graph2d->SetPoint(364,125,125,46.90043);
   graph2d->SetPoint(365,150,125,43.22175);
   graph2d->SetPoint(366,175,125,38.28765);
   graph2d->SetPoint(367,200,125,33.26502);
   graph2d->SetPoint(368,225,125,25.77941);
   graph2d->SetPoint(369,250,125,14.28944);
   graph2d->SetPoint(370,275,125,3.166453);
   graph2d->SetPoint(371,300,125,1.748205);
   graph2d->SetPoint(372,325,125,1.39136);
   graph2d->SetPoint(373,350,125,1.283515);
   graph2d->SetPoint(374,400,125,1.299);
   graph2d->SetPoint(375,450,125,1.41686);
   graph2d->SetPoint(376,525,125,1.59514);
   graph2d->SetPoint(377,600,125,1.980784);
   graph2d->SetPoint(378,725,125,2.842735);
   graph2d->SetPoint(379,800,125,3.52365);
   graph2d->SetPoint(380,925,125,4.976123);
   graph2d->SetPoint(381,1000,125,6.073813);
   graph2d->SetPoint(382,1200,125,10.5857);
   graph2d->SetPoint(383,245,127,20.19772);
   graph2d->SetPoint(384,274,132,7.487066);
   graph2d->SetPoint(385,10,135,61.7067);
   graph2d->SetPoint(386,20,135,63.45043);
   graph2d->SetPoint(387,30,135,63.48711);
   graph2d->SetPoint(388,40,135,61.9875);
   graph2d->SetPoint(389,50,135,61.54711);
   graph2d->SetPoint(390,60,135,61.88037);
   graph2d->SetPoint(391,70,135,60.62645);
   graph2d->SetPoint(392,80,135,59.85383);
   graph2d->SetPoint(393,90,135,59.32943);
   graph2d->SetPoint(394,100,135,58.0851);
   graph2d->SetPoint(395,125,135,55.22804);
   graph2d->SetPoint(396,150,135,51.63856);
   graph2d->SetPoint(397,175,135,46.67623);
   graph2d->SetPoint(398,200,135,41.78832);
   graph2d->SetPoint(399,225,135,35.09504);
   graph2d->SetPoint(400,250,135,26.93618);
   graph2d->SetPoint(401,275,135,11.1786);
   graph2d->SetPoint(402,300,135,3.03911);
   graph2d->SetPoint(403,325,135,1.91894);
   graph2d->SetPoint(404,350,135,1.596988);
   graph2d->SetPoint(405,400,135,1.438578);
   graph2d->SetPoint(406,450,135,1.513428);
   graph2d->SetPoint(407,525,135,1.667111);
   graph2d->SetPoint(408,600,135,2.042938);
   graph2d->SetPoint(409,725,135,2.913391);
   graph2d->SetPoint(410,800,135,3.583221);
   graph2d->SetPoint(411,925,135,5.054092);
   graph2d->SetPoint(412,1000,135,6.232119);
   graph2d->SetPoint(413,1125,135,8.46377);
   graph2d->SetPoint(414,1200,135,10.33925);
   graph2d->SetPoint(415,265,137,22.56615);
   graph2d->SetPoint(416,294,142,8.654442);
   graph2d->SetPoint(417,285,147,25.14716);
   graph2d->SetPoint(418,10,150,76.6213);
   graph2d->SetPoint(419,20,150,78.72288);
   graph2d->SetPoint(420,30,150,79.0619);
   graph2d->SetPoint(421,40,150,77.53679);
   graph2d->SetPoint(422,50,150,77.06892);
   graph2d->SetPoint(423,60,150,76.64283);
   graph2d->SetPoint(424,70,150,76.50014);
   graph2d->SetPoint(425,80,150,75.24041);
   graph2d->SetPoint(426,90,150,74.1857);
   graph2d->SetPoint(427,100,150,73.17691);
   graph2d->SetPoint(428,125,150,69.76381);
   graph2d->SetPoint(429,150,150,66.69773);
   graph2d->SetPoint(430,175,150,61.37503);
   graph2d->SetPoint(431,200,150,56.11007);
   graph2d->SetPoint(432,225,150,50.14509);
   graph2d->SetPoint(433,250,150,43.08668);
   graph2d->SetPoint(434,275,150,34.13434);
   graph2d->SetPoint(435,300,150,17.86743);
   graph2d->SetPoint(436,325,150,4.484006);
   graph2d->SetPoint(437,350,150,2.558938);
   graph2d->SetPoint(438,400,150,1.832528);
   graph2d->SetPoint(439,450,150,1.768833);
   graph2d->SetPoint(440,525,150,1.841079);
   graph2d->SetPoint(441,600,150,2.184097);
   graph2d->SetPoint(442,725,150,3.003717);
   graph2d->SetPoint(443,800,150,3.66017);
   graph2d->SetPoint(444,925,150,5.08691);
   graph2d->SetPoint(445,1000,150,6.312908);
   graph2d->SetPoint(446,1125,150,8.583567);
   graph2d->SetPoint(447,1200,150,10.31215);
   graph2d->SetPoint(448,314,152,8.832063);
   graph2d->SetPoint(449,305,157,24.37387);
   graph2d->SetPoint(450,334,162,10.27903);
   graph2d->SetPoint(451,325,167,27.1876);
   graph2d->SetPoint(452,354,172,11.68295);
   graph2d->SetPoint(453,10,175,97.39271);
   graph2d->SetPoint(454,20,175,97.27171);
   graph2d->SetPoint(455,30,175,96.66904);
   graph2d->SetPoint(456,40,175,96.15788);
   graph2d->SetPoint(457,50,175,95.31132);
   graph2d->SetPoint(458,60,175,95.71757);
   graph2d->SetPoint(459,70,175,94.4805);
   graph2d->SetPoint(460,80,175,94.08452);
   graph2d->SetPoint(461,90,175,93.30392);
   graph2d->SetPoint(462,100,175,91.95642);
   graph2d->SetPoint(463,125,175,89.87855);
   graph2d->SetPoint(464,150,175,86.06517);
   graph2d->SetPoint(465,175,175,82.07607);
   graph2d->SetPoint(466,200,175,76.75999);
   graph2d->SetPoint(467,225,175,71.22749);
   graph2d->SetPoint(468,250,175,64.65525);
   graph2d->SetPoint(469,275,175,57.73959);
   graph2d->SetPoint(470,300,175,48.59844);
   graph2d->SetPoint(471,325,175,38.45247);
   graph2d->SetPoint(472,350,175,21.90964);
   graph2d->SetPoint(473,400,175,3.499867);
   graph2d->SetPoint(474,450,175,2.381917);
   graph2d->SetPoint(475,525,175,2.207815);
   graph2d->SetPoint(476,600,175,2.44551);
   graph2d->SetPoint(477,725,175,3.221583);
   graph2d->SetPoint(478,800,175,3.852738);
   graph2d->SetPoint(479,925,175,5.359386);
   graph2d->SetPoint(480,1000,175,6.440414);
   graph2d->SetPoint(481,1200,175,10.59133);
   graph2d->SetPoint(482,345,177,29.91299);
   graph2d->SetPoint(483,374,182,13.42699);
   graph2d->SetPoint(484,365,187,33.04992);
   graph2d->SetPoint(485,394,192,15.19698);
   graph2d->SetPoint(486,385,197,36.00537);
   graph2d->SetPoint(487,10,200,133.0668);
   graph2d->SetPoint(488,20,200,133.6862);
   graph2d->SetPoint(489,30,200,131.6867);
   graph2d->SetPoint(490,40,200,132.031);
   graph2d->SetPoint(491,50,200,129.1813);
   graph2d->SetPoint(492,60,200,130.3283);
   graph2d->SetPoint(493,70,200,131.5133);
   graph2d->SetPoint(494,80,200,130.2044);
   graph2d->SetPoint(495,90,200,129.0298);
   graph2d->SetPoint(496,100,200,127.121);
   graph2d->SetPoint(497,125,200,124.7369);
   graph2d->SetPoint(498,150,200,119.5762);
   graph2d->SetPoint(499,175,200,115.0716);
   graph2d->SetPoint(500,200,200,109.4828);
   graph2d->SetPoint(501,225,200,104.7475);
   graph2d->SetPoint(502,250,200,98.14846);
   graph2d->SetPoint(503,275,200,90.16501);
   graph2d->SetPoint(504,300,200,81.49433);
   graph2d->SetPoint(505,325,200,71.48801);
   graph2d->SetPoint(506,350,200,61.08255);
   graph2d->SetPoint(507,400,200,28.06272);
   graph2d->SetPoint(508,450,200,4.970954);
   graph2d->SetPoint(509,525,200,2.96286);
   graph2d->SetPoint(510,600,200,2.880856);
   graph2d->SetPoint(511,725,200,3.534777);
   graph2d->SetPoint(512,800,200,4.169762);
   graph2d->SetPoint(513,925,200,5.584048);
   graph2d->SetPoint(514,1000,200,6.672092);
   graph2d->SetPoint(515,1125,200,9.090097);
   graph2d->SetPoint(516,1200,200,10.96999);
   graph2d->SetPoint(517,414,202,17.31691);
   graph2d->SetPoint(518,405,207,39.20426);
   graph2d->SetPoint(519,434,212,19.32099);
   graph2d->SetPoint(520,425,217,42.70095);
   graph2d->SetPoint(521,454,222,21.67336);
   graph2d->SetPoint(522,445,227,46.86672);
   graph2d->SetPoint(523,474,232,24.42805);
   graph2d->SetPoint(524,465,237,51.13357);
   graph2d->SetPoint(525,494,242,26.72027);
   graph2d->SetPoint(526,485,247,54.55124);
   graph2d->SetPoint(527,10,250,235.0806);
   graph2d->SetPoint(528,20,250,231.9342);
   graph2d->SetPoint(529,30,250,232.1864);
   graph2d->SetPoint(530,40,250,230.057);
   graph2d->SetPoint(531,60,250,228.5114);
   graph2d->SetPoint(532,70,250,227.9141);
   graph2d->SetPoint(533,80,250,227.3618);
   graph2d->SetPoint(534,90,250,225.2493);
   graph2d->SetPoint(535,100,250,225.686);
   graph2d->SetPoint(536,125,250,222.8242);
   graph2d->SetPoint(537,150,250,217.9871);
   graph2d->SetPoint(538,175,250,211.2);
   graph2d->SetPoint(539,200,250,204.7165);
   graph2d->SetPoint(540,225,250,197.2154);
   graph2d->SetPoint(541,250,250,187.2561);
   graph2d->SetPoint(542,275,250,180.1357);
   graph2d->SetPoint(543,300,250,171.6849);
   graph2d->SetPoint(544,325,250,161.7628);
   graph2d->SetPoint(545,350,250,149.6585);
   graph2d->SetPoint(546,400,250,123.7164);
   graph2d->SetPoint(547,450,250,92.34368);
   graph2d->SetPoint(548,525,250,16.75367);
   graph2d->SetPoint(549,600,250,5.697557);
   graph2d->SetPoint(550,725,250,4.723052);
   graph2d->SetPoint(551,800,250,5.140217);
   graph2d->SetPoint(552,925,250,6.367156);
   graph2d->SetPoint(553,1000,250,7.521592);
   graph2d->SetPoint(554,1125,250,9.760615);
   graph2d->SetPoint(555,1200,250,11.73313);
   graph2d->SetPoint(556,514,252,30.05057);
   graph2d->SetPoint(557,505,257,60.38209);
   graph2d->SetPoint(558,534,262,33.07358);
   graph2d->SetPoint(559,525,267,66.0853);
   graph2d->SetPoint(560,554,272,36.55092);
   graph2d->SetPoint(561,545,277,70.01322);
   graph2d->SetPoint(562,574,282,40.0928);
   graph2d->SetPoint(563,565,287,76.71874);
   graph2d->SetPoint(564,594,292,44.25384);
   graph2d->SetPoint(565,585,297,82.82504);
   graph2d->SetPoint(566,10,300,393.7155);
   graph2d->SetPoint(567,20,300,384.4208);
   graph2d->SetPoint(568,30,300,383.7436);
   graph2d->SetPoint(569,40,300,380.9706);
   graph2d->SetPoint(570,50,300,384.7132);
   graph2d->SetPoint(571,60,300,382.9386);
   graph2d->SetPoint(572,70,300,382.6466);
   graph2d->SetPoint(573,80,300,380.0258);
   graph2d->SetPoint(574,90,300,375.7519);
   graph2d->SetPoint(575,100,300,375.5883);
   graph2d->SetPoint(576,125,300,372.1347);
   graph2d->SetPoint(577,150,300,367.4897);
   graph2d->SetPoint(578,175,300,361.4994);
   graph2d->SetPoint(579,200,300,352.3974);
   graph2d->SetPoint(580,225,300,345.2621);
   graph2d->SetPoint(581,250,300,334.042);
   graph2d->SetPoint(582,275,300,317.0905);
   graph2d->SetPoint(583,300,300,313.1248);
   graph2d->SetPoint(584,325,300,298.5739);
   graph2d->SetPoint(585,350,300,287.5736);
   graph2d->SetPoint(586,400,300,255.4843);
   graph2d->SetPoint(587,450,300,219.2671);
   graph2d->SetPoint(588,525,300,158.5651);
   graph2d->SetPoint(589,600,300,68.35241);
   graph2d->SetPoint(590,725,300,8.453384);
   graph2d->SetPoint(591,800,300,7.385876);
   graph2d->SetPoint(592,925,300,7.74625);
   graph2d->SetPoint(593,1000,300,8.80748);
   graph2d->SetPoint(594,1125,300,10.96797);
   graph2d->SetPoint(595,1200,300,12.82687);
   graph2d->SetPoint(596,10,400,982.3812);
   graph2d->SetPoint(597,20,400,945.8023);
   graph2d->SetPoint(598,30,400,944.4181);
   graph2d->SetPoint(599,40,400,943.2885);
   graph2d->SetPoint(600,50,400,956.2994);
   graph2d->SetPoint(601,60,400,946.6069);
   graph2d->SetPoint(602,70,400,943.3488);
   graph2d->SetPoint(603,80,400,942.0926);
   graph2d->SetPoint(604,90,400,951.8344);
   graph2d->SetPoint(605,100,400,940.8209);
   graph2d->SetPoint(606,125,400,938.0826);
   graph2d->SetPoint(607,150,400,914.8867);
   graph2d->SetPoint(608,175,400,913.1033);
   graph2d->SetPoint(609,200,400,901.423);
   graph2d->SetPoint(610,225,400,893.5474);
   graph2d->SetPoint(611,250,400,869.9564);
   graph2d->SetPoint(612,275,400,855.3342);
   graph2d->SetPoint(613,300,400,839.7473);
   graph2d->SetPoint(614,325,400,824.6034);
   graph2d->SetPoint(615,350,400,807.151);
   graph2d->SetPoint(616,400,400,750.2086);
   graph2d->SetPoint(617,450,400,705.5563);
   graph2d->SetPoint(618,525,400,628.3632);
   graph2d->SetPoint(619,600,400,520.8774);
   graph2d->SetPoint(620,725,400,321.6763);
   graph2d->SetPoint(621,800,400,143.0896);
   graph2d->SetPoint(622,925,400,20.73488);
   graph2d->SetPoint(623,1000,400,16.62641);
   graph2d->SetPoint(624,1125,400,16.34292);
   graph2d->SetPoint(625,1200,400,17.41647);
   for(int i=1; i<=1200; i++) { for(int j=1; j<=400; j++) {
    if(j>3*i && j>=10) triangulation->SetBinContent(i,j,100);
    else if(j>395) triangulation->SetBinContent(i,j,TMath::Min(10.,TMath::Max(0.1,graph2d->Interpolate(i-.01,j-.01))));
    else triangulation->SetBinContent(i,j,TMath::Min(10.,TMath::Max(0.1,graph2d->Interpolate(i+.01,j+.01))));
   }}
   
   triangulation->SetMaximum(5);
   triangulation->SetMinimum(0.1);
   triangulation->GetXaxis()->SetRangeUser(0,1200);
   triangulation->GetYaxis()->SetRangeUser(0,400);
   triangulation->Draw("colz");
   triangulation->GetXaxis()->SetTitle("m_{A} [GeV]");
   triangulation->GetYaxis()->SetTitle("m_{#chi} [GeV]");
   triangulation->GetXaxis()->SetTitleOffset(1.5);
   triangulation->GetYaxis()->SetTitleOffset(1.5);
   triangulation->GetZaxis()->SetTitle("95% C.L. observed limit on #sigma_{obs}/#sigma_{theo}");
 
   Double_t _fx1[14] = {
   467.5517,
   464.6446,
   439.2374,
   401.7937,
   354.2422,
   305.8115,
   266.0165,
   238.2166,
   217.8712,
   203.8091,
   190.4207,
   179.9639,
   151.5296,
   120.9205};
   Double_t _fy1[14] = {
   1.287552,
   42.20308,
   77.37501,
   102.5214,
   113.1802,
   110.1866,
   100.4143,
   91.72272,
   84.06628,
   82.26399,
   73.75899,
   73.15532,
   63.2815,
   52.16918};
   TGraph *graph1 = new TGraph(14,_fx1,_fy1);
   graph1->SetName("");
   graph1->SetTitle("");
   graph1->SetFillColor(1);
   graph1->SetLineWidth(2);
   graph1->SetMarkerStyle(20);
   graph1->SetMarkerSize(0.8);
   
   TH1F *Graph_Graph1 = new TH1F("Graph_Graph1","",100,86.25737,502.2149);
   Graph_Graph1->SetMinimum(0);
   Graph_Graph1->SetMaximum(124.3695);
   Graph_Graph1->SetDirectory(0);
   Graph_Graph1->SetStats(0);
   Graph_Graph1->SetLineStyle(0);
   Graph_Graph1->SetMarkerStyle(20);
   Graph_Graph1->GetXaxis()->SetLabelFont(42);
   Graph_Graph1->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph1->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph1->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph1->GetXaxis()->SetTitleFont(42);
   Graph_Graph1->GetYaxis()->SetLabelFont(42);
   Graph_Graph1->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph1->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph1->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph1->GetYaxis()->SetTitleFont(42);
   Graph_Graph1->GetZaxis()->SetLabelFont(42);
   Graph_Graph1->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph1->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph1->GetZaxis()->SetTitleFont(42);
   graph1->SetHistogram(Graph_Graph1);
   
   graph1->Draw("c s");
   
   Double_t _fx2[14] = {
   367.6158,
   368.3536,
   354.2413,
   330.9124,
   302.2184,
   269.2519,
   244.1856,
   226.1252,
   209.0782,
   195.9379,
   174.8667,
   147.8328,
   113.0116,
   48.27356};
   Double_t _fy2[14] = {
   1.187616,
   29.57322,
   54.91901,
   73.83499,
   84.4721,
   83.94025,
   81.60421,
   81.01437,
   75.22519,
   71.01271,
   69.06426,
   56.67236,
   46.65321,
   20.84815};
   TGraph *graph2 = new TGraph(14,_fx2,_fy2);
   graph2->SetName("");
   graph2->SetTitle("");
   graph2->SetFillColor(1);
   graph2->SetLineStyle(2);
   graph2->SetLineWidth(2);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#cccccc");
   graph2->SetMarkerColor(ci);
   graph2->SetMarkerStyle(20);
   graph2->SetMarkerSize(0.8);
   
   TH1F *Graph_Graph2 = new TH1F("Graph_Graph2","",100,16.26556,400.3616);
   Graph_Graph2->SetMinimum(0);
   Graph_Graph2->SetMaximum(92.80054);
   Graph_Graph2->SetDirectory(0);
   Graph_Graph2->SetStats(0);
   Graph_Graph2->SetLineStyle(0);
   Graph_Graph2->SetMarkerStyle(20);
   Graph_Graph2->GetXaxis()->SetLabelFont(42);
   Graph_Graph2->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph2->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph2->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph2->GetXaxis()->SetTitleFont(42);
   Graph_Graph2->GetYaxis()->SetLabelFont(42);
   Graph_Graph2->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph2->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph2->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph2->GetYaxis()->SetTitleFont(42);
   Graph_Graph2->GetZaxis()->SetLabelFont(42);
   Graph_Graph2->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph2->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph2->GetZaxis()->SetTitleFont(42);
   graph2->SetHistogram(Graph_Graph2);
   
   graph2->Draw("c s");
   
   Double_t _fx3[14] = {
   587.4477,
   590.7393,
   564.8672,
   513.9956,
   440.4482,
   385.3148,
   345.387,
   313.1133,
   286.3094,
   267.2142,
   249.9483,
   206.0547,
   158.1022,
   65.49045};
   Double_t _fy3[14] = {
   1.337448,
   55.29968,
   103.62,
   135.7952,
   139.6016,
   136.5179,
   132.4823,
   125.0661,
   112.9775,
   110.0743,
   104.4014,
   87.17297,
   67.73958,
   30.21399};
   TGraph *graph3 = new TGraph(14,_fx3,_fy3);
   graph3->SetName("");
   graph3->SetTitle("");
   graph3->SetFillColor(1);
   graph3->SetLineStyle(2);
   graph3->SetLineWidth(2);

   ci = TColor::GetColor("#cccccc");
   graph3->SetMarkerColor(ci);
   graph3->SetMarkerStyle(20);
   graph3->SetMarkerSize(0.8);
   
   TH1F *Graph_Graph3 = new TH1F("Graph_Graph3","",100,12.96556,643.2642);
   Graph_Graph3->SetMinimum(0);
   Graph_Graph3->SetMaximum(153.4281);
   Graph_Graph3->SetDirectory(0);
   Graph_Graph3->SetStats(0);
   Graph_Graph3->SetLineStyle(0);
   Graph_Graph3->SetMarkerStyle(20);
   Graph_Graph3->GetXaxis()->SetLabelFont(42);
   Graph_Graph3->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph3->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph3->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph3->GetXaxis()->SetTitleFont(42);
   Graph_Graph3->GetYaxis()->SetLabelFont(42);
   Graph_Graph3->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph3->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph3->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph3->GetYaxis()->SetTitleFont(42);
   Graph_Graph3->GetZaxis()->SetLabelFont(42);
   Graph_Graph3->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph3->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph3->GetZaxis()->SetTitleFont(42);
   graph3->SetHistogram(Graph_Graph3);
   
   graph3->Draw("c s");
   
   Double_t _fx4[13] = {
   426.2478,
   432.7702,
   417.6973,
   388.8148,
   353.99,
   315.4473,
   285.1163,
   260.7222,
   242.647,
   227.1302,
   213.2686,
   173.9607,
   125.6712};
   Double_t _fy4[13] = {
   1.206248,
   36.71228,
   69.06737,
   92.5419,
   105.4586,
   104.8369,
   100.817,
   93.99682,
   90.64914,
   87.60256,
   81.77132,
   71.41981,
   52.02895};
   TGraph *graph4 = new TGraph(13,_fx4,_fy4);
   graph4->SetName("");
   graph4->SetTitle("");
   graph4->SetFillColor(1);

   ci = TColor::GetColor("#ff0000");
   graph4->SetLineStyle(4);
   graph4->SetLineColor(ci);
   graph4->SetLineWidth(2);

   ci = TColor::GetColor("#ff0000");
   graph4->SetMarkerColor(ci);
   graph4->SetMarkerStyle(20);
   graph4->SetMarkerSize(0.8);
   
   TH1F *Graph_Graph4 = new TH1F("Graph_Graph4","",100,94.96128,463.4801);
   Graph_Graph4->SetMinimum(0);
   Graph_Graph4->SetMaximum(115.8838);
   Graph_Graph4->SetDirectory(0);
   Graph_Graph4->SetStats(0);
   Graph_Graph4->SetLineStyle(0);
   Graph_Graph4->SetMarkerStyle(20);
   Graph_Graph4->GetXaxis()->SetLabelFont(42);
   Graph_Graph4->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph4->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph4->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph4->GetXaxis()->SetTitleFont(42);
   Graph_Graph4->GetYaxis()->SetLabelFont(42);
   Graph_Graph4->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph4->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph4->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph4->GetYaxis()->SetTitleFont(42);
   Graph_Graph4->GetZaxis()->SetLabelFont(42);
   Graph_Graph4->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph4->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph4->GetZaxis()->SetTitleFont(42);
   graph4->SetHistogram(Graph_Graph4);
   
   graph4->Draw("c s");
   
   Double_t _fx5[14] = {
   392.5598,
   401.194,
   386.7686,
   359.3754,
   327.9309,
   292.8911,
   264.7587,
   243.1378,
   226.8109,
   212.55,
   199.9611,
   168.7521,
   130.4409,
   55.24912};
   Double_t _fy5[14] = {
   1.19256,
   33.06196,
   61.8707,
   82.37652,
   94.1037,
   94.03052,
   90.26407,
   85.79884,
   83.68409,
   80.52051,
   78.74658,
   62.27438,
   51.5164,
   23.91887};
   TGraph *graph5 = new TGraph(14,_fx5,_fy5);
   graph5->SetName("");
   graph5->SetTitle("");
   graph5->SetFillColor(1);

   ci = TColor::GetColor("#ff0000");
   graph5->SetLineColor(ci);
   graph5->SetLineStyle(3);
   graph5->SetLineWidth(2);
   graph5->SetMarkerColor(2);
   graph5->SetMarkerStyle(20);
   graph5->SetMarkerSize(0.8);
   
   TH1F *Graph_Graph5 = new TH1F("Graph_Graph5","",100,20.65463,435.7885);
   Graph_Graph5->SetMinimum(0);
   Graph_Graph5->SetMaximum(103.3948);
   Graph_Graph5->SetDirectory(0);
   Graph_Graph5->SetStats(0);
   Graph_Graph5->SetLineStyle(0);
   Graph_Graph5->SetMarkerStyle(20);
   Graph_Graph5->GetXaxis()->SetLabelFont(42);
   Graph_Graph5->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph5->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph5->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph5->GetXaxis()->SetTitleFont(42);
   Graph_Graph5->GetYaxis()->SetLabelFont(42);
   Graph_Graph5->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph5->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph5->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph5->GetYaxis()->SetTitleFont(42);
   Graph_Graph5->GetZaxis()->SetLabelFont(42);
   Graph_Graph5->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph5->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph5->GetZaxis()->SetTitleFont(42);
   graph5->SetHistogram(Graph_Graph5);
   
   graph5->Draw("c s");
   
   Double_t _fx6[15] = {
   472.8078,
   479.1157,
   465.6224,
   436.5313,
   403.9601,
   364.7362,
   331.3912,
   303.9902,
   280.8615,
   262.6928,
   247.0837,
   233.1506,
   194.2918,
   148.6257,
   62.18772};
   Double_t _fy6[15] = {
   1.232808,
   37.27383,
   70.81893,
   95.85207,
   112.9806,
   116.9153,
   115.769,
   112.0051,
   105.3031,
   100.6863,
   96.19395,
   91.819,
   80.10797,
   63.27247,
   27.79223};
   TGraph *graph6 = new TGraph(15,_fx6,_fy6);
   graph6->SetName("");
   graph6->SetTitle("");
   graph6->SetFillColor(1);

   ci = TColor::GetColor("#ff0000");
   graph6->SetLineColor(ci);
   graph6->SetLineStyle(3);
   graph6->SetLineWidth(2);
   graph6->SetMarkerColor(2);
   graph6->SetMarkerStyle(20);
   graph6->SetMarkerSize(0.8);
   
   TH1F *Graph_Graph6 = new TH1F("Graph_Graph6","",100,20.49492,520.8085);
   Graph_Graph6->SetMinimum(0);
   Graph_Graph6->SetMaximum(128.4835);
   Graph_Graph6->SetDirectory(0);
   Graph_Graph6->SetStats(0);
   Graph_Graph6->SetLineStyle(0);
   Graph_Graph6->SetMarkerStyle(20);
   Graph_Graph6->GetXaxis()->SetLabelFont(42);
   Graph_Graph6->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph6->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph6->GetXaxis()->SetTitleFont(42);
   Graph_Graph6->GetYaxis()->SetLabelFont(42);
   Graph_Graph6->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph6->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph6->GetYaxis()->SetTitleFont(42);
   Graph_Graph6->GetZaxis()->SetLabelFont(42);
   Graph_Graph6->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph6->GetZaxis()->SetTitleFont(42);
   graph6->SetHistogram(Graph_Graph6);
   
   graph6->Draw("c s");
   
   TPaveText *pt = new TPaveText(0.55,0.946,0.84,0.996,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetLineColor(0);
   pt->SetTextFont(42);
   TText *AText = pt->AddText("12.9 fb^{-1} (13 TeV)");
   AText->SetTextAlign(22);
   pt->Draw();
   
   pt = new TPaveText(0.17,0.845,0.37,0.908,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetLineColor(0);
   pt->SetTextFont(42);
   AText = pt->AddText("#splitline{#bf{CMS}}{#it{Preliminary}}");
   AText->SetTextAlign(22);
   pt->Draw();
   
   pt = new TPaveText(0.55,0.6,0.75,0.68,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetLineColor(0);
   pt->SetTextFont(42);
   pt->SetTextSize(0.035);
   AText = pt->AddText("Axial-vector mediator");
   AText->SetTextAlign(22);
   pt->Draw();
   
   pt = new TPaveText(0.55,0.52,0.75,0.6,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetLineColor(0);
   pt->SetTextFont(42);
   pt->SetTextSize(0.035);
   AText = pt->AddText("Dirac fermion #chi");
   AText->SetTextAlign(22);
   pt->Draw();
   
   pt = new TPaveText(0.55,0.44,0.75,0.52,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetLineColor(0);
   pt->SetTextFont(42);
   pt->SetTextSize(0.035);
   AText = pt->AddText("#it{g}_{#chi}=1, #it{g}_{q}=0.25");
   AText->SetTextAlign(22);
   pt->Draw();
   
   TLegend *leg = new TLegend(0.45,0.75,0.78,0.9,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("NULL","#sigma/#sigma_{theo}=1:","h");

   leg->AddEntry(graph1, "Expected Limit", "L");
   leg->AddEntry(graph2, "Expected #pm1#sigma", "L");
   leg->AddEntry(graph4, "Observed Limit", "L");
   leg->AddEntry(graph5, "Theory Uncertainty", "L");
   leg->Draw();
   t2->Modified();
   c2->cd();
   c2->Modified();
   c2->cd();
   c2->SetSelected(c2);
   c2->Print("Limit_Mx_MA_obs_0p25.png");
   c2->Print("Limit_Mx_MA_obs_0p25.pdf");

   TFile* f= new TFile("monoz_exo16038_A.root","RECREATE");
   graph2d->Write("g_obs");
   triangulation->Write("h_obs");



}
