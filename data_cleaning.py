import matplotlib
import numpy
import pandas as pd
import scipy.signal as signal

# This module gets path of the file from command line. After that data is
# filtered, cleaned and processed.
#

# Created global data windows as list.
data_windows_ecg = []
data_windows_gsr = []


def filtering(datafile):
    fs = 500
    h = signal.firwin(fs, cutoff=1, window="hanning")
    filtered_data = filter(h,1,datafile)
    return filtered_data


def windowing_ecg(filtered_ecg, fs):

    interval = 60*fs
    moving_length = 10*fs

    for start in range(0, filtered_ecg, moving_length):
        for window in range(start, filtered_ecg, interval):
            data_windows_ecg.append(window)

    return data_windows_ecg


def windowing_gsr(filtered_gsr, fs):

    interval = 60*fs
    moving_length = 10*fs

    for start in range(0, filtered_gsr, moving_length):
        for window in range(start, filtered_gsr, interval):
            data_windows_gsr.append(window)

    return data_windows_gsr






