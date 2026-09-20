import string

potential_spam = {
    "urgent", "attention", "renew", "free", "congrats", "offer", "click", "deal", "now", "cancel",
    "refund", "giveaway", "profit", "promise", "riskfree", "special", "instant", "winner", "obligation",
    "debt", "unpaid", "cheap", "claim", "discount", "loan", "warranty", "trial", "unlimited", "quote", "luxury"
}
#Common wordage used in spam

def check_for_spam(text):
    text_fixer = text.lower().translate(str.maketrans('', '', string.punctuation))
    spam = text_fixer.split()

#Makes any and all text lowercase to check it without any issues due to capitalization

    email_checker = len(spam)
    if email_checker == 0:
        return {
            "total_wordage": 0,
            "total_spam_wordage": 0,
            "total_spam_percentage": 0.0,
            "flagged_wordage": [],
        }
    flagged_wordage = [word for word in spam if word in potential_spam]
    total_spam_wordage = len(flagged_wordage)

    #Checks the words that are in the "Potential_Spam" set

    total_spam_percentage = (total_spam_wordage / email_checker) * 100

    return {
        "total_wordage": email_checker,
        "total_spam_wordage": total_spam_wordage,
        "total_spam_percentage": round(total_spam_percentage, 2),
        "flagged_wordage": flagged_wordage,
    }
#Returns the wordage with a percentage

def get_spam_level(spam_percentage):
    if spam_percentage == 0:
        return "No spam found"
    elif spam_percentage < 25:
        return "Maybe Spam"
    elif spam_percentage < 50:
        return "Most likely Spam"
    else:
        return "Found to be Spam"

#Tell you the likelihood of spam

result = check_for_spam(input("Please enter text: "))

spam_level = get_spam_level(result["total_spam_percentage"])

print(result)
print("Spam Level:", spam_level)
#Checks the text and outputs the results