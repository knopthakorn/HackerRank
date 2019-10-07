"""
In this task, we would like for you to appreciate
the usefulness of the groupby() function of itertools .
To read more about this function, Check this out .
https://docs.python.org/2/library/itertools.html#itertools.groupby
"""

import itertools

S = input()

for k, g in itertools.groupby(S):
    print("{}".format((len(list(g)), int(k))), end=' ')
