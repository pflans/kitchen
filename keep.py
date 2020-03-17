import gkeepapi

keep = gkeepapi.Keep()
success = keep.login('patfmurray@gmail.com', 'uunmqnvciqhgnhph')

# gnotes = keep.all()
artLabel = keep.findLabel('Art')
# gnotes = keep.find(artLabel)

#gnotes = keep.find(query='wikipedia')
#print([n for n in gnotes])
#noteList = list(gnotes)
#for note in noteList:
#  print(note.text)

labels = keep.labels()
gnotes = keep.find(labels=[keep.findLabel('Art')])
noteList = list(gnotes)
for note in noteList:
  print(note.text)
