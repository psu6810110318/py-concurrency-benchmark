from concurrent.futures import ThreadPoolExecutor
from utils import count_chars_in_file

def run_thread(files):
    results = {}
    with ThreadPoolExecutor() as executor:
        counts = list(executor.map(count_chars_in_file, files))
    for f, c in zip(files, counts):
        results[f] = c
    return results