import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ankaraNO2 = pd.read_excel("Ankara 2019-2020 NO2.xlsx")
ankaraNOX = pd.read_excel("Ankara 2019-2020 NOX.xlsx")
ankaraSO2 = pd.read_excel("Ankara 2019-2020 SO2.xlsx")

ankaraNO2.fillna(value="0")
ankaraNOX.fillna(value="0")
ankaraSO2.fillna(value="0")

#ankaraNO2["Ankara - Çankaya"].plot()
#ankaraNO2["EMEP - Ankara Çubuk"].plot()
#ankaraNO2["Ankara - Siteler"].plot()
#ankaraNO2["Ankara - Sincan"].plot()
#ankaraNO2["Ankara - Keçiören Sanatoryum"].plot()
#ankaraNO2["Ankara - Demetevler"].plot()
#ankaraNO2["Ankara - Bahçelievler"].plot()

#ankaraNOX["Ankara - Çankaya"].plot()
#ankaraNOX["EMEP - Ankara Çubuk"].plot()
#ankaraNOX["Ankara - Siteler"].plot()
#ankaraNOX["Ankara - Sincan"].plot()
#ankaraNOX["Ankara - Keçiören Sanatoryum"].plot()
#ankaraNOX["Ankara - Demetevler"].plot()
#ankaraNOX["Ankara - Bahçelievler"].plot()

#ankaraSO2["Ankara - Çankaya"].plot()
#ankaraSO2["EMEP - Ankara Çubuk"].plot()
#ankaraSO2["Ankara - Siteler"].plot()
#ankaraSO2["Ankara - Sincan"].plot()
#ankaraSO2["Ankara - Keçiören Sanatoryum"].plot()
#ankaraSO2["Ankara - Demetevler"].plot()
#ankaraSO2["Ankara - Bahçelievler"].plot()

