# -*- coding: utf-8 -*-
"""
Created on Mon May 14 01:17:52 2018

@author: CO2
"""

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))