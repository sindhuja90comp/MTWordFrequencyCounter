import threading
from collections import Counter

def count_words(segment, result, index):
    print(f"Thread {index} started processing.")
    words = segment.split()
    freq = Counter(words)
    result[index] = freq
    print(f"Thread {index} finished. Intermediate count: {freq}")

def partition_text(text, n):
    print("Partitioning text into segments...")
    words = text.split()
    avg = len(words) // n
    segments = [' '.join(words[i*avg : (i+1)*avg]) for i in range(n)]
    if len(words) % n:
        segments[-1] += ' ' + ' '.join(words[n*avg:])
    print(f"Created {n} segments.")
    return segments

def print_table(counter, columns=5):
    items = list(counter.items())
    total = len(items)
    
    # Wider spacing: 20 chars for word, 10 chars for count
    header = ""
    for _ in range(columns):
        header += f"{'Word':<20}{'Count':<10}"
    print(header)
    print("-" * len(header))
    
    # Print rows row-wise with fixed-width columns to align counts
    for i in range(0, total, columns):
        row_items = items[i:i+columns]
        row_str = ""
        for word, count in row_items:
            row_str += f"{word:<20}{count:<10}"
        print(row_str)

def main():
    print("\n" + "="*50)
    print("     Welcome to Word Frequency Counter")
    print("     (Implemented using Multi-threading)")
    print("="*50 + "\n")

    filename = input("Enter the filename (e.g., sample.txt): ").strip()
    num_segments = int(input("Enter the number of segments (e.g., 4): "))

    print(f"\nReading file: {filename}")
    with open(filename, 'r') as f:
        text = f.read().lower()
    print("File read successfully.")

    segments = partition_text(text, num_segments)
    threads = []
    results = [None] * num_segments

    print("\nSpawning threads for each segment...")
    for i in range(num_segments):
        t = threading.Thread(target=count_words, args=(segments[i], results, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("\nAll threads have completed.")

    final_result = Counter()
    print("\nConsolidating results...")
    for r in results:
        final_result.update(r)

    print("\nFinal consolidated word frequency count:\n")
    print_table(final_result, columns=5)

if __name__ == "__main__":
    main()
