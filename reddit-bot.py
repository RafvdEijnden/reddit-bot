import praw
import spacy


reddit = praw.Reddit(client_id = '4mji8PuEMwOj7A',
                     client_secret = 'Mnp9sUknLQfPJnUXAWGULv628PI',
                     username = 'ARareWordOccured',
                     password = '1kwilbotten',
                     user_agent = 'ARareWordOccuredV1')

subreddit = reddit.subreddit('news')
nlp = spacy.load('en_core_web_md')

for comment in subreddit.stream.comments():
    tokenized_comment = nlp(comment.body)
    print(type(tokenized_comment))
    print(comment.body)
    for token in tokenized_comment:
        if token.prob > -20 and token.prob < -18.5:
            print(token.prob, token)
    print()
    print()



sent1 = "degust draff dragoman flocculent gaita gallus hazardus wrok clangignthe perpendicular car was left afreet of the grim restaurant colporteur. Nevermore have intelligence agencies been more claggy"
sent1_tokenized = nlp(sent1)

for i, token in enumerate(sent1_tokenized):
    print(sent1_tokenized[i].prob, token)
