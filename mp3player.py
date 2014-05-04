from optparse import OptionParser
import glob
import subprocess
import re
import os

def main():
    usage = "python %prog [--sitemap] [--index <index>]"

    parser = OptionParser(usage)
    parser.add_option("--sitemap", "-s",
                        dest = "sitemap",
                        action = "store_true",
                        default = False,
                        help = "Update the demo.sitemap file with the songs in the mp3 folder"
                        )

    parser.add_option("--index", "-i",
                        dest = "index",
                        action = "store",
                        default = 0,
                        type = "int",
                        help = "Play the song in playlist specified by index, index=0 stop song"
                        )
    (option, args) = parser.parse_args()

    playlist = glob.glob("mp3/*.mp3")
    for i in range(len(playlist)):
        playlist[i] = os.path.abspath(playlist[i])
        #print playlist[i]

    if option.sitemap :
        sitemap_update("mp3")
    elif(option.index == 0):
        os.system("pgrep mpg321 | xargs kill ")
    elif(option.index != 0):
        os.system("pgrep mpg321 | xargs kill ")
        subprocess.Popen(["/usr/bin/mpg321", playlist[option.index-1]])
    else:
        print "No action!!"




def sitemap_update(directory = "mp3"):
    sitemap = open("configurations/sitemaps/demo.sitemap").read()
    selection_regex = re.compile(r'(Selection\s+item\s*=\s*Music_Player.*?)(mappings.*)')
    songs = glob.glob1(directory, "*.mp3")
    map_list = []
    for i in range(len(songs)):
        map_list.append(str(i+1) + '="' + songs[i] + '"')
    map_str = "mappings=[0=STOP, " + ", ".join(map_list) + "]"
    sitemap = selection_regex.sub(r"\1" + map_str, sitemap)
    #print sitemap
    f = open("configurations/sitemaps/demo.sitemap", "w")
    f.write(sitemap)
    f.close()



if __name__ == "__main__":
    main()
