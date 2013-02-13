from math import *

def mass_outer(r1, r2, p1):
	m = 3.14 * (r1 ** 2 - r2 ** 2) * p1
	return m

def calc_r2(a, b, m_o):
	m_in = b * m_o / a
	r2 = sqrt(m_in / 3.14)
	return r2

a/b = (r1 ** 2 - r2 ** 2) * p1 / (p2 * r2 ** 2)
