import json
import pandas as pd
import numpy as np
import matplotlib as mltb
import re
import nltk
import matplotlib.pyplot as plt
import datetime


def setup():
    intro_file = input('Give filename:')
    working_file = pd.read_json('{}.json'.format(intro_file))
    working_file = working_file.transpose()
    return working_file


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


def main():
    working_file = setup()
    list_of_retweets_stats = stats_for_retweet(working_file)
    print(list_of_retweets_stats)
    # print(working_file)


if __name__ == '__main__':
    main()
