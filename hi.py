
import aseegg as ag
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dane = pd.read_csv("dane.csv", delimiter=';', engine='python')
mojeDane = dane['Sub02']
przefiltrowany= ag.pasmowozaporowy(mojeDane, 256, 49, 51)
przefiltrowany=ag.gornoprzepustowy(mojeDane, 256, 3)
ag.spektrogram(przefiltrowany, 256)
ag.rysujFFT(przefiltrowany[8*256:20*256])
## 8hz 8-20 sekunda
##podpisy dodać - os x i y
