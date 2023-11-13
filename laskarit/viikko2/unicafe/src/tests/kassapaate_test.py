import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate = Kassapaate()

    def test_konstruktori_asettaa_rahan_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_konstruktori_asettaa_myydyt_lounaat_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_kasvattaa_kassan_saldoa_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)

    def test_kateisosto_kasvattaa_kassan_saldoa_edullisesti(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

    def test_vaihtorahan_maara_on_oikea_maukkaasti(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(maksu, 600)

    def test_vaihtorahan_maara_on_oikea_edullisesti(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(maksu, 760)

    def test_myytyjen_lounaiden_maara_kasvaa_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_myytyjen_lounaiden_maara_kasvaa_edullisesti(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kassa_ei_muutu_jos_maksu_ei_ole_riittava_maukkaasti(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(maksu, 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kassa_ei_muutu_jos_maksu_ei_ole_riittava_edullisesti(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(maksu, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_korttimaksu_toimii_maukkaasti(self):
        maksu = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(maksu, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.maksukortti.saldo_euroina(), 6.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_korttimaksu_toimii_edullisesti(self):
        maksu = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(maksu, True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_korttimaksu_ei_mene_lapi_jos_saldo_ei_riita_maukkaasti(self):
        kortti = Maksukortti(200)
        maksu = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(maksu, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(kortti.saldo_euroina(), 2.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_korttimaksu_ei_mene_lapi_jos_saldo_ei_riita_edulliseseti(self):
        kortti = Maksukortti(200)
        maksu = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(maksu, False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(kortti.saldo_euroina(), 2.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kassan_saldo_kasvaa_kun_korttia_ladataan(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1010.0)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_kassan_saldo_ei_muutu_jos_maksun_maara_on_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)