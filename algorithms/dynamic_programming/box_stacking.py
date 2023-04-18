import unittest

Box = tuple[int]


def max_box_height(boxes: list[Box]) -> int:
    # Generate all possible rotations of boxes
    rotated_boxes = []
    for box in boxes:
        rotated_boxes.append(box)
        rotated_boxes.append((box[1], box[2], box[0]))
        rotated_boxes.append((box[2], box[0], box[1]))

    # Sort boxes in descending order based on their base area
    rotated_boxes.sort(key=lambda x: x[0] * x[1], reverse=True)

    n = len(rotated_boxes)
    # Initialize dp array to store the maximum height
    # achievable up to each box
    dp = [0] * n

    for i in range(n):
        # Initialize the height with the height of the current box
        dp[i] = rotated_boxes[i][2]
        for j in range(i):
            # Check if the current box can be stacked on top of
            # the previous box
            if rotated_boxes[i][0] < rotated_boxes[j][0]\
                    and rotated_boxes[i][1] < rotated_boxes[j][1]:
                # Update the maximum height
                dp[i] = max(dp[i], dp[j] + rotated_boxes[i][2])

    return max(dp)  # Return the overall maximum height


class BoxStackingTestCase(unittest.TestCase):
    def test_max_box_height_with_multiple_boxes(self):
        boxes = [(1, 2, 3), (2, 3, 4), (3, 4, 1), (4, 5, 6)]
        expected = 19
        result = max_box_height(boxes)
        self.assertEqual(result, expected)

    def test_max_box_height_with_identical_boxes(self):
        boxes = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
        expected = 6
        result = max_box_height(boxes)
        self.assertEqual(result, expected)

    def test_max_box_height_with_different_orientations(self):
        boxes = [(2, 2, 2), (1, 3, 1), (3, 1, 3)]
        expected = 6
        result = max_box_height(boxes)
        self.assertEqual(result, expected)

    def test_max_box_height_with_large_number_of_boxes(self):
        boxes = [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5)]
        expected = 15
        result = max_box_height(boxes)
        self.assertEqual(result, expected)

    def test_max_box_height_with_single_box(self):
        boxes = [(1, 1, 1)]
        expected = 1
        result = max_box_height(boxes)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
