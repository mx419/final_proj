# User Guide
- DS-GA-1007  Final Project
- Team Member:
  - Muhe Xie(mx419) mx419@nyu.edu
  - Sida Ye(sy1743) sy1743@nyu.edu
  - Junchao Zheng(jz2327) jz2327@nyu.edu

##### 
### Part1 : Usage of the Application.

1. This data visualization will generate four graphs with two pie plots and two bar plots: gender distribution, user type distribution, daily usage and daily miles.

2. The station frequency visualization part (option 2) will print the name of  top 5 high frequency stations and generate 3 plots automatically (close one to see the next plot).
- Plot 1: The points of citi bike stations on the map
- Plot 2: The top 5 high frequency stations on the map
- Plot 3: The heat map of the station frequency

3. 
 - Get information of usage of the station on that particular date on historical date and get recommendation on the station.
 - Get two alternative stations nearby which meet with the criterion: I. within 15-minute walk, II. predicted to be recommended.

### Part2 : Configuration:

1. Pandas to access data.
2. Numpy to perform statistical analysis.
3. Matplotlib for graphics including pie plots and bar plots.
4. Basemap for graphics including geometric maps.
5.
6.

### How to run the program:

In terminal, enter the command to run the program:

```sh
$ git clone [git-repo-url]
$ cd [repo file]
$ python citibike_1007project.py
```

##### Main Menu:

- enter 1 to go to a sub menu of monthly data visualization.
- enter 3 to go to a sub menu of station frequency visualization.
- enter 3 to go to a sub menu of prediction and recommendation.


###### Option 1: Monthly data visualization

- Input year and month between 2013/7 and 2015/10:
  - Enter a year between 2013, 2014, 2015.
  - Enter an integer from 1 to 12 as month.
- Enter back: go back to main menu.
- Enter quit: exit the program.

###### Option 2: Station frequency visualization
2.

###### Option 3: Prediction and recommendation


- Enter 1 to run the prediction function, enter station ID, day, month and each end with return.
- Enter 2 to run the recommendation function, enter station ID, day, month and each end with return.
- Enter back: go back to main menu.
- Enter quit: exit the program.

*** Main program
package pickle installed and use pickle to load dictionary form .p file.

***remain problem
transfer station name to station ID or versa.



# Dillinger

Dillinger is a cloud-enabled, mobile-ready, offline-storage, AngularJS powered HTML5 Markdown editor.

  - Type some Markdown on the left
  - See HTML in the right
  - Magic

Markdown is a lightweight markup language based on the formatting conventions that people naturally use in email.  As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

### Version
3.2.0

### Tech

Dillinger uses a number of open source projects to work properly:

* [AngularJS] - HTML enhanced for web apps!
* [Ace Editor] - awesome web-based text editor
* [Marked] - a super fast port of Markdown to JavaScript
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework [@tjholowaychuk]
* [Gulp] - the streaming build system
* [keymaster.js] - awesome keyboard handler lib by [@thomasfuchs]
* [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Installation

You need Gulp installed globally:

```sh
$ npm i -g gulp
```

```sh
$ git clone [git-repo-url] dillinger
$ cd dillinger
$ npm i -d
$ mkdir -p downloads/files/{md,html,pdf}
$ gulp build --prod
$ NODE_ENV=production node app
```

### Plugins

Dillinger is currently extended with the following plugins

* Dropbox
* Github
* Google Drive
* OneDrive

Readmes, how to use them in your own application can be found here:

* [plugins/dropbox/README.md] [PlDb]
* [plugins/github/README.md] [PlGh]
* [plugins/googledrive/README.md] [PlGd]
* [plugins/onedrive/README.md] [PlOd]

### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantanously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma start
```

### Todos

 - Write Tests
 - Rethink Github Save
 - Add Code Comments
 - Add Night Mode

License
----

MIT


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [@thomasfuchs]: <http://twitter.com/thomasfuchs>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [marked]: <https://github.com/chjj/marked>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [keymaster.js]: <https://github.com/madrobby/keymaster>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>
   
   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]:  <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>


