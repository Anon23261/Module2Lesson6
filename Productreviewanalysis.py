# Task 1: Keyword Highlighter

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

# Task 1: Highlight the keywords by capitalizing them in the reviews
def highlight_keywords(reviews, keywords):
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        
        print(review)

# Execute Task 1: Keyword Highlighting
print("Task 1: Keyword Highlighter")
highlight_keywords(reviews, keywords)
print()  # Blank line for separation

# Task 2: Sentiment Tally

# Lists of positive and negative words
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Function to tally positive and negative words in a review
def sentiment_tally(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0

    # Iterate through each review
    for review in reviews:
        # Check each word in the review and tally positive/negative words
        words = review.lower().split()
        for word in words:
            if word.strip(".,!") in positive_words:
                positive_count += 1
            elif word.strip(".,!") in negative_words:
                negative_count += 1

    # Return the final counts of positive and negative words
    return positive_count, negative_count

# Execute Task 2: Sentiment Tally
positive, negative = sentiment_tally(reviews, positive_words, negative_words)
print("Task 2: Sentiment Tally")
print(f"Total Positive Words: {positive}")
print(f"Total Negative Words: {negative}")
print()

# Task 3: Review Summary

# Function to generate a summary of the first 30 characters without cutting off in the middle of a word
def review_summary(reviews):
    summaries = []

    for review in reviews:
        if len(review) <= 30:
            summaries.append(review)
        else:
            summary = review[:30]
            if " " in summary:
                summary = summary[:summary.rfind(" ")]  
            summaries.append(summary + "…")

    for i, summary in enumerate(summaries):
        print(f"Review {i+1} Summary: {summary}")

# Execute Task 3: Review Summary
print("Task 3: Review Summary")
review_summary(reviews)
