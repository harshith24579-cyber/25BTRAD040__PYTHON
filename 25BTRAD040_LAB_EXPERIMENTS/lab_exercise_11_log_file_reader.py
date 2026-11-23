# NAME  : Harshith G
# USN   : 25BTRAD040
# BRANCH: CSE – AIDE A
# LAB EXPERIMENT - 4
# Lab Exercise 11: Log File Reader Program

def log_file_reader():
    try:
        with open("application.log", "r") as file:
            logs = file.readlines()

        error = 0
        warning = 0
        info = 0

        for line in logs:
            if "ERROR" in line:
                error += 1
            if "WARNING" in line:
                warning += 1
            if "INFO" in line:
                info += 1

        print("\nLog Summary")
        print("Errors:", error)
        print("Warnings:", warning)
        print("Info:", info)

        if len(logs) == 0:
            print("The log file is empty.")

    except FileNotFoundError:
        print("Log file not found.")


if __name__ == "__main__":
    log_file_reader()
