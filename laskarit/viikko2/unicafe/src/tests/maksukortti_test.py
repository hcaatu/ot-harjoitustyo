import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate = Kassapaate()

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 15.0)

    def test_ei_ladata_negatiivista_summaa_kortille(self):
        self.maksukortti.lataa_rahaa(-100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo_euroina(), 6.0)

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 2.0)

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 2.0)
    
    def test_metodi_palauttaa_true_jos_rahat_riittavat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        
    def test_str_palauttaa_oikeassa_muodossa_saldon(self):
        self.assertEqual(self.maksukortti.__str__(), "Kortilla on rahaa 10.00 euroa")

    def test_saldo_ei_muutu_jos_raha_ei_riita(self):
        kortti = Maksukortti(200)
        maksu = kortti.ota_rahaa(400)
        self.assertEqual(maksu, False)
