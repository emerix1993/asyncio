import os
import threading
import requests
from time import perf_counter, sleep
from multiprocessing import Process

# encryption_counter = 0
# download_counter = 0
# total = 0

# CPU-bound task (heavy computation)
def encrypt_file(path):
    start = perf_counter()
    image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU3U-4xDOog9iWCcdkA4Xgg4cawIYyG2O-RA&usqp=CAU"
    print(f"Processing image from {image_url} in process {os.getpid()}")
    _ = [i for i in range(100_000_000)]
    # sleep(4)
    encryption_counter = perf_counter() - start
    print(f"Time for encrypt {encryption_counter}")


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    start = perf_counter()
    print(f"Downloading image from {image_url} in thread {threading.current_thread().name}")
    response = requests.get(image_url)
    with open("../../image.jpg", "wb") as f:
        f.write(response.content)
    download_counter = perf_counter() - start
    print(f"time for download image {download_counter}")
    # total = encryption_counter + download_counter
    # print(total)


# try:
#     start = perf_counter()
#     encrypt_file("rockyou.txt")
#     download_image(
#         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU3U-4xDOog9iWCcdkA4Xgg4cawIYyG2O-RA&usqp=CAU")
#     total = perf_counter() - start
#     print(
#         f"Time taken for encryption task: {encryption_counter}, I/O-bound task: {download_counter}, Total: {total} seconds")
# except Exception as e:
#     print(f"Error occurred: {e}")

if __name__ == "__main__":
    start = perf_counter()
    p1 = Process(target=encrypt_file, args=("path/to/file",))
    p2 = Process(target=download_image, args=("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU3U-4xDOog9iWCcdkA4Xgg4cawIYyG2O-RA&usqp=CAU",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    total = perf_counter() - start
    print(f"Time taken for encryption task: {None}, I/O-bound task: {True}, Total: {total} seconds")
