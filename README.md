# Teknofest 2024 Doğal Dil İşleme - Doğal Dil İşleme Senaryosu Kategorisi

Verilen senaryo kapsamında müşteri şikayetlerinin içerisinde geçen markalar tespit edilecek, ardından her bir marka için ayrı bir duygu durumu analizi yapılacaktır.\
Bu doğrultuda takım olarak öncelikle bu görevi Pretrained Instruction Modeller ile verimli bir eğitim sonrası çözebileceğimizi düşünerek GPT-2 ve gemma2b modelini eğitmeye çalıştık. Yaptığımız eğitimler sonrası elde ettiğimiz model, json yapısı ve entity'leri tespit etmekte oldukça başarılı iken özellikle karmaşık cümlelerde duygu analizi yapmakta zorlanıyordu. Dolayısıyla bu görevi NER + ABSA olacak şekilde tekrar düzenledik ve model geliştirmelerinde bulunduk.

Yarışma süresince geliştirilen modeller Hugging Face sayfamız üzerinden paylaşılmıştır:\\
[Karayel Nazır-ABSA](https://huggingface.co/Karayel-DDI/Nazir_ABSA) \
[Karayel Nazır-NER](https://huggingface.co/Karayel-DDI/Nazir_NER)

Eğitimler sırasında kullanılmak üzere hazırladığımız veri setinin hazırlık aşamalarını hızlandırmak ve iyileştirmek adına araçlar geliştirdik. Araçlarımızın kaynak kodlarına aşağıdan ulaşabilirsiniz.\\
Veri kazıma işlemleri: [Karayel-Uren](https://github.com/karayel-ddi/Karayel-Uren)\
Veri etiketleme işlemleri: [Karayel-Label-App](https://github.com/karayel-ddi/Karayel-Label-App)
  
