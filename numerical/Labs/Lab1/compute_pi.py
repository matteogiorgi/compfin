#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

n = 50
iteration_vec = [2]

for i in range(1, n):
    new_value = 2 ** (i + 1 - 1 / 2) * np.sqrt(
        1 - np.sqrt(1 - 2 ** (2 - 2 * (i + 1)) * iteration_vec[i - 1] ** 2)
    )
    iteration_vec.append(new_value)

# plt.figure()
# plt.semilogy(np.abs(np.array(iteration_vec) - np.pi) / np.pi, "-")
# plt.title("Unstable algorithm for computing pi")
# plt.show()


iteration_vec_good = [2]

for i in range(1, n):
    new_value = (
        np.sqrt(2)
        * iteration_vec_good[i - 1]
        / (
            np.sqrt(
                1 + np.sqrt(1 - 2 ** (2 - 2 * (i + 1)) * iteration_vec_good[i - 1] ** 2)
            )
        )
    )
    iteration_vec_good.append(new_value)

# plt.figure()
# plt.semilogy(np.abs(np.array(iteration_vec_good) - np.pi) / np.pi, "-")
# plt.title("Stable algorithm for computing pi")
# plt.show()


plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.semilogy(np.abs(np.array(iteration_vec) - np.pi) / np.pi, "-")
plt.title("Unstable algorithm for computing pi")

plt.subplot(2, 1, 2)
plt.semilogy(np.abs(np.array(iteration_vec_good) - np.pi) / np.pi, "-")
plt.title("Stable algorithm for computing pi")

plt.tight_layout()
plt.show()
