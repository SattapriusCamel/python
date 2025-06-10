class employee:
    def __init__(self):
        print("Employee Created")
    def __del__(self):
        print("Boss Mad, Employee Fired")

job = employee()
del job