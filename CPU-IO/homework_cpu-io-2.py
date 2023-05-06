import os
import threading
import requests
from time import perf_counter, sleep
from multiprocessing import Process

# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU3U-4xDOog9iWCcdkA4Xgg4cawIYyG2O-RA&usqp=CAU"
    print(f"Processing image from {image_url} in process {os.getpid()}")
    sleep(4)
    start = perf_counter()
    _ = [i for i in range(100_000_000)]
    encryption_counter = perf_counter() - start
    print(f"Time for encrypt {encryption_counter}")

# I/O-bound task (downloading image from URL)
def download_image(image_url):
    print(f"Downloading image from {image_url} in thread {threading.current_thread().name}")
    start = perf_counter()
    response = requests.get(image_url)
    with open("../../image.jpg", "wb") as f:
        f.write(response.content)
    download_counter = perf_counter() - start
    print(f"time for download image {download_counter}")

try:
    start = perf_counter()
    encrypt_file("rockyou.txt")
    download_image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU3U-4xDOog9iWCcdkA4Xgg4cawIYyG2O-RA&usqp=CAU")
    total = perf_counter() - start
    print(f"Time taken for encryption task: {None}, I/O-bound task: {None}, Total: {total} seconds")
except Exception as e:
    print(f"Error occurred: {e}")