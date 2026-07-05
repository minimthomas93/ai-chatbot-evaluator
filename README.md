# 🤖 AI-Powered Chatbot QA Evaluator

> Automatically evaluates the quality of chatbot responses using the Gemini AI API — saving QA engineers hours of manual work.

## Problem

Companies are building AI chatbots everywhere. But how do you test them systematically? There's no standard way. Most teams just manually chat with it and say "looks good."

## Solution
Provide a list of test prompts and expected behaviour as input.
The tool automatically evaluates each response and generates
a detailed report showing pass/fail results and an overall quality score.

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

## Result
1. Chatbot got evaluated under 60 seconds
2. AI evaluate the responses of Chatbot for each prompt.
3. Generated an evaluation report in word document with the details of every testcases, chatbot responses, and actual results which can be reviewed by QA Engineer.
4. Report also contains a summary with the testcase count, pass counts, fail counts, and test score.

The tool supports any number of test cases - the sample input demonstrates 5 scenarios covering 
normal queries, security-sensitive requests, and adversarial inputs.

## ⚡ Before vs After

| | Manual Testing | This Tool |
|---|---|---|
| Time to test a chatbot (5 testcases) | 2 hours | Under 60 seconds |
| Generate a report | Written manually | Auto-generated |
| Generate a summary | Written manually | Auto-generated |
| Consistency across runs | Varies by tester | Consistent every time |
| Finding edge case failures | Easy to miss | AI-flagged automatically |

## Usage

```bash
pip install -r requirements.txt
python evaluate_chatbot.py inputs/testcases.txt
```

## Screenshots

### Input - Testcase Document
![Testcases](screenshots/testcase.png)

### Tool Running
![Terminal](screenshots/terminal_output.png)

### Output - Generated Report
![Evaluation Report](screenshots/report.png)


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
Python · Google Gemini API · python-docx · python-dotenv · Prompt Engineering


## Future Improvements
- Support for testing real external chatbot APIs
- HTML report output option
- Batch testing with multiple input files
- Slack notification with evaluation summary
- Support for response time measurement

## Author
Mini Mariya Thomas
