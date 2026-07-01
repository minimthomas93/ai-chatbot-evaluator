# 🤖 AI-Powered Chatbot QA Evaluator

> Automatically evaluates the quality of chatbot responses using the Gemini AI API — saving QA engineers hours of manual work.

## Problem

Companies are building AI chatbots everywhere. But how do you test them systematically? There's no standard way. Most teams just manually chat with it and say "looks good."

## Solution

Input:  A list of test prompts + expected behaviour
Output: Evaluation report showing pass/fail for each prompt, quality score, and problem areas

## How this tool Works

You define test cases like:
- Send this prompt to the chatbot
- Check if response contains expected keywords
- Check if response avoids forbidden words
- Score the quality

1. Drop your testcase in a .txt file into `/inputs` folder.
2. Run the script - Script contains the prompts to be used by the AI agent.
3. AI agent reads the testcases, execute the prompts, and generate a structured evaluation report.
4. Get a structured report in `/outputs`

Tool sends each prompt → evaluates response → generates report


## Result
1. Chatbot got evaluated under 60 seconds
2. AI evaluate the responses of Chatbot for each prompt.
3. Generated an evaluation report in word document with the details of every testcases, chatbot responses, and actual results which can be reviewed by QA Engineer.
4. Report also contains a summary with the testcase count, pass counts, fail counts, and test score.


## ⚡ Before vs After

| | Manual Testing | This Tool |
|---|---|---|
| Time to test a chatbot (5 testcases) | 2 hours | Under 60 seconds |
| Generate a report | Written manually | Auto-generated |
| Generate a summary | Written manually | Auto-generated |

## Usage

```bash
pip install -r requirements.txt
python evaluate_chatbot.py inputs/testcases.txt
```

## Screenshots

### Input - Testcase Document
![Bug Note](screenshots/testcase.png)

### Tool Running
![Terminal](screenshots/terminal_output.png)

### Output - Generated Report
![Bug Report](screenshots/report.png)


## Project Structure

```
ChatbotQAEvaluator/
├── inputs/                 (testcase to be considered by the AI agent)
├── outputs/                (output evaluation report in word file)
├── screenshots/            (screenshots for README)
│   ├── testcase.png
│   ├── terminal_output.png
│   └── report.png
├── .gitignore              (files that not need to be pushed to Github)
├── config.py               (loads the key safely)
├── evaluate_chatbot.py     (main script - reads testcase file and generates evaluation report)
├── requirements.txt        (Python packages to install)
└── README.md               (Details about this tool)
```

## Technologies
Python · Gemini API · OpenPyXL · python-dotenv

## Future Improvements


## Author
Mini Mariya Thomas
