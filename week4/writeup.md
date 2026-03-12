# Week 4 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: **Noor Khalisa** \
SUNet ID: **TODO** \
Citations: **GitHub Copilot Documentation, Pydantic V2 Migration Guide, FastAPI Lifespan Events Docs**

This assignment took me about **3** hours to do. 


## YOUR RESPONSES
### Automation #1
a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)
> Inspirasi datang dari Claude Code best practices mengenai pentingnya memberikan instruksi spesifik repositori. Karena bekerja di Windows, saya mengadaptasi konsep ini ke GitHub Copilot menggunakan .github/copilot-instructions.md agar AI memahami batasan lingkungan (PowerShell vs Makefile).

b. Design of each automation, including goals, inputs/outputs, steps
> Goal: Menghindari saran perintah Linux yang tidak valid di Windows.

> Inputs: Pertanyaan pengguna di Chat Copilot.

> Outputs: Perintah PowerShell yang valid (e.g., $env:PYTHONPATH).

> Steps: Membuat file instruksi yang mendefinisikan environment cs146s dan perintah rutin untuk run serta test.

c. How to run it (exact commands), expected outputs, and rollback/safety notes
> Commands: Ketik @workspace how to run tests di Copilot Chat.

> Expected Outputs: Copilot menyarankan python -m pytest dengan setting environment variable Windows.

> Rollback: Jika saran tidak bekerja, hapus file instruksi atau berikan koreksi langsung di chat.

d. Before vs. after (i.e. manual workflow vs. automated workflow)
> Before: Harus selalu mengetik manual atau mencari referensi perintah Windows yang panjang karena Makefile error.

> After: Copilot secara otomatis memberikan perintah yang tepat setiap kali ditanya, mempercepat alur kerja.

e. How you used the automation to enhance the starter application
> Saya menggunakannya untuk menjalankan testing dan startup server tanpa harus memodifikasi file Makefile asli, menjaga kompatibilitas proyek.


### Automation #2
a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)
> Terinspirasi dari SubAgents overview tentang pemisahan tugas khusus. Saya memposisikan Copilot sebagai "Refactor Agent" yang fokus mengubah kode usang (V1) menjadi modern (V2) berdasarkan pesan warning yang muncul saat pengetesan.

b. Design of each automation, including goals, inputs/outputs, steps
> Goal: Menghilangkan Deprecation Warnings pada Pydantic secara otomatis.

> Inputs: File backend/app/schemas.py.

> Outputs: Kode yang menggunakan ConfigDict dan model_config.

> Steps: Menggunakan Inline Chat (Ctrl + I) untuk mendeteksi class Config dan menggantinya dengan standar Pydantic V2.

c. How to run it (exact commands), expected outputs, and rollback/safety notes
> Commands: Pilih kode di file, tekan Ctrl + I, ketik Refactor to Pydantic V2.

> Expected Outputs: Perubahan otomatis pada file schemas.py dan penambahan import ConfigDict.

> Rollback: Gunakan Ctrl + Z atau tombol Discard pada jendela Copilot.

d. Before vs. after (i.e. manual workflow vs. automated workflow)
> Before: Harus mengubah manual satu per satu di setiap class model yang memakan waktu dan rentan salah ketik.

> After: Perubahan dilakukan secara instan dan konsisten di seluruh file oleh AI.

e. How you used the automation to enhance the starter application
> Automasi ini membersihkan terminal dari pesan peringatan yang mengganggu, membuat log pengujian lebih mudah dibaca dan kode aplikasi lebih masa kini (future-proof).


### *(Optional) Automation #3*
*If you choose to build additional automations, feel free to detail them here!*

a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)
> TODO

b. Design of each automation, including goals, inputs/outputs, steps
> TODO

c. How to run it (exact commands), expected outputs, and rollback/safety notes
> TODO

d. Before vs. after (i.e. manual workflow vs. automated workflow)
> TODO

e. How you used the automation to enhance the starter application
> TODO
