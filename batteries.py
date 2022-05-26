from ent import readdata, entropy, pearsonchisquare, correlation, pochisq, monte_carlo
from fips import *
from scipy import stats
import numpy

import os

def ent (path):
    data, count = readdata(path)
    res_entropy = entropy(count)
    res_chi_score = pearsonchisquare(count)
    res_serial_correlation = correlation(data)
    res_p_val_chi = pochisq(res_chi_score)
    res_monte_carlo = monte_carlo(data)

    return res_entropy, res_chi_score, res_serial_correlation, res_p_val_chi, res_monte_carlo

def fips(fn, ver, p):
    res = []
    c = []

    fs = os.stat(fn)

    with open(fn, 'rb') as seq:
        params = p

        if fs.st_size/(2500*params) < 1:
            params = int(fs.st_size/2500)

        for i in range(params):
            stat = []
            r = []

            s = seq.read(2500)

            rtmp, stattmp = monobits(s, ver)
            r.append(rtmp)
            stat.append(stattmp)

            rtmp, stattmp = poker(s, ver)
            r.append(rtmp)
            stat.append(stattmp)

            rtmp, stattmp = run(s, ver)
            r.append(rtmp)
            stat.append(stattmp)

            rtmp, stattmp = longruns(s, ver)
            r.append(rtmp)
            stat.append(stattmp)

            rtmp = contrun(s, ver)
            r.append(rtmp)

            res.append(r)
            c.append(stat)

    return res, c, params