from __future__ import annotations

import unittest


class Process:
    def __init__(self, pid: int, duration: int) -> None:
        self.pid = pid
        self.duration = duration
        self.waiting_time = 0
        self.turnaround_time = 0

    def __repr__(self) -> str:
        return f"\
            Process ID: {self.pid}, Duration: {self.duration},\
            Waiting Time: {self.waiting_time}, Turnaround Time:\
            {self.turnaround_time}"


class Scheduler:
    def __init__(self, processes: list[Process]) -> None:
        self.processes = processes

    def calculate_waiting_times(self) -> list[int]:
        """
        This function calculates the waiting time of some processes that have a
        specified duration time.
            Return: The waiting time for each process.
        """
        waiting_times = [0] * len(self.processes)
        for i in range(1, len(self.processes)):
            waiting_times[i] = self.processes[i - 1].duration\
                + waiting_times[i - 1]
            self.processes[i].waiting_time = waiting_times[i]
        return waiting_times

    def calculate_turnaround_times(self) -> list[int]:
        """
        This function calculates the turnaround time of some processes.
            Return: The time difference between the completion time and the
                    arrival time.
                    Practically waiting_time + duration_time
        """
        for _i, process in enumerate(self.processes):
            process.turnaround_time = process.waiting_time + process.duration
        return [process.turnaround_time for process in self.processes]

    def calculate_average_turnaround_time(self) -> float:
        """
        This function calculates the average of the turnaround times
            Return: The average of the turnaround times.
        """
        return sum([process.turnaround_time for process in self.processes])\
            / len(self.processes)

    def calculate_average_waiting_time(self) -> float:
        """
        This function calculates the average of the waiting times
            Return: The average of the waiting times.
        """
        return sum([process.waiting_time for process in self.processes])\
            / len(self.processes)

    def schedule(self) -> None:
        # ensure that we actually have processes
        if len(self.processes) == 0:
            print("Zero amount of processes")
            raise SystemExit(0)

        # get the waiting times and the turnaround times
        self.calculate_waiting_times()
        self.calculate_turnaround_times()

        # get the average times
        average_waiting_time = self.calculate_average_waiting_time()
        average_turnaround_time = self.calculate_average_turnaround_time()

        # print all the results
        print("Process ID\tDuration Time\tWaiting Time\tTurnaround Time")
        for process in self.processes:
            print(process)
        print(f"Average waiting time = {average_waiting_time}")
        print(f"Average turn around time = {average_turnaround_time}")


class TestScheduler(unittest.TestCase):
    def setUp(self) -> None:
        self.processes: list[Process] = [
            Process(1, 8),
            Process(2, 4),
            Process(3, 9),
            Process(4, 5)
        ]
        self.scheduler = Scheduler(self.processes)

    def test_calculate_waiting_times(self) -> None:
        waiting_times = self.scheduler.calculate_waiting_times()
        self.assertEqual(waiting_times, [0, 8, 12, 21])

    def test_calculate_turnaround_times(self) -> None:
        self.scheduler.calculate_waiting_times()
        turnaround_times = self.scheduler.calculate_turnaround_times()
        self.assertEqual(turnaround_times, [8, 12, 21, 26])

    def test_calculate_average_waiting_time(self) -> None:
        self.scheduler.calculate_waiting_times()
        average_waiting_time = self.scheduler.calculate_average_waiting_time()
        self.assertEqual(average_waiting_time, 10.25)

    def test_calculate_average_turnaround_time(self) -> None:
        self.scheduler.calculate_waiting_times()
        self.scheduler.calculate_turnaround_times()
        average_turnaround_time = \
            self.scheduler.calculate_average_turnaround_time()
        self.assertEqual(average_turnaround_time, 16.75)

    def test_schedule_zero_processes(self) -> None:
        with self.assertRaises(SystemExit):
            Scheduler([]).schedule()


if __name__ == '__main__':
    unittest.main()
