import requests

# Ensure your Flask server is running on port 5000
BASE_URL = "http://127.0.0.1:5000"

def run_tests():
    # 1. Test Notes
    print("Testing Note Submission...")
    r1 = requests.post(f"{BASE_URL}/", data={"note": "TestNoteXYZ"})
    if "TestNoteXYZ" in r1.text:
        print("✅ Note Added Successfully")
    else:
        print("❌ Note Not Found in HTML")

    # 2. Test Regex
    print("\nTesting Regex Matcher...")
    payload = {
        "regex": r"\d+", 
        "test_string": "Room 101 and 202"
    }
    r2 = requests.post(f"{BASE_URL}/results", data=payload)
    
    # IMPROVED CHECK: Look for 'Found:' and the number separately to ignore spaces
    html_content = r2.text
    if "Found:" in html_content and "101" in html_content and "202" in html_content:
        print("✅ Regex Matches Found Successfully")
    else:
        print("❌ Regex Match Not Found in HTML")
        print("\n--- DEBUG: Check these values in your HTML snippet above ---")
        print("Found 'Found:':", "Found:" in html_content)
        print("Found '101':", "101" in html_content)

if __name__ == "__main__":
    try:
        run_tests()
    except Exception as e:
        print(f"❌ CONNECTION ERROR: {e}")