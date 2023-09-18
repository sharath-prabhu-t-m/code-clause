import difflib

def calculate_similarity(text1, text2):
    """
    Calculate the similarity ratio between two text documents.
    """
    # Tokenize the text into lines
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()

    # Calculate the similarity ratio
    similarity_ratio = difflib.SequenceMatcher(None, lines1, lines2).ratio()
    return similarity_ratio

def main():
    # Input two text documents
    text1 = """This is the first text document.
    It's a simple example for plagiarism checking."""

    text2 = """This is the second text document.
    It's similar to the first one but not identical."""

    # Calculate the similarity ratio
    similarity_ratio = calculate_similarity(text1, text2)

    # Define a threshold for plagiarism detection (adjust as needed)
    plagiarism_threshold = 0.8

    # Check for plagiarism
    if similarity_ratio >= plagiarism_threshold:
        print("Plagiarism detected!")
        print(f"Similarity Ratio: {similarity_ratio}")
    else:
        print("No plagiarism detected.")
        print(f"Similarity Ratio: {similarity_ratio}")

if __name__ == "__main__":
    main()
