# Breaking JerseyCTF_2023

One-mo'-dance-for-mary premiered during the JerseyCTF III event in April 2023. Despite receiving an incredible amount of messages complaining that it was too guessy of a challenge, I knew that it was not. Why? Because I took the time to build it so meticulously that I knew they should be able to find it if they simply did what I so often jokingly suggest: get good. 

![image](https://user-images.githubusercontent.com/73041922/232670739-3dfa936a-ecf6-42e3-b133-b4c6929fa655.png)


# Step One (All methods)

If you've ever watched any of my videos or read any of my writeups, you know by now: the first thing to do is to get out a notepad. I use the one on my PC, but you can use physical. Why? Because you're solving a case and you need to take notes.

You have to solve a challenge, but the goal is not just "find the flag". The goal is whatever the challenge needs you to do. In this case, my challenge was forcing competitors to find the dance that Mary and Maya went to in an old newspaper. 

You should also take note of anything odd, irregular, or otherwise important in what is, most likely, a sea of nonsense.

Here's the text of the description:
```
one-mo'-dance-for-mary

We still can't find Mary ... and now Maya's missing, too.... The last time we heard from Mary ... was when she performed in her Aunt Helen's play in Poughkeepsie.
And Maya's been stuck on Mary like glue since they met ... So she's vanished, too!
We figured she'd find a way ... Ford through the waves of time ... back to modern times, but not yet ...
We've been scouring everything ... for any news of Modern Women ... in the past.
Back then ... if you wanted to know what people were doing ... you had to read the newspaper ...
We've got time to set straight ... and I bet those two are off dancing the night away ...
They can't Dodge their responsibilities forever!
Flag will be formatted as the name of the dance (dance is not included) followed by the date it happened in MMDDYYYY Example: jctf{Name_Of_DanceMMDDYYYY}
```
And here are the keywords I'd pick out, and where they'd fall in my list of things to watch out for:

**People**:
```
Mary [If you connected the dots AND watched the walk through from SFCTF, you knew it was Morse or saw the ... everywhere. However, I assumed you didn't.]
Maya
Aunt Helen - But the description didn't state she was with them and probably wasn't there.
```
**Possible locations**:
```
Poughkeepsie - It was mentioned, but not specified that it was there. It could have been, though.
Detroit [Ford, Dodge, and mo' like motorcity or motown was mentioned. You may not have noticed that, though, and it wasn't necessary to solve.]
```

**Key words**:
```
Ford, Dodge : maybe something to do with cars?
mo' : Possibly motown, short for more, or motor?
stuck like glue: Unknown, just odd phrasing
Modern Women: Capitalized - why? Possibly the newspaper?
the newspapers: It was mentioned we had to read the newspaper, probably where we should look.
Dance: in the flagformat we are told to look for the name of the dance  and the date it (the dance) happened. So contrary to those 70+ "jitterbug" submissions: No, we needed to find the name of the dance they attended.
... : why are ellipsis used so much?
```

Great, now we know what was important in the description, how can we solve it?

# Step two - Work backwards

So we need to find Mary and Maya in an old newspaper. Perfect, how do we find old newspapers?

*Google it*

Great, you googled newspaper archive or old newspapers online or something like that. Thankfully the Library of Congress has good SEO and you, hopefully, found this site. https://chroniclingamerica.loc.gov/

# Actually finding the newspaper article

Here is where your paths might diverge. There were many ways to solve this, so yours might not be here. However, here are the ways I anticipated a solve to come from.

## The easiest routes

Without knowing the last name Morse, you could have tried any of these three searches to get the desired outcome:

* Mary, Maya, dance, within 10 words of each other.
* * This produces only one result: the exact page the article is on.
* * Yes, that's **it**. Yes, it was that easy.

![image](https://user-images.githubusercontent.com/73041922/232670946-c0637899-bf2b-492e-b6c9-19ffc6c8bf03.png)


Or you could identify the paper it was taken in:
* Do a basic search here for "News Modern Women" (no quotes), and you'll find dozens of results for the first few pages all with the title "News for Modern Women", a section of the Detroit Evening Times. Now you know which paper it was in.
* * Using this information, you can add the Detroit Evening Times as a filter and search any of the following to get one result:
* * Maya dance within 10 words of each other
* * Mary dance within 10 words of each other, and 'with all of the words': maya dance
* * Maya Elmer (for those who would guess why glue was mentioned)
* * mary maya ... dance within 10 words of each other
* * night, mary, maya (2 results)
  


Of course, if you did know the last name, all you had to search (Without any advanced searching) was:
```
Mary Morse Maya
```
This, too, turns up only one result. 

In total, I identified at least 5 different searches that one could do with the limited information provided that would return only one result which contained the answer to the challenge.

## Harder routes

Searching any of these phrases also turned up the desired article, but it was alongside many others (but less than 75 generally):

Some examples: 
* “the phrase "Mary"” and “Maya, dance”
* * Produces 75 results, the desired article being #12 (and the only one that talks about dancing)
* Advanced search, all of the words: mary maya ... dance
* * Produces 36 results, the 2nd of which is the correct one

There were in total about 10-15 searches I found that could gave a very small sample size of newspapers that contained our result (which was typically #1 or #2 in the list).

![image](https://user-images.githubusercontent.com/73041922/232671048-3b74d579-e6cb-43b1-b74f-01d0bba11ebf.png)


# Final steps: Find the date/dance

The dance name was below their photo: Russian War Relief Dance. THe article also stated it was on Saturday. This article was printed on a Tuesday, August 25th 1942 4 days before the dance. You'd need the date of the dance added to correctly solve the challenge. This was the easiest part.

![image](https://user-images.githubusercontent.com/73041922/232670668-356deaf3-76df-45f6-b1e2-10cfdeb017b7.png)
