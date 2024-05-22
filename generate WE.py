from openai import OpenAI
client = OpenAI()

## --------------- QUESTIONS -------------------------------------------------------------------------
# Format: q_240610_1 means question 1 from exam 2024 june 10  in the course "Algorithms and Data Structures (HI1029)" at KTH
 
# Concepts: Recursion, depth-first search, algorithm construction
q_240313_4 = """In this task, we aim to reach the number one from a given integer in as few steps as possible if it is feasible. In each step, we can perform any of the following operations (if they are permitted): 

(a) If the number is divisible by 7, we can subtract 20 
(b) If the number is divisible by 5, we can subtract 16 
(c) If the number is divisible by 2, we can halve it 
(d) We can always choose to subtract 7 

If we start with the number 70, we can reach one in 4 steps by choosing c, d, d, and finally a (70/2=35, 35-7=28, 28-7=21, 21-20=1). If instead, we start with 623, it requires 9 steps: dcccdcdda. In this task, you are required to write functions that return the number of steps but do not present which steps need to be taken.
Write a program that takes an integer as an input parameter and returns the number of steps required to reach 1 according to the above. If no solution is found, the program should return -1. Use a recursive depth first search approach."""

# Concepts: Hash tabel (Dictionary in python), algorithm construction
q_230607_6 = "Given a list of integers, find a pair of integers that sum up to a specific value. For example, for the list: {3, 4, 1, 7, 9, 5, 3, 6} and the sum 13, one can find (4, 9) or (6, 7). Write a program that takes a list of integers and a target sum, and returns a list with one of the pairs that has the correct sum. If there are multiple pairs, it should find only one. If there are no pairs with the correct sum, it should return None. The program should solve the task in O(n) time complexity. Use a Dictionary."

# Concepts: Algorithm construction, sorting algorithm, complexity ordonotation
q_220610_5 = "Write a program that sorts a list of integers. It should minimize the number of swaps required. For a list with n integers, it should require a maximum of n - 1 swaps. The efficiency should be O(n^2) or better."

## ------------------ PROMPTS ----------------------------------------------------------------------------

# The prompt used by Jury et al. described in our report
jury_prompt = """Write a worked example for the given question in {language}.
Mark the start of any code with ‘START_OF_CODE’.
Mark the end of any code with ‘END_OF_CODE’.
Clearly mark each step with the heading ‘STEP X’.
Each step must contain both written explanation and code,
and be separable from the other content.
There should be minimum 3 and maximum 10 steps.
Also include an overview at the beginning, with no code.
Do not include steps in the overview.
Include a review at the end with the complete code.
The output should be suitable for a novice programmer.
Here is an example output to mimic:
Overview: Overview Explanation
STEP 1: Step 1 Explanation
START_OF_CODE Step 1 Code END_OF_CODE
STEP 2: Step 2 Explanation
START_OF_CODE Step 2 Code END_OF_CODE
STEP 3: Step 3 Explanation
START_OF_CODE Step 3 Code END_OF_CODE
Review: Review Explanation
START_OF_CODE Review Code END_OF_CODE
The question is: ### {question} ###"""

# The prompt we used to generate the WEs for the report
prompt = """Write a worked example for the given CS2 question in English.
      Use Python as the programming language.
      Write the python code as python syntax-highlighted Markdown.
      Clearly mark each step with the heading ‘STEP X’.
      Each step must contain both written explanation and code,
      and be separable from the other content.
      There should be minimum 3 and maximum 10 steps.
      Include the complete code at the end.
      Also include an overview at the beginning, with no code.
      Do not include steps in the overview.
      The output should be suitable for a novice programmer.
      Here is an example output to mimic:
      Overview: Overview Explanation
      STEP 1: Step 1 Explanation
      Step 1 Code
      STEP 2: Step 2 Explanation
      Step 2 Code
      STEP 3: Step 3 Explanation
      Step 3 Code
      Complete code: 
      complete code
      The CS2 question is: ### {} ###""".format(q_220610_5)

## ------------------ Generation ----------------------------------------------------------------------------

## Generating a worked example by API call to GPT-4
completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "user", "content": prompt}
  ]
)
print(completion.choices[0].message.content)