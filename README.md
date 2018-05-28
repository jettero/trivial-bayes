# Trival Bayesian Computer

I'm just practicing my python — converted the little story problem I had solved
in Perl into a classifier in Python, then re-solved the story problem with it.
(I dropped my original Perl solution in the contrib folder.)

Everything done here is done better and more completely in
[bayespy](http://bayespy.org).  I made absolutely no attempt to include
docstring documentation in the functions because the entire point of this lib is
as an example of doing these compuations. For real actual Bayesian systems,
bayespy is probably the better choice.

Note that I called the class Classifier … that's not quite right, since it
really only does classifying using `prob_label_not_label_given_addr`.

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

# classifier-example.py — outputs this (random seed 390)
    corpus:
      label: spam  attr: {'that', 'blah', 'stuff', 'the-other', 'viagra', 'this'}
      label: spam  attr: {'the-other', 'blah', 'viagra'}
      label: spam  attr: {'blah', 'the-other', 'stuff', 'viagra', 'this'}
      label: spam  attr: {'stuff', 'the-other', 'that', 'this'}
      label: spam  attr: {'that', 'blah', 'stuff', 'the-other', 'viagra', 'this'}
      label: spam  attr: {'that', 'this'}
      label: spam  attr: {'that', 'blah', 'stuff', 'viagra', 'this'}
      label: spam  attr: {'blah', 'the-other', 'stuff', 'viagra', 'this'}
      label: spam  attr: {'that', 'the-other', 'this', 'blah'}
      label: spam  attr: {'that', 'blah', 'the-other', 'stuff', 'viagra'}
      label: spam  attr: {'that', 'this', 'blah', 'viagra'}
      label: spam  attr: {'blah', 'the-other', 'stuff', 'viagra', 'this'}
      label: spam  attr: {'that', 'blah', 'the-other', 'viagra', 'this'}
      label: spam  attr: {'stuff', 'this', 'blah', 'viagra'}
      label: spam  attr: {'that', 'blah', 'the-other', 'stuff', 'viagra', 'this'}
      label: spam  attr: {'that', 'blah', 'stuff', 'the-other', 'viagra', 'this'}
      label: ham   attr: {'that', 'douglas', 'blah', 'the-other', 'this'}
      label: ham   attr: {'that', 'this', 'blah'}
      label: ham   attr: {'that', 'douglas', 'jimmy', 'blah', 'this'}
      label: ham   attr: {'that', 'jimmy', 'douglas', 'blah', 'the-other', 'this'}
      label: ham   attr: {'that', 'douglas', 'jimmy', 'blah', 'this'}
      label: ham   attr: {'that', 'douglas', 'jimmy', 'blah', 'the-other', 'this'}
      label: ham   attr: {'that', 'douglas', 'jimmy', 'the-other', 'this'}
      label: ham   attr: {'that', 'jimmy', 'douglas', 'blah', 'the-other', 'this'}
      label: ham   attr: {'that', 'douglas', 'jimmy', 'blah', 'the-other'}
      label: ham   attr: {'that', 'douglas', 'the-other', 'this'}
      label: ham   attr: {'douglas', 'the-other', 'this', 'jimmy'}
      label: ham   attr: {'that', 'douglas', 'jimmy', 'blah', 'the-other'}
      label: ham   attr: {'that', 'douglas', 'jimmy', 'blah', 'the-other'}
      label: ham   attr: {'that', 'the-other', 'this', 'blah'}
      label: ham   attr: {'that', 'jimmy', 'douglas', 'blah', 'the-other', 'this'}

    P(spam|data[ 0]) = 1.0000 classified correctly
    P(spam|data[ 1]) = 1.0000 classified correctly
    P(spam|data[ 2]) = 1.0000 classified correctly
    P(spam|data[ 3]) = 1.0000 classified correctly
    P(spam|data[ 4]) = 1.0000 classified correctly
    P(spam|data[ 5]) = 0.4783 false negative {'that', 'this'}
    P(spam|data[ 6]) = 1.0000 classified correctly
    P(spam|data[ 7]) = 1.0000 classified correctly
    P(spam|data[ 8]) = 0.5168 classified correctly
    P(spam|data[ 9]) = 1.0000 classified correctly
    P(spam|data[10]) = 1.0000 classified correctly
    P(spam|data[11]) = 1.0000 classified correctly
    P(spam|data[12]) = 1.0000 classified correctly
    P(spam|data[13]) = 1.0000 classified correctly
    P(spam|data[14]) = 1.0000 classified correctly
    P(spam|data[15]) = 1.0000 classified correctly
    P(spam|data[16]) = 0.0000 classified correctly
    P(spam|data[17]) = 0.5168 false positive {'that', 'this', 'blah'}
    P(spam|data[18]) = 0.0000 classified correctly
    P(spam|data[19]) = 0.0000 classified correctly
    P(spam|data[20]) = 0.0000 classified correctly
    P(spam|data[21]) = 0.0000 classified correctly
    P(spam|data[22]) = 0.0000 classified correctly
    P(spam|data[23]) = 0.0000 classified correctly
    P(spam|data[24]) = 0.0000 classified correctly
    P(spam|data[25]) = 0.0000 classified correctly
    P(spam|data[26]) = 0.0000 classified correctly
    P(spam|data[27]) = 0.0000 classified correctly
    P(spam|data[28]) = 0.0000 classified correctly
    P(spam|data[29]) = 0.5168 false positive {'that', 'the-other', 'this', 'blah'}
    P(spam|data[30]) = 0.0000 classified correctly

    method 2
    R(data[ 0]) = spam (actual: spam)
    R(data[ 1]) = spam (actual: spam)
    R(data[ 2]) = spam (actual: spam)
    R(data[ 3]) = spam (actual: spam)
    R(data[ 4]) = spam (actual: spam)
    R(data[ 5]) = ham  (actual: spam)
    R(data[ 6]) = spam (actual: spam)
    R(data[ 7]) = spam (actual: spam)
    R(data[ 8]) = spam (actual: spam)
    R(data[ 9]) = spam (actual: spam)
    R(data[10]) = spam (actual: spam)
    R(data[11]) = spam (actual: spam)
    R(data[12]) = spam (actual: spam)
    R(data[13]) = spam (actual: spam)
    R(data[14]) = spam (actual: spam)
    R(data[15]) = spam (actual: spam)
    R(data[16]) = ham  (actual: ham )
    R(data[17]) = spam (actual: ham )
    R(data[18]) = ham  (actual: ham )
    R(data[19]) = ham  (actual: ham )
    R(data[20]) = ham  (actual: ham )
    R(data[21]) = ham  (actual: ham )
    R(data[22]) = ham  (actual: ham )
    R(data[23]) = ham  (actual: ham )
    R(data[24]) = ham  (actual: ham )
    R(data[25]) = ham  (actual: ham )
    R(data[26]) = ham  (actual: ham )
    R(data[27]) = ham  (actual: ham )
    R(data[28]) = ham  (actual: ham )
    R(data[29]) = spam (actual: ham )
    R(data[30]) = ham  (actual: ham )
