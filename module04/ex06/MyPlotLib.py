import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
class MyPlotLib:

    @staticmethod
    def histogram(data, features):
        fig, ax = plt.subplots(1, len(features))
        uniq = data.drop_duplicates(['Name'])
        i = 0
        for feature in features:
            print(np.object)
            df = uniq[feature]
            ax[i].set_title(feature)
            ax[i].hist(df)
            ax[i].grid()
            i += 1
        plt.show()

