# Multi-threaded Cache Simulator

## Tujuan Tugas

Program ini dibuat untuk mensimulasikan cara kerja cache pada sistem multi-thread dan untuk mengamati perbedaan perilaku sistem saat menggunakan dan tidak menggunakan protokol koherensi. Dalam sistem komputasi modern, koherensi cache sangat penting agar data yang disimpan pada cache lokal masing-masing thread tetap konsisten dengan memori utama yang dibagikan bersama (shared memory). Simulasi ini bertujuan untuk menunjukkan bagaimana dua thread (CPU1 dan CPU2) mengakses dan memodifikasi variabel bersama (x) dalam dua skenario berbeda: tanpa koherensi dan dengan koherensi.


## Hasil

### Tanpa Koherensi

![alt text](tanpa_koherensi.png)

Pada skenario tanpa koherensi, masing-masing thread membaca dan menulis langsung ke shared memory. Karena tidak ada salinan lokal di cache, setiap operasi baca dan tulis dilakukan secara langsung ke memori utama. Hal ini memang terlihat sederhana, namun berisiko tinggi terjadi data race, yaitu kondisi di mana beberapa thread membaca dan menulis ke data yang sama secara bersamaan, sehingga menyebabkan hasil yang tidak konsisten atau sulit diprediksi. Dalam simulasi ini, meskipun hasil akhirnya tetap x = 3, proses menuju nilai tersebut menunjukkan bahwa kedua thread secara bersamaan bisa menulis nilai yang sama ke shared memory setelah membaca nilai lama, yang dapat menyebabkan pemborosan siklus eksekusi atau bahkan inkonsistensi dalam skenario yang lebih kompleks.

### Dengan Koherensi

![alt text](dengan_koherensi-1.png)

Pada skenario dengan koherensi, setiap thread memiliki cache lokal yang menyimpan salinan nilai x dari memori utama. Sebelum menulis ulang nilai ke shared memory, nilai tersebut terlebih dahulu dimodifikasi di cache lokal. Mekanisme ini menggambarkan bagaimana protokol koherensi bekerja: setiap CPU menyinkronkan cache lokalnya dengan memori utama agar data tetap konsisten. Meskipun hasil akhir simulasi juga menunjukkan nilai x = 3, namun prosesnya jauh lebih tertata dan mencerminkan bagaimana sistem cache sesungguhnya bekerja di prosesor multi-core saat ini. Koherensi membuat sistem lebih efisien dalam pembacaan data karena tidak harus selalu mengakses memori utama, dan memastikan bahwa perubahan data pada satu cache bisa diketahui oleh cache lain.


## Kesimpulan

Hasil dari kedua simulasi tersebut menunjukkan bahwa meskipun nilai akhir dapat terlihat sama, pendekatan dengan koherensi jauh lebih aman, efisien, dan realistis untuk sistem paralel di dunia nyata. Simulasi ini menggambarkan pentingnya implementasi protokol koherensi untuk menghindari inkonsistensi data yang disebabkan oleh akses paralel dari banyak thread. Oleh karena itu, penggunaan cache dengan protokol koherensi sangat direkomendasikan untuk memastikan akurasi dan efisiensi dalam komputasi multi-thread.

