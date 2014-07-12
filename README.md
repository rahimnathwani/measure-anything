measure-anything
================
Inspired by the book [How to measure anything](http://www.amazon.com/dp/1118539273)

The book 'How to measure anything'[0] says that people can get better at estimation through practice. Specifically, it says that practice and feedback can help people give better answer to questions like:
"Estimate a range for the population of Nevada, with 80% confidence."

The book's definition of 'better' here is that, if asked a large number of questions:

- Right about 80% of the time: good calibration

- Right much more than 80% of the time: your upper/lower bounds are too far apart, i.e. you're being too conservative. e.g. I could estimate the population as being between 0 and 7bn, and I'd be right, but not usefully right.

- Right much less than 80% of the time: too confident, with too narrow ranges.

I want to create a free app to train calibration.  I'm imagining something which presents you with a question, after which you enter an upper and lower bound.  You get asked a few questions and then shown the answers.  After you've answered more than, say, 20 questions cumulatively (not per session) the app will start to show an indicator about whether you are over-confident, under-confident, or just right. (The confidence intervals for each question need not be the same.)

The closest thing I have found (thanks to gtardini on HN), is this [iPhone app](https://itunes.apple.com/it/app/updating-game/id524916372?mt=8)

I'll use Python 2.7 and Flask.  I'll update this file with installation instructions when there's something to see.