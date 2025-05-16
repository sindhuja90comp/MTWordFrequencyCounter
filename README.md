# MTWordFrequencyCounter

A multi-threaded Python application that counts the frequency of words in a text file by partitioning the file into segments and processing each segment concurrently.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Requirements](#requirements)
4. [How to Run](#how-to-run)
5. [Sample Input](#sample-input)
6. [Output](#output)
7. [License](#license)

---

## Project Overview

**MTWordFrequencyCounter** is designed to efficiently count word frequencies in a text file. The workload is divided among multiple threads, each responsible for a segment of the file, and results are merged for a consolidated view.

---

## Project Structure

```
MTWordFrequencyCounter/
│
├── word_counter.py    # Main Python script to run the word frequency counter
├── sample.txt         # Example input file
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation
```

---

## Requirements

- Python 3.x

No external dependencies are required; only standard Python libraries are used.

---

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sindhuja90comp/MTWordFrequencyCounter.git
   cd MTWordFrequencyCounter
   ```

2. **Prepare your input file:**
   - You can use the provided `sample.txt` or create your own text file.

3. **Run the program:**
   ```bash
   python word_counter.py
   ```
   - When prompted, enter the filename (e.g., `sample.txt`).
   - Enter the number of segments (threads) you want (e.g., `4`).

---

## Sample Input

Example prompt flow:
```
Enter the filename (e.g., sample.txt): sample.txt
Enter the number of segments (e.g., 4): 4
```

---

## Output

- The program prints word frequencies in a formatted table, processing the file in parallel for efficiency.
