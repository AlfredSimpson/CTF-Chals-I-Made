# A Quick explanation of the challenge's creation


One-mo'-dance-for-mary was one of the only unsolved challenges at JerseyCTF, but I promise you, it wasn't that hard. Go see the Breakdown for why...

## What went into making the challenge

Making a GOOD osint challenge has multiple paths you can take to find the answer. It shouldn't rely on one exact search, but rather multiple interpretations to find the right result. It should also help you explore a thing you probably weren't aware of before.

In the case of one mo' dance for mary, I wanted to continue the storyline of Mary Morse (introduced in SpringForwardCTF). In order to do this, I would need to find a Mary Morse online in a way that was not only easily found, but could be narrowed down to the point that you'd get the exact answer.

## Find a tool for them to use

I knew I wanted to use a newspaper, so I began looking in the New York Times. I then realized that people would need to pay for this, so I decided against it. Again, this should be accessible and found in multiple ways. So I did what someone should do to start after they gathered the data:

Search for a newspaper archive collection.

Thankfully I found the Library of Congress's archive. https://chroniclingamerica.loc.gov/

## Find recreatable results

I searched, at first, solely for Mary Morse.

Unfortunately, that wasn't such a great search. As Mary Morse has shown up in many different newspapers, I'd need to find a way to make the search as recreatable as possible. 

As I had, at this point, been making a lot of music themes in my challenges, I wanted to do the same here. I happened to be listening to some motown at the time, so I opted to bring it to Detroit. I turned to the Advanced Search tab on the database and searched using  “Detroit OR dance” and “the phrase "Mary Morse"”. The very first result just happened to showcase two women going to a dance. However, this search also had 823 other results. But now I knew what I wanted them to find. Now my job was to analyze the article it was in and find multiple recreatable searches. This first search that brought me here, of course, is one way a user could find it. 

After reading the article I decided that I was going to incorporate Maya Elmer as well. This would be one way to narrow down the results. However, the search function on this site is... nuanced. While you can search with a phrase (and combinations of the other search parameters), you cannot duplicate a search parameter. That is to say, you cannot search with the phrase "Mary Morse" and "Maya Elmer". You can only choose to search with the phrase Mary Morse AND all of the words in the field provided and/or any of the words in that field provided and/or with a set of words within a certain distance to each other. You could abuse the url, if you wanted to, to achieve this... but I knew people would struggle already so I avoided that.

I found three separate searches that significantly lowered the results and, satisfied with the results, wrote the description.

## The Description:

OSINT typically needs a good description. Now that I knew who, what, and where I wanted this to take place, I carefully laid out the challenge. I wanted most lines to contain a reference or clue to the final answer. For many challenges I will include one or two red herrings, but mostly  give solutions every step of the way.




