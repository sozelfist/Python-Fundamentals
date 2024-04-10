# Contributing to Python Fundamentals

I always welcome your contributions to Python Fundamentals! Whether you're fixing a bug, implementing a new feature, or improving documentation, I're glad to have you on board.

## Getting Started

1. Fork the repository on GitHub
2. Clone the forked repository to your local machine
3. Create a new branch for your changes
4. Make your changes and commit them
5. Push your changes to your forked repository
6. Create a pull request (PR) against the original repository

## Code of Conduct

I am committed to providing a friendly, safe and welcoming environment for all, regardless of level of experience, gender, gender identity and expression, sexual orientation, disability, personal appearance, body size, race, ethnicity, age, religion, or nationality. Please read and abide by the [Code of Conduct](CODE_OF_CONDUCT.md).

## How to Contribute

I always welcome contributions of all kinds, including but not limited to:

- Bug reports and fixes
- Feature requests and new features
- Documentation improvements
- Code refactoring and cleanup
- Test coverage and improvements

If you're not sure where to start, take a look at the issues labeled with [good first issue](https://github.com/TruongNhanNguyen/Python-Fundamentals/labels/good%20first%20issue) or [help wanted](https://github.com/TruongNhanNguyen/Python-Fundamentals/labels/help%20wanted). These issues are a good starting point for new contributors.

## Unit Testing Guidelines for Python Projects

### Purpose
Unit testing is crucial for ensuring the reliability and correctness of your codebase. By writing comprehensive unit tests, we can detect and prevent bugs early in the development cycle, maintain code quality, and facilitate easier maintenance and refactoring.

### Guidelines

1. **Naming Convention**: Name test functions descriptively to indicate what functionality they are testing. Use the `test_` prefix for test functions.
2. **Isolation**: Ensure that each test is independent and isolated from other tests. Avoid dependencies between tests to prevent cascading failures.
3. **Arrange-Act-Assert (AAA) Pattern**: Structure each test into three sections: Arrange, Act, and Assert. This pattern enhances readability and maintainability.
    - **Arrange**: Set up the test environment, including initializing variables and dependencies.
    - **Act**: Execute the specific functionality or method being tested.
    - **Assert**: Verify the expected behavior or outcome.
4. **Test Coverage**: Aim for high test coverage to ensure that most, if not all, of your codebase is tested. Utilize coverage analysis tools to identify untested code paths. (optional)
5. **Edge Cases and Boundary Conditions**: Test not only typical use cases but also edge cases and boundary conditions. Consider scenarios such as empty inputs, maximum and minimum values, and unexpected inputs.
6. **Readable Assertions**: Write clear and descriptive assertions to clearly state the expected behavior. Utilize assertion libraries (e.g., `unittest`, `pytest`, `assert`) to enhance readability.
7. **Continuous Integration (CI)**: Integrate unit tests into your CI/CD pipeline to automatically run tests on each commit or pull request. This ensures that changes are thoroughly tested before being merged into the main codebase. (CI worlflow will run automatedly on each PRs.)
8. **Documentation**: Document your test cases, especially complex or non-intuitive ones, to aid understanding for future maintainers.
9. **Refactoring**: Update unit tests as necessary when refactoring code to maintain their relevance and accuracy.

### Tools
- **pytest**: A popular testing framework for Python that offers a wide range of features for simple and complex testing scenarios.
- **unittest**: The built-in unit testing framework in Python that provides a solid foundation for writing tests.
- **coverage.py**: A tool for measuring code coverage of Python programs.
- **Mockito**: A mocking library for Python that simplifies the creation of test doubles.

### Examples
`data_structures/queue/deque.py`
```python
import unittest
from collections.abc import Iterable
from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.prev = None
        self.next = None


class Deque(Generic[T]):
    def __init__(self) -> None:
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None
        self.count = 0

    def __len__(self) -> int:
        return self.count

    def appendleft(self, value: T) -> None:
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.count += 1

    def popleft(self) -> T:
        if self.head is None:
            raise IndexError("pop from an empty deque")
        value = self.head.value
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.count -= 1
        return value

    def append(self, value: T) -> None:
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1

    def pop(self) -> T:
        if self.tail is None:
            raise IndexError("pop from an empty deque")
        value = self.tail.value
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.count -= 1
        return value

    def clear(self) -> None:
        self.head = self.tail = None
        self.count = 0

    def extend(self, iterable: Iterable) -> None:
        for value in iterable:
            self.append(value)

    def extendleft(self, iterable: Iterable) -> None:
        for value in reversed(iterable):
            self.appendleft(value)

    def remove(self, value: T) -> None:
        node = self.head
        while node is not None:
            if node.value == value:
                if node is self.head:
                    self.popleft()
                elif node is self.tail:
                    self.pop()
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.count -= 1
                return
            node = node.next
        raise ValueError(f"{value} is not in deque")

    def rotate(self, n: int = 1) -> None:
        if not self.head or not self.tail:
            return
        if n > 0:
            for _ in range(n):
                self.appendleft(self.pop())
        else:
            for _ in range(abs(n)):
                self.append(self.popleft())


class TestDeque(unittest.TestCase):
    def test_append(self):
        deque = Deque[int]()
        deque.append(1)
        deque.append(2)
        deque.append(3)
        self.assertEqual(len(deque), 3)
        self.assertEqual(deque.pop(), 3)
        self.assertEqual(deque.pop(), 2)
        self.assertEqual(deque.pop(), 1)

    def test_appendleft(self):
        deque = Deque[int]()
        deque.appendleft(1)
        deque.appendleft(2)
        deque.appendleft(3)
        self.assertEqual(len(deque), 3)
        self.assertEqual(deque.pop(), 1)
        self.assertEqual(deque.pop(), 2)
        self.assertEqual(deque.pop(), 3)

    def test_extend(self):
        deque = Deque[int]()
        deque.extend([1, 2, 3])
        self.assertEqual(len(deque), 3)
        self.assertEqual(deque.pop(), 3)
        self.assertEqual(deque.pop(), 2)
        self.assertEqual(deque.pop(), 1)

    def test_extendleft(self):
        deque = Deque[int]()
        deque.extendleft([1, 2, 3])
        self.assertEqual(len(deque), 3)
        self.assertEqual(deque.pop(), 3)
        self.assertEqual(deque.pop(), 2)
        self.assertEqual(deque.pop(), 1)

    def test_pop(self):
        deque = Deque[int]()
        deque.extend([1, 2, 3])
        self.assertEqual(len(deque), 3)
        self.assertEqual(deque.pop(), 3)
        self.assertEqual(deque.pop(), 2)
        self.assertEqual(deque.pop(), 1)
        self.assertRaises(IndexError, deque.pop)

    def test_popleft(self):
        deque = Deque[int]()
        deque.extend([1, 2, 3])
        self.assertEqual(len(deque), 3)
        self.assertEqual(deque.popleft(), 1)
        self.assertEqual(deque.popleft(), 2)
        self.assertEqual(deque.popleft(), 3)
        self.assertRaises(IndexError, deque.popleft)


if __name__ == "__main__":
    unittest.main()
```

## Submitting a Pull Request

- Make sure that you run this command before commit changes `pre-commit run --all-files`.
- Make sure that your code passes the tests and linters by running `make` (include cleansing process for removing aux files).
- Make sure that your code is well-documented and follows the Python style guide.
- Include a good description of your changes in the pull request.
- Squash any insignificant commits before submitting the pull request.

I may suggest some changes or improvements or alternatives, but the reviewers will generally try to help you land your contribution.

## Attribution

This contribution guide is adapted from the [Atom contribution guide](https://github.com/atom/atom/blob/master/CONTRIBUTING.md).

## Thank you!

Thank you for your contribution to Python Fundamentals! I appreciate your help and look forward to working with you.
