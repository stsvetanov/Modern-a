import sqlite3


DB_FILENAME = 'Employees.db'


def main():
    connection = sqlite3.connect(DB_FILENAME, isolation_level=None)
    create_tables(connection)
    print("Tables created")


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        create table if not exists employees (
            emp_no      INT       PRIMARY KEY      NOT NULL,  -- UNSIGNED AUTO_INCREMENT??
            birth_date  DATE            NOT NULL,
            first_name  VARCHAR(14)     NOT NULL,
            last_name   VARCHAR(16)     NOT NULL,
            gender      TEXT CHECK( gender IN  ('M','F'))  NOT NULL,  -- Enumeration of either 'M' or 'F'  
            hire_date   DATE            NOT NULL
        );
    """)
    cursor.execute("""
        create table if not exists departments (
            dept_no     CHAR(4)         NOT NULL,  -- in the form of 'dxxx'
            dept_name   VARCHAR(40)     NOT NULL,
            PRIMARY KEY (dept_no),                 -- Index built automatically
            UNIQUE (dept_name)                -- Build INDEX on this unique-value column
        );
    """)
    cursor.execute("""
        create table if not exists dept_emp (
            emp_no      INT    PRIMARY KEY     NOT NULL,
            dept_no     CHAR(4)  PRIMARY KEY   NOT NULL,
            from_date   DATE        NOT NULL,
            to_date     DATE        NOT NULL,
            FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
            FOREIGN KEY (dept_no) REFERENCES departments (dept_no)
        );
    """)
    cursor.execute("""
        create table if not exists dept_manager (
           dept_no      CHAR(4)  NOT NULL PRIMARY KEY,
           emp_no       INT      NOT NULL PRIMARY KEY,
           from_date    DATE     NOT NULL,
           to_date      DATE     NOT NULL,
           FOREIGN KEY (emp_no)  REFERENCES employees (emp_no),
           FOREIGN KEY (dept_no) REFERENCES departments (dept_no)

        );
    """)
    cursor.execute("""
       create table if not exists titles (
            emp_no      INT    PRIMARY KEY      NOT NULL,
            title       VARCHAR(50) PRIMARY KEY  NOT NULL,
            from_date   DATE     PRIMARY KEY    NOT NULL,
            to_date     DATE,
            FOREIGN KEY (emp_no) REFERENCES employees (emp_no)
        );
    """)
    cursor.execute("""
        create table if not exists CREATE TABLE salaries (
            emp_no      INT    NOT NULL PRIMARY KEY,
            salary      INT    NOT NULL,
            from_date   DATE   NOT NULL PRIMARY KEY,
            to_date     DATE   NOT NULL,
            FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
        );
    """)


if __name__ == '__main__':
    main()
