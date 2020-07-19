from json import JSONEncoder
from Resources.response import Response

class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class ReviewProcessor:
    def __init__(self, reviews):
        self.reviews = reviews

    def processReviews(self):
        try:
            displayReviews = []
            for review in self.reviews:
                info = Review(review['user']['name'], review['user']['image_url'], review['rating'], review['text'])
                #I don't see location as an option in this endpoint I am wondering if it only exists if the resturant has more than one location like a Culvers
                if 'location' in review:
                    info.location = review['location']
        
                displayReviews.append(Encoder().encode(info))
            return Response(True, displayReviews, "Successfully Created Formatted Reviews")
        except Exception as e:
            return Response(False, e, "Failed to format reviews due to exception [" + e + "]")

class Review:
    def __init__(self, reviewerName, avatarURL, rating, reviewContent):
        self.reviewerName = reviewerName
        self.avatarURL = avatarURL
        self.rating = rating
        self.reviewContent = reviewContent
        self.location = 'Bayview'