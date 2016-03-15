import json
import os, sys

from pprint import pprint

with open('data.json') as data_file:    
    data = json.load(data_file)
    filenames = []

    for majorkey, subdict in data.iteritems():
      # print majorkey
      if majorkey == "data":
        for subkey, value in subdict.iteritems():
          categories = value["categories"]
          if "CSS" in categories or "CSS2" in categories or "CSS3" in categories:
            filename = subkey + ".json"
            filenames.append(filename)
            
    for majorkey, subdict in data.iteritems():
      if majorkey == "data":
        for subkey, value in subdict.iteritems():
          categories = value["categories"]
          newFileName = subkey + ".json"
          if not newFileName in filenames:
            print "removed"
            os.remove(subkey + ".json")




      