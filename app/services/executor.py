def execute_command(command: str):
    """
    Fungsi ini mengeksekusi instruksi yang kamu kirim.
    Bisa diisi logika AI atau eksekusi command tertentu.
    """
    # Contoh minimal, bisa diganti AI model
    if command.lower() == "halo":
        return "Halo Bani! Saya siap mengeksekusi perintahmu."
    elif command.lower().startswith("buat file"):
        filename = command.split(" ", 2)[2]
        with open(filename, "w") as f:
            f.write("File dibuat oleh AI Command Server")
        return f"File {filename} berhasil dibuat."
    else:
        return f"Perintah '{command}' tidak dikenali."
