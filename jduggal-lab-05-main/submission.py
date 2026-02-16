from random import randint
import csv


def add1(n: int) -> int:
    return n + 1


def sum_of_squares(x: int, y: int) -> int:
    return x * x + y * y


def format_workouts(workouts: list[list[str]]) -> list[str]:
    result = []
    for weeky in workouts:
        result.append ( f"M: {weeky[0]}, W: {weeky[1]} , F: {weeky[2]}")
    return result


def build_lotto_ticket() -> str:
    nums =  [str (randint(1, 69)) for _ in range(5)]
    BBBang = str(randint(1, 26))
    return "-".join(nums) + "-PB" + BBBang



def buy_lotto_tickets(n: int) -> list[str]:
    tickets  = []
    for  _ in range(n):
        tickets.append( build_lotto_ticket() )
    return tickets


def load_pandas_csv(file_name: str):
     with open( file_name, mode="r", newline="") as f:
        readreadreadread =  csv.DictReader(f)
        return  list(readreadreadread)


def count_where_region_A_greater_than_B(data):
    countdrac = 0
    for row in data:
        if int(row["A_count"]) > int(row["B_count"]):
            countdrac += 1
    return countdrac
