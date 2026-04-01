import time
import os
from datetime import datetime
from google import genai

API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = "gemini-3.1-pro-preview"
PROMPT = "Explain quantum computing in 500 words."

client = genai.Client(api_key=API_KEY)

def run_benchmark():
    print("=== Gemini 3.1 Pro Benchmark (Legacy SDK Mode) ===")

    start = time.time()

    response = client.models.generate_content(
        model=MODEL,
        contents=PROMPT
    )

    end = time.time()

    text = response.text
    chars = len(text)
    total_time = end - start
    cps = chars / total_time

    result = (
        "=== Gemini 3.1 Pro Benchmark ===\n"
        f"Timestamp:      {datetime.now()}\n"
        f"Total time:     {total_time:.3f} sec\n"
        f"Output chars:   {chars}\n"
        f"Chars/sec:      {cps:.2f}\n"
        "------------------\n"
    )

    print(result)

    # ファイル名を日時にする
    filename = f"gemini_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(result)
        f.write("\n--- Output Text ---\n")
        f.write(text)

if __name__ == "__main__":
    run_benchmark()