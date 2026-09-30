import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("online_retail.csv")
print(df.columns)
print(df.shape)
#İptal faturalarını çıkaralım. (C ile başlayanlar iptal oluyor)
iptal=df["InvoiceNo"].astype(str).str.startswith("C")
print(iptal.sum())
df=df[~iptal]
print(df.shape)
print(df.duplicated().sum())
df=df.drop_duplicates()
df["StockCode"]=df["StockCode"].astype(str)
df["StockCode"]=df["StockCode"].str.upper()
print(df.shape)


print(df["StockCode"].str.len().value_counts())
uzunluk=df["StockCode"].str.len()
problemli=~uzunluk.isin([5,6])
print(problemli.sum())
sonuc=df[problemli][["StockCode","Description"]].drop_duplicates()

print(df.shape)
#şimdi ütün kodu olmayanlaı silelim bunlar ciro değil
sil=df["StockCode"].str.startswith("GIFT")
liste=df["StockCode"].isin(["POST","C2","DOT","M","AMAZONFEE","B","BANK CHARGES","S"])
df=df[~(liste|sil)]
print(df.shape)
print((df["Quantity"]<=0).sum())
print((df["UnitPrice"]<=0).sum())
suphe=((df["UnitPrice"]<=0)|(df["Quantity"]<=0))
sonuuc=df[suphe][["StockCode","Quantity","CustomerID"]]

print(df.shape)
df=df[~suphe]
print(df.shape)
#ABC ANALİZİ İÇİN CİRO SÜTUNU EKLERİZ.
df["Ciro"]=df["Quantity"]*df["UnitPrice"]
print(df["Ciro"].describe())
print(df.shape)
print(df[["InvoiceNo","StockCode","Description","Quantity","UnitPrice","Ciro"]].sort_values(by="Ciro",ascending=False).head(3).to_string())
df = df[~((df["InvoiceNo"].astype(str)=="581483") & (df["StockCode"]=="23843"))]
df = df[~((df["InvoiceNo"].astype(str)=="541431") & (df["StockCode"]=="23166"))]
df=df[~((df["InvoiceNo"].astype(str)=="556444")&(df["StockCode"]=="22502"))]
print(df[["InvoiceNo","StockCode","Description","Quantity","UnitPrice","Ciro"]].sort_values(by="Ciro",ascending=False).head(3).to_string())
print(df.shape)
print(df["Ciro"].describe())
gruplama=df.groupby("StockCode")["Ciro"].sum()
print(len(gruplama))
gruplama=gruplama.sort_values(ascending=False)
toplam=gruplama.sum()
pay=gruplama/toplam
kumulatif=pay.cumsum()

print(kumulatif)
def sınıflandır(sayılar):
    if sayılar<0.8:
        return "A"
    elif sayılar>=0.8 and sayılar<0.95:
        return "B"
    else:
        return "C"
sinif=kumulatif.apply(sınıflandır)
print(sinif.value_counts())
sinif_ciro = gruplama.groupby(sinif).sum() / toplam * 100
print(sinif_ciro)
sayilar=sinif.value_counts().sort_index()
sayilar.plot(kind="bar",title="ABC ANALİZİ",color=["lightblue","yellow","lightgrey"])

plt.xlabel("Sınıf(A:cironun ilk %80'i,B:%80-%95,C:kalan %5)")
plt.ylabel("Ürün Sayısı")
plt.savefig("abc_dagilim.png",dpi=150)
plt.show()
plt.figure()
plt.plot(kumulatif.values)


plt.axhline(y=0.8, color="red", linestyle="-", label="%80 (A sınıfı sınırı)")
plt.axhline(y=0.95, color="orange", linestyle="--", label="%95 (B sınıfı sınırı)")
plt.title("Pareto Eğrisi: Az Ürün, Çok Ciro")
plt.xlabel("Ürün sırası (en çok ciro getirenden başlayarak)")
plt.ylabel("Kümülatif ciro payı")
plt.legend()
plt.tight_layout()
plt.savefig("pareto.png", dpi=150)



plt.show()