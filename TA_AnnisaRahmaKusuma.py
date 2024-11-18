import tkinter as tk
from tkinter import messagebox
from random import choice
from PIL import Image, ImageTk

class RecipeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Food Recipe by Nisa")
        self.root.geometry("900x600")
        self.root.configure(bg='salmon')

        #stack resep
        self.recipe_stack = {
            "Lauk pauk": {
                "Nabati": [
                    {"name": "Tempe Goreng", 
                     "details": [
                         "1 bungkus tempe", 
                         "1 siung bawang putih", 
                         "1/2 sdt ketumbar", 
                         "Tepung bumbu", 
                         "Garam secukupnya", 
                         "Minyak goreng."
                     ]},
                    {"name": "Tahu Goreng", 
                     "details": [
                         "4 buah tahu putih", 
                         "1 siung bawang putih", 
                         "1 sdt kunyit bubuk", 
                         "Garam secukupnya", 
                         "Minyak goreng."
                     ]},
                     {"name": "Tempe Mendoan", 
                     "details": [
                         "1 bungkus tempe", 
                         "2 siung bawang putih", 
                         "1/2 sdt ketumbar", 
                         "2 sdm tepung bumbu", 
                         "5 sdm Tepung terigu",
                         "3 batang daun bawang",
                         "Sejumput garam", 
                         "Minyak goreng."
                     ]},
                     {"name": "Tahu Kecap", 
                     "details": [
                         "5 buah tahu", 
                         "2 siung bawang putih", 
                         "1 siung bawang merah", 
                         "3/4 sdt garam", 
                         "1 sdt gula",
                         "3 buah cabe merah",
                         "Kecap manis sesuai selera", 
                         "Minyak secukupnya."
                     ]},
                     {"name": "Tahu Tempe Bacem", 
                     "details": [
                         "7 buah tahu", 
                         "1 bungkus tempe", 
                         "4 lembar daun salam", 
                         "1 sdt garam", 
                         "2 sdm kecap manis",
                         "2 sdm air asam jawa",
                         "2 siung bawang putih", 
                         "3 siung bawang merah",
                         "50 gram gula jawa",
                         "1 sdt ketumbar",
                         "3 cm lengkuas"
                     ]}
                ],
                "Hewani": [
                    {"name": "Ayam Goreng", 
                     "details": [
                         "1 ekor ayam", 
                         "4 siung bawang putih", 
                         "6 siung bawang merah",
                         "2 sdm ketumbar", 
                         "1 sdm garam", 
                         "1 sdt gula pasir"
                         "3 lembar daun jeruk dan salam",
                         "2 batang serai",
                         "2 cm kunyit",
                         "Minyak goreng"
                     ]},
                    {"name": "Ikan Nila Bakar", 
                     "details": [
                         "2 ekor ikan nila", 
                         "2 sdm kecap manis", 
                         "1 buah jeruk nipis", 
                         "3 siung bawang merah", 
                         "3 siung bawang putih",
                         "3 buah cabai",
                         "2 sdt garam",
                         "1 sdm kaldu ayam bubuk",
                         "1/4 sdt merica",
                         "1/2 cm kunyit dan jahe",
                         "minyak secukupnya."
                     ]},
                     {"name": "Rendang Sapi", 
                     "details": [
                         "1 kg daging sapi", 
                         "Santan peras dari 3 butir kelapa", 
                         "4 lembar daun jeruk", 
                         "3 batang serai", 
                         "4 butir asam kandis",
                         "100 ml minyak goreng",
                         "bumbu rendang daging sapi 1 kg",
                         "1 sdm garam",
                         "6 siung bawang merah dan bawang putih",
                         "10 cabe merah besar",
                         "Lengkuas, cengkeh dan kemiri"
                     ]},
                     {"name": "Semur Telur", 
                     "details": [
                         "6 telur ayam yang sudah direbus dan dikupas", 
                         "2 lembar daun salam", 
                         "1 serai", 
                         "3 sdm kecap manis", 
                         "1 sdm gula merah",
                         "1 sdt garam",
                         "150 ml santan kental",
                         "300 ml santan encer",
                         "6 butir bawang merah",
                         "3 siung bawang putih",
                         "kemiri, pala dan merica bubuk secukupnya"
                     ]},
                      {"name": "Udang Balado", 
                     "details": [
                         "1 kg udang kupas", 
                         "1/4 kg bawang merah", 
                         "5 siung bawang putih", 
                         "1/4 kg cabe merah", 
                         "1 buah tomat",
                         "4 buah jeruk limau",
                         "Garam dan gula secukupnya",
                         "1 buah jeruk nipis (untuk merendam udang)",
                         "Minyak secukupnya",
                         "Air secukupnya",
                     ]}
                ]
            },
            "Sayuran": {
                "Berkuah": [
                    {"name": "Sayur Asem", 
                     "details": [
                         "Sayuran (wortel, kacang panjang, jagung manis, dll)", 
                         "Asam jawa secukupnya", 
                         "2 cm lengkuas", 
                         "3 lembar daun salam", 
                         "5 siung bawang merah", 
                         "2 siung bawang putih",
                         "2 buah cabai merah", 
                         "1 sdt garam",
                         "1/2 sdt gula",
                         "1 liter air",
                         "Penyedap rasa secukupnya."
                     ]},
                    {"name": "Sup Jamur Kancing", 
                     "details": [
                         "125 gram jamur kancing", 
                         "100 gram dada ayam fillet (potong dadu)", 
                         "Sayuran(kentang, wortel, brokoli, dll)", 
                         "750 ml air", 
                         "2 siung bawang putih", 
                         "1 siung bawang merah", 
                         "1/2 bawang bombay",
                         "Sejumput lada",
                         "Penyedap rasa secukupnya."
                     ]},
                     {"name": "Sayur Bayam", 
                     "details": [
                         "1 ikat bayam", 
                         "1 jagung manis", 
                         "2 siung bawang merah", 
                         "3 cm kunci", 
                         "700 ml air", 
                         "1 siung bawang merah", 
                         "1 sdt garam",
                         "1/2 sdt gula pasir",
                         "Penyedap rasa secukupnya."
                     ]},
                     {"name": "Sayur Sawi Putih dan Bakso", 
                     "details": [
                         "1 bonggol sawi putih", 
                         "8 buah bakso, iris", 
                         "4 siung bawang putih", 
                         "Garam secukupnya", 
                         "Kaldu bubuk secukupnya", 
                         "1 sdt kecap ikan", 
                         "Air secukupnya",
                     ]},
                     {"name": "Sayur Gambas", 
                     "details": [
                         "1 buah gambas/ oyong", 
                         "6 jagung muda", 
                         "2 bungkus kecil soun", 
                         "3 siung bawang merah", 
                         "2 siung bawang putih", 
                         "750 ml air", 
                         "1/2 sdt garam",
                         "1/2 sdt gula pasir",
                         "Kaldu bubuk secukupnya."
                     ]},
                     {"name": "Tomyam", 
                     "details": [
                         "4 buah tahu sutra", 
                         "Crabstick, udang, bakso seafood secukupnya", 
                         "Jamur kancing dan pakcoy secukupnya", 
                         "2 sdm minyak ikan", 
                         "1 wortel", 
                         "4 cabai rawit", 
                         "1/2 sdt garam",
                         "3 batang serai",
                         "5 lembar daun jeruk",
                         "1 sdm ebi",
                         "3 siung bawang putih",
                         "1,5 liter kaldu udang."
                     ]}
                ],
                "Bersantan": [
                    {"name": "Lodeh Kacang Terong", 
                     "details": [
                         "1 buah terong", 
                         "150 gram kacang panjang", 
                         "1 jagung manis",
                         "2 siung bawang putih", 
                         "3 siung bawang merah", 
                         "Cabai rawit",
                         "1 lembar daun salam",
                         "3 cm lengkuas",
                         "800 ml santan",
                         "1 sdt garam",
                         "1/2 sdt gula pasir",
                         "Penyedap rasa secukupnya."
                     ]},
                    {"name": "Sayur Bobor Kangkung", 
                     "details": [
                         "1 ikat kangkung", 
                         "1 labu siam besar", 
                         "1 wortel", 
                         "Kemangi secukupnya", 
                         "1 siung bawang merah", 
                         "1 siung bawang putih",
                         "1/2 sdt garam",
                         "1 kemiri",
                         "1 bungkus santan instan (65 ml)",
                         "Daun salam."
                     ]},
                     {"name": "Gulai Nangka", 
                     "details": [
                         "1/4 kg nangka muda", 
                         "1/4 kg daging sapi tetelan", 
                         "1/2 bungkus santan kelapa kental", 
                         "Serai, daun salam, daun jeruk purut", 
                         "sejempol lengkuas", 
                         "Air secukupnya",
                         "1/2 sdt garam",
                         "Air dan gula secukupnya",
                         "3 siung bawang putih",
                         "4 siung bawang merah",
                         "Cabai merah secukupnya",
                         "Kunyit, jahe dan kencur."
                     ]},
                     {"name": "Selada Air Kuah Santan", 
                     "details": [
                         "2 ikat selada air", 
                         "5 butir bawang merah", 
                         "3 siung bawang putih", 
                         "2 buah cabai merah", 
                         "segenggam udang kering, goreng", 
                         "500 ml santan sedang",
                         "Garam dan gula secukupnya."
                     ]},
                ],
                "Tumis": [
                    {"name": "Tumis Kangkung Saus Tiram", 
                     "details": [
                         "1 ikat kangkung", 
                         "2 siung bawang putih", 
                         "2 siung bawang merah", 
                         "Garam secukupnya",
                         "1 sdm saus tiram",
                         "75 ml air",
                         "2 buah otak-otak(opsional)",
                         "1 sdm minyak goreng"
                     ]},
                    {"name": "Tumis Buncis", 
                     "details": [
                         "250g buncis", 
                         "2 siung bawang putih", 
                         "1 sdm saus tiram", 
                         "2 buah cabai merah",
                         "2 butir telur ayam",
                         "3 butir bawang merah",
                         "100 ml air",
                         "Garam secukupnya"
                         "Royco ayam secukupnya",
                         "1 sdm kecap manis",
                         "Sejumput merica",
                         "1 sdm minyak goreng"
                     ]},
                     {"name": "Tumis Tauge", 
                     "details": [
                         "200g tauge", 
                         "4 siung bawang putih", 
                         "1 sdm saus tiram", 
                         "4 buah cabai merah",
                         "1/2 tomat merah",
                         "6 butir bawang merah",
                         "30 ml air",
                         "Garam secukupnya",
                         "1/2 sdt gula",
                         "Sejumput merica",
                         "1 sdm minyak goreng"
                     ]},
                ]
            },
            "Camilan": {
                "Manis": [
                    {"name": "Bolu Kukus Pandan", 
                     "details": [
                         "125g tepung terigu", 
                         "100g gula pasir", 
                         "2 butir telur", 
                         "120ml susu cair", 
                         "1 sdt baking powder",
                         "1 sdt emulsifier (SP)",
                         "1 sdt pasta pandan"
                     ]},
                    {"name": "Kue Putri Salju", 
                     "details": [
                         "100gr butter", 
                         "70gr gula halus", 
                         "50gr margarin", 
                         "50g keju parut",
                         "Sedikit garam",
                         "1 butir kuning telur",
                         "2 kuning telur rebus (haluskan)",
                         "175gr tepung terigu",
                         "15gr tepung maizena",
                         "15gr susu bubuk."
                     ]},
                     {"name": "Bika Ambon", 
                     "details": [
                         "12 butir kuning telur", 
                         "150 gram gula pasir", 
                         "100 gram tepung sagu", 
                         "200 ml santan kental",
                         "1/4 sdt garam",
                         "10 lembar daun jeruk",
                         "1 serai",
                         "1 sdt ragi instan",
                         "1 sdm gula pasir",
                         "1 sdm terigu",
                         "50 ml air hangat"
                     ]},
                     {"name": "Mochi Strawberry", 
                     "details": [
                         "130 gr tepung ketan", 
                         "130 gr air", 
                         "65 ml santan instan", 
                         "2 1/2 sdm gula",
                         "1/2 sdt garam",
                         "2 sdm minyak goreng",
                         "Pewarna makanan merah secukupnya",
                         "5 sdm maizena",
                         "Strawberry segar",
                         "Selai strawberry",
                         "Krim strawberry."
                     ]},
                     {"name": "Donat Kentang", 
                     "details": [
                         "Tepung protein tinggi 250 gr", 
                         "Terigu 250 gr", 
                         "Topping sesuai selera (meises,keju,glaze,gula halus)", 
                         "Ragi instan 8gr",
                         "Roti improver 3gr",
                         "Gula 50gr",
                         "Susu bubuk skim 25gr",
                         "Garam 8gr",
                         "Kuning telur 60gr",
                         "Margarin untuk kue 75gr",
                         "Air Dingin 225ml"
                     ]},
                ],
                "Asin": [
                    {"name": "Risol Mayo", 
                     "details": [
                         "10 buah kulit lumpia siap pakai", 
                         "5 buah sosis", 
                         "5 lembar keju", 
                         "4 butir telur rebus",
                         "Mayones secukupnya",
                         "Mentega",
                         "Minyak untuk menggoreng",
                         "====Bahan Pelapis====",
                         "¼ kg tepung panir",
                         "Tepung terigu secukupnya",
                         "½ sdt garam",
                         "Air secukupnya."
                     ]},
                    {"name": "Cireng Ayam Suwir Pedas", 
                     "details": [
                         "15 sdm tepung terigu",
                         "15 sendok makan tepung tapioka", 
                         "2 sachet kaldu bubuk", 
                         "air panas secukupnya", 
                         "====Bahan Isian====",
                         "2 potong dada ayam yang telah direbus",
                         "10 siung bawang merah",
                         "10 siung bawang putih",
                         "10 buah cabai merah",
                         "2 sendok teh cabai bubuk",
                         "Gula dan garam secukupnya", 
                         "Daun bawang secukupnya"
                     ]},
                      {"name": "Cilor", 
                     "details": [
                         "10 sdm tepung sagu",
                         "7 sdm tepung terigu", 
                         "2 siung bawang putih parut", 
                         "1/2 sdt garam", 
                         "1/2 sdt kaldu bubuk",
                         "Secukupnya air matang",
                         "1 butir telur kocok lepas."
                     ]},
                     {"name": "Dimsum Ayam", 
                     "details": [
                         "3 potong ayam paha, fillet dagingnya",
                         "1 sdt garam", 
                         "1 sdm gula pasir", 
                         "1/2 sdt lada halus",
                         "3/4 sdm kecap asin",
                         "3/4 sdm saus tiram",
                         "25 gram sagu tani",
                         "1 lembar daun bawang,iris",
                         "kulit pangsit rebus 15 buah",
                         "====Bahan Saus====",
                         "5 sachet saus sambal",
                         "1 sdt gula pasir",
                         "3 sdm air panas."
                     ]},
                ]
            }
        }

        self.welcome_page()

    def welcome_page(self):
        # Welcome page UI
        for widget in self.root.winfo_children():
            widget.destroy()
        
        welcome_frame = tk.Frame(self.root, bg='wheat')
        welcome_frame.pack(pady=50)

        welcome_label = tk.Label(welcome_frame, text="Selamat Datang", font=("Century", 25), bg='ivory')
        welcome_label.pack(pady=20)
        
        welcome_label = tk.Label(welcome_frame, text="Random Food Recipe Picker by Nisa", font=("Century", 20), bg='ivory')
        welcome_label.pack(pady=20)

        welcome_label = tk.Label(welcome_frame, text="Full screen untuk pengalaman lebih nyaman", font=("Century", 15), bg='ivory')
        welcome_label.pack(pady=20)

        start_button = tk.Button(welcome_frame, text="Mulai", font=("Century", 30), bg='ivory', command=self.login_page)
        start_button.pack(pady=10)

        try:
            image = Image.open("A.jpg")  
            image = image.resize((400, 250))  
            self.welcome_photo = ImageTk.PhotoImage(image)
            label_image = tk.Label(welcome_frame, image=self.welcome_photo)
            label_image.pack(pady=10)
        except FileNotFoundError:
            messagebox.showerror("Error", "Image 'A.jpg' not found.")

    def login_page(self):
        # Login page UI
        for widget in self.root.winfo_children():
            widget.destroy()

        welcome_frame = tk.Frame(self.root, bg='wheat')
        welcome_frame.pack(pady=50)

        welcome_label = tk.Label(welcome_frame, text="Sebelum lanjut, Login dulu yuk", font=("Century", 25), bg='ivory')
        welcome_label.pack(pady=20)
        
        login_frame = tk.Frame(self.root, bg='wheat')
        login_frame.pack(pady=10)        

        tk.Label(login_frame, text="Login", font=("Century", 40), bg='ivory').grid(row=0, column=0, columnspan=2, pady=20)

        # Username Label dan Box disamping
        tk.Label(login_frame, text="Username:", font=("Century", 20), bg='ivory').grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.username_entry = tk.Entry(login_frame, font=("Century", 20))
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(login_frame, text="Password:", font=("Century", 20), bg='ivory').grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.password_entry = tk.Entry(login_frame, show="*", font=("Century", 20))
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        self.terms_var = tk.IntVar()
        terms_checkbox = tk.Checkbutton(login_frame, text="Saya menyetujui syarat & ketentuan", bg='ivory', variable=self.terms_var)
        terms_checkbox.grid(row=3, column=0, columnspan=2, pady=10)

        login_button = tk.Button(login_frame, text="Login", font=("Century", 20), bg='ivory', command=self.validate_login)
        login_button.grid(row=4, column=0, columnspan=2, pady=10)

    def validate_login(self):
        # Login validation
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not username or not password:
            messagebox.showwarning("Error", "Username dan Password harus diisi")
        elif not self.terms_var.get():
            messagebox.showwarning("Error", "Anda harus menyetujui syarat & ketentuan")
        else:
            self.recipe_category_page()

    def recipe_category_page(self):
        # Recipe category selection page
        for widget in self.root.winfo_children():
            widget.destroy()

        category_frame = tk.Frame(self.root, bg='salmon')
        category_frame.pack(pady=50)

        tk.Label(category_frame, text="Pilih Kategori Resep", font=("Century", 30), bg='ivory').pack(pady=70)

        images = {}
        frames = tk.Frame(category_frame, bg='Salmon')
        frames.pack()

        for category, img_file in zip(["Lauk pauk", "Sayuran", "Camilan"], ["Lauk.png", "Sayurr.jpg", "camilan.jpg"]):
            try:
                img = Image.open(img_file).resize((200, 150))
                images[category] = ImageTk.PhotoImage(img)
            except FileNotFoundError:
                messagebox.showerror("Error", f"Image '{img_file}' not found.")
                return

        for idx, category in enumerate(["Lauk pauk", "Sayuran", "Camilan"]):
            frame = tk.Frame(frames, bg='salmon')
            frame.pack(side=tk.LEFT, padx=20, pady=30)

            img_label = tk.Label(frame, image=images[category], bg='ivory')
            img_label.image = images[category]
            img_label.pack()

            button = tk.Button(frame, text=category, bg='ivory', font=("Century", 20), command=lambda c=category: self.show_subcategories(c))
            button.pack(pady=60)

    def show_subcategories(self, category):
        # Show subcategories for the selected category
        for widget in self.root.winfo_children():
            widget.destroy()

        subcategory_frame = tk.Frame(self.root, bg='salmon')
        subcategory_frame.pack(pady=60)

        tk.Label(subcategory_frame, text=f"Pilih Subkategori {category}", font=("Century", 30), bg='ivory').pack(pady=50)

        images = {}
        subcategories = []
        if category == "Lauk pauk":
            subcategories = [("Nabati", "nabati.jpg"), ("Hewani", "hewani.jpg.webp")]
        elif category == "Sayuran":
            subcategories = [("Berkuah", "berkuahh.jpg"), ("Bersantan", "bersantan.jpg"), ("Tumis", "tumis.jpg")]
        elif category == "Camilan":
            subcategories = [("Manis", "manis.jpg"), ("Asin", "asin.jpg")]

        frames = tk.Frame(subcategory_frame, bg='salmon')
        frames.pack()

        for subcategory, img_file in subcategories:
            try:
                img = Image.open(img_file).resize((180, 150))
                images[subcategory] = ImageTk.PhotoImage(img)
            except FileNotFoundError:
                messagebox.showerror("Error", f"Image '{img_file}' not found.")
                return

        for subcategory, img in images.items():
            frame = tk.Frame(frames, bg='salmon')
            frame.pack(side=tk.LEFT, padx=20, pady=40)

            img_label = tk.Label(frame, image=img, bg='ivory')
            img_label.image = img
            img_label.pack()

            button = tk.Button(frame, text=subcategory, bg='ivory', font=("Century", 20), command=lambda s=subcategory: self.show_recipe(category, s))
            button.pack(pady=35)

        # Add back button to go back to category page
        back_button = tk.Button(subcategory_frame, text="Kembali", font=("Century", 20), bg='ivory', command=self.recipe_category_page)
        back_button.pack(pady=10)

    def format_recipe_details(self, details):
        """
        Mengubah daftar bahan menjadi string multi-baris dengan tanda titik (-) di awal setiap baris.
        """
        return "\n".join(f"- {item}" for item in details)

    def show_recipe(self, category, subcategory):
        # Display a random recipe from the selected subcategory
        recipes = self.recipe_stack[category][subcategory]
        recipe = choice(recipes)
        formatted_details = self.format_recipe_details(recipe['details'])
        recipe_text = f"{recipe['name']}\n\nBahan yang dibutuhkan\n{formatted_details}"

        for widget in self.root.winfo_children():
            widget.destroy()

        recipe_frame = tk.Frame(self.root, bg='salmon')
        recipe_frame.pack(pady=20, padx=30, fill=tk.BOTH, expand=True)

        tk.Label(recipe_frame, text=f"Resep {subcategory}", font=("Century", 30), bg='ivory').pack(pady=10)
        
        # Menggunakan Label dengan opsi justify dan anchor untuk perataan kiri
        recipe_label = tk.Label(recipe_frame, text=recipe_text, font=("Century", 20), bg='wheat', justify="left", anchor="w", padx=10)
        recipe_label.pack(pady=10, fill=tk.BOTH, expand=True)

        back_button = tk.Button(recipe_frame, text="Kembali", font=("Century", 20), bg='ivory', command=lambda: self.show_subcategories(category))
        back_button.pack(pady=10)

# Inisialisasi aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()


