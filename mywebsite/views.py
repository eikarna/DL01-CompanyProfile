from django.shortcuts import render

def index(request):
    fasilitas_list = [
        "Unit Gawat Darurat 24 jam dengan penanganan kasus darurat jantung dan stroke.",
        "Ruang operasi modern dengan standar internasional.",
        "Laboratorium diagnostik lengkap.",
        "Fasilitas rawat inap nyaman dengan berbagai kelas.",
        "Klinik rawat jalan dengan layanan konsultasi spesialis."
    ]
    
    keunggulan_list = [
        "Menggunakan teknologi medis terkini seperti MRI, CT Scan, dan EKG untuk diagnosa cepat dan akurat.",
        "Tim dokter spesialis jantung dan saraf berpengalaman lebih dari 10 tahun.",
        "Program edukasi kesehatan untuk masyarakat seputar pencegahan penyakit jantung dan stroke."
    ]
    
    kelas_kategori_list = [
        "Kelas 1",
        "Executive",
        "VIP"
    ]
    
    kelas_gambar_list = [
        "/static/img/kelas1.jpg",
        "/static/img/kelas1.jpg",
        "/static/img/kelas1.jpg"
    ]
    
    kelas_deskripsi_list = {
        "kelas1": ["1 tempat tidur pasien dengan kenyamanan premium (1 Kamar berisi 2 Pasien).", "Ruangan ber-AC.", "Kamar mandi dengan pemanas air.", "TV LED 32 Inchi", "Lemari pakaian kecil", "Makanan sehat 3 kali sehari (sesuai rekomendasi gizi)."],
        "kelas2": ["1 tempat tidur pasien elektrik dengan pengaturan otomatis (1 Kamar 1 pasien).", "Ruangan ber-AC.", "Kamar mandi dengan pemanas air.", "TV LED 42 Inchi.", "Sofa untuk pendamping.", "Wi-Fi gratis.", "Makanan bisa disesuaikan dengan preferensi."],
        "kelas3": ["Kamar luas dengan desain mewah", "1 tempat tidur pasien elektrik dengan pengaturan otomatis (1 Kamar 1 pasien).", "Ruangan ber-AC dengan tata interior modern.", "Kamar mandi dengan pemanas air.", "TV LED 50 Inchi dengan saluran premium.", "Sofa bed dan kursi tambahan untuk keluarga/pengunjung.", "Lemari pakaian besar dan meja kerja ekslusif.", "Mini kulkas, pantry, dan fasilitas pembuat teh/kopi.", "Makanan premium dengan pilihan menu harian.", "Parkir khusus untuk pasien VIP."]
    }
    
    context = {
        'title': 'Fasilitas Rumah Sakit Sehat Sejahtera',
        'fasilitas': 'Fasilitas',
        'keunggulan': 'Keunggulan',
        'fasilitas_list': fasilitas_list,
        'keunggulan_list': keunggulan_list,
        'kelas_kategori_list': kelas_kategori_list,
        'kelas_gambar_list': kelas_gambar_list,
        'kelas_deskripsi_list': kelas_deskripsi_list
    }
    return render(request, 'index.html', context)