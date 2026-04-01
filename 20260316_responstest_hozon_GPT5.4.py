import time
import os
from datetime import datetime
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-5.4"
PROMPT = "Explain quantum computing in 500 words."

client = OpenAI(api_key=API_KEY)

def run_benchmark():
    print("=== GPT-5.4 Benchmark (chars/sec unified spec) ===")

    start = time.time()

    response = client.responses.create(
        model=MODEL,
        input=PROMPT
    )

    end = time.time()

    text = response.output_text
    chars = len(text)
    total_time = end - start
    cps = chars / total_time

    result = (
        "=== GPT-5.4 Benchmark ===\n"
        f"Timestamp:      {datetime.now()}\n"
        f"Total time:     {total_time:.3f} sec\n"
        f"Output chars:   {chars}\n"
        f"Chars/sec:      {cps:.2f}\n"
        "------------------\n"
    )

    print(result)

    # ファイル名を日時にする
    filename = f"gpt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(result)
        f.write("\n--- Output Text ---\n")
        f.write(text)

if __name__ == "__main__":
    run_benchmark()