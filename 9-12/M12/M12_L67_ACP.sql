CREATE TABLE IF NOT EXISTS Student (
    RegNum TEXT PRIMARY KEY,
    SName TEXT,
    Grade INTEGER,
    Mark TEXT
);

insert into Student(RegNum, SName, Grade, Mark) values
("S-9001", "Tanaka Kennichiro", 9, "A+"),
("S-9002", "Shinnichi Watanabe", 10, "B+"),
("S-9003", "Mangata Gentala", 11, "A+");

-- displaying data where mardk is A+
select * from Student where Mark="A+";