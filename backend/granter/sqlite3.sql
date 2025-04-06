-- -----------------------------------------------------
-- Schema startup_plus
-- -----------------------------------------------------
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS organization;
DROP TABLE IF EXISTS startup;
DROP TABLE IF EXISTS private_message;
DROP TABLE IF EXISTS topic;
DROP TABLE IF EXISTS organization_has_user;
DROP TABLE IF EXISTS topic_message;
DROP TABLE IF EXISTS file;
DROP TABLE IF EXISTS private_message_has_file;
DROP TABLE IF EXISTS topic_message_has_file;

-- -----------------------------------------------------
-- Table user
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  telegram_id INTEGER,
  email TEXT NOT NULL,
  password TEXT NOT NULL,
  role TEXT CHECK(role IN ('executor', 'customer')) NOT NULL,
  avatar BLOB
);

-- -----------------------------------------------------
-- Table organization
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS organization (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name TEXT NOT NULL,
  short_name TEXT,
  region TEXT NOT NULL,
  industry TEXT NOT NULL
);

-- -----------------------------------------------------
-- Table startup
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS startup (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  organization_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  description TEXT,
  status TEXT CHECK(status IN ('waiting', 'inprogress', 'done')) NOT NULL DEFAULT 'waiting',
  region TEXT,
  industry TEXT,
  direction TEXT,
  budget REAL,
  publish_date DATE NOT NULL,
  finish_date DATE NOT NULL,
  days INTEGER NOT NULL,
  FOREIGN KEY (organization_id) REFERENCES organization (id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table private_message
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS private_message (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  sender_id INTEGER NOT NULL,
  recipient_id INTEGER NOT NULL,
  text TEXT NOT NULL,
  sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  is_read INTEGER NOT NULL DEFAULT 0,
  FOREIGN KEY (sender_id) REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (recipient_id) REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table topic
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS topic (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  startup_id INTEGER NOT NULL,
  name TEXT NOT NULL UNIQUE,
  FOREIGN KEY (startup_id) REFERENCES startup (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table organization_has_user
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS organization_has_user (
  organization_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  role TEXT CHECK(role IN ('owner', 'participant')) NOT NULL,
  PRIMARY KEY (organization_id, user_id),
  FOREIGN KEY (organization_id) REFERENCES organization (id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table topic_message
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS topic_message (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  topic_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  text TEXT NOT NULL,
  is_read INTEGER NOT NULL DEFAULT 0,
  FOREIGN KEY (topic_id) REFERENCES topic (id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table file
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS file (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  data BLOB NOT NULL,
  user_id INTEGER NOT NULL,
  type TEXT CHECK(type IN ('file', 'photo', 'voice')) NOT NULL DEFAULT 'file',
  FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table private_message_has_file
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS private_message_has_file (
  private_message_id INTEGER NOT NULL,
  file_id INTEGER NOT NULL,
  PRIMARY KEY (private_message_id, file_id),
  FOREIGN KEY (private_message_id) REFERENCES private_message (id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (file_id) REFERENCES file (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table topic_message_has_file
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS topic_message_has_file (
  topic_message_id INTEGER NOT NULL,
  file_id INTEGER NOT NULL,
  PRIMARY KEY (topic_message_id, file_id),
  FOREIGN KEY (topic_message_id) REFERENCES topic_message (id

-- -----------------------------------------------------
-- Table notification
-- -----------------------------------------------------
DROP TABLE IF EXISTS notification;

CREATE TABLE IF NOT EXISTS notification (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  got_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  is_sent INTEGER NOT NULL DEFAULT 0,
  is_read INTEGER NOT NULL DEFAULT 0,
  type TEXT CHECK(type IN ('private', 'topic', 'startup')) NOT NULL,
  title TEXT NOT NULL,
  content TEXT,
  startup_id INTEGER,
  topic_message_id INTEGER,
  private_message_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (startup_id) REFERENCES startup (id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (topic_message_id) REFERENCES topic_message (id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (private_message_id) REFERENCES private_message (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Placeholder table for view organizations_and_users
-- -----------------------------------------------------
DROP VIEW IF EXISTS organizations_and_users;
CREATE VIEW IF NOT EXISTS organizations_and_users AS
SELECT 
    OU.user_id, U.username, U.email, U.role, OU.organization_id, O.full_name, O.short_name
FROM
    organization O
        JOIN
    organization_has_user OU ON O.id = OU.organization_id
        JOIN
    user U ON OU.user_id = U.id;

-- -----------------------------------------------------
-- Placeholder table for view users_and_files
-- -----------------------------------------------------
DROP VIEW IF EXISTS users_and_files;
CREATE VIEW IF NOT EXISTS users_and_files AS
SELECT 
    U.id AS user_id,
    U.username,
    U.name,
    U.telegram_id,
    U.email,
    U.password,
    U.role,
    U.avatar,
    F.id AS file_id,
    F.name AS file_name,
    F.data,
    F.type AS file_type
FROM
    user U
        JOIN
    file F ON U.id = F.user_id
WHERE
    F.type != 'voice';

-- -----------------------------------------------------
-- Trigger startup_AFTER_UPDATE
-- -----------------------------------------------------
DROP TRIGGER IF EXISTS startup_AFTER_UPDATE;
CREATE TRIGGER startup_AFTER_UPDATE AFTER UPDATE ON startup
FOR EACH ROW
BEGIN
    -- Получаем organization_id из таблицы startup
    DECLARE org_id_var INTEGER;
    SELECT organization_id INTO org_id_var FROM startup WHERE id = NEW.id;

    -- Вставляем уведомления для всех пользователей организации
    INSERT INTO notification (
        user_id,
        got_at,
        type,
        title,
        content,
        startup_id,
        topic_message_id,
        private_message_id
    )
    SELECT 
        ou.user_id,
        CURRENT_TIMESTAMP,
        'startup',
        'Статус стартапа изменён',
        NULL,
        NEW.id,
        NULL,
        NULL
    FROM organization_has_user ou
    WHERE ou.organization_id = org_id_var AND ou.user_id != NEW.user_id; -- Исключаем отправителя сообщения
END;

-- -----------------------------------------------------
-- Trigger private_message_AFTER_INSERT
-- -----------------------------------------------------
DROP TRIGGER IF EXISTS private_message_AFTER_INSERT;
CREATE TRIGGER private_message_AFTER_INSERT AFTER INSERT ON private_message
FOR EACH ROW 
BEGIN
    INSERT INTO notification
    (user_id, type, title, content, private_message_id)
    VALUES (NEW.recipient_id, 'private', 'Новое сообщение', NEW.text, NEW.id);
END;

-- -----------------------------------------------------
-- Trigger topic_message_AFTER_INSERT
-- -----------------------------------------------------
DROP TRIGGER IF EXISTS topic_message_AFTER_INSERT;
CREATE TRIGGER topic_message_AFTER_INSERT AFTER INSERT ON topic_message
FOR EACH ROW
BEGIN
    -- Объявляем переменные для хранения промежуточных значений
    DECLARE startup_id_var INTEGER;
    DECLARE org_id_var INTEGER;

    -- Получаем startup_id из таблицы topic
    SELECT startup_id INTO startup_id_var FROM topic WHERE id = NEW.topic_id;

    -- Получаем organization_id из таблицы startup
    SELECT organization_id INTO org_id_var FROM startup WHERE id = startup_id_var;

    -- Вставляем уведомления для всех пользователей организации
    INSERT INTO notification (
        user_id,
        got_at,
        type,
        title,
        content,
        startup_id,
        topic_message_id,
        private_message_id
    )
    SELECT 
        ou.user_id,
        CURRENT_TIMESTAMP,
        'topic',
        'Новое сообщение в теме',
        NEW.text,
        startup_id_var,
        NEW.id,
        NULL
    FROM organization_has_user ou
    WHERE ou.organization_id = org_id_var AND ou.user_id != NEW.user_id; -- Исключаем отправителя сообщения
END;
