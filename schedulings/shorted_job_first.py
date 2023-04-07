from __future__ import annotations

import unittest
from io import StringIO
from unittest.mock import patch


class Process:
    def __init__(self, id: int, arrival_time: int, burst_time: int) -> None:
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time

    def __repr__(self) -> str:
        return f'Process {self.id}'


class SJF:
    def __init__(self, processes: list[Process]) -> None:
        self.processes = processes
        self.no_of_processes = len(processes)
        self.waiting_time = [0] * self.no_of_processes
        self.turn_around_time = [0] * self.no_of_processes

    def run(self) -> None:
        remaining_time = [p.burst_time for p in self.processes]

        complete = 0
        increment_time = 0

        while complete != self.no_of_processes:
            min_bt = float('inf')
            shortest = None

            for j in range(self.no_of_processes):
                if self.processes[j].arrival_time <= increment_time and remaining_time[j] > 0:
                    if remaining_time[j] < min_bt:
                        min_bt = remaining_time[j]
                        shortest = j

            if shortest is None:
                increment_time += 1
                continue

            remaining_time[shortest] -= 1

            if remaining_time[shortest] == 0:
                complete += 1
                finish_time = increment_time + 1
                finar = finish_time - self.processes[shortest].arrival_time
                self.waiting_time[shortest] = finar - self.processes[shortest].burst_time

                if self.waiting_time[shortest] < 0:
                    self.waiting_time[shortest] = 0

                self.turn_around_time[shortest] = self.processes[shortest].burst_time + self.waiting_time[shortest]

            increment_time += 1

    def calculate_average_times(self) -> None:
        total_waiting_time = sum(self.waiting_time)
        total_turn_around_time = sum(self.turn_around_time)

        print(f"Average waiting time = {total_waiting_time / self.no_of_processes:.5f}")
        print(f"Average turn around time = {total_turn_around_time / self.no_of_processes:.5f}")

    def __repr__(self) -> str:
        return '\n'.join([f'{p}: arrival time={p.arrival_time}, burst time={p.burst_time}' for p in self.processes])


class TestSJF(unittest.TestCase):
    def setUp(self) -> None:
        self.processes: list[Process] = [
            Process(1, 0, 6),
            Process(2, 1, 8),
            Process(3, 2, 7),
            Process(4, 3, 3),
        ]

    def test_run(self) -> None:
        sjf = SJF(self.processes)
        sjf.run()

        # Verify waiting time and turn around time
        self.assertEqual(sjf.waiting_time, [0, 15, 7, 3])
        self.assertEqual(sjf.turn_around_time, [6, 23, 14, 6])

    def test_calculate_average_times(self) -> None:
        sjf = SJF(self.processes)
        sjf.waiting_time = [0, 6, 8, 9]
        sjf.turn_around_time = [6, 14, 15, 12]

        # Mock print() method and capture output to verify average times
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            sjf.calculate_average_times()
            output = mock_stdout.getvalue().strip()

        self.assertEqual(output, 'Average waiting time = 5.75000\nAverage turn around time = 11.75000')


if __name__ == '__main__':
    unittest.main()
