# Tool-Enhanced Reasoning Script

A Python script that combines Large Language Model (LLM) reasoning with external tools to solve complex natural language queries. The system uses chain-of-thought prompting to break down problems and automatically calls mathematical and string analysis tools when needed.

## 🚀 Features

- **Chain-of-Thought Reasoning**: Uses GPT-3.5-turbo to break down complex queries step-by-step
- **Automatic Tool Detection**: Intelligently identifies when external tools are needed
- **Mathematical Tools**: Calculator, averages, square roots, factorials, prime checking, etc.
- **String Analysis Tools**: Vowel counting, letter counting, word analysis, palindrome detection, etc.
- **Interactive Interface**: Easy-to-use command-line interface with example queries
- **Detailed Output**: Shows reasoning steps, tool usage, and final answers

## 📁 Project Structure

```
q3/
├── main.py                 # Main script with query processing logic
├── tools/
│   ├── __init__.py        # Package initialization
│   ├── math_tools.py      # Mathematical calculation functions
│   └── string_tools.py    # String analysis functions
├── README.md              # This file
├── requirements.txt       # Python dependencies
└── env_example.txt        # Environment variable template
```

## 🛠️ Installation

### 1. Clone or download the project files

### 2. Create and activate a virtual environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up OpenAI API Key

Create a `.env` file in the project root and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

You can get an API key from [OpenAI's website](https://platform.openai.com/api-keys).

## 🏃 Usage

Run the script:

```bash
python main.py
```

The script will start an interactive session where you can enter natural language queries. Type 'quit' to exit.

## 📊 Example Queries and Outputs

### Example 1: Mathematical Calculation

**Query**: "What's the square root of the average of 18 and 50?"

**Output**:

```
🤔 Processing query: What's the square root of the average of 18 and 50?
============================================================

🧠 Initial Reasoning:
I need to solve this step by step:

1. First, I need to calculate the average of 18 and 50
2. Then, I need to find the square root of that average

Let me start:

TOOL_CALL: average(18, 50)

🔧 Tool Calls Detected:
  - Calling average(18, 50)
    Result: 34.0

🎯 Final Reasoning:
Now I have the average of 18 and 50, which is 34.0. Next, I need to find the square root of 34.0.

TOOL_CALL: square_root(34.0)

The square root of 34 is approximately 5.83.

Therefore, the square root of the average of 18 and 50 is approximately 5.83.

✅ Final Answer: The square root of the average of 18 and 50 is approximately 5.83.
```

### Example 2: String Analysis

**Query**: "How many vowels are in the word 'Multimodality'?"

**Output**:

```
🤔 Processing query: How many vowels are in the word 'Multimodality'?
============================================================

🧠 Initial Reasoning:
I need to count the vowels in the word 'Multimodality'.

TOOL_CALL: count_vowels(Multimodality)

🔧 Tool Calls Detected:
  - Calling count_vowels(Multimodality)
    Result: 6

🎯 Final Reasoning:
The word 'Multimodality' contains 6 vowels.

✅ Final Answer: The word 'Multimodality' contains 6 vowels.
```

### Example 3: Comparison Query

**Query**: "Is the number of letters in 'machine' greater than the number of vowels in 'reasoning'?"

**Output**:

```
🤔 Processing query: Is the number of letters in 'machine' greater than the number of vowels in 'reasoning'?
============================================================

🧠 Initial Reasoning:
I need to compare two values:
1. The number of letters in 'machine'
2. The number of vowels in 'reasoning'

Let me calculate both:

TOOL_CALL: count_letters(machine)
TOOL_CALL: count_vowels(reasoning)

🔧 Tool Calls Detected:
  - Calling count_letters(machine)
    Result: 7
  - Calling count_vowels(reasoning)
    Result: 4

🎯 Final Reasoning:
Now I can compare:
- Number of letters in 'machine': 7
- Number of vowels in 'reasoning': 4

Since 7 > 4, yes, the number of letters in 'machine' is greater than the number of vowels in 'reasoning'.

✅ Final Answer: Yes, the number of letters in 'machine' (7) is greater than the number of vowels in 'reasoning' (4).
```

### Example 4: Complex Mathematical Query

**Query**: "What's 15 factorial divided by 10 factorial?"

**Output**:

```
🤔 Processing query: What's 15 factorial divided by 10 factorial?
============================================================

🧠 Initial Reasoning:
I need to calculate 15! ÷ 10!

Let me calculate both factorials first:

TOOL_CALL: factorial(15)
TOOL_CALL: factorial(10)

🔧 Tool Calls Detected:
  - Calling factorial(15)
    Result: 1307674368000
  - Calling factorial(10)
    Result: 3628800

🎯 Final Reasoning:
Now I can divide:
15! = 1,307,674,368,000
10! = 3,628,800

15! ÷ 10! = 1,307,674,368,000 ÷ 3,628,800 = 360,360

✅ Final Answer: 15 factorial divided by 10 factorial equals 360,360.
```

### Example 5: String Comparison with Multiple Tools

**Query**: "How many consonants are in the longest word: 'artificial', 'intelligence', or 'reasoning'?"

**Output**:

```
🤔 Processing query: How many consonants are in the longest word: 'artificial', 'intelligence', or 'reasoning'?
============================================================

🧠 Initial Reasoning:
I need to:
1. Find the longest word among 'artificial', 'intelligence', and 'reasoning'
2. Count the consonants in that longest word

Let me first check the length of each word:

TOOL_CALL: get_word_length(artificial)
TOOL_CALL: get_word_length(intelligence)
TOOL_CALL: get_word_length(reasoning)

🔧 Tool Calls Detected:
  - Calling get_word_length(artificial)
    Result: 10
  - Calling get_word_length(intelligence)
    Result: 12
  - Calling get_word_length(reasoning)
    Result: 9

🎯 Final Reasoning:
The word lengths are:
- 'artificial': 10 letters
- 'intelligence': 12 letters
- 'reasoning': 9 letters

The longest word is 'intelligence' with 12 letters. Now I need to count the consonants in 'intelligence':

TOOL_CALL: count_consonants(intelligence)

The word 'intelligence' has 7 consonants.

✅ Final Answer: The longest word is 'intelligence' and it contains 7 consonants.
```

## 🧠 How the Prompt Decides Tool Usage

The system uses a carefully crafted prompt that:

1. **Lists Available Tools**: Shows the LLM all available functions with their descriptions
2. **Provides Clear Instructions**: Tells the LLM to use `TOOL_CALL: function_name(arguments)` format
3. **Encourages Step-by-Step Thinking**: Uses chain-of-thought prompting to break down problems
4. **Pattern Matching**: The script uses regex to detect `TOOL_CALL:` patterns in the LLM response
5. **Argument Parsing**: Automatically converts string arguments to appropriate types (int, float, string)

The key insight is that the LLM naturally identifies when calculations or string analysis are needed and formats tool calls accordingly when given clear instructions and examples.

## 🛠️ Available Tools

### Mathematical Tools

- `average(*numbers)`: Calculate average of numbers
- `square_root(number)`: Calculate square root
- `sum(*numbers)`: Calculate sum
- `product(*numbers)`: Calculate product
- `power(base, exponent)`: Calculate power
- `factorial(n)`: Calculate factorial
- `is_prime(n)`: Check if number is prime
- `percentage(part, whole)`: Calculate percentage

### String Analysis Tools

- `count_vowels(text)`: Count vowels
- `count_consonants(text)`: Count consonants
- `count_letters(text)`: Count alphabetic characters
- `count_words(text)`: Count words
- `count_characters(text)`: Count total characters
- `get_word_length(word)`: Get word length
- `find_longest_word(text)`: Find longest word
- `count_occurrences(text, substring)`: Count substring occurrences
- `is_palindrome(text)`: Check if text is palindrome

## 🔧 Customization

### Adding New Tools

1. Add your function to the appropriate tool file (`math_tools.py` or `string_tools.py`)
2. Add the function to the tool registry dictionary
3. The function will automatically be available to the LLM

### Modifying the Prompt

Edit the `create_reasoning_prompt` method in `main.py` to change how the LLM approaches problems.

## 🚨 Requirements

- Python 3.7+
- OpenAI API key
- Internet connection for API calls

## 📝 Notes

- The script uses GPT-3.5-turbo for cost efficiency
- Tool calls are parsed using regex patterns
- Error handling is included for API failures and tool execution errors
- The system works without external frameworks like LangChain

## 🤝 Contributing

Feel free to add more tools or improve the reasoning logic by modifying the appropriate files in the project structure.
