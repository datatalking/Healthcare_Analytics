# SOURCE https://www.ncqa.org/wp-content/uploads/HEDIS-MY-2024-Measure-Description.pdf
# packtpub book

import sqlite3
from model import patient_predictions


# TODO add EDA from https://towardsdatascience.com/exploratory-analysis-python-kaggle-data-b0afb6ec1788
# TODO add https://github.com/azeezat123/Hafsat-Website-Sales-Analysis
# TODO dashboard https://towardsdatascience.com/how-to-build-a-complex-reporting-dashboard-using-dash-and-plotl-4f4257c18a7f
# HUGE HUGE POST


# TODO use https://github.com/PacktPublishing/Healthcare-Analytics-Made-Simple
# cihwof-vyvteS-9matre
def main():
    insert_HEDIS_data()
    print_hi(name)
    patient_predictions


# TODO add VITALS, MORT, MEDICATIONS, LABS
# TODO add python faker to future version
# TODO create a prompt in tests for PATIENT.sql and VISIT.sql if not exists create them.


def insert_HEDIS_data():
    """
    insert test patient data
    :return:
    """
    # TODO move mortality.db PATH to .env
    connection = sqlite3.connect("data/mortality.db")
    cursor = connection.cursor()

    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS PATIENT(
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
                )
            """
    )

    # TODO expand sample patient data from fnames.db in .env
    patients_data = [
        (
            "1",
            "John",
            "A",
            "Smith",
            "1952-01-01",
            "1206 Fox Hollow Rd.",
            "Pittsburgh",
            "PA",
            "15213",
            "6789871234",
            "M",
        ),
        (
            "2",
            "Candice",
            "P",
            "Jones",
            "1978-02-03",
            "1429 Orlyn Dr.",
            "Los Angeles",
            "CA",
            "90024",
            "3107381419",
            "F",
        ),
        (
            "3",
            "Regina",
            "H",
            "Wilson",
            "1985-04-23",
            "765 Chestnut Ln.",
            "Albany",
            "NY",
            "12065",
            "5184590206",
            "F",
        ),
        (
            "4",
            "Harold",
            "",
            "Lee",
            "1966-11-15",
            "2928 Policy St.",
            "Providence",
            "RI",
            "02912",
            "6593482691",
            "M",
        ),
        (
            "5",
            "Stan",
            "P",
            "Davis",
            "1958-12-30",
            "4271 12th St.",
            "Atlanta",
            "GA",
            "30339",
            "4049814933",
            "M",
        ),
    ]

    cursor.executemany(
        """
                INSERT OR REPLACE INTO PATIENT (Pid, Fname, Minit, Lname, Bdate, Street, City, State, Zip, Phone, Sex)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
        patients_data,
    )

    connection.commit()
    connection.close()


def print_hi(name):
    """
    insert my name in script
    :param name:
    :return:
    """
    # TODO in future version prompt user for their user name
    print(f"Hi, {name}")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    name = "Andrew"
    main()
    print_hi("PyCharm")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
