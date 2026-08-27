-- =============================================================
-- Student Grade Management System
-- Phase 2, Task 1: Database & Table Creation
-- create_tables.sql
-- =============================================================

DROP DATABASE IF EXISTS grade_management;
CREATE DATABASE grade_management
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE grade_management;

-- -------------------------------------------------------------
-- Table: roles
-- Stores system roles: student, teacher, admin
-- -------------------------------------------------------------
CREATE TABLE roles (
    role_id   TINYINT      NOT NULL AUTO_INCREMENT,
    role_name VARCHAR(20)  NOT NULL UNIQUE COMMENT 'student | teacher | admin',
    PRIMARY KEY (role_id)
) ENGINE=InnoDB COMMENT='User roles';

-- -------------------------------------------------------------
-- Table: users
-- Stores login credentials for all system users
-- -------------------------------------------------------------
CREATE TABLE users (
    user_id       INT          NOT NULL AUTO_INCREMENT,
    username      VARCHAR(50)  NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL COMMENT 'Store hashed passwords only',
    role_id       TINYINT      NOT NULL,
    is_active     TINYINT(1)   NOT NULL DEFAULT 1,
    created_at    DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id),
    CONSTRAINT fk_users_role FOREIGN KEY (role_id) REFERENCES roles(role_id)
) ENGINE=InnoDB COMMENT='Login accounts for all users';

-- -------------------------------------------------------------
-- Table: departments
-- Academic departments
-- -------------------------------------------------------------
CREATE TABLE departments (
    dept_id   CHAR(6)     NOT NULL COMMENT 'e.g. CS001',
    dept_name VARCHAR(80) NOT NULL UNIQUE,
    PRIMARY KEY (dept_id)
) ENGINE=InnoDB COMMENT='Academic departments';

-- -------------------------------------------------------------
-- Table: students
-- F01 – Student information
-- -------------------------------------------------------------
CREATE TABLE students (
    student_id      CHAR(12)     NOT NULL COMMENT 'Student number, e.g. 2022010001',
    user_id         INT          NOT NULL UNIQUE COMMENT 'Linked login account',
    full_name       VARCHAR(60)  NOT NULL,
    gender          ENUM('M','F','Other') NOT NULL,
    birth_date      DATE         NOT NULL,
    dept_id         CHAR(6)      NOT NULL,
    enrollment_year YEAR         NOT NULL,
    PRIMARY KEY (student_id),
    CONSTRAINT fk_stu_user FOREIGN KEY (user_id)   REFERENCES users(user_id),
    CONSTRAINT fk_stu_dept FOREIGN KEY (dept_id)   REFERENCES departments(dept_id)
) ENGINE=InnoDB COMMENT='Student information (F01)';

-- -------------------------------------------------------------
-- Table: teachers
-- Teacher profile (also have a users row with role=teacher)
-- -------------------------------------------------------------
CREATE TABLE teachers (
    teacher_id CHAR(8)    NOT NULL COMMENT 'e.g. T2018001',
    user_id    INT        NOT NULL UNIQUE,
    full_name  VARCHAR(60) NOT NULL,
    dept_id    CHAR(6)    NOT NULL,
    PRIMARY KEY (teacher_id),
    CONSTRAINT fk_tch_user FOREIGN KEY (user_id) REFERENCES users(user_id),
    CONSTRAINT fk_tch_dept FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
) ENGINE=InnoDB COMMENT='Teacher profiles';

-- -------------------------------------------------------------
-- Table: semesters
-- Academic semesters (e.g. 2023-2024-1)
-- -------------------------------------------------------------
CREATE TABLE semesters (
    semester_id   CHAR(12)    NOT NULL COMMENT 'e.g. 2023-2024-1',
    semester_name VARCHAR(40) NOT NULL,
    start_date    DATE        NOT NULL,
    end_date      DATE        NOT NULL,
    PRIMARY KEY (semester_id),
    CONSTRAINT chk_sem_dates CHECK (end_date > start_date)
) ENGINE=InnoDB COMMENT='Academic semesters';

-- -------------------------------------------------------------
-- Table: courses
-- F02 – Course information
-- -------------------------------------------------------------
CREATE TABLE courses (
    course_id   CHAR(8)      NOT NULL COMMENT 'e.g. CS10001',
    course_name VARCHAR(100) NOT NULL,
    credits     DECIMAL(3,1) NOT NULL CHECK (credits > 0),
    teacher_id  CHAR(8)      NOT NULL,
    dept_id     CHAR(6)      NOT NULL,
    semester_id CHAR(12)     NOT NULL,
    capacity    SMALLINT     NOT NULL DEFAULT 30 CHECK (capacity > 0),
    PRIMARY KEY (course_id, semester_id),
    CONSTRAINT fk_crs_teacher  FOREIGN KEY (teacher_id)  REFERENCES teachers(teacher_id),
    CONSTRAINT fk_crs_dept     FOREIGN KEY (dept_id)     REFERENCES departments(dept_id),
    CONSTRAINT fk_crs_semester FOREIGN KEY (semester_id) REFERENCES semesters(semester_id)
) ENGINE=InnoDB COMMENT='Course offerings per semester (F02)';

-- -------------------------------------------------------------
-- Table: enrollments
-- F03 – Student course enrollment (M:N between students & courses)
-- -------------------------------------------------------------
CREATE TABLE enrollments (
    enrollment_id BIGINT   NOT NULL AUTO_INCREMENT,
    student_id    CHAR(12) NOT NULL,
    course_id     CHAR(8)  NOT NULL,
    semester_id   CHAR(12) NOT NULL,
    enrolled_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (enrollment_id),
    UNIQUE KEY uq_enrollment (student_id, course_id, semester_id),
    CONSTRAINT fk_enr_student FOREIGN KEY (student_id)            REFERENCES students(student_id),
    CONSTRAINT fk_enr_course  FOREIGN KEY (course_id, semester_id) REFERENCES courses(course_id, semester_id)
) ENGINE=InnoDB COMMENT='Course enrollment records (F03)';

-- -------------------------------------------------------------
-- Table: grades
-- F04 – Grade entry; one row per enrollment
-- -------------------------------------------------------------
CREATE TABLE grades (
    grade_id      BIGINT         NOT NULL AUTO_INCREMENT,
    enrollment_id BIGINT         NOT NULL UNIQUE,
    score         DECIMAL(5,2)   NOT NULL CHECK (score >= 0 AND score <= 100),
    letter_grade  CHAR(2)        GENERATED ALWAYS AS (
        CASE
            WHEN score >= 90 THEN 'A'
            WHEN score >= 80 THEN 'B'
            WHEN score >= 70 THEN 'C'
            WHEN score >= 60 THEN 'D'
            ELSE 'F'
        END
    ) STORED COMMENT 'Auto-computed from score',
    gpa_points    DECIMAL(4,2)   DEFAULT NULL COMMENT 'Populated by trigger',
    entered_by    INT            NOT NULL COMMENT 'user_id of teacher/admin',
    entered_at    DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at    DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (grade_id),
    CONSTRAINT fk_grd_enrollment FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id),
    CONSTRAINT fk_grd_entered_by FOREIGN KEY (entered_by)    REFERENCES users(user_id)
) ENGINE=InnoDB COMMENT='Grade records (F04)';

-- -------------------------------------------------------------
-- Table: drop_log
-- Used by the transaction example (Phase 2, Task 3 – Transaction)
-- -------------------------------------------------------------
CREATE TABLE drop_log (
    log_id        BIGINT   NOT NULL AUTO_INCREMENT,
    enrollment_id BIGINT   NOT NULL COMMENT 'Original enrollment ID before deletion',
    student_id    CHAR(12) NOT NULL,
    course_id     CHAR(8)  NOT NULL,
    semester_id   CHAR(12) NOT NULL,
    dropped_by    INT      NOT NULL COMMENT 'user_id who initiated the drop',
    dropped_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (log_id)
) ENGINE=InnoDB COMMENT='Audit log for dropped courses (Transaction demo)';