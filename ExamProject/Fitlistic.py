import tkinter as tk

from PIL import Image, ImageTk

from ExamProject.src.RoundedButton import RoundedButton
from ExamProject.src.GradientFrame import GradientFrame

# Initialize the root window
root = tk.Tk()
root.minsize(width=700, height=800)
root.title('Fitlistic')
root.configure(background="White")

# Variable to store the user's name
name = tk.StringVar()


# Clearing the widget for new usage
def clear_widgets(root):
    for widget in root.winfo_children():
        widget.destroy()


def intro_gui(root):
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

    name_entry = tk.Entry(root, textvariable=name, font=('Arial', 20), bg='grey')
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
                           # Transporting the name over to the next screen
                           command=lambda: overview_gui(root, name.get())
                           )
    button.place(relx=0.5, y=600, anchor="center")


def overview_gui(root, user_name):
    clear_widgets(root)

    gradient_frame = GradientFrame(root, "lightgreen", "green", bg_color="white")
    gradient_frame.pack(fill="both", expand=True)

    welcome_label = tk.Label(root,
                             text=f"Welcome, {user_name}",
                             font=('Arial', 18, 'bold'),
                             bg="white", fg="black")
    welcome_label.place(relx=0.5, y=100, anchor="center")

    welcome_label = tk.Label(root,
                             text="Start a Session",
                             font=('Arial', 18, 'bold'),
                             bg="white", fg="black")
    welcome_label.place(relx=0.5, y=350, anchor="center")

    button = RoundedButton(root,
                           300,
                           100,
                           25,
                           5,
                           '#42D742',
                           'white',
                           text="Fullbody Workout",
                           text_color="black",
                           command=lambda: exercise_gui(root, name.get())
                           )
    button.place(relx=0.5, y=425, anchor="center")

    button = RoundedButton(root,
                           300,
                           100,
                           25,
                           5,
                           '#42D742',
                           'white',
                           text="Fullbody Workout",
                           text_color="black",
                           )
    button.place(relx=0.5, y=550, anchor="center")

    button = RoundedButton(root,
                           300,
                           100,
                           25,
                           5,
                           '#42D742',
                           'white',
                           text="Power Recovery",
                           text_color="black",
                           )
    button.place(relx=0.5, y=675, anchor="center")


def exercise_gui(root, user_name):
    clear_widgets(root)

    gradient_frame = GradientFrame(root, "lightgreen", "green", bg_color="white")
    gradient_frame.pack(fill="both", expand=True)

    welcome_label = tk.Label(root,
                             text="Exercise Session",
                             font=('Arial', 18, 'bold'),
                             bg="white", fg="black")
    welcome_label.place(relx=0.5, y=100, anchor="center")

    button = RoundedButton(root,
                           200,
                           75,
                           25,
                           5,
                           '#42D742',
                           'white',
                           text="Workout done",
                           text_color="black",
                           command=lambda: exercisedone_gui(root, name.get())
                           )
    button.place(relx=0.5, y=675, anchor="center")


def exercisedone_gui(root, user_name):
    clear_widgets(root)

    gradient_frame = GradientFrame(root, "lightgreen", "green", bg_color="white")
    gradient_frame.pack(fill="both", expand=True)

    button = RoundedButton(root,
                           300,
                           100,
                           25,
                           5,
                           '#42D742',
                           'white',
                           text="Back",
                           text_color="black",
                           command=lambda: overview_gui(root, name.get())
                           )
    button.place(relx=0.5, y=675, anchor="center")


# Call the main GUI function to initialize the main page
intro_gui(root)

root.mainloop()
