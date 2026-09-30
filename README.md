# Online Retail ABC Analizi

## Soru
Bir İngiliz hediyelik eşya toptancısının cirosunun büyük kısmını hangi ürünler getiriyor?

## Veri
[UCI Online Retail veri seti](https://archive.ics.uci.edu/dataset/352/online-retail),
1 Aralık 2010 - 9 Aralık 2011 arası işlem kayıtları (541.909 satır).
Lisans: CC BY 4.0.

## Temizlik
- 5.268 tam tekrar eden satır silindi
- 9.251 iptal fatura satırı (InvoiceNo "C" ile başlayanlar) çıkarıldı
- Fatura numarası 6 haneli olmayan 3 satır incelendi: bunlar "A" ile
  başlayan, StockCode'u "B" (Adjust bad debt) olan muhasebe düzeltme
  kayıtları çıktı, çıkarıldı
- Ürün kodu olmayan kalemler (kargo, banka masrafı, hediye çeki, manuel
  kayıt, numune vb.) çıkarıldı
- Miktarı ya da birim fiyatı sıfır/negatif olan satırlar çıkarıldı
  (imha edilmiş iki üründen kalan negatif miktarlı kayıtlar dahil)
- 3 büyük sipariş (toplam ~284.600 £), aynı gün içinde iptal edildiği
  tespit edilip ciro hesabından çıkarıldı. Bunlardan biri standart "C"
  faturasıyla değil, "Manual" düzeltme kaydıyla iptal edilmişti, bu yüzden
  otomatik filtrelerle yakalanmıyordu
- Temiz veri: **522.537 satır, 3.798 farklı ürün**

## Bulgular
Ürünlerin %22'si (834 ürün, A sınıfı) cironun **%80**'ini getiriyor.
B sınıfı (962 ürün) cironun %15'ini, C sınıfı (2.002 ürün, ürünlerin
yarısından fazlası) ise cironun sadece **%5**'ini oluşturuyor.

Pareto kuralı (80/20) bu veride neredeyse birebir doğrulanıyor: az sayıda
ürün cironun büyük kısmını taşıyor, çok sayıda ürün ise ciroya çok az
katkı yapıyor.

## Nasıl çalıştırılır
1. `pip install pandas matplotlib`
2. Veriyi [UCI linkinden](https://archive.ics.uci.edu/dataset/352/online-retail)
   indirin, Excel dosyasını CSV'ye çevirip `online_retail.csv` adıyla proje
   klasörüne koyun
3. Kod dosyasını çalıştırın