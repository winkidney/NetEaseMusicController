from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["message"],
    "excludes": [
        "tkinter",
        "ssl",
        "sqlite3",
    ],
    "optimize": 2,
    'include_files': [
        "templates",
        "static"
    ],
}


setup(
    name='ne_music_controller',
    version='0.0.1',
    url='https://github.com/winkidney/NetEaseMusicController',
    license='MIT',
    author='winkidney',
    author_email='winkidney@gmail.com',
    description='mobile controller for  NetEase Music on PC',
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "music_switcher.py",
            packages=["flask", "autopy"],
        )
    ]
)
