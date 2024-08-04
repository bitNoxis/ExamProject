import random
import tkinter as tk

from PIL import Image, ImageTk

from ExamProject.src.RoundedButton import RoundedButton
from ExamProject.src.GradientFrame import GradientFrame

# Initialize the root window
root = tk.Tk()
root.minsize(width=600, height=800)
root.title('Fitlistic')
root.configure(background="White")

# Variable to store the user's name
name = tk.StringVar()

# Dictionary to store quotations
quotations = {
    1: "Exercises is king and nutrition is queen. Combine the two and you will have a kingdom.",
    2: "The only bad workout is the one that didn't happen.",
    3: "Fitness is not about being better than someone else. It's about being better than you used to be."
}

# List of image file paths and corresponding texts
image_text_pairs = [
    ("../ExamProject/images/Squat.png", "15x3 Squat"),
    ("../ExamProject/images/Dips.png", "10x4 Dips"),
    ("../ExamProject/images/Meditate.png", "3 Minute Breathwork"),
    ("../ExamProject/images/Plank.png", "30 Seconds Plank"),
    ("../ExamProject/images/Stretch.png", "1 Minute Stretch")
]


# Clearing the widget for new usage
def clear_widgets(root):
    for widget in root.winfo_children():
        widget.destroy()


def intro_gui(root):
    clear_widgets(root)

    image_file_path = "images/Logo.png"
    image = Image.open(image_file_path)
    image = image.resize((300, 300), Image.Resampling.LANCZOS)

    root.logo_image = ImageTk.PhotoImage(image)
    logo_label = tk.Label(root, image=root.logo_image, bg="white")
    logo_label.place(relx=0.5, y=150, anchor="center")

    slogan_label = tk.Label(root,
                            text="Your holistic fitness journey starts here",
                            font=('Arial', 18, 'bold'),
                            bg="white", fg="black")
    slogan_label.place(relx=0.5, y=250, anchor="center")

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
                           text_color="white",
                           # Transporting the name over to the next screen
                           command=lambda: overview_gui(root, name.get())
                           )
    button.place(relx=0.5, y=600, anchor="center")


def overview_gui(root, user_name):
    clear_widgets(root)

    gradient_frame = GradientFrame(root, "lightgreen", "green", bg_color="white")
    gradient_frame.pack(fill="both", expand=True)

    welcome_label = tk.Label(root,
                             text=f"Welcome back, {user_name}",
                             font=('Arial', 18, 'bold'),
                             bg="white", fg="black")
    welcome_label.place(relx=0.5, y=100, anchor="center")

    score_label = tk.Label(root,
                           text="Wellbeing Score",
                           font=('Arial', 18, 'bold'),
                           bg="white", fg="black")
    score_label.place(relx=0.5, y=230, anchor="center")

    imagefinish_file_path = "../ExamProject/images/Score.png"
    imageFinish = Image.open(imagefinish_file_path)
    imageFinish = imageFinish.resize((335, 177))

    root.finish_image = ImageTk.PhotoImage(imageFinish)
    finishimage_label = tk.Label(root, image=root.finish_image, bg="white")
    finishimage_label.place(relx=0.5, y=335, anchor="center")

    start_label = tk.Label(root,
                           text="Start a Session",
                           font=('Arial', 18, 'bold'),
                           bg="white", fg="black")
    start_label.place(relx=0.5, y=475, anchor="center")

    button = RoundedButton(root,
                           300,
                           75,
                           25,
                           2,
                           '#42D742',
                           'white',
                           text="Fullbody Workout",
                           text_color="white",
                           command=lambda: exercise_gui(root, name.get())
                           )
    button.place(relx=0.5, y=540, anchor="center")

    button = RoundedButton(root,
                           300,
                           75,
                           25,
                           2,
                           '#42D742',
                           'white',
                           text="Upperbody Workout",
                           text_color="white",
                           command=lambda: exercise_gui(root, name.get())
                           )
    button.place(relx=0.5, y=630, anchor="center")

    button = RoundedButton(root,
                           300,
                           75,
                           25,
                           2,
                           '#42D742',
                           'white',
                           text="Power Recovery",
                           text_color="white",
                           command=lambda: exercise_gui(root, name.get())
                           )
    button.place(relx=0.5, y=720, anchor="center")


def exercise_gui(root, user_name):
    clear_widgets(root)

    gradient_frame = GradientFrame(root, "lightblue", "blue", bg_color="white")
    gradient_frame.pack(fill="both", expand=True)

    exercise_label = tk.Label(root,
                              text="Exercise Session",
                              font=('Arial', 18, 'bold'),
                              bg="white", fg="black")
    exercise_label.place(relx=0.5, y=75, anchor="center")

    details_label = tk.Label(root,
                             text="5 Exercises | 15 Minutes | 150 Calorie Burn",
                             font=('Arial', 14,),
                             bg="black", fg="white")
    details_label.place(relx=0.5, y=125, anchor="center")

    button = RoundedButton(root,
                           250,
                           75,
                           25,
                           5,
                           '#42D742',
                           'white',
                           text="Workout completed",
                           text_color="white",
                           command=lambda: exercisedone_gui(root, name.get())
                           )
    button.place(relx=0.5, y=675, anchor="center")

    photo = Image.open("images/X.png")
    photo = photo.resize((30, 30), Image.Resampling.LANCZOS)
    photoimage = ImageTk.PhotoImage(photo)

    cancel_button = tk.Button(root, bg="white", font="Helvetica", image=photoimage, compound=tk.LEFT,
                              command=lambda: overview_gui(root, user_name))
    cancel_button.image = photoimage  # Keep a reference to avoid garbage collection
    cancel_button.place(relx=0.05, rely=0.04, anchor="center")

    screen_height = root.winfo_screenheight()
    top_margin_height = int(screen_height * 0.22)

    container = tk.Frame(gradient_frame, bg="white")
    container.pack(pady=(top_margin_height, 20), fill="x")

    for image_path, description in image_text_pairs:
        frame = tk.Frame(container, bg="white")
        frame.pack(pady=10, padx=20, anchor="center")

        image = Image.open(image_path)
        image = image.resize((50, 50), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(frame, image=photo, bg="white")
        image_label.image = photo  # Keep a reference to prevent garbage collection
        image_label.pack(side="left", padx=10)

        text_label = tk.Label(frame, text=description, bg="white", font=('Arial', 14), anchor="w")
        text_label.pack(side="left", padx=10)


def exercisedone_gui(root, user_name):
    clear_widgets(root)

    imagefinish_file_path = "../ExamProject/images/Finish.png"
    imageFinish = Image.open(imagefinish_file_path)
    imageFinish = imageFinish.resize((255, 327), Image.Resampling.LANCZOS)

    root.finish_image = ImageTk.PhotoImage(imageFinish)
    finishimage_label = tk.Label(root, image=root.finish_image, bg="white")
    finishimage_label.place(relx=0.5, y=200, anchor="center")

    # Selecting one of the quotes with the random library
    motivational_quote = random.choice(list(quotations.values()))

    completed_label = tk.Label(root,
                               text=f"Congratulations {user_name}, you have completed your session!",
                               font=('Arial', 18, 'bold'), bg="white", fg="black", wraplength=500)
    completed_label.place(relx=0.5, y=450, anchor="center")

    quote_label = tk.Label(root,
                           text=motivational_quote,
                           font=('Arial', 14, 'italic'),
                           bg="white", fg="black", wraplength=500)
    quote_label.place(relx=0.5, y=525, anchor="center")

    button = RoundedButton(root,
                           200,
                           75,
                           25,
                           2,
                           '#42D742',
                           'white',
                           text="Back home",
                           text_color="white",
                           command=lambda: overview_gui(root, name.get())
                           )
    button.place(relx=0.5, y=675, anchor="center")


# Setting intro_gui as the initial screen
intro_gui(root)

root.mainloop()
