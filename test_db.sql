CREATE TABLE IF NOT EXISTS 'dataset'(
'id' INTEGER PRIMARY KEY AUTOINCREMENT,
'apid' INTEGER NOT NULL,
'fname' varchar(50) DEFAULT NULL,
'lname' varchar(50) DEFAULT NULL,
'createdtime' DATE DEFAULT (datetime('now','localtime'))
);

CREATE TRIGGER remove_old_record BEFORE INSERT ON dataset
BEGIN
  DELETE FROM dataset WHERE createdtime < datetime('now', '-1 hour','localtime');
END ;