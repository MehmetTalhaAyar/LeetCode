
Öncelikle bu algoritmayı kendim çözmediğimi kodu yazarken chatgpt den yardım aldıgımı belirtmek istiyorum.


# 📊 Dönüşüm Uzunluğu Hesaplama Algoritması

Bu algoritma, bir string üzerinde belirli kurallara göre `t` defa karakter dönüşümü gerçekleştirdikten sonra oluşan stringin **uzunluğunu (mod 10^9 + 7)** ile hesaplar.

---

## ✅ Algoritma Adımları

### 1. Giriş Verilerini Matris Formatına Çevir

**`characterMatrix[]`** dizisi oluşturulur:  
- `characterMatrix[i]`, stringde `i` numaralı harften (`a` için 0) kaç tane olduğunu tutar.  
- Örneğin `s = "abcyy"` için:  
  ```
  characterMatrix = [1, 1, 1, 0, ..., 2, 0]
  ```

---

### 2. Dönüşüm (Transformasyon) Matrisini Oluştur

**`convertMatrix[from][to]`** matrisine göre:
- Her harf için, kaç karakter ileriye dönüşeceği `nums[i]` ile bellidir.
- Örnek: `nums[0] = 3` için `a → b,c,d` olur.
- Bu durumda:
  ```
  convertMatrix[1][0] = 1
  convertMatrix[2][0] = 1
  convertMatrix[3][0] = 1
  ```

---

### 3. Hızlı Matris Üs Alma (Fast Exponentiation)

#### Neden?
- t defa dönüşüm yapmak, matrisi t kez kendisiyle çarpmak anlamına gelir:  
  `convertMatrix^t`

#### Nasıl?
- Başlangıçta `result` birim matristir (identity matrix).
- `t` ikili olarak incelenir:
  - Eğer `t`'nin biti 1 ise `result = result × base`
  - Her adımda `base = base × base`
  - `t = t / 2`
- Toplam adım: `O(log t)`

🎥 [Fast Matrix Exponentiation Açıklaması (YouTube)](https://www.youtube.com/watch?v=WAzGvZbaAOw)

---

### 4. Sonuç Matrisiyle Karakterleri Güncelle

- `resultMatrix[i][j]`: `j` karakteri `t` dönüşüm sonunda kaç adet `i` karakterine dönüşür.
- Yeni toplam uzunluk:
  ```
  for i = 0 to 25:
      for j = 0 to 25:
          ans += result[i][j] * characterMatrix[j]
  ```

---

### 5. Mod Kullanımı

- Sonuç çok büyük olabileceğinden her adımda `MOD = 10^9 + 7` kullanılır.

---

## ⏱️ Zaman Karmaşıklığı

```
O(26^3 * log t)
```
- Matris çarpımı `O(26^3)` sürer.
- log(t) kadar üs alınır.

---

## 🎯 Örnek Girdi

```java
s = "abcyy"
t = 2
nums = [1, 1, ..., 2]
```

## 🔚 Özet

Bu yöntem klasik simülasyondan farklı olarak **verimli bir matris tabanlı çözüm** sunar. Karakter dönüşümleri hızlı üs alma ile modellenir ve sonucu hızlıca hesaplar.
