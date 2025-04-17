import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class KasirApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Kasir")
        self.root.geometry("500x400")

        self.items = []
        self.total = 0

        self.create_widgets()

    def create_widgets(self):
        self.item_label = tk.Label(self.root, text="Nama Barang:")
        self.item_label.grid(row=0, column=0, padx=5, pady=5)

        self.item_entry = tk.Entry(self.root)
        self.item_entry.grid(row=0, column=1, padx=5, pady=5)

        self.price_label = tk.Label(self.root, text="Harga:")
        self.price_label.grid(row=1, column=0, padx=5, pady=5)

        self.price_entry = tk.Entry(self.root)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.root, text="Tambah", command=self.add_item)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.remove_button = tk.Button(self.root, text="Hapus", command=self.remove_item)
        self.remove_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.items_list = tk.Listbox(self.root, width=50)
        self.items_list.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.total_label = tk.Label(self.root, text="Total: Rp 0")
        self.total_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.save_button = tk.Button(self.root, text="Simpan Transaksi", command=self.save_transaction)
        self.save_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def add_item(self):
        item = self.item_entry.get()
        try:
            price = float(self.price_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Harga harus berupa angka!")
            return
        
        if item == "":
            messagebox.showerror("Error", "Nama barang tidak boleh kosong!")
            return

        self.items.append((item, price))
        self.total += price

        self.items_list.insert(tk.END, f"{item}: Rp {price}")
        self.total_label.config(text=f"Total: Rp {self.total}")

        self.item_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def remove_item(self):
        selected_index = self.items_list.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Pilih item untuk dihapus!")
            return

        index = selected_index[0]
        item, price = self.items[index]
        self.total -= price
        self.items.pop(index)

        self.items_list.delete(index)
        self.total_label.config(text=f"Total: Rp {self.total}")

    def save_transaction(self):
        if not self.items:
            messagebox.showerror("Error", "Tidak ada item untuk disimpan!")
            return

        now = datetime.now()
        filename = f"transaksi_{now.strftime('%Y%m%d_%H%M%S')}.txt"

        with open(filename, "w") as file:
            file.write("Transaksi Kasir\n")
            file.write("====================\n")
            for item, price in self.items:
                file.write(f"{item}: Rp {price}\n")
            file.write("====================\n")
            file.write(f"Total: Rp {self.total}\n")
            file.write(f"Waktu: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

        messagebox.showinfo("Info", f"Transaksi berhasil disimpan ke file {filename}")
        self.reset_app()

    def reset_app(self):
        self.items = []
        self.total = 0
        self.items_list.delete(0, tk.END)
        self.total_label.config(text="Total: Rp 0")
        self.item_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = KasirApp(root)
    root.mainloop()
