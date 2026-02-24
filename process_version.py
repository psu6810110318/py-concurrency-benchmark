from concurrent.futures import ProcessPoolExecutor
from utils import count_chars_in_file

def run_process(files):
    results = {}
    with ProcessPoolExecutor() as executor:
        counts = list(executor.map(count_chars_in_file, files))
    for f, c in zip(files, counts):
        results[f] = c
    return results