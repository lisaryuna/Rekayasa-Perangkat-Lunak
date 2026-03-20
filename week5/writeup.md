# Week 5 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: **Noor Khalisa** \
SUNet ID: **TODO** \
Citations: **Warp AI Agent for code generation and Task implementation**

This assignment took me about **2** hours to do. 


## YOUR RESPONSES
### Automation A: Warp Drive saved prompts, rules, MCP servers

a. Design of each automation, including goals, inputs/outputs, steps
> Python QA Checker.
> Goal: Memastikan kode yang dihasilkan agen AI memenuhi standar kualitas sebelum commit.
> Inputs: Perintah terminal make format, make lint, dan pytest.
> Steps: 1. Merapikan format (Black). 2. Mengecek error statis (Ruff). 3. Menjalankan unit tests (Pytest).

b. Before vs. after (i.e. manual workflow vs. automated workflow)
> Before: Saya harus mengetik tiga perintah berbeda secara manual setiap kali ada perubahan kode dan menunggu satu-satu.
> After: Cukup memanggil satu "Saved Prompt" di Warp Drive, dan seluruh rangkaian pengujian berjalan otomatis.

c. Autonomy levels used for each completed task (what code permissions, why, and how you supervised)
> Level: Full Autonomy untuk eksekusi terminal. Agen diberikan izin untuk memodifikasi file lokal karena lingkungannya berada di dalam virtual environment yang terisolasi. Saya mengawasi lewat panel output terminal untuk memastikan tidak ada file sistem yang terhapus.

d. (if applicable) Multi‑agent notes: roles, coordination strategy, and concurrency wins/risks/failures
> N/A (Fokus pada pengujian sekuensial).

e. How you used the automation (what pain point it resolves or accelerates)
> Otomatisasi ini menyelesaikan masalah "human error" saat lupa menjalankan linter. Ini menjamin repositori tetap bersih tanpa saya harus menghafal banyak command flags.



### Automation B: Multi‑agent workflows in Warp 

a. Design of each automation, including goals, inputs/outputs, steps
> Goal: Menyelesaikan Task 7 (Error Handling) dan Task 8 (Pagination) secara simultan.
> Inputs: Deskripsi tugas dari TASKS.md dalam bahasa natural.
> Steps: Membuka dua tab Warp terpisah, mengaktifkan Agent Mode di masing-masing tab, dan memberikan instruksi spesifik untuk setiap tugas.

b. Before vs. after (i.e. manual workflow vs. automated workflow)
> Before: Saya harus mengerjakan Task 7 sampai selesai, melakukan testing, lalu baru bisa pindah ke Task 8 agar tidak pusing dengan logika yang berbeda.
> After: Kedua tugas selesai dalam waktu yang hampir bersamaan (paralel), memotong waktu pengerjaan hingga 50%.

c. Autonomy levels used for each completed task (what code permissions, why, and how you supervised)
> Level: Full Read/Write. Agen diizinkan membaca docs/TASKS.md. Saya melakukan supervisi dengan memantau perubahan file secara real-time di VS Code.

d. (if applicable) Multi‑agent notes: roles, coordination strategy, and concurrency wins/risks/failures
> Roles: Agen 1 fokus pada Global Exception Handlers, Agen 2 fokus pada Query Logic di routers.
> Concurrency Wins: Sangat cepat.
> Risks: Sempat terjadi kegagalan import karena kedua agen mengedit file schemas.py secara bersamaan, namun berhasil diatasi dengan menyuruh agen melakukan "Self-fix" pada sintaks yang rusak.

e. How you used the automation (what pain point it resolves or accelerates)
> Mengatasi cognitive load (beban pikiran) saat harus memikirkan dua fitur berbeda. Saya hanya berperan sebagai "Reviewer" kode, bukan pengetik kode manual.


### (Optional) Automation C: Any Additional Automations
a. Design of each automation, including goals, inputs/outputs, steps
> TODO

b. Before vs. after (i.e. manual workflow vs. automated workflow)
> TODO

c. Autonomy levels used for each completed task (what code permissions, why, and how you supervised)
> TODO

d. (if applicable) Multi‑agent notes: roles, coordination strategy, and concurrency wins/risks/failures
> TODO

e. How you used the automation (what pain point it resolves or accelerates)
> TODO

