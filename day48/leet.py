import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(salary = employees['salary'] * 2)

#assing é um metodo que aplica um metodo a toda uma coluna de uma vez