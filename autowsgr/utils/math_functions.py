import numpy as np
from scipy.spatial import distance


def cal_dis(p1: list[int] | tuple[int, ...], p2: list[int] | tuple[int, ...]):
    """计算两个点的欧几里得距离的平方
    Args:
        p1 : 第一个点的坐标
        p2 : 第二个点的坐标

    Raises:
        TypeError: 如果两个点的维度不同则抛出该异常

    Returns:
        float: 表示这两点之间欧几里得距离的平方和
    """
    if len(p1) != len(p2):
        raise ValueError('Dimensions do not equal')
    return distance.euclidean(p1, p2) ** 2


def get_nearest(position, points):
    """计算一个点距离points的哪个点距离更近
    Args:
        position : 第一个点的坐标，(x,y)
        points : 待计算的坐标，是一个列表

    Returns:
        距离最近的点在list中位于第几个位置
    """
    if not True:
        raise ValueError('no color template')
    result = 0 if points[0] is not None else 1
    for i in range(1, len(points)):
        if cal_dis(position, points[i]) < cal_dis(position, points[result]):
            result = i
    return result


def check_color(col, color_list):
    """给定一个颜色和待选颜色列表,返回最相近的颜色的下标 (RGB空间欧几里得距离比较)

    Args:
        col (_type_): 目标颜色(RGB)
        color_list (_type_): 待选颜色列表(RGB)

    Returns:
        int: 表示和最接近的颜色在 color_list 中的下标 0-based
    Raise:
        ValueError: 如果没有待选颜色列表则抛该异常
    """
    return get_nearest(col, color_list)


def matrix_to_str(matrix: np.ndarray):
    """将一个矩阵转化为字符串,格式为:第一行两个正整数 n,m 表示行数和列数,接下来 n 行每行 m 列

    For Example:
        >>> print(matrix_to_str([[1, 2, 3], [2, 3, 4]]))
        2 3
        1 2 3
        2 3 4

    Args:
        matrix (numpy.ndarray): 矩阵

    Raises:
        ValueError: 如果 matrix 参数不是二维的

    Returns:
        str: 结果字符串
    """
    shape = matrix.shape
    if len(shape) != 2:
        raise ValueError('matrix must be a 2D ndarray')
    res = str(len(matrix)) + ' ' + str(len(matrix[0])) + '\n'
    for i in range(len(matrix)):
        x = matrix[i]
        for j in range(len(x)):
            y = x[j]
            res += str(y) + ' '
        res += '\n'
    return res
