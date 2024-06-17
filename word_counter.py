def count_words(text):
    """
    Function to count the number of words in the given text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    int: The word count.
    """
    # Split the text by whitespace to get the words
    words = text.split()
    return len(words)

def get_user_input():
    """
    Function to get user input.
    
    Returns:
    str: The user's input.
    """
    user_input = input("Please enter a sentence or paragraph: ").strip()
    if not user_input:
        print("Error: You did not enter any text. Please try again.")
        return get_user_input()
    return user_input

def main():
    """
    Main function to handle user input, count words, and display the result.
    """
    # Get the user input
    user_input = get_user_input()
    
    # Count the words in the input text
    word_count = count_words(user_input)
    
    # Display the word count
    print(f"The number of words in the given text is: {word_count}")

# Ensure a clear and user-friendly interface
if __name__ == "__main__":
    main()
