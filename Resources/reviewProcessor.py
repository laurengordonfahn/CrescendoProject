from json import JSONEncoder
class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class ReviewProcessor:
    def __init__(self, reviews):
        self.reviews = reviews

    def processReviews(self):
        displayReviews = []
        for review in self.reviews:
            info = Review(review['user']['name'], review['user']['image_url'], review['rating'], review['text'])
            #I don't see location as an option in this endpoint I am wondering if it only exists if the resturant has more than one location like a Culvers
            if 'location' in review:
                info.location = review['location']
                
            print("info", Encoder().encode(info))
            displayReviews.append(Encoder().encode(info))
        return displayReviews

class Review:
    def __init__(self, reviewerName, avatarURL, rating, reviewContent):
        self.reviewerName = reviewerName
        self.avatarURL = avatarURL
        self.rating = rating
        self.reviewContent = reviewContent
        self.location = 'Bayview'