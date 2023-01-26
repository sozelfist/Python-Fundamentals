import numpy as np


class VectorTransformations:
    def __init__(self):
        pass

    def rotate(self, vector, angle):
        angle = np.deg2rad(angle)
        transformation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        return np.matmul(transformation_matrix, vector)

    def reflect_over_x(self, vector):
        transformation_matrix = np.array([[1, 0], [0, -1]])
        return np.matmul(transformation_matrix, vector)

    def reflect_over_y(self, vector):
        transformation_matrix = np.array([[-1, 0], [0, 1]])
        return np.matmul(transformation_matrix, vector)

    def dilation(self, vector, scale_factor):
        transformation_matrix = np.array([[scale_factor, 0], [0, scale_factor]])
        return np.matmul(transformation_matrix, vector)

    def shearing(self, vector, shear_factor):
        transformation_matrix = np.array([[1, shear_factor], [0, 1]])
        return np.matmul(transformation_matrix, vector)


if __name__ == '__main__':
    v_transform = VectorTransformations()
    vector = np.array([1, 2])
    # rotating a vector by an angle of 30 degree
    rotated_vector = v_transform.rotate(vector, 30)
    print(rotated_vector)
    # Reflecting a vector over the x-axis
    reflected_vector_x = v_transform.reflect_over_x(vector)
    print(reflected_vector_x)
    # Reflecting a vector over the y-axis
    reflected_vector_y = v_transform.reflect_over_y(vector)
    print(reflected_vector_y)
    # Dilating a vector by a scale factor of 2
    scaled_vector = v_transform.dilation(vector, 2)
    print(scaled_vector)
    # Shearing a vector by a factor of 0.5
    sheared_vector = v_transform.shearing(vector, 0.5)
    print(sheared_vector)
    # Creating a complex transformation
    vector = np.array([1, 2])
    transformed_vector = v_transform.dilation(v_transform.reflect_over_x(v_transform.rotate(vector, 30)), 2)
    print(transformed_vector)
