from random import choice

print """ 
         _......._
       .-:::::::::::-.
     .:::::::::::::::::.
    :::::::' .-. `:::::::
   :::::::  :   :  :::::::
  ::::::::  :   :  ::::::::
  :::::::::._`-'_.:::::::::
  :::::::::' .-. `:::::::::
  ::::::::  :   :  ::::::::
   :::::::  :   :  :::::::
    :::::::._`-'_.:::::::
     `:::::::::::::::::'
 jgs   `-:::::::::::-'
          `'''''''`    """
print "\n I am the all knowing Magic 8 Ball. Ask me a question.\n"

prompt = '>'

question = raw_input(prompt )

answers = ['It is certain', 'It is decidedly so', 'Without a doubt',
 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 
'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 
'Ask again later', 'Better not tell you now', 'Cannot predict now',
'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 
'My sources say no', 'Outlook not so good', 'Very doubtful']

print choice(answers)
print "\n"






