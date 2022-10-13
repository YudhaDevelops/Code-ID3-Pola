# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 23:50:43 2022

@author: Gallery
"""
import pandas as pd # for manipulating the csv data

data_test = pd.read_csv("dataMangga.csv")


jum_data_test = data_test.shape[0]

hasil = []
prediksi = []

def klasifikasi(bentuk, warnaDaun, lebar, teksDaun, tulDaun):
    
    if bentuk == 1:
        hasil.append("Sirih")
    elif bentuk == 8:
        hasil.append("Singkong")
    elif bentuk == 11 :
        hasil.append("Paku")
    elif bentuk == 15 :
        hasil.append("Nangka")
    elif bentuk == 17 :
        hasil.append("Ketapang")
    elif bentuk == 23 :
        hasil.append("Palem")
    elif bentuk == 3 :
        if  warnaDaun == 1 :
            hasil.append("Bayam Liar")
        elif warnaDaun == 2 :
            hasil.append("Zamioculcas")
        else:
            hasil.append('Data Tidak Dikenali')
    elif bentuk == 4 :
        if teksDaun == 0 :
            hasil.append("Kamboja")
        elif teksDaun == 2 :
            hasil.append("Rambutan")
        else:
            hasil.append('Data Tidak Dikenali')
    elif bentuk == 6 :
        if lebar == 1 or lebar == 3 :
            hasil.append("Jambu")
        elif lebar == 2 :
            if tulDaun == 0 :
                hasil.append("Tanjung")
            elif tulDaun == 1 :
                hasil.append("Jambu")
            else:
                hasil.append('Data Tidak Dikenali')
        elif lebar == 4 or lebar == 5 :
            hasil.append("Mangga")
        else:
            hasil.append('Data Tidak Dikenali')
    elif bentuk == 18 :
        if tulDaun == 0 :
            hasil.append("SunFlower")
        elif tulDaun == 2:
            hasil.append("Bambu")
        else:
            hasil.append("Daun tidak dikenali")
    else:
        hasil.append("Daun tidak dikenali")

def cariPred(tabelDaunPred, daunPred):
    jum_data_daun = len(tabelDaunPred)
    
    for i in range(0,jum_data_daun):
        if(tabelDaunPred[i] == daunPred):
            prediksi.append("True")
        else:
            prediksi.append("False")

def hitungPred(tabelPred):
    jumBenar = 0
    jum_data_pred = len(tabelPred)
    
    for i in range(0,jum_data_pred):
        if(tabelPred[i] == "True"):
            jumBenar=jumBenar+1
    
    akurasi = (jumBenar / jum_data_pred)*100
    
    return akurasi
    

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
    klasifikasi(test_bentuk, test_warna, test_lebar, test_teksDaun, 
                test_tulDaun)
    
    
data_test["Hasil Akhir"] = hasil
cariPred(hasil, "Mangga")
data_test["Prediksi"] = prediksi

akurasiPred_1=hitungPred(prediksi)
print("Hasil Perhitungan Akurasi Rule : ", akurasiPred_1)