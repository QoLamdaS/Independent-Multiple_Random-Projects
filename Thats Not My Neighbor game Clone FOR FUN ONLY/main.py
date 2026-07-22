import random
import time

# --- GAME DATA ---
VALID_NAMES = ["Alice Smith", "Bob Jones", "Charlie Brown", "Diana Prince", "Evan Wright"]

DOPPELGANGER_TRAITS = [
    "Unusually pale skin with no eyebrows",
    "Third eye hidden under hair",
    "Unnatural, wide unnerving smile",
    "Voice sounds like static and metallic distortion",
    "Extra finger on left hand"
]

NORMAL_APPEARANCES = [
    "Looks completely normal",
    "Wearing glasses, looks tired",
    "Friendly smile, wearing a jacket",
    "Carrying groceries, normal appearance"
]

def generate_resident():
    """Generates a visitor. Could be a real resident or a doppelganger."""
    is_doppelganger = random.choice([True, False])
    real_name = random.choice(VALID_NAMES)
    real_id = str(hash(real_name) % 90000 + 10000)  # Consistent 5-digit ID based on name

    if not is_doppelganger:
        # Honest resident
        return {
            "name": real_name,
            "id": real_id,
            "appearance": random.choice(NORMAL_APPEARANCES),
            "is_doppelganger": False,
            "reason": "None"
        }
    else:
        # Doppelganger with 1 flaw
        flaw_type = random.choice(["fake_name", "fake_id", "weird_appearance"])
        
        name = "Unknown Impostor" if flaw_type == "fake_name" else real_name
        id_num = str(random.randint(10000, 99999)) if flaw_type == "fake_id" else real_id
        # Ensure fake ID isn't accidentally correct
        if flaw_type == "fake_id" and id_num == real_id:
            id_num = "99999"

        appearance = random.choice(DOPPELGANGER_TRAITS) if flaw_type == "weird_appearance" else random.choice(NORMAL_APPEARANCES)

        return {
            "name": name,
            "id": id_num,
            "appearance": appearance,
            "is_doppelganger": True,
            "reason": f"Flaw was in {flaw_type.replace('_', ' ')}"
        }

def print_registry():
    """Prints the official building registry for reference."""
    print("\n" + "="*45)
    print("📋 OFFICIAL BUILDING REGISTRY (AUTHORIZED)")
    print("="*45)
    for name in VALID_NAMES:
        correct_id = str(hash(name) % 90000 + 10000)
        print(f" • {name:<20} | ID: {correct_id}")
    print("="*45 + "\n")

def main():
    print("="*50)
    print("🚪 THAT'S NOT MY NEIGHBOR - CLI EDITION 🚪")
    print("="*50)
    print("Welcome, Doorman. Verify every visitor carefully.")
    print("Compare their claims against your Official Registry.")
    print("Watch out for fake IDs, unlisted names, or strange features!\n")

    score = 0
    rounds = 5

    for round_num in range(1, rounds + 1):
        print(f"\n--- VISITOR #{round_num} OF {rounds} ---")
        
        # Show Registry first each time
        print_registry()
        
        visitor = generate_resident()
        
        # Present Visitor Data
        print("🔍 VISITOR AT THE DOOR:")
        print(f" ├─ Claimed Name : {visitor['name']}")
        print(f" ├─ ID Badge     : {visitor['id']}")
        print(f" └─ Appearance   : {visitor['appearance']}\n")

        # Player Decision
        while True:
            choice = input("Action? [E]ntry / [D]eny & Call DDD: ").strip().lower()
            if choice in ['e', 'd']:
                break
            print("Invalid input! Type 'E' to allow entry or 'D' to call DDD.")

        # Evaluate Result
        is_entry_allowed = (choice == 'e')
        
        if is_entry_allowed and not visitor["is_doppelganger"]:
            print("✅ CORRECT: You let in a legitimate resident.")
            score += 1
        elif not is_entry_allowed and visitor["is_doppelganger"]:
            print(f"🚨 CORRECT: DDD apprehended the doppelganger! ({visitor['reason']})")
            score += 1
        elif is_entry_allowed and visitor["is_doppelganger"]:
            print(f"❌ GAME OVER TRAITOR: You let a doppelganger inside! ({visitor['reason']})")
            print("The building was compromised...")
            return
        else:
            print("⚠️ ERROR: You reported an innocent resident to the DDD!")

        time.sleep(1)

    # Final Score
    print("\n" + "="*50)
    print(f"🎉 SHIFT COMPLETED! Final Score: {score}/{rounds}")
    if score == rounds:
        print("🏆 Perfect job! The building is 100% safe.")
    else:
        print("Keep practicing your observation skills!")
    print("="*50)

if __name__ == "__main__":
    main()