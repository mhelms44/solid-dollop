import argparse
parser = argparse.ArgumentParser(description="Takes a BPM and spits out MS values")
parser.add_argument("bpm",type=int,help="Specify the BPM you want to calculate")
args = parser.parse_args()
print(args.bpm)
quarter_note = (60000 / args.bpm)
eighth_note = (quarter_note / 2)
sixteenth_note = (eighth_note / 2)
thirtysecond_note = (sixteenth_note / 2)
print(quarter_note,"\n",eighth_note,"\n",sixteenth_note,"\n",thirtysecond_note)