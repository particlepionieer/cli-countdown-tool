import time
import os


def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(0.7)


def open_file(filepath):
    os.system(f"start {filepath}")
