
"""Track applicants, shortlist candidates, and export recruitment reports."""

import csv
import sqlite3


def create_connection():
    """Create the in-memory database and its applicants table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE applicants (
            id INTEGER PRIMARY KEY,
            name TEXT,
            role TEXT,
            expected_salary INTEGER,
            status TEXT
        )
        """
    )
    return connection


conn = create_connection()


def add_applicant(name, role, expected_salary, status="applied"):
    """Add an applicant using a parameterized SQL query."""
    conn.execute(
        """
        INSERT INTO applicants (name, role, expected_salary, status)
        VALUES (?, ?, ?, ?)
        """,
        (name, role, expected_salary, status),
    )
    conn.commit()


def shortlist(role, salary_limit):
    """Return names for a role whose salary is within the given limit."""
    if not isinstance(salary_limit, int) or salary_limit < 0:
        raise ValueError("Salary limit must be a non-negative integer.")

    rows = conn.execute(
        """
        SELECT name, expected_salary
        FROM applicants
        WHERE role = ?
        """,
        (role,),
    ).fetchall()

    result = [
        name for name, salary in rows
        if salary <= salary_limit
    ]
    return result


def update_status(applicant_id, status):
    """Update an applicant's status, raising errors if the update fails."""
    cursor = conn.execute(
        "UPDATE applicants SET status = ? WHERE id = ?",
        (status, applicant_id),
    )
    conn.commit()

    if cursor.rowcount == 0:
        raise ValueError(f"No applicant found with ID {applicant_id}.")


def export_report(path):
    """Export applicant names, roles, and statuses to a CSV file."""
    with open(path, "w", newline="", encoding="utf-8") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["name", "role", "status"])
        writer.writerows(
            conn.execute("SELECT name, role, status FROM applicants")
        )


def count_by_status(status):
    """Return the number of applicants with the requested status."""
    return conn.execute(
        "SELECT COUNT(*) FROM applicants WHERE status = ?",
        (status,),
    ).fetchone()[0]


def main():
    """Run the sample recruitment-tracker workflow."""
    add_applicant("Nina", "analyst", 600000)
    add_applicant("Omar", "analyst", 750000, "interview")
    add_applicant("Priya", "developer", 900000)
    update_status(1, "interview")

    print(shortlist("analyst", 650000))
    export_report("applicants_report.csv")
    print(count_by_status("interview"), "in interview")


if __name__ == "__main__":
    main()
