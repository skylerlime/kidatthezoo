import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import predict

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.root.resizable(False, False)
        self.root.configure(background='gray14')

        self.image_path = ''
        self.image_label = None
        self.prediction_label = None

        self.setup_ui()

    def setup_ui(self):
        title = tk.Label(self.root, text='KID AT THE ZOO', fg="DarkOrchid1", bg="gray14", font=('Helvetica', 28, 'bold'))
        subtitle = tk.Label(self.root, text='\"Mom what is that???\"', fg="DarkOrchid1", bg="gray14", font=('Helvetica', 14, 'italic'))
        title.pack(pady=(20, 0))
        subtitle.pack()

        image_frame = tk.Frame(self.root, bg='gray14', width=600, height=400)
        image_frame.pack(expand=True, fill='both')

        self.image_label = tk.Label(image_frame, bg='gray14')
        self.image_label.pack(expand=True)

        bottom_frame = tk.Frame(self.root, bg='gray14')
        bottom_frame.pack(side='bottom', fill='x', pady=20)

        self.prediction_label = tk.Label(bottom_frame, text='', fg="DarkOrchid1", bg="gray14", font=('Helvetica', 14, 'italic'))
        upload_btn = tk.Button(bottom_frame, text="Upload Image", fg="DarkOrchid1", bg="gray30",
                               font=('Helvetica', 20, 'bold'), border='0', command=self.upload_handler)
        predict_btn = tk.Button(bottom_frame, text="Predict Animal", fg="DarkOrchid1", bg="gray30",
                                font=('Helvetica', 20, 'bold'), border='0', command=self.predict_handler)

        self.prediction_label.pack(pady=(0, 10))
        button_row = tk.Frame(bottom_frame, bg="gray14")
        button_row.pack()

        upload_btn = tk.Button(button_row, text="Upload Image", fg="DarkOrchid1", bg="gray30",
                            font=('Helvetica', 20, 'bold'), border='0', command=self.upload_handler)
        predict_btn = tk.Button(button_row, text="Predict Animal", fg="DarkOrchid1", bg="gray30",
                                font=('Helvetica', 20, 'bold'), border='0', command=self.predict_handler)

        upload_btn.pack(side='left', padx=20)
        predict_btn.pack(side='left', padx=20)


    def upload_handler(self):
        file_path = filedialog.askopenfilename(
            title="Select a File",
            initialdir="./sampleimages",
            filetypes=(("Image files", "*.jpg *.jpeg *.png *.webp"),)
        )
        if file_path:
            self.image_path = file_path
            img = Image.open(file_path)
            img = img.resize((300, 300))
            photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            self.prediction_label.config(text="")

    def predict_handler(self):
        if self.image_path:
            prediction = predict.predict_image(self.image_path)
            self.prediction_label.config(text=f"\"Hmm... I think it's a {prediction}.\"")
        else:
            self.prediction_label.config(text="\"What are you looking at? Please upload an image first, dear.\"")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Kid at the Zoo")
    app = App(root)
    root.mainloop()
