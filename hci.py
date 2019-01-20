import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import aseegg as ag


dane = pd.read_csv('sub-01_trial-03.csv', delimiter=',', engine='python')
mojeDane = dane[1]
czestotliwoscp = 200


przefiltrowane = ag.pasmowoprzepustowy(mojeDane, czestotliwoscp, 1,50)
przefiltrowane = ag.pasmowozaporowy(przefiltrowane, czestotliwoscp, 49, 51)

ag.spektrogram(mojeDane, 200)
ag.spektrogram(przefiltrowane, 200)