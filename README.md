# CrescendoProject
Written on Servereless Framework that runs on AWS
Written in python
RESTful API for Hungry Sumo Yelp Reviews
This GET endpoint calls out to the YELP API to retrieve reviews for the Hungry Sumo Resturant in BayView
The id for this resturant was gotten using the business phone number YELP endpoint in postman
https://api.yelp.com/v3/businesses/search/phone?phone=+14145959656

# How to Access Endpoint
 - setup a postman account
 - in a new postman tab set to GET in the url input field add 
 https://hxt2eg2bo5.execute-api.us-east-2.amazonaws.com/prod/getHungrySumoReviews
 - press send 

# Points of Reflection
- This project can become more dynamic by taking in a phone number of a resturant to a new endpoint that calls the YELP get business by phone number endpoint and then grabing the id  of the resturant in order to call for reviews 

- I was not able to find location information. I am not certain if that is because this resturant has only one location. I hard sinned and coded, I am happy to have feed back to learn if I over looked something

- Yelp caps their number of reviews returned via API to get more reviews I would have had to use scrapping following something similar to the process outlined in : https://www.youtube.com/watch?v=r3-v81c2Oew
