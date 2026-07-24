def generate_study_prompt():
    subject = input("Enter subject: ")
    topic = input("Enter topic: ")
    difficulty = input("Enter difficulty (Beginner/Intermediate/Advanced): ")
    prompt = f"""Act as an experienced {subject} instructor.
Teach the topic '{topic}' to a {difficulty} student.
Use simple language.
Include real-life examples.
Give 5 practice questions.
End with a short quiz."""
    print("\nGenerated Prompt:\n")
    print(prompt)
    return prompt
def save_prompt(prompt):
    file = open("prompts.txt", "a")
    file.write(prompt)
    file.write("\n")
    file.write("-" * 50)
    file.write("\n")
    file.close()
    print("Prompt saved successfully!")
def view_saved_prompts():
    try:
        file = open("prompts.txt","r")
        print("\n==== SAVED PROMPTS =====\n")
        for line in file:
            print(line,end="")
        file.close()
    except FileNotFoundError:
        print("No saved prompts found.")
def improve_existing_prompt():
    prompt = input("Paste your existing prompt:\n")
    improved_prompt = f"""Improve the following AI prompt:
{prompt}
Make it more detailed.
Use clear instructions.
Include examples if needed.
Specify the desired output format.
End with a short summary."""
    print("\nImproved Prompt:\n")
    print(improved_prompt)
    return improved_prompt
while True:
    print("=" * 40)
    print("  SMART PROMPT STUDIO")
    print("=" * 40)
    print("1. Generate Study Prompt")
    print("2. Improve Existing Prompt")
    print("3. View Saved Prompts")
    print("4. Exit")
    print("=" * 40)
    choice = input("Enter your choice: ")
    if choice == "1":
        print("You selected Generate Study Prompt.")
        generated_prompt = generate_study_prompt()
        save = input("\nDo you want to save this prompt? (yes/no): ")
        if save.lower() == "yes":
            save_prompt(generated_prompt)
        else:
            print("Prompt was not saved.")
    elif choice == "2":
        print("You selected Improve Existing Prompt.")
        improved_prompt = improve_existing_prompt()
        save = input("\nDo you want to save this improved prompt? (yes/no): ")
        if save.lower() == "yes":
            save_prompt(improved_prompt)
        else:
            print("Improved prompt was not saved.")
    elif choice == "3":
        print("You selected View Saved Prompts.")
        view_saved_prompts()
    elif choice == "4":
        print("Thank you for using Smart Prompt Studio!")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 4.")