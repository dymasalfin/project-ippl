import pytest
from  projectippl import hitung

class Test_hitung():
    @pytest.mark.parametrize("a,hasil",[(100,212), (-11,12.2)])
    def test_Faranheit(self,a ,hasil):
        hasil_Faranheit = hitung.test_suhuF(a)
        assert hasil_Faranheit == hasil

    @pytest.mark.parametrize("a,hasil",[(100,80), (-11,-8.8)])
    def test_Reamur(self,a ,hasil ):
        hasil_Reamur = hitung.test_suhuR(a)
        assert hasil_Reamur == hasil
    
    @pytest.mark.parametrize("a,hasil",[(100,373.15), (-11,262.15)])
    def test_Kelvin(self, a, hasil):
        hasil_Kelvin = hitung.test_suhuK(a)
        assert hasil_Kelvin== hasil
    
    def test_jarak(self):
        hasil_jarak = hitung.test_jarak(25,10,30)
        assert hasil_jarak == 5250
    