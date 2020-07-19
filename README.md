# CrescendoProject
Written on the Servereless Framework that runs on AWS
Written in python
RESTful API for Hungry Sumo Yelp Reviews
This GET endpoint calls out to the YELP API to retrieve reviews for the Hungry Sumo Resturant in BayView
The id for this resturant was gotten using the business phone number YELP endpoint in postman
https://api.yelp.com/v3/businesses/search/phone?phone=+14145959656

# How to Access Endpoint
 - setup a postman account
 - in a new postman tab in the url input field add 
 https://hxt2eg2bo5.execute-api.us-east-2.amazonaws.com/prod/getHungrySumoReviews
 - press send 

# Points of Reflection
- This project can become more dynamic by taking in a phone number of a resturant to a new endpoint that calls the YELP get business by phone number and then grabing the id and then calling out for the reviews 

- I was not able to find location information. I am not certain if that is because this resturant has only one location so that is hard coded, I am happy to have feed back to learn if I over looked something
