CREATE TABLE PATIENT(
    PiD VARCHAR(30) NOT NULL,
    Fname VARCHAR(30) NOT NULL,
    Minit CHAR,
    Lname VARCHAR(30) NOT NULL,
    Bdate TEXT NOT NULL,
    Street VARCHAR(50),
    City VARCHAR(30),
    State VARCHAR(2),
    Zip VARCHAR(5),
    Phone VARCHAR(10) NOT NULL,
    Sex CHAR,
    PRIMARY KEY (Pid)
);
