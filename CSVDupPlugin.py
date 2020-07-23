class CSVDupPlugin:
   def input(self, inputfile):
      self.inputfile = inputfile
      self.rowcounts = dict()
      self.colcounts = dict()

   def run(self):
      filestuff = open(self.inputfile, 'r')

      # Duplicate columns
      firstline = filestuff.readline().strip()      
      contents = firstline.split(',')
      for column in contents:
         if (column in self.colcounts):
            self.colcounts[column] += 1
         else:
            self.colcounts[column] = 1

      # Duplicate rows
      for line in filestuff:
         contents = line.split(',')
         row = contents[0]
         if (row in self.rowcounts):
            self.rowcounts[row] += 1
         else:
            self.rowcounts[row] = 1

   def output(self, outputfile):
      filestuff_row = open(outputfile+".row.noa", 'w')
      filestuff_col = open(outputfile+".col.noa", 'w')
      filestuff_row.write("DupRow\tCount")
      filestuff_col.write("DupCol\tCount")
      for row in self.rowcounts:
         if (self.rowcounts[row] > 1):
            filestuff_row.write(row+"\t"+str(self.rowcounts[row])+"\n")
      for col in self.colcounts:
         if (self.colcounts[col] > 1):
            filestuff_col.write(col+"\t"+str(self.colcounts[col])+"\n")


