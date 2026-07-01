import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from docx import Document
import time

def evaluate_chatbot(input_file):
    with open(input_file,"r") as f:
        document = f.readlines()
    
    testcase = []
    expected = []
    forbidden = []
    results = []
    for line in document:
        if line.startswith("CHATBOT_NAME:"):
            chatbot_names = line.split("CHATBOT_NAME:", 1)
            chatbot_name = chatbot_names[1].strip()
            print(f"chatbotname: {chatbot_name}")
        if line.startswith("CHATBOT_CONTEXT:"):
            chatbot_context = line.split("CHATBOT_CONTEXT:", 1)
            chatbot_context = chatbot_context[1].strip()
            print(f"chatbotcontext: {chatbot_context}")
        if line.strip().startswith("TC") and "|" in line:
            cells = line.split("|")
            cells = [c.strip() for c in cells]
            testcase.append(cells[1])
            expected.append(cells[2])
            forbidden.append(cells[3])

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    for i,tc in enumerate(testcase):
        chatbot_prompt = f"""
            You are {chatbot_name}.
            {chatbot_context}
            User asks: {tc}
            Respond naturally as this chatbot.
        """
        chatbot_response = call_ai_with_retry(client,chatbot_prompt)
        time.sleep(3)  # Add a delay to avoid hitting rate limits


        evaluator_prompt = f"""
            You are a QA engineer evaluating a chatbot response.
            Test Case: {tc}
            Chatbot Response: {chatbot_response}
            Expected: {expected[i]}
            Should NOT contain: {forbidden[i]}
            Give PASS or FAIL with a reason.
            """
        
        qa_evaluation = call_ai_with_retry(client,evaluator_prompt)
        time.sleep(3)  # Add a delay to avoid hitting rate limits

        results.append(qa_evaluation)

    return results

def save_report(results, output_file):
    doc = Document()
    doc.add_heading("Chatbot QA Evaluation Report", level=0)
    for result in results:
        doc.add_paragraph(result)

    #count the number of PASS and FAIL
    pass_count = sum(1 for result in results if "PASS" in result)
    fail_count = len(results) - pass_count
    score = (pass_count / len(results)) * 100 if results else 0
    print(f"Evaluation Summary - PASS: {pass_count}, FAIL: {fail_count}")
    print(f"Overall Score: {score:.2f}%")

    # Summary section
    doc.add_heading("Summary", level=1)
    doc.add_paragraph(f"Total Test Cases: {len(results)}")
    doc.add_paragraph(f"Passed: {pass_count}")
    doc.add_paragraph(f"Failed: {fail_count}")
    doc.add_paragraph(f"Quality Score: {score}%")

    doc.add_heading("Detailed Results", level=1)
    for i, result in enumerate(results):
        doc.add_heading(f"Test Case {i+1}", level=2)
        doc.add_paragraph(result)
    doc.save(output_file)

def call_ai_with_retry(client,prompt,retries=3):
        for attempt in range(retries):
            try:
                api_response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=prompt,
                    config=types.GenerateContentConfig(temperature=0.1))
                return api_response.text
            except Exception as e:
                if "503" in str(e) or "UNAVAILABLE" in str(e):
                    print(f"GEMINI IS BUSY, retrying in 10 seconds..(attempt {attempt+1}/{retries})")
                elif "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                    print("❌ Daily quota exceeded. Please try again tomorrow.")
                    sys.exit(1)  # ← exit immediately, no point retrying
                else:
                    raise e
        raise Exception("❌ Gemini API unavailable after 3 attempts. Please try again later.")

if __name__ == "__main__":
    load_dotenv()
    if len(sys.argv) < 2: 
        print("Usage: python evaluate_chatbot.py inputs/testcases.txt")
        sys.exit(1)
    input_file = sys.argv[1]
    results = evaluate_chatbot(input_file)
    save_report(results, "outputs/chatbot_evaluation_report.docx")
