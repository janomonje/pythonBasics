# Importing the Libraries
from typing import Text
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

throw = int(input("Enter the amount of times you would like to flip the coin : "))


# Flipping the coin and Calculating Coin Frequencies
rolls = [random.randrange(1, 3) for i in range(throw)]
values, frequencies = np.unique(rolls, return_counts=True)

# Creating the Initial Bar Plot
title = f"Flipping a Coin {len(rolls):,} Times"
sns.set_style("whitegrid")
axes = sns.barplot(x=values, y=frequencies, palette="bright")

# Setting the Window Title and Labeling the x- and y-Axes
axes.set_title(title)
# Text(0.5, 1, "Flipping a Coin 100 times")

axes.set(xlabel="Coin Value", ylabel="Frequency")
# [Text(92.6667, 0.5, "Frequency"), Text(0.5, 58.7667, "Coin Value")]

# Finalizing the Bar Plot
axes.set_ylim(top=max(frequencies) * 1.10)
(0.0, 122.10000000000001)
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f"{frequency:,}\n{frequency / len(rolls):.3%}"
    axes.text(text_x, text_y, text, fontsize=11, ha="center", va="bottom")
plt.show()