from rich import print,pretty
from pyfiglet import Figlet
from main2 import twolane
from main3 import threelane
from main4 import fourlane
from absl import app
from absl import flags

FLAGS = flags.FLAGS
flags.DEFINE_integer('lane', 4, 'Number of Lanes')
flags.DEFINE_integer('minwait', 15, 'Minimum Go Time')

def main(_argv):
    print("")
    f=Figlet(font='banner')
    starter=f.renderText("D. B. T. W. C.")
    print('[blue]'+starter)
    print("")
    print("Project by:> Harshita Yadav | Hemant Kumar Chaudhary | Hrithik Puri | Kartikeya Saraswat")
    print("Roll nums.:>   1819210130   |       1819210132       |  1819210136  |     1819210145    ")
    print()
    #lanec=int(input("Kindly Enter the Number of Lanes:> "))
    #minwait=int(input("Enter Minimum Go Time:> "))

    if FLAGS.lane == 2:
        twolane(FLAGS.minwait)
    if FLAGS.lane == 3:
        threelane(FLAGS.minwait)
    if FLAGS.lane == 4:
        fourlane(FLAGS.minwait)

if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
