def analyze_data():
    a = [7, 8, 7, 4, 5, 3, 9, 8, 4]  # Sample list
    box = {}  # Frequency dictionary

    # 1️⃣ Frequency Count + Duplicate Detection
    for ele in a:
        box[ele] = box.get(ele, 0) + 1

    print("🔁 Frequency of each element:")
    for key, val in box.items():
        print(f"{key} appears {val} times")

    print("\n📌 Duplicates:")
    for key, val in box.items():
        if val > 1:
            print(f"{key} is duplicated ({val} times)")

    # 2️⃣ Most Frequent Element
    most_common = max(box, key=box.get)
    print(f"\n🔥 Most frequent element: {most_common} ({box[most_common]} times)")

    # 3️⃣ Anagram Check (example)
    s1 = "listen"
    s2 = "silent"

    def is_anagram(x, y):
        if len(x) != len(y):
            return False
        freq = {}
        for ch in x:
            freq[ch] = freq.get(ch, 0) + 1
        for ch in y:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] < 0:
                return False
        return True

    print(f"\n🔤 Are '{s1}' and '{s2}' anagrams? → {is_anagram(s1, s2)}")

# Run the function
analyze_data()
"""
- Frequency Count: How many times each item appears.
- Occurrence Count: Just another way of saying the same — how often something occurs.

"""
def string_analysis(s1, s2):
    freq = {}

    # 1️⃣ Frequency Count
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    print("🔁 Frequency of each character:")
    for ch, count in freq.items():
        print(f"'{ch}' appears {count} times")

    # 2️⃣ Duplicates
    print("\n📌 Duplicates:")
    for ch, count in freq.items():
        if count > 1:
            print(f"'{ch}' is duplicated ({count} times)")

    # 3️⃣ Most Frequent Character
    most_common = max(freq, key=freq.get)
    print(f"\n🔥 Most frequent character: '{most_common}' ({freq[most_common]} times)")

    # 4️⃣ Anagram Check
    def is_anagram(x, y):
        if len(x) != len(y):
            return False
        freq_x = {}
        for ch in x:
            freq_x[ch] = freq_x.get(ch, 0) + 1
        for ch in y:
            if ch not in freq_x:
                return False
            freq_x[ch] -= 1
            if freq_x[ch] < 0:
                return False
        return True

    print(f"\n🔤 Are '{s1}' and '{s2}' anagrams? → {is_anagram(s1, s2)}")

# Example usage
string_analysis("banana", "anaban")