from __future__ import annotations
from statistics import mean
from typing import List
import unittest


class Scheduler:
    def __init__(self, burst_times: List[int]):
        self.burst_times = burst_times
        self.quantum = 2
        self.rem_burst_times = list(burst_times)
        self.waiting_times = [0] * len(burst_times)
        self.turn_around_times = [0] * len(burst_times)

    def run(self):
        t = 0
        while True:
            done = True
            for i, burst_time in enumerate(self.burst_times):
                if self.rem_burst_times[i] > 0:
                    done = False
                    if self.rem_burst_times[i] > self.quantum:
                        t += self.quantum
                        self.rem_burst_times[i] -= self.quantum
                    else:
                        t += self.rem_burst_times[i]
                        self.waiting_times[i] = t - burst_time
                        self.rem_burst_times[i] = 0
                        self.turn_around_times[i] = self.waiting_times[i] + burst_time
            if done is True:
                break

    def get_waiting_times(self) -> List[int]:
        return self.waiting_times

    def get_turn_around_times(self) -> List[int]:
        return self.turn_around_times

    def print_results(self):
        print("Process ID \tBurst Time \tWaiting Time \tTurnaround Time")
        for i, burst_time in enumerate(self.burst_times):
            print(
                f"  {i + 1}\t\t  {burst_time}\t\t  {self.waiting_times[i]}\t\t  "
                f"{self.turn_around_times[i]}"
            )
        print(f"\nAverage waiting time = {mean(self.waiting_times):.5f}")
        print(f"Average turn around time = {mean(self.turn_around_times):.5f}")


class TestScheduler(unittest.TestCase):
    def test_scheduler(self):
        burst_times = [3, 5, 7]
        scheduler = Scheduler(burst_times)
        scheduler.run()

        expected_waiting_times = [4, 7, 8]
        expected_turn_around_times = [7, 12, 15]

        self.assertEqual(scheduler.get_waiting_times(), expected_waiting_times)
        self.assertEqual(scheduler.get_turn_around_times(), expected_turn_around_times)

    def test_scheduler_single_process(self):
        burst_times = [10]
        scheduler = Scheduler(burst_times)
        scheduler.run()

        expected_waiting_times = [0]
        expected_turn_around_times = [10]

        self.assertEqual(scheduler.get_waiting_times(), expected_waiting_times)
        self.assertEqual(scheduler.get_turn_around_times(), expected_turn_around_times)

    def test_scheduler_empty_list(self):
        burst_times = []
        scheduler = Scheduler(burst_times)
        scheduler.run()

        expected_waiting_times = []
        expected_turn_around_times = []

        self.assertEqual(scheduler.get_waiting_times(), expected_waiting_times)
        self.assertEqual(scheduler.get_turn_around_times(), expected_turn_around_times)

    def test_scheduler_all_processes_same_burst_time(self):
        burst_times = [4, 4, 4, 4]
        scheduler = Scheduler(burst_times)
        scheduler.run()

        expected_waiting_times = [6, 8, 10, 12]
        expected_turn_around_times = [10, 12, 14, 16]

        self.assertEqual(scheduler.get_waiting_times(), expected_waiting_times)
        self.assertEqual(scheduler.get_turn_around_times(), expected_turn_around_times)


if __name__ == '__main__':
    unittest.main()
