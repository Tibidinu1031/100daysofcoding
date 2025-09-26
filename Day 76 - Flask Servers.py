from flask import Flask
import os

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
  page = """
  <html>
  <body>
  <p><a href = '/portfolio'>Go to Porfolio</a></p>
  <p><a href = '/Linktree'>Go to Linktree</a></p>
  <p>Can't find the file pane in Replit to add the files so there will be no images</p>
  </body>
  </html>
  """
  return page
  

@app.route('/portfolio')
def portfolio():
  page = """
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Tibi Dinu's 5 Random Portfolio</title>
      <link rel="stylesheet" href="static/style.css">
  </head>
  <body>
  <h1>These are 5 random Python projects that I picked as Replit 100 Days of Code Challenge for Day 73</h1> 
  <br>
  <br>

  <div class = "days" id="day-1">
  <h2>Day 24</h2> 
  <p><u>This was a rookie project in the early days in which the course takers create a subroutine for dice with countless faces and simply roll it.</u></p>
  <br>
  <a href = https://replit.com/@tiberiusdinu95/day24100-days-of-code target="_blank"><img src="assets/Day 24.PNG" alt="Day 24"></a>
  <br>
  <br>
  <br>
  <br>
  <br>
  </div>   

  <div class = "days" id="day-2">
  <h2>Day 35</h2> 
  <p><u>This was a task manager with prettyPrints, autosaves/autoloads, os and time libraries.<br> I felt good when i finished it and it gave me confidence in my coding abilities.<br> It prolly has a few tiny bugs or rookie code if I were to check it. But hey, that's how we learn. Every master was once a fool.</u></p>
  <br>
  <a href = https://replit.com/@tiberiusdinu95/day35100-days target="_blank"><img src="assets/Day 35.PNG" alt="Day 35"></a>
  <br>
  <br>
  <br>
  <br>
  <br>
  </div>  

  <div class = "days" id="day-3">
  <h2>Day 56</h2>
  <p>Fucking day 56 bruh. I still recap it to this day.</p> 
  <br>
  <a href = "https://replit.com/@tiberiusdinu95/Day56100Days" target="_blank"><img src="assets/Day 56.PNG" alt="Day 56"></a>
  <br>
  <br>
  <br>
  <br>
  <br>
  </div>

  <div class = "days" id="day-4">
  <h2>Day 63</h2> 
  <p><u>This one was in a way similar to this one. It was about importing code from our other Python files and create a 10x coder libraby.<br> Because I'm a time freak I chose to pick 3 other random files and import them there.</u></p>
  <br>
  <a href = "https://replit.com/@tiberiusdinu95/Day63100Days" target="_blank"><img src="assets/Day 63.PNG" alt="Day 63"></a>
  <br>
  <br>
  <br>
  <br>
  <br>
  </div>

  <div class = "days" id="day-5">
  <h2>Day 72</h2>    
  <p><u>Arguably my most complex code I've written. If not the most, mos def makes top 3.</u></p>
  <br>
  <a href="https://replit.com/@tiberiusdinu95/Day72100Days" target="_blank"><img src="assets/Day 72.PNG" alt="Day 72"></a>
  </div>

  </body>
  </html>
  """
  return page

@app.route('/Linktree')
def Linktree():
  page = """
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Tiberius Dinu LinkTree-like Page</title>
      <link rel="stylesheet" href="static/style2.css">
  </head>
  <body>
      <div>
          <img src="assets/me.jpg">
      </div>

      <div>
          <h1>Tiberius Dinu</h1>
          <h5><span>Neoteq Founder</span></h5>
          <br>
          <h4><span>Socials</span></h4>
          <br>
          <ul>
              <li><a href="https://www.linkedin.com/in/tiberius-dinu-51a625170/" target="_blank">LinkedIn - Tiberius Dinu</a></li>
              <li><a href="https://www.linkedin.com/company/neoteq-us/" target="_blank">LinkedIn - Neoteq</a></li>
              <li><a href="https://podcasts.apple.com/us/podcast/startup-brainframe/id1810706175" target="_blank">Startup Brainframe - Apple Podcasts</a></li>
              <li><a href="https://open.spotify.com/show/1RJ2M29oEHaORdCeFEpMuW" target="_blank">Startup Brainframe - Spotify</a></li>
              <li><a href="https://github.com/Tibidinu1031" target="_blank">GitHub</a></li>
          </ul>
      </div>
  </body>
  </html>
  """ 
  return page


app.run(host='0.0.0.0', port=81)