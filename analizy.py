import json
import pandas as pd
import numpy as np
import matplotlib as mltb
import re
import nltk
import matplotlib.pyplot as plt
import datetime

# Analysis module. Work in progress.

# Setup gets filename from user and turns json file into pandaframe. Returns working file.


def setup():
    intro_file = input('Give filename:')
    working_file = pd.read_json('{}.json'.format(intro_file))
    working_file = working_file.transpose()
    return working_file


# Stats for retweet uses working file and returns list of stat data for retweets: sum, mean, median, std, max, min.


def stats_for_retweet(working_file):
    r_stats = working_file.retweet_count
    r_mean = np.mean(r_stats)
    r_sum = np.sum(r_stats)
    r_median = np.median(r_stats)
    r_std = np.std(r_stats)
    r_max = np.max(r_stats)
    r_min = np.min(r_stats)
    list_of_retweet_stats = ['mean:', r_mean, 'sum:', r_sum, 'median:', r_median, 'std:', r_std, 'max:', r_max, 'min:', r_min]
    return list_of_retweet_stats


# This function returns figure of retweet stat in time.


def figure_retweet_time(working_file):
    working_file.set_index('created_at', inplace=True, drop=False)
    working_file[['retweet_count']].plot(figsize=[12, 6], subplots=True)
    plt.savefig('fig_retweet_time.png')


def main():
    working_file = setup()
    list_of_retweets_stats = stats_for_retweet(working_file)
    print(list_of_retweets_stats)
    figure_retweet_time(working_file)


if __name__ == '__main__':
    main()
