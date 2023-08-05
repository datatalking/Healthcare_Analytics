CREATE TABLE VISIT(
	Pid	VARCHAR(30)	NOT NULL,
	Visit_id VARCHAR(30) NOT NULL,
	Visit_date DATE NOT NULL,
	Attending_md VARCHAR(30) NOT NULL,
	Pri_dx_icd VARCHAR(20)	NOT NULL,
	Pri_dx_name	VARCHAR(100) NOT NULL,
	Sec_dx_icd VARCHAR(20),
	Sec_dx_name	VARCHAR(100),
  PRIMARY KEY (Visit_id)
);
