import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.cross_decomposition as skcd

t_ind = pd.read_csv('./dataIn/Industrie.csv', index_col=0)
t_pop = pd.read_csv('./dataIn/PopulatieLocalitati.csv', index_col=0)
# print(t_ind)
# print(t_pop)

industrii = list(t_ind.columns[1:].values)

# Cerinta 1
t1 = t_ind.merge(right=t_pop, left_index=True, right_index=True)


# Cifra de afaceri pe localitate
def ca_loc(t, variabile, populatie):
    x = t[variabile].values / t[populatie]
    # este ndarray
    v = list(x)
    v.insert(0, t["Localitate_x"])
    return pd.Series(data=v, index=["Localitate"] + variabile)


# ca_loc(t1[["Localitate_x", "Populatie"] + industrii], industrii, "Populatie")

t2 = t1[["Localitate_x", "Populatie"] + industrii].apply(func=ca_loc, axis=1, variabile=industrii,
                                                         populatie="Populatie")

t2.to_csv("./dataOut/Cerinta1.csv")


# Cerinta 2
def max_ca(t):
    x = t.values
    max_linie = np.argmax(x)
    return pd.Series(data=[t.index[max_linie], x[max_linie]], index=["Activitate", "Cifra de afaceri"])


t3 = t1[industrii + ['Judet']].groupby(by='Judet').agg(sum)
# industrii este o lista de stringuri;
# Judet va trb sa fie lista (motivul pentru care e in paranteze patrate)

t4 = t3[industrii].apply(func=max_ca, axis=1)
# print(t4)
t4.to_csv("./dataOut/Cerinta2.csv")

# Cerinta 3
tabel = pd.read_csv('./dataIn/DataSet_34.csv', index_col=0)
obs_nume = tabel.index.values
var_nume = tabel.columns.values
# print(obs_nume, var_nume)
x_coloane = var_nume[:4]
y_coloane = var_nume[4:]

X = tabel[x_coloane].values
Y = tabel[y_coloane].values


# standardizare pe ndarray
def standardizare(X):
    medii = np.mean(X, axis=0)
    abateri = np.std(X, axis=0)
    return (X - medii) / abateri


Xstd = standardizare(X)
Xstd_df = pd.DataFrame(data=Xstd, index=obs_nume, columns=x_coloane)
Xstd_df.to_csv("./dataOut/Xstd.csv")
Ystd = standardizare(Y)
Ystd_df = pd.DataFrame(data=Ystd, index=obs_nume, columns=y_coloane)
Ystd_df.to_csv("./dataOut/Ystd.csv")

# Cerinta 4
# Crearea model ACC
n, p = np.shape(X)
q = np.shape(Y)[1]  # nr de coloane
m = min(p, q)
# print(n,p,q,m)
modelACC = skcd.CCA(n_components=m)
modelACC.fit(X=Xstd, Y=Ystd)

z, u = modelACC.transform(X=Xstd, Y=Ystd)
# print(z, u)
z_df = pd.DataFrame(data=z, index=obs_nume, columns=["Z" + str(i) for i in range(1, m + 1)])
z_df.to_csv("./dataOut/Xscores.csv")
u_df = pd.DataFrame(data=u, index=obs_nume, columns=["U" + str(i) for i in range(1, m + 1)])
u_df.to_csv("./dataOut/Yscores.csv")

# Cerinta 5
Rxz = modelACC.x_loadings_
Rxz_df = pd.DataFrame(data=Rxz, index=x_coloane, columns=["Z" + str(i) for i in range(1, m + 1)])
Rxz_df.to_csv("./dataOut/Rxz.csv")

Ryu = modelACC.y_loadings_
Ryu_df = pd.DataFrame(data=Ryu, index=y_coloane, columns=["U" + str(i) for i in range(1, m + 1)])
Ryu_df.to_csv("./dataOut/Ryu.csv")


# Cerinta 6
def biplot(x, y, xLabel='X', yLabel='Y', title='Biplot', e1=None, e2=None):
    f = plt.figure(figsize=(11, 7), dpi=100)
    ax = f.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(title, fontsize=16)
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.scatter(x=x[:, 0], y=x[:, 1], color='red', label='Set X')
    ax.scatter(x=y[:, 0], y=y[:, 1], color='blue', label='Set Y')
    if e1 is not None:
        for i, txt in enumerate(e1):
            ax.annotate(txt, (x[i, 0], x[i, 1]))
    if e2 is not None:
        for i, txt in enumerate(e2):
            ax.annotate(txt, (y[i, 0], y[i, 1]))

    # if e1 is not None:
    #     for i in range(len(e1)):
    #         ax.text(x=x[i, 0], y=x[i, 1], s=e1[i])
    # if e2 is not None:
    #     for i in range(len(e2)):
    #         ax.text(x=y[i, 0], y=y[i, 1], s=e2[i])
    ax.legend()


biplot(z[:, :2], u[:, :2], xLabel='(z1,z2)', yLabel='(u1,u2)',
       title='Biplot tari in spatiul radacinilor canonice (z1,z2) si (u1,u2)', e1=list(obs_nume), e2=(obs_nume))

plt.show()
