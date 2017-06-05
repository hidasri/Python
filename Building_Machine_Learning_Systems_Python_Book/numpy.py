# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 06:35:40 2017

@author: Sridharan Kamalakannan
"""

import numpy as np
import timeit as ti

list_time=ti.timeit('sum((x*x) for x in range(1000))',number=10000)
print('list time %f'%list_time)


bad_np_time=ti.timeit('sum(na*na)',
                      setup="import numpy as np;na=np.arange(1000);",
                      number=10000)
print('bad numpy time %f'%bad_np_time)

good_np_time=ti.timeit('na.dot(na)',
                      setup="import numpy as np;na=np.arange(1000);",
                      number=10000)
print('good numpy time %f'%good_np_time)