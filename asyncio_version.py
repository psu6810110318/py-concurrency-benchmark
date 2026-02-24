import asyncio
from utils import count_chars_in_file

async def run_asyncio(files):
    loop = asyncio.get_running_loop()
    
    tasks = [
        loop.run_in_executor(None, count_chars_in_file, f)
        for f in files
    ]
    counts = await asyncio.gather(*tasks)
    results = {}
    for f, c in zip(files, counts):
        results[f] = c
    return results