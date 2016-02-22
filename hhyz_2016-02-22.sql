# ************************************************************
# Sequel Pro SQL dump
# Version 4499
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.5.44)
# Database: hhyz
# Generation Time: 2016-02-22 13:59:27 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table alembic_version
# ------------------------------------------------------------

DROP TABLE IF EXISTS `alembic_version`;

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;

INSERT INTO `alembic_version` (`version_num`)
VALUES
	('c09253ee92b3');

/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table classification
# ------------------------------------------------------------

DROP TABLE IF EXISTS `classification`;

CREATE TABLE `classification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `parent_id` (`parent_id`),
  CONSTRAINT `classification_ibfk_1` FOREIGN KEY (`parent_id`) REFERENCES `classification` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `classification` WRITE;
/*!40000 ALTER TABLE `classification` DISABLE KEYS */;

INSERT INTO `classification` (`id`, `name`, `parent_id`)
VALUES
	(15,'电脑数码',NULL),
	(16,'家用电器',NULL),
	(17,'运动户外',NULL),
	(18,'服饰鞋包',NULL),
	(19,'个护化妆',NULL),
	(20,'母婴用品',NULL),
	(21,'日用百货',NULL),
	(22,'食品保健',NULL),
	(23,'礼品钟表',NULL),
	(24,'图书音像',NULL),
	(25,'玩模乐器',NULL),
	(26,'办公设备',NULL),
	(27,'家居家装',NULL),
	(28,'汽车用品',NULL),
	(29,'其他分类',NULL);

/*!40000 ALTER TABLE `classification` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table comments
# ------------------------------------------------------------

DROP TABLE IF EXISTS `comments`;

CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime DEFAULT NULL,
  `up` int(11) DEFAULT NULL,
  `down` int(11) DEFAULT NULL,
  `disabled` tinyint(1) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `post_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `parent_id` (`parent_id`),
  KEY `post_id` (`post_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`parent_id`) REFERENCES `comments` (`id`),
  CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`),
  CONSTRAINT `comments_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table post_tag
# ------------------------------------------------------------

DROP TABLE IF EXISTS `post_tag`;

CREATE TABLE `post_tag` (
  `post_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`post_id`,`tag_id`),
  KEY `tag_id` (`tag_id`),
  CONSTRAINT `post_tag_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`),
  CONSTRAINT `post_tag_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table posts
# ------------------------------------------------------------

DROP TABLE IF EXISTS `posts`;

CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `up` int(11) DEFAULT NULL,
  `down` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `special_title` varchar(255) DEFAULT NULL,
  `tags` varchar(128) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  `content` text,
  `disabled` tinyint(1) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  `from_name` varchar(64) DEFAULT NULL,
  `from_url` varchar(255) DEFAULT NULL,
  `classification_id` int(11) DEFAULT NULL,
  `category` varchar(64) DEFAULT NULL,
  `store` varchar(64) DEFAULT NULL,
  `collect` int(11) DEFAULT NULL,
  `comment_num` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `classification_id` (`classification_id`),
  CONSTRAINT `posts_ibfk_1` FOREIGN KEY (`classification_id`) REFERENCES `classification` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;

INSERT INTO `posts` (`id`, `up`, `down`, `title`, `special_title`, `tags`, `timestamp`, `link`, `content`, `disabled`, `img`, `from_name`, `from_url`, `classification_id`, `category`, `store`, `collect`, `comment_num`)
VALUES
	(129,0,0,' 凑单品：Aveeno Positively Nourishing Whipped Souffle 乳木果深层滋养护体乳 170g','$5.05（需coupon+S&S）','换新颜','2016-02-20 16:55:40','http://www.smzdm.com/gourl/AFE3D4720915D396/AA_HT_113','<p>目前170g在S&S订购条件下购买为5.64美元，可享受10%coupon后实付5.05美元，需满25美元发货，可以直邮中国，近期入手好价，建议凑单其他商品带回~</p><p>Aveeno 婴儿用品始创于1945年，1999年被美国强生公司收购成为其旗下品牌。这款Aveeno沐浴露，属于Positively Nourishing 深层滋养系列。</p><p>这款护体乳含有抗氧化的乳木果和可可脂以及天然燕麦精华，在24小时滋润肌肤保湿的同时，提供抗氧化效果，让肌肤保持水嫩健康，适合深秋及冬季使用。规格170g</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/1e4bdfb95ecd95a600ed8ffb7d516a7b\" width=400 height=300 class=\"content-img\" />',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/6b5be2124321765ef8e282725cacafe2','什么值得买','http://www.smzdm.com/',19,'白菜价','美国亚马逊',0,0),
	(130,0,0,' 新低价：zoomer Chomplingz Tiger Tail Dinosaur 智能恐龙电子玩具','£8.33+£6.67直邮中国（约¥140）','Zoomer','2016-02-20 16:55:43','http://www.smzdm.com/gourl/3062B6B363901138/AA_HT_93','<p>目前售价10英镑，下单退税后实际8.33英镑，支付运费6.67英镑，到手约140元，价格新低，相比</p><p>又降20元，需要注意商品3月1日有货，目前可提前锁价。</p><p>Zoomer Chomplingz Tiger Tail Dinosaur 智能恐龙电子玩具，在恐龙的鼻子和嘴巴部位有感应器；将食物放进恐龙嘴巴，恐龙嘴巴会动并发声发光，并会根据周围环境做出反应。推着它走，恐龙嘴巴会不停张合，恐龙前腿上下摇摆。尾巴也会随之摆动。大小为，25*13.4*17.5cm。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/313414ed09add36ee2893befc3583470\" width=400 height=300 class=\"content-img\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/9ba10e3427735dfe7ac8bc9eee861487','什么值得买','http://www.smzdm.com/',25,'白菜价','英国亚马逊',0,0),
	(131,0,0,' 凑单品：Burt\'s Bees 小蜜蜂 Intense Hydration Treatment Mask 深层补水免洗面膜','$9.99 ','Intense Hydration','2016-02-20 16:55:43','http://www.smzdm.com/gourl/6CD168205D7CA749/AA_HT_113','<p>目前此款特价至9.99美元，add-on单品，适合凑单带回，淘宝代购约130-300元，海淘有一定价格优势且保真。</p><p>Burt\'s Bees 小蜜蜂因为使用百分百纯天然提取物而颇受大家的认可，号称是“皮肤可以吃的保养品”，相信大家都很熟悉。这款小蜜蜂面膜，主打补水保湿，对于细纹干纹有一定的帮助；99%天然成分，含有芦荟、大豆蛋白等，鼠尾草成分，保湿锁水功效也比较不错；美亚用户评价4星半，反馈效果不错，皮肤滋润舒适又柔软。使用方法：洁面后，取适量涂于面部及颈部，约5-10分钟后，用纸巾拭去，然后按摩吸收即可。每周1-2次。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/dbef8299c958dbb25feec54c7be55d50\" width=400 height=300 class=\"content-img\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/532d84e588649786341c1b943a2abf16','什么值得买','http://www.smzdm.com/',19,'白菜价','美国亚马逊',0,0),
	(132,0,0,' FURLA 芙拉 Saffiano Leather Mini 女士斜挎包','€81+€14.04含税直邮（约￥685）','换新装','2016-02-20 16:55:43','http://www.smzdm.com/gourl/C108253C75298711/AA_HT_57','<p>目前枚红色特价至98.01欧元，加入购物车后自动退税为81欧元，可5.94欧元直邮中国，但需8.1欧元的直邮税费，到手约685元，库存有限，mini款斜挎包适合休闲出行~另外</p><p>色、</p><p>均是同价。</p><p>FURLA 芙拉 mini款 女士斜挎包采用真皮材质，圆润的包型简洁大方，荔枝纹皮面凸显质感。同色系真皮拼链条款式增添一丝活泼。大小适合休闲出行。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/e49578af8529176598d73e0fcad1dd6c\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/9c7cefbe3607556972a17ac578b75136','什么值得买','http://www.smzdm.com/',18,'海淘精选','西班牙亚马逊',0,0),
	(133,0,0,' HYPERX 骇客神条 DDR3 1600 笔记本内存条 8GB*2条（cl9、马甲）','426.08元+15.94元直邮中国（约￥442）','送礼品','2016-02-20 16:55:43','http://www.smzdm.com/gourl/E42683074F3BC359/AA_HT_163','<p>目前售价426.36元，直邮到手约442元，新低价，目前国内这款内存条价格看涨，需要的网友可以关注一下。</p><p>金士顿笔记本内存高端系列HyperX 骇客神条，DDR3，1600Mhz，8G容量，1.35V电压，CL=9，一款低电压、低时序的马甲条，适合游戏本升级内存或者小超频使用。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/2e766c9b3841def1967fb5b54241345a\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/2e766c9b3841def1967fb5b54241345a','什么值得买','http://www.smzdm.com/',15,'海淘精选','亚马逊海外购',0,0),
	(134,0,0,' PHILIPS 飞利浦 Sonicare Diamondclean系列 HX6068/26 电动牙刷刷头','£26.66+£5.36直邮中国（约￥301）','焕新居','2016-02-20 16:55:43','http://www.smzdm.com/gourl/966AA75F4966E237/AA_HT_27','<p>目前此款8支装31.99英镑，退税后实付26.66英镑，直邮中国运费5.36英镑，到手约合301元，平均每个38元。同款</p><p>3个装249元，着急可选择国内入手。对于这种消耗品来说，便宜一点是一点，直邮也很方便，小伙伴们凑单走起吧~</p><p>飞利浦HX6068/26电动刷头是飞利浦旗舰级电动牙刷DiamondClean系列HX9332、HX9362的替换刷头，是飞利浦目前最顶级的刷头，独创的仿钻石型菱形设计，刷毛增量44%，去除牙菌斑效果能达到手动牙刷的四倍，刷毛属于中等硬度，使用一周就可看到牙齿美白效果。作为顶级刷头价格比其余款式贵了不少，但是用钻石系列牙刷不搭配钻石刷头是个很憋屈的事情，坚持原装刷头的童鞋囤货可入。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/e18c15716141cf5cca33bee902aa4140\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/8579405b69cc58ecde32afb995cf98c5','什么值得买','http://www.smzdm.com/',16,'海淘精选','英国亚马逊',0,0),
	(135,0,0,' Pringles 品客 薯片 酸乳酪洋葱味 110g*11罐+凑单品','59元（99-40）','节日礼品','2016-02-20 16:55:43','http://www.smzdm.com/gourl/599C91467FECF4C7/AA_YH_95','<p>目前售价8.9元，参加</p><p>，下单</p><p>再凑单包</p><p>实付59元，合5.4元/罐，各渠道低价，喜欢这口味的童鞋又可以愉快的长肉了。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/9c6ba3c0821456b0f88965c24f83ab12\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/9c6ba3c0821456b0f88965c24f83ab12','什么值得买','http://www.smzdm.com/',22,'优惠精选','京东',0,0),
	(136,0,0,' 16点、移动端：HiWiFi 极路由 HC5661 极壹S无线路由器 腾讯视频&京东微联特别合作版','79元包邮','送礼品','2016-02-20 16:55:43','http://www.smzdm.com/gourl/FFE566B9D92AF718/AA_YH_163','<p>移动端16点掌上秒杀特价至79元包邮，已属该版本路由器的历史最低价，比上次推荐的还要低10元，有需求的值友可以到时候抢一个。</p><p>：腾讯视频&京东微联特别合作版，还外送1个月腾讯视频会员。</p><p>极壹S采用了两根5dBi高增益全向天线，无线信号覆盖更广。支持IEEE 802.11n标准，向下兼容IEEE 802.11b/g网络设备，理论可达到300Mbps的无线速率，较上一代产品提升一倍。机身仍采用全铝合金材质，阳极氧化喷砂。三个指示灯，分别指示系统、互联网和无线信号，直观看到运行状态。四个LAN口，增设SD卡槽插入SD卡，以拓展内存空间。去广告、appstore加速插件等等丰富的应用都是其特色，作为百元价位的智能路由还是有很多拥簇者的。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/341085e6143195d35816a116acf430e4\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/1bb0aacc83d0c241b88cb04fe605fb89','什么值得买','http://www.smzdm.com/',15,'优惠精选','京东',0,0),
	(137,0,0,' Microsoft 微软 Xbox One 家庭娱乐游戏机 + Kinect体感 + 4款游戏','$399，返$50礼品卡（约￥2800）','送礼品','2016-02-20 16:55:43','http://www.smzdm.com/gourl/C5334BD12B0885D0/AA_FX_163','<p>目前Xbox One+Kinect套装特价399美元，并且赠送50美元礼品卡，套装自带《舞动全身：夺目焦点》、《 Kinect体育竞技》和《动物园大亨》三个Kinect游戏，下单时还可再免费选择一款游戏。已经，不过需要转运才能到手。已经是近期较大的优惠力度了，不过需要转运或人肉带回。</p><p>XBOX ONE就不再详细介绍了，相对于PS4来说，Xbox One从外观以及接口配置来看，更像是一台电视机顶盒，配备HDMI IN的选择，也表明了其占领客厅的野心。虽然国内已经推出了行货，不过由于恼人的锁区问题和相对高昂的价格，并没有太大吸引力。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/a6c9bf4f324b2ef02f561f1dd645f489\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/9e309d771d42105a039ffa87f2d8090f','什么值得买','http://www.smzdm.com/',15,'海淘精选','Microsoft美国官方商城',0,0),
	(138,0,0,' KOHLER 科勒 72704T-B4-CP 花洒套装','1338元包邮（1598元，双重优惠）','Z秒杀','2016-02-20 16:55:43','http://www.smzdm.com/gourl/EA298717DC7F3A1A/AA_MS_37','<p>目前Z秒杀特价1438元，页面可领999减100优惠码，实付1338元包邮，近期好价，其他B2C渠道均在1499元以上了。</p><p>130多年历史的美国KOHLER科勒集团是卫浴、发电系统、家装等多个领域的顶尖品牌。这款KOHLER科勒72704T-B4-CP花洒套装，采用铸铜本体，外表面抛光镀铬处理。内部陶瓷阀芯，使用寿命更长。头顶花洒采用随心雨亲氧技术，出水前使水中融入氧气，使出水更柔和，节水的同时还能感受到犹如林中雨后的清新。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/33c719c02dfa16f69a16b4699cd81c95\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/e6f1e8ccccd3b451c3c1edc88868a2ea','什么值得买','http://www.smzdm.com/',27,'优惠精选','亚马逊中国',0,0),
	(139,0,0,' Calvin Klein Black Print Tunic 女童两件套','￥78.93起+￥28.39直邮中国（约￥108起）','换新装','2016-02-20 16:55:48','http://www.smzdm.com/gourl/841B41DDEF2F03CA/AA_HT_57','<p>目前售价78.93元起，支持28.39元直邮中国，到手约合108元起。其他尺码也是好价~</p><p>Calvin Klein Black Print Tunic 女童两件套，采用60%棉和40%涤纶材质，套装包含一件长袖T恤和一条长裤，简洁设计，可以机洗。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/3b98cce0539819e73ec5f8ad5a4433b6\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/b0709ab96246c1d3f286a32b52dfed01','什么值得买','http://www.smzdm.com/',18,'海淘精选','亚马逊海外购',0,0),
	(140,0,0,' GoodSmile “奸笑社” 进击的巨人 利威尔兵长 1/8 涂装完成品','7774日元+1866日元运费（约¥560）','进击的巨人','2016-02-20 16:55:48','http://www.smzdm.com/gourl/9A2DD039C29BC123/AA_HT_93','<p>售价8396日元，可直邮中国，退税后7774日元，运费1866日元，只是现在汇率不太友好，折合回人民币560元，相比</p><p>降价有限。兵长也是进击的人气王了，喜欢的朋友可以考虑。</p><p>利威尔·阿克曼，调查兵团的士兵长、调查兵团特别作战班班长、一米六的身高成功逆袭、单人战力相当于一个旅团，外表的冷酷和死鱼眼与细腻的内心形成强烈的对比，和三爷分别为进击的巨人中人气及实力最高的男女性角色。此款全高280mm，重1.1kg。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/d6bff782c553effadb3472dd205fe20b\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/9e520e7fafcbe4962619527a6eae43e0','什么值得买','http://www.smzdm.com/',25,'海淘精选','日本亚马逊',0,0),
	(141,0,0,' Nine West 玖熙 Katja 女士高跟鞋','$40.99（约￥325）','换新装','2016-02-20 16:55:48','http://www.smzdm.com/gourl/81429C3A060613E6/AA_HT_57','<p>目前尺码齐全，售价为40.99美元，转运到手约325元，虽然价格优势比较小，但胜在貌美，相对适合脚面相对窄的女生，喜欢的朋友可以入手了~</p><p>根据值友推荐：“这款Nine West Katja 女款真皮尖头高跟鞋，鞋面采用100%真皮材质构成，柔软有质感，一脚蹬款式方便穿脱，搭配近几年大热的尖头样式，以及鞋面的蝴蝶结饰物，整体性感又带些许可爱气质，内衬和鞋底都为人造材质，鞋跟高7.62cm”</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/6b78986764cbb916a3c2816b2d746b24\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/29f8f1e105a5887d261dfdfec2940e89','什么值得买','http://www.smzdm.com/',18,'海淘精选','6PM',0,0),
	(142,0,0,' Oral-B 欧乐B EB20-4 精准清洁型 电动牙刷头10只装','€20.66+€5.5直邮中国（约￥190）','焕新居','2016-02-20 16:55:48','http://www.smzdm.com/gourl/50D73692D9A69D17/AA_HT_27','<p>目前售价25欧元，选择国内地址收货退税价20.66欧元，5.5欧元直邮中国，到手价约190元，再到好价，需要的网友们可以下手了。</p><p>OralB 欧乐B EB20-4 电动牙刷头，适用于博朗欧乐B旗下所有电动牙刷（非声波），如DB4510、D12等，杯型刷头全面覆盖牙齿表面，有效去除牙菌斑和牙渍。显示型刷毛，提醒您及时更换刷头。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/07b45c90a828418001e74e332cc91f76\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/6198d06f98a034b5dd5d14da2bc5a055','什么值得买','http://www.smzdm.com/',16,'海淘精选','西班牙亚马逊',0,0),
	(143,0,0,' 限PRIME会员：AUSSIE Moist Conditioner 保湿护发素 （400ML*6瓶）','$11.94+$3.98直邮中国（约￥104）','换新颜','2016-02-20 16:55:49','http://www.smzdm.com/gourl/45769C122F70C245/AA_HT_113','<p>目前6瓶装售价为11.94美元，且支持3.98美元直邮中国，但需PRIME会员下单够阿米，6瓶装适合大家拼单购买，近期入手好价~</p><p>Aussie是澳大利亚著名的美发品牌。产品大致分为染发修护系列、奇迹水润系列、光彩发丝系列、海藻长发系列、卷发风情系列，以及一些头发特殊护理产品等。它家的Moist水润系列，口碑一向很好，值得尝试。</p><p>这款AUSSIE Moist Conditioner保湿护发素，含有芦荟保湿成分，配方温和无刺激，深层滋润，更适合干性发质、烫染后受损发质，味道也很宜人。很多女生在烫染后会有易断裂和发质干枯的问题，值得入手尝试。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/20703fa20b22552244c447e12bfd245d\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/b738637ec2702809ebdceb9c945e220a','什么值得买','http://www.smzdm.com/',19,'海淘精选','美国亚马逊',0,0),
	(144,0,0,' Delonghi 德龙 ECAM22.110.SB 家用 全自动咖啡机','€268.07+€29直邮中国（约￥2221）','焕新居','2016-02-20 16:55:49','https://www.computeruniverse.net/products/90539180/delonghi-ecam-22-110b-magnifica.asp','<p>目前德国电商平台</p><p>特价268.07欧元，再计入29欧元直邮运费+4.2欧元加固费以及4.87欧元的信用卡手续费，总计合306.14欧元，直邮到手约合2221元，对比国内同款产品拥有较大的价差，因此有需求的朋友可走海淘渠道购买。</p><p>作为意大利本土品牌，德龙不仅制造咖啡机，还生产其他厨房及生活电器，并先后收购了英国小家电生产商凯伍德（Kenwood）及德国博朗（Braun）的部分产品线。其咖啡机产品线较为丰富，这款意大利德龙 ECAM22.320.SB 是一款家用全自动咖啡机，配备手动卡布基诺系统，可为卡布基诺制作牛奶泡沫，可拆卸式咖啡杯盘和水箱。带有显示屏可直观看到模式状态，可根据个人的饮用量选择小中大杯等不同杯份，静音型咖啡豆研磨器同时具有13种研磨程度设置。另外可定制个性化的咖啡模式，咖啡机会自动记忆咖啡杯量。参数方面，CRF无管道系统以及快速泵压转换，更适合家用，水箱容量1.8L，泵压15BAR，静音磨豆器豆仓容量250g，对于家用而言绰绰有余。产品尺寸 (宽x长x高 cm):43cmx23.8cmx35.1cm。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/4e5005e5a78543e02dc381145fb049f2\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/4a5cadc3c05039a4dbc3164328137856','什么值得买','http://www.smzdm.com/',16,'海淘精选','computeruniverse',0,0),
	(145,0,0,' MI 小米 Note 64GB 顶配版 移动联通双4G','2138.08元','送礼品','2016-02-20 16:55:49','http://www.smzdm.com/gourl/736C28FDB027FA49/AA_YH_163','<p>目前降价至2138.08元，已是近期推荐最低的价格了，喜欢的值友不妨关注一下。</p><p>随着小米5发布会的临近，旧款机型降价销售也不新鲜。小米Note顶配版采用高通骁龙810处理器，虽然口碑一般，但也是820出现之前，高通最强的处理器了，除了发热其他都还好。除此之外，64GB的内存在使用时也更为从容，如今2000出头的价格，还是比较值的。</p><p>相对2299元的小米Note标配版，顶配版的小米Note除了处理器升级到高通目前最强的骁龙810，还使用了速度更快的4GB LPDDR4内存，屏幕也提升到了了2K分辨率（2560*1440），但是电池容量没有明显提升，所以续航时间可能不如标配版。不过小米Note顶配版采用了双充电模块，一个小时即可充满电池的70%，并且解决了快充技术普遍存在的发热问题。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/534d0e5638a4160cae8ccc7bbb2eb3e4\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/34c65261ebd3c7e8e6a5a097f835620b','什么值得买','http://www.smzdm.com/',15,'优惠精选','亚马逊中国',0,0),
	(146,0,0,' UGG australia Lace-Up Glitter  童款休闲鞋','$22.99（约￥230）','休闲鞋','2016-02-20 16:55:49','http://www.smzdm.com/gourl/219F8890E3D46513/AA_HT_57','<p>目前售价22.99美元，低至原价的3.8折，尺码齐全，两色可选，凑单转运到手约230元。</p><p>UGG在澳洲是雪地靴的通用名，而在澳洲以外，即我们通常所说的UGG，则指的是美国Deckers旗下的UGG Australia这个雪地靴的著名品牌。这款UGG australia Lace-Up Glitter童款休闲鞋，鞋面亮片设计。闪亮的外观外加经典系带休闲鞋造型，时尚大方。UGGpure®鞋垫可以保证穿着舒适。还有与RMAT专利技术合作的加厚塑模外底，柔韧性好，脚感更加舒适。而Treadlite技术的运用，采用了在干湿地面都有不错抓地力的橡胶，柔软有弹力，且经久耐磨</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/c1f5ec63d9e6f797469dfb8187d50b12\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/4fbf3fa2f0f8f48ecdd356c691148407','什么值得买','http://www.smzdm.com/',18,'海淘精选','6PM',0,0),
	(147,0,0,' 限M码：KENNETH COLE Ls 1 Pkt Sqr Print 男款长袖衬衫','￥106.93+￥26.09直邮中国（约￥133）','换新装','2016-02-20 16:55:49','http://www.smzdm.com/gourl/9E2E520297116C3B/AA_HT_57','<p>目前M码售价106.93元，支持26.09元直邮中国，到手约133元。配色比较清新，喜欢的上吧~</p><p>KENNETH COLE是来自美国的设计师品牌，目前品牌的服饰鞋包领域均有设计，产品以简洁耐看的款式而被大家所认同。这款KENNETH COLE Ls 1 Pkt Sqr Print 男款长袖衬衫，100%纯棉材质，修身美观、搭配西裤与牛仔裤均合适。可机洗。</p><img src=\"http://7xqubs.com1.z0.glb.clouddn.com/59b71bae11f7e552940a0131480ce3a9\" width=400 height=300 class=\"\"/>',NULL,'http://7xqubs.com1.z0.glb.clouddn.com/12abf0db5ba0c8821a0f5df4fe8fe256','什么值得买','http://www.smzdm.com/',18,'海淘精选','亚马逊海外购',0,0);

/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table roles
# ------------------------------------------------------------

DROP TABLE IF EXISTS `roles`;

CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `default` tinyint(1) DEFAULT NULL,
  `permissions` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_roles_default` (`default`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table tags
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tags`;

CREATE TABLE `tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table user_post
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user_post`;

CREATE TABLE `user_post` (
  `user_id` int(11) DEFAULT NULL,
  `post_id` int(11) DEFAULT NULL,
  KEY `user_id` (`user_id`),
  KEY `post_id` (`post_id`),
  CONSTRAINT `user_post_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `user_post_ibfk_2` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table users
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `permission` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `name` varchar(64) DEFAULT NULL,
  `phone` varchar(13) DEFAULT NULL,
  `gender` int(11) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `confirmed` int(11) DEFAULT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `member_since` datetime DEFAULT NULL,
  `last_seen` datetime DEFAULT NULL,
  `disabled` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_username` (`username`),
  UNIQUE KEY `ix_users_email` (`email`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;

INSERT INTO `users` (`id`, `username`, `email`, `password_hash`, `permission`, `role_id`, `name`, `phone`, `gender`, `age`, `confirmed`, `avatar`, `member_since`, `last_seen`, `disabled`)
VALUES
	(8,'cc959798','cc959798@163.com','pbkdf2:sha1:1000$DsFu1KkB$7fe6288d4de5dab6fc96404c09aec31eee0c52da',1,NULL,NULL,NULL,1,NULL,NULL,NULL,'2016-02-21 09:26:10','2016-02-21 09:26:10',0);

/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
