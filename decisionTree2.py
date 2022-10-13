# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 23:50:43 2022

@author: Gallery
"""
import pandas as pd # for manipulating the csv data

data_test = pd.read_csv("dataMangga2.csv")


jum_data_test = data_test.shape[0]

hasil = [];
def klasifikasi(bentuk, warnaDaun, lebar, teksDaun, tulDaun):
    
    if bentuk == 1:
        hasil.append("Daun Sirih")
        print("Daun Sirih")
    elif bentuk == 8:
        hasil.append("Daun Singkong")
        print("Daun Singkong")
    elif bentuk == 11 :
        hasil.append("Daun Paku")
        print("Daun Paku")
    elif bentuk == 15 :
        hasil.append("Daun Nangka")
        print("Daun Nangka")
    elif bentuk == 17 :
        hasil.append("Daun Ketapang")
        print("Daun Ketapang")
    elif bentuk == 23 :
        hasil.append("Daun Palem")
        print("Daun Palem")
    elif bentuk == 3 :
        if  warnaDaun == 1 :
            hasil.append("Daun Bayam Liar")
            print("Daun Bayam Liar")
        elif warnaDaun == 2 :
            hasil.append("Daun Zamioculcas")
            print("Daun Zamioculcas")
        else:
            hasil.append('Data Tidak Dikenali')
            print('Data Tidak Dikenali')
    elif bentuk == 4 :
        if teksDaun == 0 :
            hasil.append("Kamboja")
            print("Kamboja")
        elif teksDaun == 2 :
            hasil.append("Rambutan")
            print("Rambutan")
        else:
            hasil.append('Data Tidak Dikenali')
            print('Data Tidak Dikenali')
    elif bentuk == 6 :
        if lebar == 1 or lebar == 3 :
            hasil.append("Daun Jambu")
            print("Daun Jambu")
        elif lebar == 2 :
            if tulDaun == 0 :
                hasil.append("Tanjung")
                print("Tanjung")
            elif tulDaun == 1 :
                hasil.append("Daun Jambu")
                print("Daun Jambu")
            else:
                print('Data Tidak Dikenali')
        elif lebar == 4 or lebar == 5 :
            hasil.append("Mangga")
            print("Mangga")
        else:
            hasil.append('Data Tidak Dikenali')
            print('Data Tidak Dikenali')
    elif bentuk == 18 :
        if tulDaun == 0 :
            hasil.append("SunFlower")
            print("SunFlower")
        elif tulDaun == 2:
            hasil.append("Bambu");
            print("Daun Bambu")
        else:
            hasil.append("Daun tidak dikenali")
            print("Daun tidak dikenali")
    else:
        print('Data Tidak Dikenali')
        hasil.append('Data Tidak Dikenali')
        

for i in range(0,jum_data_test):
    test1 = data_test['warna']
    test_warna = test1[i]
    
    test2 = data_test['Bentuk']
    test_bentuk = test2[i]
    
    test3 = data_test['Lebar']
    test_lebar = test3[i]
    
    test4 = data_test['Tekstur Daun']
    test_teksDaun = test4[i]
    
    test5 = data_test['Tulang Daun']
    test_tulDaun = test5[i]
    klasifikasi(test_bentuk, test_warna, test_lebar, test_teksDaun, test_tulDaun)
    
    
data_test["Hasil Akhir"] = hasil
#print(data_test)
