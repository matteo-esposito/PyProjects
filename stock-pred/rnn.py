#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Applying a recurrent neural network to some crypto currency pricing data, 
   which will present a much more significant challenge and be a bit more realistic 
   to your experience when trying to apply an RNN to time-series data. 
"""

# Libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM, CuDNNLSTM

mnist = tf.keras.datasets.mnist