CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users
(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
TELEGRAM_ID INTEGER,
USERNAME CHAR(50),
FIRST_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE (TELEGRAM_ID)
)
"""
CREATE_BAN_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS ban_users
(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
TELEGRAM_ID INTEGER,
COUNT INTEGER,
UNIQUE (TELEGRAM_ID)
)
"""
CREATE_LIKE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS like_forms
(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
OWNER_TELEGRAM_ID INTEGER,
LIKER_TELEGRAM_ID INTEGER,
UNIQUE (OWNER_TELEGRAM_ID, LIKER_TELEGRAM_ID)
)
"""

CREATE_REFERRAL_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS referral
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
REFERRAL_TELEGRAM_ID INTEGER,
UNIQUE (OWNER_TELEGRAM_ID, REFERRAL_TELEGRAM_ID)
)
"""

CREATE_USER_PROFILE_QUERY = """
CREATE TABLE IF NOT EXISTS user_profile
(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
TELEGRAM_ID INTEGER,
NICKNAME CHAR(50),
AGE INTEGER,
SEX CHAR (50),
BIOGRAPHY CHAR(50),
GEOLOCATION CHAR(50),
PHOTO TEXT,
UNIQUE (TELEGRAM_ID)
)
"""

INSERT_USER_QUERY = """
INSERT INTO telegram_users VALUES (?, ?, ?, ?, ?, ?, ?)
"""
INSERT_BAN_USER_QUERY = """
INSERT INTO ban_users VALUES (?, ?, ?)"""

INSERT_LIKE_QUERY = """
INSERT INTO like_forms VALUES (?, ?, ?)"""

INSERT_USER_PROFILE_QUERY = """
INSERT INTO user_profile VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

SELECT_ALL_USER_PROFILE = """
SELECT * FROM user_profile
"""
SELECT_USER_BY_LINK_QUERY = """
SELECT TELEGRAM_ID FROM telegram_users WHERE REFERENCE_LINK = ?
"""
SELECT_USER_LINK_QUERY = """
SELECT REFERENCE_LINK FROM telegram_users WHERE TELEGRAM_ID = ?
"""
SELECT_USER_FORM_QUERY = """
SELECT * FROM user_profile WHERE TELEGRAM_ID = ?
"""
SELECT_BAN_USER_QUERY = """
SELECT * FROM ban_users WHERE TELEGRAM_ID = ?
"""

ALTER_USER_TABLE = """
ALTER TABLE telegram_users
ADD COLUMN REFERENCE_LINK TEXT
"""

ALTER_USERV2_TABLE = """
ALTER TABLE telegram_users
ADD COLUMN BALANCE INTEGER
"""

UPDATE_BAN_USER_COUNT_QUERY = """
UPDATE ban_users SET COUNT = COUNT + 1 WHERE TELEGRAM_ID = ?
"""

FILTER_LEFT_JOIN_USER_FORM_LIKE_QUERY = """
SELECT * FROM user_profile
LEFT JOIN like_forms ON user_profile.TELEGRAM_ID = like_forms.OWNER_TELEGRAM_ID
AND like_forms.LIKER_TELEGRAM_ID = ?
WHERE like_forms.ID IS NULL
AND user_profile.TELEGRAM_ID != ?
"""

DOUBLE_SELECT_REFERRAL_USER_QUERY = """
SELECT
    COALESCE(telegram_users.BALANCE, 0) AS BALANCE,
    COUNT(referral.ID) AS total_referral
FROM
    telegram_users
LEFT JOIN
    referral ON telegram_users.TELEGRAM_ID = referral.OWNER_TELEGRAM_ID
WHERE
    telegram_users.TELEGRAM_ID = ?
"""

UPDATE_REFERENCE_LINK_QUERY = """
UPDATE telegram_users SET REFERENCE_LINK = ? WHERE TELEGRAM_ID = ?
"""

UPDATE_USER_BALANCE_QUERY = """
UPDATE telegram_users SET BALANCE = COALESCE(BALANCE, 0) + 100 WHERE TELEGRAM_ID = ?
"""
INSERT_REFERRAL_QUERY = """
INSERT INTO referral VALUES (?,?,?)
"""

