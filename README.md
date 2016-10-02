# harassment-check

## Inspiration
Gendered and interpersonal violence and harassment is a pervasive issue on the internet, and women and minorities are especially vulnerable. When Uplift came to WHACK and shared their problem statement, we were inspired to build something that would help combat online abuse in a significant way. We agree that calling abusers out is important; however, we also believe that embarrassing an abuser often exacerbates the behavior, opposed to curbing it. Through gentle suggestions that aim to educate the user, we hope to end ignorant hurtful remarks online. 

As more and more schools provide computers for students, we hope that schools will pre-download our extension. We imagine this tool to be especially impactful for middle and high school students who may be just beginning to become aware of the social impact that their online presence can have. This extension will provide a real-time reminder for users to be mindful of their posts and comments.

## What it does
The Anti-Troll Harassment Checker is an extension for Google Chrome that analyzes text a user types in any text box, checking it for misogynistic, racist, homophobic, or other problematic content as well as performing a sentiment analysis on it. If any problematic content is detected, a popup appears with an appropriate quote, a brief explanation, and relevant links that the user can navigate to if they are particularly interested in learning more.

Users can also click the extension's icon to view a popup with a text box and submit button, where they can enter and check select phrases.

## How we built it
We wrote JavaScript code that executes every half second after a user stops typing sends the content that was typed to a background Python script (hosted on a Flask server for initial development, and then on AWS), which utilizes the Watson API to perform a sentiment analysis. The script then sends back an appropriate response to display in the popup, which we designed with HTML and CSS.

## Challenges we ran into
This was our first time building a Chrome extension, and we definitely had some trouble understanding how the it connected to the browser, and how the server played a role in relaying information between the content and the background. 
At first we didn't know how to access the content that was typed in the browser, and learned a lot about JavaScript on our way to getting that to work!

## Accomplishments that we're proud of
Using the Watson API was very new and cool for us, and we were definitely really excited about being able to use that to get a more accurate idea on how to judge content. In general, we stayed focused and cohesive as a team, and worked hard to create something that we could see making a tangible impact on communities.

## What we learned
We learned so much about the structure of extensions, JavaScript, working with CSS, and how REST requests work!

## What's next for Anti-Troll Harassment Checker
We have a few bugs in our code we'd like to fix. Currently the content checking in the popup text box works as expected, but isn't as successful with content typed in the browser webpage. We have responses from the server being printed out in the console, and eventually we'd like some sort of alert or desktop notification to relay our messages and links.