from ent import readdata, entropy, pearsonchisquare, correlation, pochisq, monte_carlo
from fips import *
import math
from scipy import stats
import numpy

import os


def ent(path):
    data, count = readdata(path)
    res_entropy = entropy(count)
    res_chi_score = pearsonchisquare(count)
    res_serial_correlation = correlation(data)
    res_p_val_chi = pochisq(res_chi_score)
    res_p_val_chi_per = math.fabs(res_p_val_chi * 100 - 50)
    res_monte_carlo = monte_carlo(data)
    res_mean = data.mean()

    return res_entropy, res_p_val_chi, res_serial_correlation, res_mean, res_monte_carlo


def fips(fn):
    res = []
    c = []

    fs = os.stat(fn)

    with open(fn, 'rb') as seq:
        stat = []
        r = []

        s = seq.read(2500)

        rtmp, stattmp = monobits(s)
        r.append(rtmp)
        stat.append(stattmp)

        rtmp, stattmp = poker(s)
        r.append(rtmp)
        stat.append(stattmp)

        rtmp, stattmp = run(s)
        r.append(rtmp)
        stat.append(stattmp)

        rtmp, stattmp = longruns(s)
        r.append(rtmp)
        stat.append(stattmp)

        rtmp = contrun(s)
        r.append(rtmp)

    return r, stat
