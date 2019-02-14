import numpy as np
import matplotlib.pyplot as plt

KW = 1.0e-14
acidConc = float(input('Concentration of acid ? '))
acidVolume = float(input('Acid volume ? '))

baseConc = float(input('Concentration of base ? '))
equivalenceBaseVolume = acidConc * acidVolume / baseConc
baseVolumes = np.linspace(0, equivalenceBaseVolume * 2, 1000)

def pH_Acid(H_Conc):
    return -1 * np.log10(H_Conc)

def pH_Base(OH_Conc):
    H_Conc = KW / OH_Conc
    return -1 * np.log10(H_Conc)

pH = []
for baseVolume in baseVolumes:
    totalVolume = acidVolume + baseVolume

    unneutralizedMol = acidConc * acidVolume - baseConc * baseVolume
    if unneutralizedMol > 0:
        pH.append(pH_Acid(unneutralizedMol / totalVolume))
    if unneutralizedMol < 0:
        pH.append(pH_Base(abs(unneutralizedMol / totalVolume))) #cannot take log10 of -ive

plt.plot(baseVolumes, pH)
plt.show()
