def hitung_nilai_akhir():
    print("Selamat datang di Aplikasi perhitungan nilai Mahasiswa")
    
    nilai_tugas = float(input("Silahkan Masukkan nilai Tugas Anda: "))
    nilai_uts = float(input("Silahkan Masukkan nilai UTS Anda: "))
    nilai_uas = float(input("Silahkan Masukkan nilai UAS Anda: "))
    
    nilai_akhir = 0.25 * nilai_tugas + 0.35 * nilai_uts + 0.40 * nilai_uas
    
    if nilai_akhir > 85:
        grade = "A"
    elif nilai_akhir > 80:
        grade = "A-"
    elif nilai_akhir > 75:
        grade = "B+"
    elif nilai_akhir > 70:
        grade = "B"
    elif nilai_akhir > 65:
        grade = "B-"
    elif nilai_akhir > 60:
        grade = "C+"
    elif nilai_akhir > 55:
        grade = "C"
    elif nilai_akhir > 50:
        grade = "C-"
    elif nilai_akhir > 30:
        grade = "D"
    else:
        grade = "E"
    
    print("Nilai Akhir Anda:", nilai_akhir)
    print("Dalam Huruf:", grade)

hitung_nilai_akhir()