# Lab 05: Python and Files

## General Tips and Grading

The `submission.py` has signatures and starter code, and `test_submission.py` has tests similar to what we did during the lectures.

- You should have at least **one commit per function**, or (**8 total** including the initial commit)
- In general: commit each time you're confident in your function, have manually tested it, and got an 'OK' from the automated tests, or whenever you reach a good breaking point
- This builds on the topics we practiced for the first few weeks of class. The opening [Python chapter in the book](https://cgi.luddy.indiana.edu/~hayesall/info-infra-book/latest/prerequisites/python-cheat-sheet.html) can be a useful reference as well.

## 00 Setup your workspace

Clone your repo, open it in Visual Studio Code, and inspect the files that you'll be working with.

<details>
<summary><strong>Hint</strong>: cloning and VS Code</summary>

```bash
git clone https://github.iu.edu/i211sp2026/USERNAME-lab-05.git
cd ./USERNAME-lab-05
code .
```

</details>

## 01 Adder

Implement the `add1()` function, which takes an integer $x$ and adds 1 to it. For example:

```python
>>> add1(0)
1
>>> add1(5)
6
>>> add1(-1)
0
```

Test manually, then with automated tests, then commit.

```bash
python3 test_submission.py Lab_05_01
```

## 02 Sum of Squares

Now let's write a `sum_of_squares()` function, which takes two integers $x$ and $y$ and computes $x^{2} + y^{2}$.

For example:

```python
>>> sum_of_squares(0, 0)
0
>>> sum_of_squares(1, 1)
2
>>> sum_of_squares(1, 2)
5
>>> sum_of_squares(2, 1)
5
```

Test manually, then with automated tests, then commit.

```bash
python3 test_submission.py Lab_05_02
```

## 03 Workout formatting

Now let's practice strings, lists, and loops.

Implement the `format_workouts()` function, which takes a list-of-lists of three exercises, like:

```python
[
    ["Cardio", "Rest", "Leg Day"],
    ["Rest", "Leg Day", "Core"],
]
```

... and returns a list of strings showing the Monday/Wednesday/Friday schedule for each week.

For example, for one week this should return a list with one string:

```python
>>> format_workouts([["A", "B", "C"]])
['M: A, W: B, F: C']

>>> format_workouts([["Cardio", "Rest", "Leg Day"]])
['M: Cardio, W: Rest, F: Leg Day']
```
... for two weeks this should return a list with two strings:

```python
>>> format_workouts([["A", "B", "C"], ["D", "E", "F"]])
['M: A, W: B, F: C', 'M: D, W: E, F: F']

>>> format_workouts([["Cardio", "Rest", "Leg Day"], ["Rest", "Leg Day", "Core"]])
['M: Cardio, W: Rest, F: Leg Day', 'M: Rest, W: Leg Day, F: Core']
```

Test manually, then with automated tests, then commit.

```bash
python3 test_submission.py Lab_05_03
```

## 04 Building a lotto ticket

Implement a `build_lotto_ticket()` function to simulate Indiana powerball tickets, using Python [`random`](https://docs.python.org/3/library/random.html) module (**hint**: the `randint` method should already be imported at the top!). Since `randint` returns integers, we will need to cast the data into a `str` before we can return the result (i.e. `str(5)`).

A lottery ticket has:

- 5 numbers from 1 to 69 (inclusive)
- 1 number from 1 to 26 (inclusive, representing the "powerball")
- hyphen-delimited numbers (e.g. 1-2-3-4-5)
- a powerball number starting with "PB"

Since the outputs are random, expect small differences each time this function runs. Results should look similar to the following:

```python
>>> build_lotto_ticket()
'1-28-31-57-66-PB1'

>>> build_lotto_ticket()
'7-9-30-37-69-PB11'
```

Test manually, then with automated tests, then commit.

```bash
python3 test_submission.py Lab_05_04
```

## 05 Simulating multiple lotto tickets

Now write a function to simulate buying multiple lotto tickets. The function takes an integer `n_draws` (>= 0) representing how many times a ticket gets drawn from the possible outcomes, and returns tickets as a list of strings:

Similar to the previous question, expect small differences each time this function runs:

```python
>>> buy_lotto_tickets(2)
['1-28-31-57-66-PB1', '7-9-30-37-69-PB11']
```

Test manually, then with automated tests, then commit.

```bash
python3 test_submission.py Lab_05_05
```

## New Topic!

A researcher has a dataset representing the number of pandas in four regions ("Region A", "Region B", "Region C", and "Region D") over a few years.

|               |             |
| ------------: | ----------: |
|        🐼🐼 A |   🐼🐼🐼 B |
| 🐼🐼🐼🐼🐼 C |        🐼 D |

The researcher put the panda data in CSV files that look similar to the following, where the `date` column is in `YYYY-MM-DD` (*year, month, day*) format and each column represents the number of pandas counted in each region on a particular day:

|       date |   A_count |   B_count |   C_count |   D_count |
| ----------:|----------:|----------:|----------:|----------:|
| 2009-01-01 |         2 |         1 |         1 |         2 |
| 2009-01-02 |         3 |         3 |         3 |         3 |
| 2010-01-01 |         4 |         4 |         4 |         4 |

... which look like the plain-text CSV files we practiced with previously:

```
date,A_count,B_count,C_count,D_count
2009-01-01,2,1,1,2
2009-01-02,3,3,3,3
2010-01-01,4,4,4,4
```

Example files are in the `data/` directory.

## 06 Load panda data

Next, we'll turn our attention to loading data from CSVs. Inspect the files in the `data/` directory (but **do not** modify them, modifying the data will invalidate the tests).

Write a helper function to load data from a CSV file: `load_pandas_csv(filename)` like we practiced in class. *Hint*: This was the "[Read Function](https://cgi.luddy.indiana.edu/~hayesall/info-infra-book/latest/i211/tabular-data.html#summary-read-and-write-functions)" in the book, but incorporates a file name as an argument! Revisit your notes from the lecture.

```python
>>> load_pandas_csv("./data/01_demo_tiny.csv")
```

Run the automated tests and commit when you're ready.

```sh
python3 test_submission.py Lab_05_06
```

## 07 Count by region

Now that we have a function to load data from a file, let's implement a function to answer a question about that data: counting how many times the value in one column is greater than another. (*Hint*: similar to the lottery ticket question, we need to do the *inverse* here and convert from strings to integers with `int('1')`).

Implement the `count_where_region_A_greater_than_B()`, which takes the pandas data as an argument, and counts the number of rows (days) where the `A_count` column is greater than the `B_count` column.

For example, the `data/01_demo_tiny.csv` only contains one row where A is greater than B (2 > 1):

|       date |   A_count |   B_count |     |
| ----------:|----------:|----------:| --- |
| 2009-01-01 |         2 |         1 | ⬅️   |
| 2009-01-02 |         3 |         3 |     |
| 2010-01-01 |         4 |         4 |     |

So the function should return `1`:

```python
>>> df = load_pandas_csv("./data/01_demo_tiny.csv")
>>> count_where_region_A_greater_than_B(df)
1
```

Run the tests when you're ready:

```sh
python3 test_submission.py Lab_05_07
```
