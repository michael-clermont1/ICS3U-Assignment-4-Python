#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program is to calculate a bonus on a yearly salary


def main():
    # this function is to calculate a 5% bonus on a yearly salary

    # input
    salary_string = input("Enter your yearly salary: ")
    years_of_service_string = input("Enter your years of service: ")
    # process & output
    print("")
    try:
        salary_int = int(salary_string)
        years_of_service_int = int(years_of_service_string)
        if years_of_service_int > 5:
            salary_int = salary_int * 1.05
            print("The net worth amount is {0}.".format(salary_int))
        else:
            print("The net worth amount is {0}.".format(salary_int))
    except Exception:
        print("That is not a integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
