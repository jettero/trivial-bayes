# Trival Bayesian Computer

I'm just practicing my python — converted the little story problem I had solved
in Perl into a classifier in Python, then re-solved the story problem with it.
(I dropped my original Perl solution in the contrib folder.)

Everything done here is done better and more completely in [bayespy](http://bayespy.org).

Note that I called the class Classifier … that's not quite right, since it
doesn't classify, it just computes.  I had a classifier in mind for the next
step, but lost track of what I was doing.

This girl/boy trousers problem is really famous. If you look up anything about
Bayes anywhere, you'll run into it eventually.

# trousers-example.py — outputs this

    There is a population of students, 60% boys, 40% girls, all wearing uniforms.
    The girls may choose either trousers or skirts (and do so on a 50/50 basis),
    but the boys must all wear trousers.

    You see a silhouette of a student wearing trousers.  What is the probability
    that it is a girl [q1.a]?  A boy [q1.b]?  if you saw the same figure huddled
    in the grass nearby (and it was definitely a female student), what would be
    the probability she was wearing trousers [q2]?


    Q1 corpus:
      label: boy   attr: {'trousers'}
      label: boy   attr: {'trousers'}
      label: boy   attr: {'trousers'}
      label: boy   attr: {'trousers'}
      label: boy   attr: {'trousers'}
      label: boy   attr: {'trousers'}
      label: girl  attr: {'skirt'}
      label: girl  attr: {'skirt'}
      label: girl  attr: {'trousers'}
      label: girl  attr: {'trousers'}

    prob girl: 0.400000 ; prob boy: 0.600000
    prob trousers given girl: 0.500000
    prob trousers given  boy: 1.000000
    probability girl given trousers: 0.250000
    probability boy  given trousers: 0.750000

    Q2:
    prob trousers: 0.800000 ; prob skirt: 0.200000
    prob girl given trousers: 0.250000
    prob boy  given trousers: 0.750000
    probability trousers given girl: 0.500000

    Alternate Q2 (reversed data) corpus:
      label: trousers  attr: {'boy'}
      label: trousers  attr: {'boy'}
      label: trousers  attr: {'boy'}
      label: trousers  attr: {'boy'}
      label: trousers  attr: {'boy'}
      label: trousers  attr: {'boy'}
      label: skirt     attr: {'girl'}
      label: skirt     attr: {'girl'}
      label: trousers  attr: {'girl'}
      label: trousers  attr: {'girl'}

    prob trousers: 0.800000 ; prob skirt: 0.200000
    prob girl given trousers: 0.250000
    prob boy  given trousers: 0.750000
    probability trousers given girl: 0.500000

# cards-example.py — outputs this

    Have someone draw a card from a deck. They tell you it's a face card, what's
    the probability it's a king?

    (You could totally do this without invoking Bayes… Here's how you use Bayes.)


    P(King)              = 0.0769 aka the prior probability
    P(Face)              = 0.2308 aka the evidence
    P(Face|King)         = 1.0000
    P(Face|King)/P(Face) = 4.3333 aka the likelyhood ratio
    P(King|Face)         = P(Face|King)/P(Face) * P(King) aka the posterior probability
                         = 1.0000/0.2308 * 0.0769
                         = 0.3333
