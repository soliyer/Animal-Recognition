# gui.py

import tkinter as tk
from tkinter import filedialog
from main import get_prediction


def upload_action(event=None):
    file_path = filedialog.askopenfilename()
    if file_path:
        prediction = get_prediction(file_path)
        label_prediction.config(text=f"Predicted class: {prediction}")


root = tk.Tk()
root.title("Animal Image Recognition")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

btn_upload = tk.Button(frame, text="Upload an Image", command=upload_action)
btn_upload.pack(side=tk.TOP, padx=10, pady=10)

label_prediction = tk.Label(frame, text="Prediction will appear here")
label_prediction.pack(side=tk.TOP, pady=10)

root.mainloop()
