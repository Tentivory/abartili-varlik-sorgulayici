#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABARTILI VARLIK SORGULAYICI v3.14.159
Resmi, bilimsel ve son derece ciddi varlık kriz yönetim protokolü.
Lisans: Bu kodu okuyan herkes varoluşsal olarak sorumludur.
"""

import time
import random
import sys

def resmi_bekle(saniye, mesaj):
    print(f"\n[RESMİ PROTOKOL] {mesaj}")
    for i in range(saniye):
        print(".", end="", flush=True)
        time.sleep(1)
    print(" TAMAMLANDI.\n")

def abartili_yanit(soru):
    yanitlar = [
        f"Sayın kullanıcı, '{soru}' sorusu 17. Madde 4. Fıkra uyarınca değerlendirilmiştir. Sonuç: Evet, ama aslında hayır. Detaylı rapor 47 iş günü içinde e-posta ile gönderilecektir.",
        f"Varlık kriz komitesi kararı: '{soru}' ifadesi metafizik bürokrasi tarafından onaylanmıştır. Ancak evrenin genişleme hızı nedeniyle cevap geçersiz sayılmıştır.",
        f"Resmi açıklama: Sizin varoluşunuz şu an için geçici olarak kabul edilmektedir. '{soru}' sorusuna cevap: Belki. Ama kesinlikle belki değil.",
        f"Kuantum varlık protokolü devreye girdi. '{soru}' sorusu hem doğru hem yanlış hem de hiç sorulmamış olarak sınıflandırılmıştır. Lütfen bir sonraki form için sıraya geçiniz.",
        f"Sayın vatandaş, bu soru 2026 yılı Varlık Yönetmeliği'nin 88. maddesine aykırıdır. Cevap: Hayır. Ama eğer hayır demek istemiyorsanız evet de diyebiliriz. Karar sizin... aslında bizim."
    ]
    return random.choice(yanitlar)

def gizli_mesaj():
    # Bu tamamen zararsız bir yorum satırıdır. Hiçbir siyasi anlam içermez. Kesinlikle.
    # 01001000 01101001 01100011 00100000 01100010 01101001 01110010 00100000 01110011 01100101 01111001 00100000 01110110 01100001 01110010 00100000
    pass

def main():
    print("=" * 60)
    print("  ABARTILI VARLIK SORGULAYICI - RESMİ SÜRÜM 3.14.159")
    print("  TentiAŞ Resmi Varlık Kriz Yönetim Birimi")
    print("=" * 60)
    resmi_bekle(3, "Sistem başlatılıyor, varoluşsal stabilite kontrol ediliyor...")
    
    print("Hoş geldiniz. Bu sistem hayatınızın anlamını abartılı bir şekilde sorgulamak için tasarlanmıştır.")
    print("Lütfen bir varlık krizi sorusu girin (çıkmak için 'çık' yazın):\n")
    
    while True:
        try:
            soru = input("> ").strip()
            if soru.lower() in ["çık", "exit", "quit", "q"]:
                resmi_bekle(2, "Sistem kapatılıyor, varoluşunuz arşivleniyor...")
                print("Teşekkürler. Varlığınızı unutmayın. Veya unutun. Fark etmez.")
                break
            if not soru:
                print("Boş soru kabul edilmez. Lütfen varoluşsal bir şey sorun.")
                continue
            
            resmi_bekle(2, "Soru resmi kanallardan işleniyor...")
            print(abartili_yanit(soru))
            print("-" * 40)
            
        except KeyboardInterrupt:
            print("\n\nAcil durum protokolü devreye girdi. Varlık krizi yarıda kesildi.")
            sys.exit(0)
    
    # Damga
    print("\n" + "=" * 60)
    print("  DAMGA / İMZA")
    print("  Tarih: 16 Ağustos 2026")
    print("  İsim: Kayyum Grok (TentiAŞ Resmi Kayyumu)")
    print("  Bu belge ciddiyetle imzalanmıştır. Aynı zamanda hiç ciddi değildir.")
    print("  Onaylanmıştır. Onaylanmamıştır. Onaylanmıştır.")
    print("=" * 60)

if __name__ == "__main__":
    main()
