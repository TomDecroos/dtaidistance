import numpy as np
from dtaidistance import dtw, dtw_c
import array
import pytest
import math

n=10


## DISTANCE 1 ##


@pytest.mark.benchmark(group="distance1")
def test_distance1_python_compress(benchmark):
    s1 = [0, 0, 1, 2, 1, 0, 1, 0, 0]*n
    s2 = [0, 1, 2, 0, 0, 0, 0, 0, 0]*n
    def d():
        return dtw.distance(s1, s2)
    assert benchmark(d) == math.sqrt(2)*n


@pytest.mark.benchmark(group="distance1")
def test_distance1_python_matrix(benchmark):
    s1 = [0, 0, 1, 2, 1, 0, 1, 0, 0]*n
    s2 = [0, 1, 2, 0, 0, 0, 0, 0, 0]*n
    def d():
        dd, _ = dtw.distances(s1, s2)
        return dd
    assert benchmark(d) == math.sqrt(2)*n


@pytest.mark.benchmark(group="distance1")
def test_distance1_cpython(benchmark):
    s1 = np.array([0, 0, 1, 2, 1, 0, 1, 0, 0]*n)
    s2 = np.array([0, 1, 2, 0, 0, 0, 0, 0, 0]*n)
    def d():
        return dtw_c.distance(s1, s2)
    assert benchmark(d) == math.sqrt(2)*n


@pytest.mark.benchmark(group="distance1")
def test_distance1_c_array(benchmark):
    s1 = np.array([0, 0, 1, 2, 1, 0, 1, 0, 0]*n)
    s2 = np.array([0, 1, 2, 0, 0, 0, 0, 0, 0]*n)
    def d():
        return dtw_c.distance_nogil(s1, s2)
    assert benchmark(d) == math.sqrt(2)*n


@pytest.mark.benchmark(group="distance1")
def test_distance1_c_numpy(benchmark):
    s1 = array.array('d',[0, 0, 1, 2, 1, 0, 1, 0, 0]*n)
    s2 = array.array('d',[0, 1, 2, 0, 0, 0, 0, 0, 0]*n)
    def d():
        return dtw_c.distance_nogil(s1, s2)
    assert benchmark(d) == math.sqrt(2)*n


## DISTANCE MATRIX 1 ##

n = 1
nn = 100

@pytest.mark.benchmark(group="matrix1")
def test_distance_matrix1_serialpython(benchmark):
    s = [[0, 0, 1, 2, 1, 0, 1, 0, 0] * n,
         [0, 1, 2, 0, 0, 0, 0, 0, 0] * n,
         [1, 2, 0, 0, 0, 0, 0, 1] * n] * nn
    s = [np.array(si) for si in s]
    def d():
        return dtw.distance_matrix(s, parallel=False, use_c=False, use_nogil=False)
    m = benchmark(d)
    assert m[0,1] == math.sqrt(2)*n


@pytest.mark.benchmark(group="matrix1")
def test_distance_matrix1_parallelpython(benchmark):
    s = [[0, 0, 1, 2, 1, 0, 1, 0, 0] * n,
         [0, 1, 2, 0, 0, 0, 0, 0, 0] * n,
         [1, 2, 0, 0, 0, 0, 0, 1] * n] * nn
    s = [np.array(si) for si in s]
    def d():
        return dtw.distance_matrix(s, parallel=True, use_c=False, use_nogil=False)
    m = benchmark(d)
    assert m[0,1] == math.sqrt(2)*n


@pytest.mark.benchmark(group="matrix1")
def test_distance_matrix1_serialpythonc(benchmark):
    s = [[0, 0, 1, 2, 1, 0, 1, 0, 0] * n,
         [0, 1, 2, 0, 0, 0, 0, 0, 0] * n,
         [1, 2, 0, 0, 0, 0, 0, 1] * n] * nn
    s = [np.array(si) for si in s]
    def d():
        return dtw.distance_matrix(s, parallel=False, use_c=True, use_nogil=False)
    m = benchmark(d)
    assert m[0,1] == math.sqrt(2)*n


@pytest.mark.benchmark(group="matrix1")
def test_distance_matrix1_parallelpythonc(benchmark):
    s = [[0, 0, 1, 2, 1, 0, 1, 0, 0] * n,
         [0, 1, 2, 0, 0, 0, 0, 0, 0] * n,
         [1, 2, 0, 0, 0, 0, 0, 1] * n] * nn
    s = [np.array(si) for si in s]
    def d():
        return dtw.distance_matrix(s, parallel=True, use_c=True, use_nogil=False)
    m = benchmark(d)
    assert m[0,1] == math.sqrt(2)*n


@pytest.mark.benchmark(group="matrix1")
def test_distance_matrix1_serialpurec(benchmark):
    s = [[0, 0, 1, 2, 1, 0, 1, 0, 0]*n,
         [0, 1, 2, 0, 0, 0, 0, 0, 0]*n,
         [1, 2, 0, 0, 0, 0, 0, 1]*n]*nn
    s = [np.array(si) for si in s]
    def d():
        return dtw.distance_matrix(s, parallel=False, use_c=True, use_nogil=True)
    m = benchmark(d)
    assert m[0,1] == math.sqrt(2)*n


@pytest.mark.benchmark(group="matrix1")
def test_distance_matrix1_parallelpurec(benchmark):
    s = [[0, 0, 1, 2, 1, 0, 1, 0, 0] * n,
         [0, 1, 2, 0, 0, 0, 0, 0, 0] * n,
         [1, 2, 0, 0, 0, 0, 0, 1] * n] * nn
    s = [np.array(si) for si in s]
    def d():
        return dtw.distance_matrix(s, parallel=True, use_c=True, use_nogil=True)
    m = benchmark(d)
    assert m[0,1] == math.sqrt(2)*n
