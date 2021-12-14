class hitung:
    def test_suhuF(suhu_celcius):
        suhu_fahrenheit = (9./5)* suhu_celcius + 32 #rumus farenheit
        return suhu_fahrenheit
    
    def test_suhuR(suhu_celcius):
        suhu_reamur = (4./5)* suhu_celcius #rumus reamur
        return suhu_reamur

    def test_suhuK(suhu_celcius):
        suhu_kelvin = suhu_celcius + 273.15 #rumus kelvin
        return suhu_kelvin

    def test_jarak(v0, a, t):
        hitung_jarak = (v0*t)+(0.5*a)*t*t #rumus jarak
        return hitung_jarak


class main():
    def menu():
        while True :

            print("1: konversi suhu celcius")
            print("2: menghitung jarak")
            print("3: exit")
            
            pilih = int(input("masukan pilihan: ")) #membuat variabel baru untuk menampung pilihan user
            if(pilih == 3):
                break       
                
            if(pilih == 1):
                suhu_celcius =float(input('Masukan Suhu Dalam Celcius ')) #inputan suhu berupa celcius
                print ('Hasil Perhitungan Konversi Suhu: ')
                print("suhu celcius : " ,suhu_celcius)
                print("suhu farenheit : " ,hitung.test_suhuF(suhu_celcius)) #hasil convert ke farenheit
                print("suhu reamur : " ,hitung.test_suhuR(suhu_celcius)) #hasil convert ke reamur
                print("suhu kelvin : " ,hitung.test_suhuK(suhu_celcius)) #hasil convert ke kelvin

            elif(pilih == 2):
                print ('Menghitung Jarak Tempuh Kendaraan ')
                v0=float(input('Berapa Kecepatan Awal Kendaraan (meter/detik): '))
                a=float(input('Berapa Percepatan Kendaraan? (meter/detik): '))
                t=float(input('Berapa Lama Waktu Bergerak(detik): '))
                print ('jarak tempuh', hitung.test_jarak(v0,a,t), 'meter') #hasil perhitungan jarak
            else :
                print("invalid input")

main.menu()      
