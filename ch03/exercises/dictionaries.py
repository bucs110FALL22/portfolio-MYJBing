
article = "Effective use of virtual reality to improve student outcomes in Science"

#Creating a dictionary of substitution

substitutions = {
  "enjoyment" : "amusement",
  "opportunity" : "chance",
  "group"       : "batch" , 
  "experience"  : "encounter",
  "question"   : "query" ,
  "overall" : "universal",
  "activity" : "action",
}

for key, value in substitutions.items(): 
  article =article.replace(key, value)

print(article)
