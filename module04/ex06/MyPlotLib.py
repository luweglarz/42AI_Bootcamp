import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb

class MyPlotLib:

    @staticmethod
    def histogram(data, features):
        fig, ax = plt.subplots(len(features))
        NoDuplicates = data.drop_duplicates(['Name'])
        i = 0
        for feature in features:
            df = data[feature]
            ax[i].set_title(feature)
            ax[i].hist(df)
            i += 1
        plt.show()

    @staticmethod
    def density(data, features):
        NoDuplicates = data.drop_duplicates(['Name'])
        ax = sb.kdeplot(data=NoDuplicates[features], 
        fill=True, common_norm=False, palette="crest", 
        alpha=.5, linewidth=0) 
        plt.show()

    @staticmethod
    def pair_plot(data, features):
        NoDuplicates = data.drop_duplicates(['Name'])
        ax = sb.pairplot(data=NoDuplicates[features], diag_kind="hist") 
        plt.show()

    @staticmethod
    def box_plot(data, features):
        NoDuplicates = data.drop_duplicates(['Name'])
        sb.boxplot(data=NoDuplicates[features])
        plt.show()
