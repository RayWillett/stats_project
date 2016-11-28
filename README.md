#Getting Started
clone into $working_dir

````bash
python3 -m pip install virtualenv
cd $working_dir
virtualenv env
source ./env/bin/activate
python3 -m pip install matplotlib
```

#Documentation:
http://matplotlib.org/examples/shapes_and_collections/scatter_demo.html
http://www.ucs.cam.ac.uk/docs/course-notes/unix-courses/pythontopics/graphs.pdf


#Comments
  * Match functions to bullet points -> i.e. put in a comment this finishes part a of checklist.


#Project spec:

~~a. start with a known quadratic~~ - Ray
~~b. generate perfect data along that quadratic~~ -Ray
~~c. generate noise ~~ -Ray
~~d. add the noise to the perfect data; graph the result~~ Ray
~~e. fit a straight line to the noisy data; add that to the graph -Ray
f. compute the residual at some particular x-value (either near the
middle of the x range, or near the end, but not near where the
straight line crosses the known quadratic)
g. record the residual, add it to a histogram (plan on maybe 30 bins
since sqrt(1000) is about 30)
h. repeat at step c, maybe 1000 times (not showing each of the 1000 as
a separate frame in the movie. Maybe show 1 frame per second for 4
seconds, then 2 frames per second for 4 seconds, then 4 frames/sec for
4 sec, then 8 frames/sec for 4 sec, etc.). At some point (above 30
frames/sec?) you can just stop showing individual frames and jump to
the finished histogram.
i. On the resulting histogram, make the 0 mark clear, and also compute
the mean and SD of the recorded residuals and show them on the graph,
numerically and graphically.

We might need to run all 1000 trials first (without the animations) to
figure out the proper range for the histogram, then run them again
knowing how wide the histogram should be. If we do that, we should be
careful about seeding the random number generator, so we can reproduce
the same 1000 trials.

Then repeat a-through-i but instead of fitting a straight line, fit a
parabola each time. The resulting histogram should have a mean of 0.

Then repeat a-through-i but instead of fitting a straight line, fit a
cubic each time. The resulting histogram should have a mean of 0, but
a higher SD than when fitting a parabola.

It's also good to try it for a 4th-order polynomial, and a 0th-order
polynomial (y=avg of the noisy y values). That way we have 2 orders
below the true polynomial and 2 orders above.

Then make a summary plot or slide. Maybe each of the histograms
overlaid on each other? To overlay histograms, it's better to use a
"frequency polygon" (lines connecting the histogram bar heights,
without the bars).

Repeat at another x value? If the first one was near the middle of the
range, make the 2nd one near the outer edge of the range.

We're also interested in the values of the fitted parameters (the
coefficients in the polynomial). We could record them for each of the
1000 fits, then make histograms of them. Maybe make a grid of
histograms:

                  x^0 coeff   x^1 coeff     x^2 coeff   x^3 coeff     x^4 coeff
Flat fit
Linear fit
Parabola fit
Cubic fit
Quartic fit

and have a vertical line showing the true value used in the true
quadratic on each histogram. It would be 0 for the x^3 and x^4 coeffs.
Similarly but opposite, the x^4 coeff histogram would show all-0 (that
is, all data points in a bar at 0) for the cubic fit; the x^3 and x^4
coeff histograms would show all-0 for the Parabola fit, etc.

All this is about the bias-vs-variance tradeoff. Flexible models (ones
with lots of adjustable values: lots of coefficients on high-order
polynomials) tend to have low bias but higher variance, while
inflexible models tend to be the opposite.

One way we decide what to use is cross-validation: dividing the data
into a training set and a testing set. I'd like to make a video about
that too, using the same framework that you'll develop in the above
work. We'll see what we have time for this semester."
>Dr Ross


#Markdown cheatsheet
 * https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
