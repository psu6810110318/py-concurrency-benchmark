import time
import asyncio
import glob

from thread_version import run_thread
from asyncio_version import run_asyncio
from process_version import run_process


def print_result(title, result_dict, elapsed):
    print(f"\n===== {title} =====")
    total = 0
    for file, count in result_dict.items():
        print(f"{file} -> {count} chars")
        total += count
    print(f"Total chars: {total}")
    print(f"Time: {elapsed:.4f} sec")


def main():
    files = glob.glob("data/*.txt")

    if not files:
        print("❌ ไม่พบไฟล์ในโฟลเดอร์ data/")
        return

    print(f"📂 พบไฟล์ทั้งหมด {len(files)} ไฟล์")

    # -------- Thread --------
    start = time.time()
    thread_result = run_thread(files)
    thread_time = time.time() - start
    print_result("Thread", thread_result, thread_time)

    # -------- Asyncio --------
    start = time.time()
    asyncio_result = asyncio.run(run_asyncio(files))
    asyncio_time = time.time() - start
    print_result("Asyncio", asyncio_result, asyncio_time)

    # -------- Process Pool --------
    start = time.time()
    process_result = run_process(files)
    process_time = time.time() - start
    print_result("Process Pool", process_result, process_time)

    # -------- Summary --------
    print("\n📊 Summary Time Comparison")
    print(f"Thread       : {thread_time:.4f} sec")
    print(f"Asyncio      : {asyncio_time:.4f} sec")
    print(f"Process Pool : {process_time:.4f} sec")


if __name__ == "__main__":
    main()