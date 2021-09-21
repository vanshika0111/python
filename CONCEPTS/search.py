from typing import Sequence


def search(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {words1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score

if __name__ == "__main__":
    # print(search("This is good", "python is good"))
    sentences = ["This is India", "It's morning", "I am a programmer", "Enjoy life"]
    query = input("Enter the query string: ")
    scores = [search(query, sentence) for sentence in sentences ]
    # print(scores)
    sortedSentenceScore = [sentenceScore for sentenceScore in sorted(zip (scores, sentences), reverse = True) ]
    print(sortedSentenceScore)
    print(f" {len(sortedSentenceScore)} result(s) found! ")
    for score, item in sortedSentenceScore:
        print(f"\"{item}\": with a score of {score}")