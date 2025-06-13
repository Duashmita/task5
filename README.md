# Math Problem Solver with Knowledge Base using Symbollic knowledge

## Flow of the code:

1. **Input**: The program takes a math problem in plain English (like "What's 15% tip on a $85 bill?")

2. **Understanding**: 
   - Uses GPT-4 to understand the problem
   - Converts the English problem into a query to find the right formula

3. **Knowledge Base Lookup**:
   - Searches through our math knowledge base (stored in math_kb.json)
   - Finds the appropriate formula, constant, or conversion needed

4. **Code Generation**:
   - Uses GPT-4 to extract numbers from the problem
   - Generates Python code using the formula and numbers

5. **Execution**:
   - Returns the final answer

## Output:

The program shows each step of the process:
🔤 PROBLEM: What is the area of a circle with radius 7?
============================================================
🧠 STEP 1 - LANGUAGE UNDERSTANDING:
   Generated KB Query: circle_area

📚 STEP 2 - KNOWLEDGE BASE LOOKUP:
   Found Formula: math.pi * radius ** 2

⚙️  STEP 3 - CODE GENERATION:
   Generated Code: result = math.pi * 7 ** 2

🔢 STEP 4 - SYMBOLIC EXECUTION:
   Final Answer: 153.93804002589985

✅ RESULT: 153.93804002589985

============================================================

🔤 PROBLEM: Calculate 18% tip on a $95 bill
============================================================
🧠 STEP 1 - LANGUAGE UNDERSTANDING:
   Generated KB Query: tip_calculation

📚 STEP 2 - KNOWLEDGE BASE LOOKUP:
   KB Results: {'type': 'formula', 'data': {'variables': ['bill', 'tip_percent'], 'formula': 'bill * (tip_percent / 100)'}}
   Found Formula: bill * (tip_percent / 100)

⚙️  STEP 3 - CODE GENERATION:
   Generated Code: result = 95 * (18 / 100)

🔢 STEP 4 - SYMBOLIC EXECUTION:
   Final Answer: 17.099999999999998

✅ RESULT: 17.099999999999998

============================================================

🔤 PROBLEM: Convert 75 fahrenheit to celsius
============================================================
🧠 STEP 1 - LANGUAGE UNDERSTANDING:
   Generated KB Query: fahrenheit_to_celsius

📚 STEP 2 - KNOWLEDGE BASE LOOKUP:
   KB Results: {'type': 'formula', 'data': {'variables': ['fahrenheit'], 'formula': '(fahrenheit - 32) * 5 / 9'}}
   Found Formula: (fahrenheit - 32) * 5 / 9

⚙️  STEP 3 - CODE GENERATION:
   Generated Code: Code: result = (75 - 32) * 5 / 9

🔢 STEP 4 - SYMBOLIC EXECUTION:
   Final Answer: Execution Error: name 'result' is not defined

✅ RESULT: Execution Error: name 'result' is not defined

============================================================

🔤 PROBLEM: What is the volume of a sphere with radius 4?
============================================================
🧠 STEP 1 - LANGUAGE UNDERSTANDING:
   Generated KB Query: sphere_volume

📚 STEP 2 - KNOWLEDGE BASE LOOKUP:
   KB Results: {'type': 'formula', 'data': {'variables': ['radius'], 'formula': '(4/3) * math.pi * radius ** 3'}}
   Found Formula: (4/3) * math.pi * radius ** 3

⚙️  STEP 3 - CODE GENERATION:
   Generated Code: result = (4/3) * math.pi * 4 ** 3

🔢 STEP 4 - SYMBOLIC EXECUTION:
   Final Answer: 268.082573106329

✅ RESULT: 268.082573106329

============================================================

🔤 PROBLEM: Calculate simple interest: $1000 at 5% for 3 years
============================================================
🧠 STEP 1 - LANGUAGE UNDERSTANDING:
   Generated KB Query: simple_interest_calculation

📚 STEP 2 - KNOWLEDGE BASE LOOKUP:
   KB Results: None
   ❌ No formula found in KB

============================================================

🔤 PROBLEM: What is the value of pi?
============================================================
🧠 STEP 1 - LANGUAGE UNDERSTANDING:
   Generated KB Query: constants.pi

📚 STEP 2 - KNOWLEDGE BASE LOOKUP:
   KB Results: {'type': 'constant', 'value': 3.14159265359}
   Found Constant: 3.14159265359

============================================================