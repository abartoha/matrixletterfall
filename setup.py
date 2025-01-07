from cx_Freeze import setup, Executable

# Define the executable and additional files
executables = [ Executable("main.py", target_name="matrix.exe", icon ="icon.ico")]

# Include necessary files (e.g., fonts)
include_files = ["MS_mincho.ttf"]

setup(
    name="Matrix Rain",
    version="1.0",
    description="Matrix Rain Simulation",
    options={"build_exe": {"include_files": include_files}},
    executables=executables
)
