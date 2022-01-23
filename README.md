# food-truck-finder
Application for finding food trucks based on location


## Setup
None! Just text your latitude and longitude to the provided phone number in the format: latitude,longitude


## Design
For my solution, I want something that is easily accessible for everyone - even for people away from their computers as they are walking out of the office for lunch. That is why I decided to have a mobile phone as the primary interface, using SMS as communication between the user and the app. This also minimizes the amount of setup necessary on the user's end.

![Design Diagram](https://github.com/gdgrin/food-truck-finder/blob/main/images/Design%20Diagram.png)


## Technical Design
Web Service: Python Flask App
Deploy Pipeline: Microsoft Azure Web Service
SMS Api: Twilio

I chose to do a mix of familiarity and exploration for the technologies I used. I am very confortable with Python Flask Apps, I have some experience using the Twilio Api, and I have never deployed a Microsft Azure web app before. Had I been more comfortable with it, I probably would have used the serverless option (Function).


## Testing
I chose to test locally by running the flask app and sending requests using Postman. The next step would be adding unit and integration tests directly to the repo.


## Future Considerations
- History Based On User
    Can add features to save a user's request and choice to a database, and take this into consideration for future requests.
    By doing this we can suggest new places that the user has not seen before, or suggest types of cuisine that the user generally enjoys.