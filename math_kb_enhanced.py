# kb_utils.py - Helper functions for KB interaction

class KBQueryHelper:
    def __init__(self, prolog_instance):
        self.prolog = prolog_instance
    
    def get_all_formulas(self):
        """Get all available formulas from KB"""
        try:
            formulas = list(self.prolog.query("formula(Name, Vars, Formula)"))
            return formulas
        except:
            return []
    
    def get_all_constants(self):
        """Get all mathematical constants"""
        try:
            constants = list(self.prolog.query("constant(Name, Value)"))
            return constants
        except:
            return []
    
    def find_formula_by_keyword(self, keyword):
        """Find formulas containing a keyword"""
        try:
            query = f"formula(Name, Vars, Formula), sub_atom(Name, _, _, _, '{keyword}')"
            results = list(self.prolog.query(query))
            return results
        except:
            return []

# Example usage
def demo_kb_capabilities():
    prolog = Prolog()
    prolog.consult("math_kb.pl")
    helper = KBQueryHelper(prolog)
    
    print("📚 KNOWLEDGE BASE CONTENTS:")
    print("\n🔹 Available Formulas:")
    for formula in helper.get_all_formulas():
        print(f"   {formula}")
    
    print("\n🔹 Mathematical Constants:")
    for const in helper.get_all_constants():
        print(f"   {const}")