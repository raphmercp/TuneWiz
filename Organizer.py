import sys
from urllib.error import HTTPError
import urllib.request
import re




BAGPIPE_TUNES_URL = 'https://bagpipetunes.intertechnics.com/'

NOTES = set(['LG', 'LA', 'B', 'C', 'D', 'E', 'F', 'HG', 'HA'])

class Organizer:

    def __init__(self) -> None:
        self.tunemap = {}

    def generateTuneMap(self, json):
        pass

    def downloadBagpipeTunes(self):
        for i in range(65, 66):    # Z is 90
            character = chr(i)
            print(f"{i}: {chr(i)}")
            try:
                request = urllib.request.Request(BAGPIPE_TUNES_URL + 'alpha_results.php?d=' + character)
                response = urllib.request.urlopen(request)
                stringified = response.read().decode("utf-8")
                # print(stringified)
                teststring = 'files/Bagpipe_Player/A/Away_In_A_Manger.bww'
                filenames = re.findall(r'files/Bagpipe_Player/.{1,35}\.bww', stringified)
                print(filenames)
                for f in filenames:
                    try:
                        request2 = urllib.request.Request(BAGPIPE_TUNES_URL + f)
                        response2 = urllib.request.urlopen(request2)
                        stringifiedbww = response2.read().decode("utf-8")
                        print(self.parseAndStoreTune(stringifiedbww))
                    except HTTPError:
                        print(f"Could not find tune named {f}")
            except HTTPError:
                print("Could not access url")
                sys.exit(1)

    def parseAndStoreTune(self, stringtune):
        theme_notes = []
        lastNote = None
        title = None
        linelist = stringtune.split('\n')
        for line in linelist:
            line_items = line.split(",").strip('"')
            print(line_items)
            if title is None and len(line) > 0 and line[0] == '"' and len(line_items) > 1:
                title = line.split(',')[0].strip('"')
                print(title)

            if len(line) > 0 and line[0] == '!':
                lineitems = line.split()
                for term in lineitems:
                    if term[0] in NOTES and term[0] != lastNote:
                        theme_notes.append(term[0])
                        lastNote = term[0]
                    elif len(term) > 1 and term[:2] in NOTES and term[:2] != lastNote:
                        theme_notes.append(term[:2])
                        lastNote = term[:2]
                    if len(theme_notes) > 9:
                        return (tuple(theme_notes), title)


def main():
    org = Organizer()

    # org.downloadBagpipeTunes()
    with open("testtune", "r") as file:
        print(org.parseAndStoreTune(file.read()))     
    
if __name__ == "__main__":
    main()