import tkinter as tk
from PIL import Image, ImageTk
from ExamProject.src.RoundedButton import RoundedButton

class GradientFrame(tk.Canvas):

    def __init__(self, parent, color1="red", color2="black", bg_color="white", **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self._bg_color = bg_color
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        # Drawing of the gradient
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        gradient_height = int(height * 0.3)
        (r1, g1, b1) = self.winfo_rgb(self._color1)
        (r2, g2, b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2 - r1) / limit
        g_ratio = float(g2 - g1) / limit
        b_ratio = float(b2 - b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
            self.create_line(i, 0, i, gradient_height, tags=("gradient",), fill=color)

        # Fill the rest with bg_color
        self.create_rectangle(0, gradient_height, width, height, fill=self._bg_color, outline="")

        self.lower("gradient")

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
                           command=lambda: second_gui(root))

    button.place(relx=0.5, y=600, anchor="center")

def second_gui(root):
    clear_widgets(root)

    gradient_frame = GradientFrame(root, "lightgreen", "green", bg_color="white")
    gradient_frame.pack(fill="both", expand=True)

    welcome_label = tk.Label(gradient_frame,
                             text=f"Welcome",
                             font=('Arial', 18, 'bold'),
                             bg="white", fg="black")
    welcome_label.place(relx=0.5, y=250, anchor="center")

# Call the main GUI function to initialize the main page
main_gui(root)

root.mainloop()
