import unittest

# 1st approach
# def longest_common_prefix(strs: List[str]) -> str:
#     """
#     Finds the longest common prefix among a list of strings.

#     Args:
#         strs: A list of strings to search for a common prefix.

#     Returns:
#         The longest common prefix string, or an empty string
#         if there is no common prefix.
#     """
#     if not strs:
#         return ""

#     # Sort the list of strings lexicographically
#     sorted_strs = sorted(strs)

#     # Compare the first and last strings in the sorted list
#     first_str = sorted_strs[0]
#     last_str = sorted_strs[-1]

#     # Find the common prefix between the first and last strings
#     prefix = ""
#     for i in range(len(first_str)):
#         if first_str[i] == last_str[i]:
#             prefix += first_str[i]
#         else:
#             break

#     return prefix

# 2nd approach
# def longest_common_prefix(strs: List[str]) -> str:
#     if not strs:
#         return ""

#     # Find the minimum length of the strings in the list
#     min_len = min(len(s) for s in strs)

#     prefix = ""
#     for i in range(min_len):
#         # Use the zip function to group the characters of the strings
#         # together
#         group = [s[i] for s in strs]
#         if all(c == group[0] for c in group):
#             prefix += group[0]
#         else:
#             break

#     return prefix

# 3rd approach


def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""

    def common_prefix(left: str, right: str) -> str:
        i = 0
        while i < len(left) and i < len(right) and left[i] == right[i]:
            i += 1
        return left[:i]

    def divide_and_conquer(strs: list[str], start: int, end: int) -> str:
        if start == end:
            return strs[start]
        else:
            mid = (start + end) // 2
            left_prefix = divide_and_conquer(strs, start, mid)
            right_prefix = divide_and_conquer(strs, mid + 1, end)
            return common_prefix(left_prefix, right_prefix)

    return divide_and_conquer(strs, 0, len(strs) - 1)


class TestLongestCommonPrefix(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(longest_common_prefix([]), "")

    def test_no_common_prefix(self):
        self.assertEqual(longest_common_prefix(["hello", "world"]), "")

    def test_single_string(self):
        self.assertEqual(longest_common_prefix(["hello"]), "hello")

    def test_common_prefix(self):
        self.assertEqual(
            longest_common_prefix(["apple", "app", "apartment", "apricot"]), "ap"
        )

    def test_duplicate_strings(self):
        self.assertEqual(longest_common_prefix(["hello", "hello", "hello"]), "hello")

    def test_one_empty_string(self):
        self.assertEqual(longest_common_prefix(["", "hello", "world"]), "")

    def test_unicode_strings(self):
        self.assertEqual(
            longest_common_prefix(["བོད་སྐད་གསར་བརྙན་", "བསྟན་པའི་སྒྲུབ་པའི་ལས་དོན་"]),
            "བ",
        )


if __name__ == "__main__":
    unittest.main()
