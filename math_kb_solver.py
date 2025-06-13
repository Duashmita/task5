import openai
import json
import math
import os
from dotenv import load_dotenv

class MathKBSolver:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        # Get API key from environment variable
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("Please set your OPENAI_API_KEY environment variable")
        openai.api_key = api_key
        
        # Load knowledge base
        with open('math_kb.json', 'r') as f:
            self.kb = json.load(f)
    
    def english_to_kb_query(self, problem):
        """Convert English problem to KB lookup query"""
        prompt = f"""Convert this math problem to a query to find the right formula.
        
        Available in Knowledge Base:
        - formulas: geometric, financial, physics formulas
        - constants: mathematical constants
        - conversions: unit conversions
        
        Examples:
        "Area of circle with radius 5" → circle_area
        "Convert 100 fahrenheit to celsius" → fahrenheit_to_celsius
        "Calculate 15% tip on $80" → tip_calculation
        "What is the value of pi?" → constants.pi
        
        Problem: {problem}
        Query:"""
        
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content.strip()
    
    def extract_numbers_and_generate_code(self, problem, formula_template):
        """Extract numbers from problem and generate executable Python code"""
        prompt = f"""Given this math problem and formula template, extract the numbers and create Python code.
        
        Problem: {problem}
        Formula Template: {formula_template}
        
        Extract the numbers from the problem and substitute them into the formula.
        Return only executable Python code that calculates the result and stores it in 'result'.
        
        Examples:
        Problem: "Area of circle with radius 5"
        Template: "math.pi * radius ** 2"
        Code: result = math.pi * 5 ** 2
        
        Problem: "Calculate 15% tip on $80"  
        Template: "bill * (tip_percent / 100)"
        Code: result = 80 * (15 / 100)
        
        Now generate code:"""
        
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content.strip()
    
    def query_kb(self, query):
        """Query the knowledge base"""
        try:
            # Handle different types of queries
            if query.startswith('constants.'):
                const_name = query.split('.')[1]
                return {'type': 'constant', 'value': self.kb['constants'].get(const_name)}
            elif query in self.kb['formulas']:
                return {'type': 'formula', 'data': self.kb['formulas'][query]}
            elif query in self.kb['conversions']:
                return {'type': 'conversion', 'value': self.kb['conversions'][query]}
            else:
                return None
        except Exception as e:
            return f"KB Error: {e}"
    
    def execute_python(self, code):
        """Execute Python code safely"""
        try:
            safe_globals = {
                '__builtins__': {
                    'abs': abs, 'round': round, 'min': min, 'max': max,
                    'pow': pow, 'int': int, 'float': float
                },
                'math': math
            }
            
            exec(code, safe_globals)
            
            if 'result' in safe_globals:
                return safe_globals['result']
            else:
                return "Error: No result variable"
                
        except Exception as e:
            return f"Execution Error: {str(e)}"
    
    def solve_with_kb(self, problem):
        """Complete Symbol-LLM pipeline with Knowledge Base"""
        print(f"🔤 PROBLEM: {problem}")
        print("=" * 60)
        
        # Step 1: Convert English to KB Query (LLM)
        print("🧠 STEP 1 - LANGUAGE UNDERSTANDING:")
        kb_query = self.english_to_kb_query(problem)
        print(f"   Generated KB Query: {kb_query}")
        
        # Step 2: Query Knowledge Base (Symbolic)
        print("\n📚 STEP 2 - KNOWLEDGE BASE LOOKUP:")
        kb_result = self.query_kb(kb_query)
        print(f"   KB Results: {kb_result}")
        
        if not kb_result:
            print("   ❌ No formula found in KB")
            return None
        
        # Extract formula from KB result
        if kb_result['type'] == 'constant':
            print(f"   Found Constant: {kb_result['value']}")
            return kb_result['value']
        
        formula_template = kb_result['data']['formula']
        print(f"   Found Formula: {formula_template}")
        
        # Step 3: Generate executable code (LLM + Symbolic)
        print("\n⚙️  STEP 3 - CODE GENERATION:")
        python_code = self.extract_numbers_and_generate_code(problem, formula_template)
        print(f"   Generated Code: {python_code}")
        
        # Step 4: Execute computation (Symbolic)
        print("\n🔢 STEP 4 - SYMBOLIC EXECUTION:")
        answer = self.execute_python(python_code)
        print(f"   Final Answer: {answer}")
        
        print(f"\n✅ RESULT: {answer}")
        return answer

# Test the complete system
if __name__ == "__main__":
    solver = MathKBSolver()
    
    # First run through all example problems
    example_problems = [
        "What is the area of a circle with radius 7?",
        "Calculate 18% tip on a $95 bill",
        "Convert 75 fahrenheit to celsius",
        "What is the volume of a sphere with radius 4?",
        "Calculate simple interest: $1000 at 5% for 3 years",
        "What is the value of pi?"
    ]
    
    print("🤖 Welcome to the Math Problem Solver!")
    print("First, let's see some example problems:")
    print("=" * 60)
    
    for problem in example_problems:
        solver.solve_with_kb(problem)
        print("\n" + "="*60)
    
    print("\nNow you can enter your own problems!")
    print("Type 'exit' to quit or 'examples' to see the example problems again")
    print("=" * 60)
    
    while True:
        user_input = input("\nEnter your math problem: ").strip()
        
        if user_input.lower() == 'exit':
            print("Goodbye! 👋")
            break
        elif user_input.lower() == 'examples':
            print("\nExample problems:")
            for i, problem in enumerate(example_problems, 1):
                print(f"{i}. {problem}")
            continue
        elif user_input.isdigit() and 1 <= int(user_input) <= len(example_problems):
            # If user enters a number, show that example
            print(f"\nExample {user_input}: {example_problems[int(user_input)-1]}")
            continue
        
        if user_input:
            solver.solve_with_kb(user_input)
            print("\n" + "="*60)