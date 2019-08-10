import numpy as np
import kmeans
import common
import naive_em
import em

X = np.loadtxt("toy_data.txt")

# TODO: Your code here
K = 4
seed = 0
mixture, post = common.init(X, K, seed)
mixture, post, cost = kmeans.run(X, mixture, post)
print(cost)
common.plot(X, mixture, post, "K = %d" % K)