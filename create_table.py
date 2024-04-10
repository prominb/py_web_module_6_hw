from sqlite3 import Error

from connect import create_connection, database


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)

def main():
    sql_drop_teachers_table = """DROP TABLE IF EXISTS teachers;"""
    sql_create_teachers_table = """
    CREATE TABLE teachers (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     fullname TEXT NOT NULL
    );
    """

    sql_drop_subjects_table = """DROP TABLE IF EXISTS subjects;"""
    sql_create_subjects_table = """
    CREATE TABLE subjects (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     name TEXT NOT NULL,
     teacher_id INTEGER NOT NULL,
     FOREIGN KEY (teacher_id) REFERENCES teachers (id) ON DELETE CASCADE
    );
    """

    sql_drop_groups_table = """DROP TABLE IF EXISTS groups;"""
    sql_create_groups_table = """
    CREATE TABLE groups (
     id INTEGER PRIMARY KEY,
     name TEXT NOT NULL
    );
    """

    sql_drop_students_table = """DROP TABLE IF EXISTS students;"""
    sql_create_students_table = """
    CREATE TABLE students (
     id INTEGER PRIMARY KEY,
     fullname TEXT NOT NULL,
     group_id INTEGER NOT NULL,
     FOREIGN KEY (group_id) REFERENCES groups (id) ON DELETE CASCADE
    );
    """

    sql_drop_grades_table = """DROP TABLE IF EXISTS grades;"""
    sql_create_grades_table = """
    CREATE TABLE grades (
     id INTEGER PRIMARY KEY,
     student_id INTEGER NOT NULL,
     subject_id INTEGER NOT NULL,
     grade INTEGER CHECK (grade >= 0 AND grade <= 100) NOT NULL,
     grade_date TEXT NOT NULL,
     FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE,
     FOREIGN KEY (subject_id) REFERENCES subjects (id) ON DELETE CASCADE
    );
    """

    with create_connection(database) as conn:
        if conn is not None:
            # create teachers table
            create_table(conn, sql_drop_teachers_table)
            create_table(conn, sql_create_teachers_table)
            # create subjects table
            create_table(conn, sql_drop_subjects_table)
            create_table(conn, sql_create_subjects_table)
            # create groups table
            create_table(conn, sql_drop_groups_table)
            create_table(conn, sql_create_groups_table)
            # create students table
            create_table(conn, sql_drop_students_table)
            create_table(conn, sql_create_students_table)
            # create grades table
            create_table(conn, sql_drop_grades_table)
            create_table(conn, sql_create_grades_table)
        else:
            print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
