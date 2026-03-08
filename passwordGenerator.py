#TASK 3 - Password generator
import gradio as gr
import random
import string

# Function to generate a strong password
def generate_password(length):
    try:
        length = int(length)
        if length < 4:
            return "Password length should be at least 4 characters."

        # Define character sets
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate a random password
        password = ''.join(random.choice(characters) for _ in range(length))

        return password
    except ValueError:
        return "Invalid input! Please enter a valid number."

# Gradio Interface
iface = gr.Interface(
    fn=generate_password,
    inputs=gr.Textbox(label="Enter Password Length"),
    outputs=gr.Textbox(label="Generated Password"),
    title="Random Password Generator",
    description="Enter the desired password length, and get a secure, randomly generated password."
)

# Launch the web app
iface.launch()
