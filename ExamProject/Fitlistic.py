import tkinter as tk

from PIL import Image, ImageTk

from ExamProject.src.RoundedButton import RoundedButton

# Initialize the root window
root = tk.Tk()
root.minsize(width=700, height=700)
root.title('Fitlistic')
root.configure(background="White")


# Clearing the widget for new usage
def clear_widgets(root):
    for widget in root.winfo_children():
        widget.destroy()


def main_gui(root):
    clear_widgets(root)

    image_file_path = "../ExamProject/images/LOGO.png"
    image = Image.open(image_file_path)
    image = image.resize((300, 300), Image.Resampling.LANCZOS)

    root.logo_image = ImageTk.PhotoImage(image)
    logo_label = tk.Label(root, image=root.logo_image, bg="white")
    logo_label.place(relx=0.5, y=150, anchor="center")

    welcome_label = tk.Label(root,
                             text="Your holistic fitness journey starts here",
                             font=('Arial', 18, 'bold'),
                             bg="white", fg="black")
    welcome_label.place(relx=0.5, y=250, anchor="center")

    entry_label = tk.Label(root,
                           text="Enter your name:",
                           font=('Arial', 20),
                           bg='white')
    entry_label.place(relx=0.5, y=400, anchor='center')

    name_entry = tk.Entry(root, font=('Arial', 20), bg='grey')
    name_entry.place(relx=0.5, y=450, anchor='center')

    button = RoundedButton(root,
                           200,
                           50,
                           25,
                           2,
                           '#42D742',
                           'white',
                           text="Get Started",
                           text_color="black",
                           #Hier
                           command=lambda: second_gui(root))

    button.place(relx=0.5, y=600, anchor="center")


def second_gui(root):
    clear_widgets(root)

    welcome_label = tk.Label(root,
                             text=f"Welcome",
                             font=('Arial', 18, 'bold'),
                             bg="white", fg="black")
    welcome_label.place(relx=0.5, y=250, anchor="center")

# Call the main GUI function to initialize the main page
main_gui(root)

root.mainloop()
