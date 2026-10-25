import re

#Pattern Provided in 7.4 to find sentences
pattern  = r'\s*(.*?[.!?])(?=\s+[A-Z0-9]|\s*$)'

count = 0

#Asks for paragraphs and gives steps to add more and how to have it complete the count
while True:
    paragraph = input(
        "\nEnter a Paragraph(Or type 'done' when complete):\n"
    )

    if paragraph.lower() == "done":
        break

    if not paragraph.strip():
        print("Enter Paragraph.")
        continue

#Finds Sentences
    sentences = re.findall(pattern, paragraph)

#Removes extra spaces to make checking easier
    sentences = [s.strip() for s in sentences if s.strip()]

    count += 1

#Returns with total amount of paragraphs and the count
    print(f"\nParagraph: {count}")
    print("-" * 30)

#Returns with total amount of paragraphs and the count
    for number, sentence in enumerate(sentences, start=1):
        print(f"Sentence {number}: {sentence}")

    print(f"\nTotal Sentences: {len(sentences)}")

print(f"\nTotal Paragraphs: {count}")