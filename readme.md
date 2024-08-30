# File Scanner
## Açıklama
File Scanner, belirli bir dosya dizisi üzerinde yeni eklenen dosyaları tarayan ve sonuçlarını belirli bir dizin üzerinde kayıt
altında tutan bir Python uygulamasıdır. Bu uygulama Docker kullanilarak çalıştırılmaktadır.
## Kurulum
### 1. docker-compose.yml Dosyasının Hazırlanması:
Proje içerisinde bulunan [docker-compose.yml](docker-compose.yml) içerisnde:
- `/PATH/TO/WATCH_DIRECTORY` kısmına üzerinde yapılan değişikleri takip etmek istediğiniz dosyanın yolunu yazınız.
- `/PATH/TO/OUTPUT_DIRECTORY` kısmına tarama sonuçlarının çıktılarını kayıt altında tutmak istediğiniz dosyanın yolunu yazınız.
- `API_KEY=` kısmının devamına ise [virustotal](https://www.virustotal.com/)'den aldığınız api key anahtarını ekleniyiniz.
## Kullanım
### 1. Docker İmajının Oluşturma
Docker imajı için aşağıda bulunan komutu terminalden çalıştırın.\
```sh 
docker-compose build
```
### 2. Docker Konteynerini Başlatma
Docker konteynerini başlatmak için aşağıda bulunan kodu terminalden çalıştırın.\
```sh 
docker-compose up
```
Bu komut ile birlikte belirlenen dosya dizisi izlenmeye başlayacak ve tarama sonuçlarını belirlenen dizeye kayıtedecektir.
## Debugging ve Sorun Giderme
- Dosya İzleme:\
    Eğer dosya izleme düzgün çalışmıyorsa:
  - Docker volümlerini ve bağlama noktalarını kontrol edin.
  > [!TIP]
  > `/PATH/TO/WATCH_DIRECTORY:/app/watch_directory` ve `/PATH/TO/WATCH_DIRECTORY:/app/watch_directory` kısımlarını kontrol ediniz.
  - Api anahtarınızı kontrol ediniz.
  - Dosya ve dizinleri kontrol ediniz.
  - İzinleri kontrol ediniz.