-- Creation of departments table
CREATE TABLE IF NOT EXISTS departments (
  department_id INT NOT NULL,
  deparment varchar(450) NOT NULL,
  PRIMARY KEY (department_id)
);

-- Creation of jobs table
CREATE TABLE IF NOT EXISTS jobs (
  job_id INT NOT NULL,
  job varchar(450) NOT NULL,
  PRIMARY KEY (job_id)
);

-- Creation of hired_employees table
CREATE TABLE IF NOT EXISTS hired_employees (
  hired_employee_id INT NOT NULL,
  name varchar(250) NOT NULL,
  datetime TIMESTAMP NOT NULL,
  department_id INT NOT NULL,
  job_id INT NOT NULL,
  PRIMARY KEY (hired_employee_id),
  CONSTRAINT fk_departments
      FOREIGN KEY(department_id) 
	  REFERENCES departments(department_id),
  CONSTRAINT fk_jobs
      FOREIGN KEY(job_id) 
	    REFERENCES jobs(job_id)
);
