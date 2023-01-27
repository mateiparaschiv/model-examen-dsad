În fișierul _Industrie.csv_ se află informații privind cifra de afaceri pentru activități industriale la nivel de
localitate. Informațiile sunt următoarele:
_Siruta_ - Codul Siruta al localității;
_Localitate_ - Denumirea localității;
_Alimentara, Textila, Lemnului, ChimicaFarmaceutica, Metalurgica, ConstructiiMasini, CalculatoareElectronica, Mobila,
Energetica_ - Activitățile industriale cu cifra de afaceri.
În fișierul _PopulatieLocalitati.csv_ se află populația pe localități și indicativele de județ pentru fiecare
localitate.

1. Să se salveze în fișierul _Cerinta1.csv_ cifra de afaceri pe locuitor pentru fiecare activitate, la nivel de
   localitate. Pentru fiecare localitate se va salva codul Siruta, numele localității și cifra de afaceri pe locuitor
   pentru fiecare activitate. _(2 punct)_
2. Să se calculeze și să se salveze în fișierul _Cerinta2.csv_ activitatea industrială dominantă (cu cifra de afaceri
   cea
   mai mare) la nivel de județ. Pentru fiecare județ se va afișa indicativul de județ, activitatea dominantă și cifra de
   afaceri corespunzătoare. _(1 punct)_

3. DataSet_34.csv file contains records for 27 European countries related to the consumption and production of various
   types of meat. The observed variables are as follows:

- Pork meat production (1,000 tons);
- Beef meat production (1,000 tons);
- Sheep and goat meat production (1,000 tons);
- Poultry production (1,000 tons);
- Pork meat consumption (kg/person/year);
- Beef meat consumption (kg/person/year);
- Sheep and goat meat consumption (kg/person/year);
- Poultry consumption (kg/person/year).

In order to perform canonical correlation analysis, standardize the value of the variables and split the initial data
set into 2 data subsets analysis as follows:

- Pork meat production, Beef meat production, Sheep and goat meat production, Poultry production – _set X_;
- Pork meat consumption, Beef consumption, Sheep and goat meat consumption, Poultry consumption – _set Y_.

Save the 2 standardized data sets in files Xstd.csv and Ystd.csv. _(1 point)_

4. Determine and save the canonical scores z, and u, corresponding to _X_ and _Y_ data sets, Xscore.csv and Yscores.csv
   respectively _(1 points)_
5. Determine and save the factor loadings corresponding to variables from _X_ and _Y_ data sets in the files Rxz.csv and
   Ryu.csv respectively _(1 point)_

6. Plot the scatter of observations in the space of (z1, u1) and (z2, u2) canonical roots - biplot graphic. _(3 points)_
