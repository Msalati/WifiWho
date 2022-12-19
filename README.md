
<p align="center">
  <img src="https://i.imgur.com/j7OvRii.png" width="200px" />

</p><p align="center">
  <h1 align="center"> WifiWho? </h1>
</p>

<h2> What is the project? </h2>
This is a small python project to let you know whether you're connected to the internet or not via OS notifications.

[Let's try it!](#running-the-app)



<h2> What's the idea behind the name? </h2>
It just resembles a person who was left with no connection for a very long time until they failed to recognize the meaning of the connection in itself, in which comes the name... WifiWho?

<h2> Why was this project created? </h2>

Simply because I like to automate things, and I also wanted to learn python a bit more, and what's better than fiddling with random nonsense? 

Let me tell you what exactly what got into me, usually when I want to know whether I have internet connection or not, I use the following command:
```
ping 8.8.8.8 -t
```
what this command does, as it suggests, it 'pings' an infinite amount of times with the -t option, to a specific DNS, in this case is the well known primary DNS for <b>Google</b>, which will always return a pong when pinged.

And I usually just put that pitch black terminal on the side until the google servers start replying to my data packets I'm pinging them. 
Which has problems

<ol>
<li>I fail to notice that my internet is back</li>
<li>It annoys me having an extra unwanted window that disturbs my workflow
</li>
<li>Tend to ask other people if the internet is back or not</li>
</ol>

<h2> What's the solution? </h2>
Having said those issues and problems it's time to get to solving!
I created this CLI Application to run in the background, notifying the user when the internet connection has been restored.

The application is able to run back and fourth in case your internet connection is unstable and it won't annoy you, it will continue on pinging the server every 1.5 seconds, provided that the connection has been established, it will not notify you until the status has been changed.


## Running the app!
### Versions
I've created two versions of the application and it depends on you, the user to choose whichever you'd like:


#### Who-Version (recommended) - [Download Here 📥](https://workupload.com/file/f6KkuhQqN7p)
It's how the application is intended to work, <b>REQUIRES</b> the assets to function, and it will break if not present, assets such as a notification sounds 🎶 and the app logo 🖼️, both that add to the visual and audiable fidelity of the application.

#### Lite-Version - [Download Here 📥](https://workupload.com/file/u9JdccETQL8)
The lite version does not require you to have assets to function. pure. code. all text. Windows OS notification sounds, and no logos.


## Running a development version
If you intend on improving on the application in any shape or form, follow the normal python workflow.

Switch into the virtual environment using the following command inside the root directory:
```
$ Scripts\activate
```
Install the packages from the requirements.txt 
```
$ pip install -r requirements.txt
```
then simply run the python script called 'ui-texter.py' which what starts the CLI and everything else
```
$ py ui-texter.py
```
Have fun! and let me know if you encounter any issues.



Make sure to visit my website! [ItsMsalati](https://ItsMsalati.ly) 🤍 👋
