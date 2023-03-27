import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")
    
    def test_saldo_vähenee_oikein(self):
        self.maksukortti.ota_rahaa(240)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")

    def test_saldo_ei_muutu_kun_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(200)
        kortti.ota_rahaa(240)

        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_metodi_palauttaa_oikean_arvon(self):
        kortti = Maksukortti(300)
        self.assertEqual(kortti.ota_rahaa(400), False)
        self.assertEqual(kortti.ota_rahaa(240), True)

