import os
import customtkinter as ctk

# Download song function
def download_song():
    spotify_url = entry.get()
    if spotify_url.strip() == "":
        return

    download_button.configure(state="disabled", text="Downloading...")
    progress_bar.set(0.5)  # Half filled to show 'in progress'
    root.update_idletasks()

    download_folder = "Freakquency"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    command = f"spotdl download {spotify_url} --output {download_folder}"
    os.system(command)

    progress_bar.set(1.0)  # Fully filled on complete
    download_button.configure(state="normal", text="Download Now")

    # Reset the progress bar after 3 seconds
    root.after(3000, reset_progress_bar)

# Reset Progress Bar
def reset_progress_bar():
    progress_bar.set(0)

# --- UI Setup ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Freakquency - Spotify Downloader")
root.geometry("400x400")
root.resizable(False, False)

# Frame
frame = ctk.CTkFrame(root, width=380, height=380, corner_radius=20, fg_color="#242424")
frame.pack(padx=5, pady=5, expand=True)  # Pack the frame with 20px gap on all sides

# --- UI Components ---
# Spotify logo
logo_label = ctk.CTkLabel(frame, text="🎵", font=("Arial Black", 50), text_color="#1DB954")
logo_label.pack(pady=(0, 10))

# Heading
heading = ctk.CTkLabel(frame, text="Freakquency", font=("Arial Bold", 24), text_color="#FFFFFF")
heading.pack(pady=(0, 20))

# URL Entry
entry = ctk.CTkEntry(frame, placeholder_text="Paste your Spotify link here...", width=300,
                    corner_radius=10, fg_color="#303030", font=("Arial Italic", 14),
                    text_color="#FFFFFF", height=35, placeholder_text_color="#777777")
entry.pack(pady=(0, 20))

# Download Button
download_button = ctk.CTkButton(frame, text="Download Now", command=download_song,
                                 width=160, height=40, corner_radius=10,
                                 font=("Arial Bold", 16),
                                 fg_color="#1DB954", text_color="#FFFFFF",
                                 hover_color="#19A94D")
download_button.pack(pady=(0, 20))

# Progress Bar
progress_bar = ctk.CTkProgressBar(frame, width=250, height=8, corner_radius=50)
progress_bar.set(0)
progress_bar.pack(pady=(0, 0))

# Start the App
root.mainloop()
