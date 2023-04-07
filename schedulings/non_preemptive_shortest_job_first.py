import unittest


class Process:
    def __init__(self, pid: int, arrival_time: int, burst_time: int):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time

    def __lt__(self, other):
        return self.burst_time < other.burst_time

    def __str__(self):
        return f"Process {self.pid} - Arrival Time: {self.arrival_time}, Burst Time: {self.burst_time}"


class SJF:
    def __init__(self, processes: list[tuple[int, int]]):
        self.processes = [Process(pid, arrival_time, burst_time) for pid, arrival_time, burst_time in processes]
        self.num_processes = len(self.processes)
        self.current_time = 0
        self.waiting_time = [0] * self.num_processes
        self.turnaround_time = [0] * self.num_processes

    def run(self):
        self.processes.sort(key=lambda p: (p.arrival_time, p.burst_time))
        completed_processes = 0
        process_idx = 0
        while completed_processes < self.num_processes:
            if process_idx < self.num_processes:
                process = self.processes[process_idx]
                if process.arrival_time <= self.current_time:
                    self.waiting_time[process.pid - 1] = self.current_time - process.arrival_time
                    self.turnaround_time[process.pid - 1] = self.waiting_time[process.pid - 1] + process.burst_time
                    self.current_time += process.burst_time
                    process_idx += 1
                    completed_processes += 1
                else:
                    self.current_time += 1
            else:
                self.current_time += 1

    def get_waiting_time(self, pid: int) -> int:
        return self.waiting_time[pid - 1]

    def get_turnaround_time(self, pid: int) -> int:
        return self.turnaround_time[pid - 1]

    def get_average_waiting_time(self) -> float:
        return sum(self.waiting_time) / self.num_processes

    def get_average_turnaround_time(self) -> float:
        return sum(self.turnaround_time) / self.num_processes


class TestSJF(unittest.TestCase):
    def test_small_input(self):
        processes = [(1, 0, 5), (2, 1, 3), (3, 2, 8)]
        scheduler = SJF(processes)
        scheduler.run()
        self.assertEqual(scheduler.get_waiting_time(1), 0)
        self.assertEqual(scheduler.get_waiting_time(2), 4)
        self.assertEqual(scheduler.get_waiting_time(3), 6)
        self.assertEqual(scheduler.get_turnaround_time(1), 5)
        self.assertEqual(scheduler.get_turnaround_time(2), 7)
        self.assertEqual(scheduler.get_turnaround_time(3), 14)
        self.assertAlmostEqual(scheduler.get_average_waiting_time(), 3.33333, places=5)
        self.assertAlmostEqual(scheduler.get_average_turnaround_time(), 8.66667, places=5)

    def test_same_arrival_time(self):
        processes = [(1, 0, 3), (2, 0, 5), (3, 0, 1)]
        scheduler = SJF(processes)
        scheduler.run()
        self.assertEqual(scheduler.get_waiting_time(1), 1)
        self.assertEqual(scheduler.get_waiting_time(2), 4)
        self.assertEqual(scheduler.get_waiting_time(3), 0)
        self.assertEqual(scheduler.get_turnaround_time(1), 4)
        self.assertEqual(scheduler.get_turnaround_time(2), 9)
        self.assertEqual(scheduler.get_turnaround_time(3), 1)
        self.assertAlmostEqual(scheduler.get_average_waiting_time(), 1.66667, places=5)
        self.assertAlmostEqual(scheduler.get_average_turnaround_time(), 4.66667, places=5)

    def test_one_process(self):
        processes = [(1, 0, 5)]
        scheduler = SJF(processes)
        scheduler.run()
        self.assertEqual(scheduler.get_waiting_time(1), 0)
        self.assertEqual(scheduler.get_turnaround_time(1), 5)
        self.assertAlmostEqual(scheduler.get_average_waiting_time(), 0.0)
        self.assertAlmostEqual(scheduler.get_average_turnaround_time(), 5.0)

    def test_large_input(self):
        # 100 processes with random arrival times and burst times
        import random
        from random import randint
        random.seed(0)
        processes = [(i, randint(0, 50), randint(1, 10)) for i in range(1, 101)]
        scheduler = SJF(processes)
        scheduler.run()
        for i in range(1, 101):
            self.assertGreaterEqual(scheduler.get_waiting_time(i), 0)
            self.assertGreaterEqual(scheduler.get_turnaround_time(i), scheduler.get_waiting_time(i))
        self.assertAlmostEqual(scheduler.get_average_waiting_time(), 235.24, places=2)
        self.assertAlmostEqual(scheduler.get_average_turnaround_time(), 240.4, places=2)


if __name__ == '__main__':
    unittest.main()
