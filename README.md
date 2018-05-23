# Trival Bayesian Computer

I'm just practicing my python — converted a little story problem I had solved in perl into a classifier in python, then resolved the story problem with it

Note that I called the class Classifier … that's not quite right, since it doesn't classify, it just computes.  I had a classifier in mind for the next step, but lost track of what I was doing.

# nbc-example.py — outputs this

    There is a population of students, 60% boys, 40% girls, all wearing uniforms.
    The girls may choose either trousers or skirts (and do so on a 50/50 basis),
    but the boys must all wear trousers.

    You see a silhouette of a student wearing trousers.  What is the probability
    that it is a girl [q1.a]?  A boy [q1.b]?  if you saw the same figure huddled
    in the grass nearby (and it was definitely a female student), what would be
    the probability she was wearing trousers [q2]?


    corpus:
      label: boy   attr: set(['trousers'])
      label: boy   attr: set(['trousers'])
      label: boy   attr: set(['trousers'])
      label: boy   attr: set(['trousers'])
      label: boy   attr: set(['trousers'])
      label: boy   attr: set(['trousers'])
      label: girl  attr: set(['skirt'])
      label: girl  attr: set(['skirt'])
      label: girl  attr: set(['trousers'])
      label: girl  attr: set(['trousers'])

    prob girl: 0.400000 ; prob boy: 0.600000
    prob trousers given girl: 0.500000
    prob trousers given  boy: 1.000000
    probability girl given trousers: 0.250000
    probability boy  given trousers: 0.750000

    corpus:
      label: trousers  attr: set(['boy'])
      label: trousers  attr: set(['boy'])
      label: trousers  attr: set(['boy'])
      label: trousers  attr: set(['boy'])
      label: trousers  attr: set(['boy'])
      label: trousers  attr: set(['boy'])
      label: skirt     attr: set(['girl'])
      label: skirt     attr: set(['girl'])
      label: trousers  attr: set(['girl'])
      label: trousers  attr: set(['girl'])

    prob trousers: 0.800000 ; prob skirt: 0.200000
    prob girl given trousers: 0.250000
    prob boy  given trousers: 0.750000
    probability trousers given girl: 0.500000
