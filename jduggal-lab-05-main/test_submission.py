from random import randint
from unittest import TestCase, main

import submission as sub


class Lab_05_01(TestCase):
    def test_add_to_int_returns_int(self):
        self.assertIsInstance(sub.add1(0), int)

    def test_add_1_0_is_1(self):
        self.assertEqual(sub.add1(0), 1)

    def test_add_1_5_is_6(self):
        self.assertEqual(sub.add1(5), 6)

    def test_add_1_negative_1_is_0(self):
        self.assertEqual(sub.add1(-1), 0)


class Lab_05_02(TestCase):
    def test_sum_squares_0_0_returns_int(self):
        self.assertIsInstance(sub.sum_of_squares(0, 0), int)

    def test_sum_squares_0_0(self):
        self.assertEqual(sub.sum_of_squares(0, 0), 0)

    def test_sum_squares_1_1(self):
        self.assertEqual(sub.sum_of_squares(1, 1), 2)

    def test_sum_squares_1_2(self):
        self.assertEqual(sub.sum_of_squares(1, 2), 5)

    def test_sum_squares_2_1(self):
        self.assertEqual(sub.sum_of_squares(2, 1), 5)


class Lab_05_03(TestCase):
    def test_format_workouts_empty_list_returns_empty_list(self):
        self.assertEqual(
            sub.format_workouts([]),
            [],
        )

    def test_format_workouts_returns_list(self):
        self.assertIsInstance(
            sub.format_workouts([]),
            list,
        )

    def test_format_workouts_one_week_returns_list(self):
        self.assertIsInstance(
            sub.format_workouts([["Cardio", "Rest", "Leg Day"]]),
            list,
        )

    def test_format_workouts_one_week(self):
        self.assertEqual(
            sub.format_workouts([["Cardio", "Rest", "Leg Day"]]),
            ["M: Cardio, W: Rest, F: Leg Day"],
        )

    def test_format_workouts_one_week_a_b_c(self):
        self.assertEqual(
            sub.format_workouts([["A", "B", "C"]]),
            ["M: A, W: B, F: C"],
        )

    def test_format_workouts_two_weeks(self):
        self.assertEqual(
            sub.format_workouts(
                [["Cardio", "Rest", "Leg Day"], ["Rest", "Leg Day", "Core"]]
            ),
            ["M: Cardio, W: Rest, F: Leg Day", "M: Rest, W: Leg Day, F: Core"],
        )

    def test_format_workouts_two_weeks_a_b_c(self):
        self.assertEqual(
            sub.format_workouts([["A", "B", "C"], ["D", "E", "F"]]),
            ["M: A, W: B, F: C", "M: D, W: E, F: F"],
        )


class Lab_05_04(TestCase):
    """Property tests for building a lotto ticket."""

    def test_build_lotto_ticket_returns_string(self):
        self.assertIsInstance(
            sub.build_lotto_ticket(),
            str,
            "build_lotto_ticket() should return a string.",
        )

    def test_ticket_has_six_balls(self):
        ticket = sub.build_lotto_ticket()
        self.assertEqual(
            len(ticket.split("-")), 6, "A ticket should have 5 numbers and a powerball."
        )

    def test_ticket_composed_of_numbers(self):
        ticket = sub.build_lotto_ticket()
        self.assertTrue(
            all([b.isdigit() for b in ticket.split("-")[:-1]]),
            "All but the last ball should be a number.",
        )

    def test_last_ball_starts_with_pb(self):
        ticket = sub.build_lotto_ticket()
        self.assertTrue(
            ticket.split("-")[-1].startswith("PB"),
            "The last ball should start with PB.",
        )

    def test_last_ball_ends_with_a_number_after_pb(self):
        ticket = sub.build_lotto_ticket().replace("PB", "")
        powerball = ticket.split("-")[-1]
        self.assertTrue(
            powerball.isdigit(), "The last ball should end with a number after PB."
        )

    def test_white_balls_between_one_and_69(self):
        for _ in range(100):
            ticket = sub.build_lotto_ticket()
            white_balls = ticket.split("-")[:-1]
            self.assertTrue(
                all([1 <= int(b) <= 69 for b in white_balls]),
                f"All white balls should be between 1 and 69, but found: {white_balls}",
            )

    def test_powerball_between_one_and_26(self):
        for _ in range(100):
            ticket = sub.build_lotto_ticket()
            powerball = ticket.split("-")[-1].replace("PB", "")
            self.assertTrue(
                1 <= int(powerball) <= 26,
                f"The powerball should be between 1 and 26, but found: {powerball}",
            )


class Lab_05_05(TestCase):
    """Property tests for drawing a series of lottery tickets."""

    def test_buy_lotto_tickets_returns_list(self):
        self.assertIsInstance(
            sub.buy_lotto_tickets(3),
            list,
            "buy_lotto_tickets() should return a list.",
        )

    def test_buy_lotto_tickets_returns_list_of_strings(self):
        self.assertTrue(
            all(isinstance(t, str) for t in sub.buy_lotto_tickets(3)),
            "Each ticket should be a string.",
        )

    def test_buy_lotto_tickets_returns_correct_number_of_tickets(self):
        for _ in range(100):
            n = randint(1, 100)
            self.assertEqual(
                len(sub.buy_lotto_tickets(n)),
                n,
                f"buy_lotto_tickets({n}) should return {n} tickets.",
            )


class Lab_05_06(TestCase):
    def test_load_01_demo_tiny_returns_list(self):
        self.assertIsInstance(
            sub.load_pandas_csv("data/01_demo_tiny.csv"),
            list,
            "Loading should return a list",
        )

    def test_length_of_demo_tiny_is_3(self):
        self.assertEqual(
            len(sub.load_pandas_csv("data/01_demo_tiny.csv")),
            3,
            "There are three rows in the CSV file, so length should be 3",
        )

    def test_load_01_demo_tiny_returns_first_item_is_dict(self):
        df = sub.load_pandas_csv("data/01_demo_tiny.csv")
        self.assertIsInstance(
            df[0],
            dict,
            "The first item in 01_demo_tiny should be a dictionary",
        )

    def test_loading_02_pandas_small_set_size(self):
        self.assertEqual(
            len(sub.load_pandas_csv("data/02_pandas_small.csv")),
            30,
        )

    def test_loading_03_pandas_medium_set_size(self):
        self.assertEqual(
            len(sub.load_pandas_csv("data/03_pandas_medium.csv")),
            123,
        )

    def test_loading_04_pandas_full_set_size(self):
        self.assertEqual(
            len(sub.load_pandas_csv("data/04_pandas_full.csv")),
            1000,
        )

    def test_first_row_of_tiny_data_contains_2009_01_01(self):
        df = sub.load_pandas_csv("data/01_demo_tiny.csv")
        self.assertEqual(
            df[0]["date"],
            "2009-01-01",
        )

    def test_first_row_of_tiny_data_has_dates_and_expected_data(self):
        self.assertDictEqual(
            sub.load_pandas_csv("data/01_demo_tiny.csv")[0],
            {
                "date": "2009-01-01",
                "A_count": "2",
                "B_count": "1",
                "D_count": "2",
                "C_count": "1",
            },
        )


class Lab_05_07(TestCase):
    def test_count_region_a_greater_than_b_no_loading(self):
        self.assertEqual(
            sub.count_where_region_A_greater_than_B(
                [
                    {
                        "date": "2009-01-01",
                        "A_count": "2",
                        "B_count": "1",
                        "C_count": "1",
                        "D_count": "2",
                    },
                ]
            ),
            1,
            "For one row, the count is 1.",
        )

    def test_count_region_a_greater_than_b_in_01(self):
        self.assertEqual(
            sub.count_where_region_A_greater_than_B(
                sub.load_pandas_csv("data/01_demo_tiny.csv"),
            ),
            1,
        )

    def test_count_region_a_greater_than_b_in_02(self):
        self.assertEqual(
            sub.count_where_region_A_greater_than_B(
                sub.load_pandas_csv("data/02_pandas_small.csv"),
            ),
            8,
        )

    def test_count_region_a_greater_than_b_in_03(self):
        self.assertEqual(
            sub.count_where_region_A_greater_than_B(
                sub.load_pandas_csv("data/03_pandas_medium.csv"),
            ),
            33,
        )

    def test_count_region_a_greater_than_b_in_04(self):
        self.assertEqual(
            sub.count_where_region_A_greater_than_B(
                sub.load_pandas_csv("data/04_pandas_full.csv"),
            ),
            264,
        )


if __name__ == "__main__":
    main()
