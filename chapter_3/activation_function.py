import numpy as np
import matplotlib.pyplot as plt


def step_function(x):
    y = x > 0
    return y.astype(int)    # deprecated expression np.int


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


step_x = np.arange(-5.0, 5.0, 0.1)
step_y = step_function(step_x)

sig_x = np.arange(-5.0, 5.0, 0.1)
sig_y = sigmoid(sig_x)

plt.plot(step_x, step_y)
plt.plot(sig_x, sig_y)
plt.ylim(-0.1, 1.1)
plt.show()

# 입력이 중요하면 큰 값을 출력하고, 그렇지 않으면 작은 값을 출력한다.
# 입력이 아무리 크고 작아도 출력은 0~1

