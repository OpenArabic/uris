import re, os, shutil, sys, glob

# REMOVE PROCESSED TEXTS FROM RE

import fnmatch
import os

##with open("__Entire_Corpus_DatesTexts_2016_10_11_upd.txt", "r", encoding="utf8") as f1:
##    ids = f1.read()
##
##    for root, dirnames, filenames in os.walk('../corpus/'):
##        for filename in fnmatch.filter(filenames, '*-ara1'):
##            t = filename.replace("-ara1", "")
##            t = t.split(".")[2]
##            t = re.sub(r"(JK|Shamela|Shia)", r"\1_", t)
##
##            ids = ids.replace(t, "")
##
##    ids = re.sub("\|+", "|", ids)
##            
##    with open("__Entire_Corpus_DatesTexts_2016_10_11_upd.txt" , "w", encoding="utf8") as f9:
##        f9.write(ids)

added = []
with open("__Entire_Corpus_Working.txt", "r", encoding="utf8") as f1:
    uris = f1.read()
    split = "######## BEGofRECORD #+\n"
    for i in re.split(split, uris)[1:]:
        if re.search("\d\d\d\d[A-Za-z]+\.[A-Za-z]+", i.split("\n")[0]):
            us = re.findall("Shamela_\w+|Shia_\w+|JK_\w+", i)
            #print(us)
            added.extend(us)
            #print(added)
    print(len(added))
    print(len(list(set(added))))
    
    added = list(set(added))


    #print(addedRE)

with open("__Entire_Corpus_DatesTexts_2016_10_11_upd.txt", "r", encoding="utf8") as f1:
    ids = f1.read()

    for a in added:
        ids = ids.replace("|%s" % a, "")

    with open("__Entire_Corpus_DatesTexts_2016_10_11_upd.txt" , "w", encoding="utf8") as f9:
        f9.write(ids)

# Another list
with open("__Entire_Corpus_DatesTexts_Simple.txt", "r", encoding="utf8") as f1:
    ids = f1.read()

    for a in added:
        ids = ids.replace("\t%s\n" % a, "")

    with open("__Entire_Corpus_DatesTexts_Simple.txt" , "w", encoding="utf8") as f9:
        f9.write(ids)

print("Processed!")
