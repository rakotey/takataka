Title: The Pragmatic side of big data
tags: big data, enterprise
date: 17-04-2013


A successful big data project is far less about correlating disparate data structures and far more about articulating a testable hypothesis, designing that test, and evaluating the results.
One of the hippest tech memes in 2012 was certainly "Big Data." As shown in the image below, Google Trends shows the popularity of the search term "big data" making the hockey-stick shape starting in the last half of 2011.

What does that mean?  It can't just be that people have discovered that most data is too "big" for a human to read comfortably before bedtime. No. That is not what "big data" means. Business people don't like to read anything longer than three pages, so by that metric, data has been huge since the 8-inch floppy was on sale at Radio Shack.

The secret is that "big data" means different things depending on whether you are on the engineering or business side of the problem.

On the engineering side, big data means, "I need more and faster storage, and by the way, we should try out some of this cool new software I've been reading about on the inter-tubes."  It means using SSD instead of spinning platters; clustering; partitioning, and sharding. But this is not news to us. What we really have a hard time understanding (or a hard time caring to understand, perhaps?) is what our colleagues on the business side want from us when it comes to big data.

The Psyche of a Data-Hungry Business Person
On the business side, big data means, "How do I capitalize on the data we have internally?" Decision-makers, marketing people, and business analysts have read dozens of articles describing the immense advantage this company or that company has reaped by better understanding the usage and preference trends of its customers, and they are tired of pretending at cocktail parties that their data gets out and works for them, too.

The key to understanding the allure of big data to the marketer or business stakeholder is to understand that they view this data as a goose that lays golden eggs that they cannot get their hands on. To them, big data is data that is locked up away from the business analysts and stakeholders. 

Understand What You Have and Where You Want To Go
For an engineer approaching a big data project, the first step is to map out what you have, and how it is structured. Because it's all so disparate and mad-whack, you will need a logic layer (that is, scripts) to tie it together and transform it into…you guessed it…even more data.

Now, when you collect data from all the myriad interactions humans have with technology all day every day, it's true that it piles up quickly. But just storing it isn't the problem. Moving it is the problem. What happens if you collect everything on magnetic tapes, and then suddenly a business stakeholder wants to move that data to Amazon S3? Better build in a three-month lead time. I worked on a project where it was faster to copy all the data that changed each day onto a huge pile of hard drives, and then truck those drives to the data center after work let out at 6PM than to transfer the data over a dedicated OC12. Once the primary data has parked itself, it hates to move. 
