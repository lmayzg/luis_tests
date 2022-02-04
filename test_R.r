oct=900
nov=857
dic=1200
inc1=100*abs(nov-oct)/oct
inc2=100*abs(dic-nov)/nov
print(paste0(inc1,"% is the percentage of decrease in stores between october and november"))
print(paste0(inc2,"% is the percentage of increase in stores between november and december"))