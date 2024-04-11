BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "authentification_subscriber" (
	"id"	integer NOT NULL,
	"email"	varchar(254) NOT NULL UNIQUE,
	"subscribed_at"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (1,'contenttypes','0001_initial','2024-04-03 03:49:03.753395'),
 (2,'auth','0001_initial','2024-04-03 03:49:03.762356'),
 (3,'admin','0001_initial','2024-04-03 03:49:03.769225'),
 (4,'admin','0002_logentry_remove_auto_add','2024-04-03 03:49:03.776972'),
 (5,'admin','0003_logentry_add_action_flag_choices','2024-04-03 03:49:03.781246'),
 (6,'contenttypes','0002_remove_content_type_name','2024-04-03 03:49:03.791220'),
 (7,'auth','0002_alter_permission_name_max_length','2024-04-03 03:49:03.797882'),
 (8,'auth','0003_alter_user_email_max_length','2024-04-03 03:49:03.803390'),
 (9,'auth','0004_alter_user_username_opts','2024-04-03 03:49:03.807227'),
 (10,'auth','0005_alter_user_last_login_null','2024-04-03 03:49:03.812704'),
 (11,'auth','0006_require_contenttypes_0002','2024-04-03 03:49:03.813604'),
 (12,'auth','0007_alter_validators_add_error_messages','2024-04-03 03:49:03.816990'),
 (13,'auth','0008_alter_user_username_max_length','2024-04-03 03:49:03.822780'),
 (14,'auth','0009_alter_user_last_name_max_length','2024-04-03 03:49:03.828827'),
 (15,'auth','0010_alter_group_name_max_length','2024-04-03 03:49:03.835730'),
 (16,'auth','0011_update_proxy_permissions','2024-04-03 03:49:03.840234'),
 (17,'auth','0012_alter_user_first_name_max_length','2024-04-03 03:49:03.845998'),
 (18,'sessions','0001_initial','2024-04-03 03:49:03.848228'),
 (19,'authentification','0001_initial','2024-04-07 00:31:17.449314'),
 (20,'authentification','0002_post','2024-04-07 03:46:09.713388'),
 (21,'authentification','0003_delete_post','2024-04-07 06:57:04.092634');
INSERT INTO "django_admin_log" ("id","object_id","object_repr","action_flag","change_message","content_type_id","user_id","action_time") VALUES (1,'2','koffi',3,'',4,1,'2024-04-03 05:18:27.536197'),
 (2,'4','8ll8ll',3,'',4,1,'2024-04-03 07:26:56.830984'),
 (3,'3','koffi',3,'',4,1,'2024-04-03 07:26:56.833107'),
 (4,'5','wayou',3,'',4,1,'2024-04-03 07:26:56.834064'),
 (5,'6','koffi',3,'',4,1,'2024-04-03 07:28:39.127677'),
 (6,'7','lol',3,'',4,1,'2024-04-03 07:39:09.950990'),
 (7,'8','lol',3,'',4,1,'2024-04-03 08:04:04.368379'),
 (8,'1','admin',2,'[{"changed": {"fields": ["First name", "Last name"]}}]',4,1,'2024-04-03 08:04:40.700501'),
 (9,'9','Bileh',3,'',4,1,'2024-04-05 06:07:18.760431'),
 (10,'10','uspme',3,'',4,1,'2024-04-05 06:07:18.762407'),
 (11,'11','8ll8ll',3,'',4,1,'2024-04-05 06:16:59.321951'),
 (12,'12','8ll8ll',3,'',4,1,'2024-04-05 06:19:25.672975'),
 (13,'13','8ll8ll',3,'',4,1,'2024-04-05 06:23:24.199119'),
 (14,'14','8ll8ll',3,'',4,1,'2024-04-05 06:24:51.523582'),
 (15,'15','8ll8ll',3,'',4,1,'2024-04-05 06:29:53.019016'),
 (16,'16','8ll8ll',3,'',4,1,'2024-04-05 06:32:50.563956'),
 (17,'17','8ll8ll',3,'',4,1,'2024-04-05 06:37:08.225975'),
 (18,'18','8ll8ll',3,'',4,1,'2024-04-05 06:39:22.731413'),
 (19,'19','8ll8ll',3,'',4,1,'2024-04-05 06:41:39.059731'),
 (20,'20','8ll8ll',3,'',4,1,'2024-04-05 06:42:52.409420'),
 (21,'21','8ll8ll',3,'',4,1,'2024-04-05 06:48:22.791191'),
 (22,'22','8ll8ll',3,'',4,1,'2024-04-05 06:56:22.626605'),
 (23,'23','8ll8ll',3,'',4,1,'2024-04-05 07:04:20.014081'),
 (24,'24','8ll8ll',3,'',4,1,'2024-04-05 07:12:05.350413'),
 (25,'25','8ll8ll',3,'',4,1,'2024-04-05 07:25:00.030478'),
 (26,'26','8ll8ll',3,'',4,1,'2024-04-05 07:27:31.920611'),
 (27,'27','8ll8ll',3,'',4,1,'2024-04-05 07:35:17.031636'),
 (28,'28','8ll8ll',3,'',4,1,'2024-04-05 07:41:57.585182'),
 (29,'29','8ll8ll',3,'',4,1,'2024-04-05 07:44:43.928195'),
 (30,'30','8ll8ll',3,'',4,1,'2024-04-05 07:57:57.969184'),
 (31,'31','8ll8ll',3,'',4,1,'2024-04-05 08:00:50.409631'),
 (32,'32','8ll8ll',3,'',4,1,'2024-04-05 08:21:17.865685'),
 (33,'33','8ll8ll',3,'',4,1,'2024-04-05 08:27:21.847247'),
 (34,'34','8ll8ll',3,'',4,1,'2024-04-05 08:33:11.588245'),
 (35,'35','8ll8ll',3,'',4,1,'2024-04-05 08:35:10.906169'),
 (36,'36','8ll8ll',3,'',4,1,'2024-04-05 08:43:45.183707'),
 (37,'37','8ll8ll',3,'',4,1,'2024-04-05 08:59:45.991474'),
 (38,'38','koffi',3,'',4,1,'2024-04-05 09:11:20.155653'),
 (39,'39','koffi',3,'',4,1,'2024-04-05 09:19:45.036544'),
 (40,'1','wiconsa2014@gmail.com',3,'',7,1,'2024-04-07 00:34:45.601013'),
 (41,'2','wiconsa2014@gmail.com',3,'',7,1,'2024-04-07 00:41:25.562991'),
 (42,'3','wiconsa2014@gmail.com',3,'',7,1,'2024-04-07 00:44:23.720362'),
 (43,'4','wiconsa2014@gmail.com',3,'',7,1,'2024-04-07 00:46:05.860601'),
 (44,'5','wiconsa2014@gmail.com',3,'',7,1,'2024-04-07 00:48:07.495355'),
 (45,'41','8ll8ll',3,'',4,1,'2024-04-07 06:15:21.959035'),
 (46,'42','8ll8ll',3,'',4,1,'2024-04-07 06:18:18.775416'),
 (47,'43','8ll8ll',3,'',4,1,'2024-04-07 06:21:34.383603'),
 (48,'44','8ll8ll',3,'',4,1,'2024-04-07 06:23:27.098279'),
 (49,'45','8ll8ll',3,'',4,1,'2024-04-07 06:31:47.261990'),
 (50,'46','8ll8ll',3,'',4,1,'2024-04-07 06:42:30.540476'),
 (51,'48','BRIGHT',3,'',4,1,'2024-04-08 16:07:37.452886');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (1,'admin','logentry'),
 (2,'auth','permission'),
 (3,'auth','group'),
 (4,'auth','user'),
 (5,'contenttypes','contenttype'),
 (6,'sessions','session'),
 (7,'authentification','subscriber'),
 (8,'authentification','post');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (1,1,'add_logentry','Can add log entry'),
 (2,1,'change_logentry','Can change log entry'),
 (3,1,'delete_logentry','Can delete log entry'),
 (4,1,'view_logentry','Can view log entry'),
 (5,2,'add_permission','Can add permission'),
 (6,2,'change_permission','Can change permission'),
 (7,2,'delete_permission','Can delete permission'),
 (8,2,'view_permission','Can view permission'),
 (9,3,'add_group','Can add group'),
 (10,3,'change_group','Can change group'),
 (11,3,'delete_group','Can delete group'),
 (12,3,'view_group','Can view group'),
 (13,4,'add_user','Can add user'),
 (14,4,'change_user','Can change user'),
 (15,4,'delete_user','Can delete user'),
 (16,4,'view_user','Can view user'),
 (17,5,'add_contenttype','Can add content type'),
 (18,5,'change_contenttype','Can change content type'),
 (19,5,'delete_contenttype','Can delete content type'),
 (20,5,'view_contenttype','Can view content type'),
 (21,6,'add_session','Can add session'),
 (22,6,'change_session','Can change session'),
 (23,6,'delete_session','Can delete session'),
 (24,6,'view_session','Can view session'),
 (25,7,'add_subscriber','Can add subscriber'),
 (26,7,'change_subscriber','Can change subscriber'),
 (27,7,'delete_subscriber','Can delete subscriber'),
 (28,7,'view_subscriber','Can view subscriber'),
 (29,8,'add_post','Can add post'),
 (30,8,'change_post','Can change post'),
 (31,8,'delete_post','Can delete post'),
 (32,8,'view_post','Can view post');
INSERT INTO "auth_user" ("id","password","last_login","is_superuser","username","last_name","email","is_staff","is_active","date_joined","first_name") VALUES (1,'pbkdf2_sha256$390000$OGPsetMndytkK3a2tyKTVe$DNhEEg3t/Gjip2SpIJHwU74M8apOsvc5wSy9CjQm6lk=','2024-04-08 17:08:00.406931',1,'admin','Koffi','admin@gmail.com',1,1,'2024-04-03 03:50:37','Wilfried'),
 (40,'pbkdf2_sha256$390000$iqE4hnFzwO8tMdcRiKHN8E$R4Vdi92xie1hFWCcSsxV5zlIopqq4As9vcFeDeV0bUg=','2024-04-08 16:31:28.682130',0,'koffi','KOFFI','wiconsa2014@gmail.com',0,1,'2024-04-05 09:20:06.460042','WILFRIED ARNAUD CONSTANTIN'),
 (47,'pbkdf2_sha256$390000$DfDHrlQHzHsr3CVDDUD2AC$gFY5etWbSO22VcqRQQuMk7lfV4oiPRB/8Fb4v2xq2uw=','2024-04-07 06:45:31.505652',0,'8ll8ll','Constantin','afrostudi000@gmail.com',0,1,'2024-04-07 06:43:20.945450','Koffi');
INSERT INTO "django_session" ("session_key","session_data","expire_date") VALUES ('y58h7851cv8lvzoa7rshs2sml9rrwj3w','e30:1rrt21:V3_Fqeo1_pRk1qRYFt2YK0xMkOSDj-q7BAfbgflXfz4','2024-04-17 05:19:29.615867'),
 ('g0xrazo0ql8hy8x12uyou2a6i9zk58ib','.eJxVjDEOwyAQBP9CHSFjDgMp0_sN6IC74CTCkrGrKH-PLblIim12ZvctAm5rCVujJUxZXIUSl98uYnpSPUB-YL3PMs11XaYoD0WetMlxzvS6ne7fQcFW9rVOED0qZdghZXCdQrXHALP20Hno-0FHMuQGtuSSBXasISN6a6yO4vMF2Js3qw:1rscAX:DJj7nxSz52vzDFF9bQZH1vZwz1AxUUxYxgOKTBgblRA','2024-04-19 05:31:17.597730'),
 ('o9ff15sm5in3y19tsr1jthekp9vb3t2v','.eJxVjDsOwjAQBe_iGlneXWcdUdJzBmv9CQ4gW4qTCnF3iJQC2jcz76W8bGvxW8-Ln5M6K2vU6XcMEh-57iTdpd6ajq2uyxz0ruiDdn1tKT8vh_t3UKSXbw0RhIWMHaIFZpp4yIE5kMM42WyIUmA7CrIzgghCMAqjc1YAkEm9P-ilNr4:1rtDdV:uHYyIU-pv833yAYH9X3O7M9yFw-_VZmQzsd-mDaxicU','2024-04-20 21:31:41.790244'),
 ('wk5h8kwjqf6d9pw6raj4lvpchu49bfep','.eJxVjDEOwyAQBP9CHSFjDgMp0_sN6IC74CTCkrGrKH-PLblIim12ZvctAm5rCVujJUxZXIUSl98uYnpSPUB-YL3PMs11XaYoD0WetMlxzvS6ne7fQcFW9rVOED0qZdghZXCdQrXHALP20Hno-0FHMuQGtuSSBXasISN6a6yO4vMF2Js3qw:1rtJee:3Dzmieh6tCM7mdxFUTBUZwGxU1aKUoLLEInfVSMD-PU','2024-04-21 03:57:16.885054'),
 ('p4jt8rre7pqrynpahnl9slstme81vczu','.eJxVjDkOwjAUBe_iGll2vEJJnzNYfzMOoETKUiHuDpFSQPtm5r1UgW1tZVtkLgOri_JJnX5HBHrIuBO-w3ibNE3jOg-od0UfdNH9xPK8Hu7fQYOlfeucDLiQg5BNKYKL1rGNpiMBD45CQO8tcuUOmdyZDKHL4KMQdlUqqfcHAcU44g:1rtMHT:ni8jYzfJfU5o6yZYqCrSf_xNLQsvGRt9jaEqEkatFuQ','2024-04-21 06:45:31.515323'),
 ('a056xs56otzljcoay8y8muonj7yz9pt7','eyJvYXV0aF9zdGF0ZSI6InlrdmdrdDNYZFhxWElnQmFyZmRiR1NVNnlFNTBRWCJ9:1ruGcS:d7C8KLI6HaFQyToFlhRN4n-cqHqIFoxY--fKNXlQewU','2024-04-23 18:54:56.476643');
INSERT INTO "authentification_subscriber" ("id","email","subscribed_at") VALUES (6,'wiconsa2014@gmail.com','2024-04-07 00:48:35.143102');
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
COMMIT;
