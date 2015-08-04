
from textblob import TextBlob

print "--------"
review1Text = "This app sucks. 5 stars"
review1 = TextBlob(review1Text)
print review1Text
print "5 stars"
print review1.sentiment
print "--------"

print "--------"
review2Text = "This app rocks. 1 star"
review2 = TextBlob(review2Text)
print review2Text
print "1 star"
print review2.sentiment
print "--------"

print "--------"
review3Text = "Keep cutting out randomly"
review3 = TextBlob(review3Text)
print review3Text
print "1 star"
print review3.sentiment
print "--------"

print "--------"
review4Text = "Keeps disconnecting"
review4 = TextBlob(review4Text)
print review4Text
print "2 stars"
print review4.sentiment
print "--------"

print "--------"
review5Text = "Love listening to any station or artist I want. It helps me through my workout."
review5 = TextBlob(review5Text)
print review5Text
print "5 stars"
print review5.sentiment
print "--------"

print "--------"
review6Text = "Cracker Greatest talent in the biz"
review6 = TextBlob(review6Text)
print review6Text
print "5 stars"
print review6.sentiment
print "--------"

print "--------"
review7Text = "Awesome app I love looking for my favorite artists and hear what they like. I have heard so many songs by artist that I have never heard before. The only downfall is the limit of skips in a day."
review7 = TextBlob(review7Text)
print review7Text
print "5 stars"
print review7.sentiment
print "--------"

print "--------"
review8Text = "Took awhile , but found some instrumentals, most are walk, some are good beats Instrumentals , and beats"
review8 = TextBlob(review8Text)
print review8Text
print "4 stars"
print review8.sentiment
print "--------"

print "--------"
reviewText = "Could. Be better Only plays half a song and puts songs on that have nothing to do with the station i pick frustrating."
review = TextBlob(reviewText)
print reviewText
print "3 stars"
print review.sentiment
print "--------"
