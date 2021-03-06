# Stack-Exchange-Data-Dump
In this repository, we analyze data from Stack Exchange Data Dump. We use python and aim to find "good" questions, answers, users and visualize the flow of questions/answers over time.

Here a video proposal of this project

https://youtu.be/LQ_LLQ2v14w

# The data
We are using information from the Stack Exchange Data Dump. To start we are analizing the flow of the bitcoin, ethereum, and economics data bases. 

https://archive.org/details/stackexchange

# Requirements

We are coding in python 3. The xml files Users.xml and Posts.xml must be located in the same folder as the main code run.py

Here we include sample files to be downloaded and un-compressed

# Our aproach

The code is provided as a single file 

run.py

This code is dividede into different sections

* From xml to csv: In this section we use Apache Spark to read the xml files and transform those to csv files, of course this step is quick since we use distributed computing

* In the next step we read the users_csv files to find the top 10 questions/answers according to their score

* Then we find the questions associated with the top 10 responses

* Next we find the accepted answers (if they exists) of the top 10 questions

* We display (see examples below) the top 3 (of each cathegory) of our results: Top 3 questions, top 3 accepted answers, top 3 answers

* Then we focus in the flow of questions/answers of each data base over time (see graphs below)

* Next we focus in the users_csv files to find top responder according to our own metric

Individual Punctuation = Reputation + Up Votes -Down Votes

* Once we find the top 10 users we display relevant information for further analysis such as: Location, Age, and About Me 

* Finally, we track the activity of the top 3 users over time in terms of post history (see graphs below)

# Results
In this notebook we present the results for the Bitcoin data base (graphs for questions/answers in general, graphs for questions/answers of top users, and the top questions/answers in general). However in this repository you can find the graphs (and top responses) for the Ethereum (flowuether.png, EtherQA.odt) and Economics (flowuecon.png, EconQA.odt)  data bases as well 

## Flow chart of questions/answers
Here we show a graph with the flow of questions/answers for the three data bases (Bitcoin, Ethereum, Economics) over time

![flowquestions](https://user-images.githubusercontent.com/13289981/39436333-85353ece-4c52-11e8-8a06-ad985140e93e.png)

We oberve from the graph the following facts:

* The flow of questions and answers behave the same in each case (graph of questions is similar to those of answers), with a little bit more of answers than questions

* The graph of Ethereum appears later in 2015, which make sense according to its official appearence in July 2015.

* From 2016-2018 there are more questions/answers about Bitcoin and Ethereum than questions/answers about economics in general, with a notorius maximum at the end of 2017

* From 2013-2018 the amount of questions/answers about economics has remain about 150-250 per month

We add below a graph of the close stock prices for Bitcoin in the same period, we see that aroun the same period where BTC was going up it also raised more concerns.

![btcprice](https://user-images.githubusercontent.com/13289981/39912166-abcb8580-54b2-11e8-977f-c5121d52236b.png)


## Flow chart of questions/answers for top 3 users

![flowubitcoin](https://user-images.githubusercontent.com/13289981/39437076-a71f70fc-4c54-11e8-9b24-e80e30d9903e.png)

We oberve from the graph and our analysis the following facts:

* With exeption of one user, the amount of answers is significantly bigger than the amount of questions posted for the top 3 users according to our metric. This may also be a way to identify **difficult questions** (I mean questions posted by highly experienced users)

* From the top 10 responders 3/10 are from California, most of them are 30+ years old, they are developers, work in finance, cryptography, computer science or related fields


## Answers/Questions from Bitcoin Data Base 

### From Top 3 questions:
                                                                                            
835   &lt;p&gt;Some people keep evangelizing that Bitcoin transaction fees are much lower than in PayPal or with credit cards.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;However, once nearly all 21 million bitcoins have been mined, the network will still have to be secured.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;But &quot;miners&quot; can then no longer be rewarded by newly minted bitcoins. They will have to be rewarded by transaction fees.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;I read that the market will find the equilibrium how much these transaction fees will be.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;Are there any estimates or more concrete calculations about that? Is it even possible to foresee, as the &quot;degree of network security&quot; is a rather nebulous incentive for most (casual) users? Will they thus be enforced by the software? Will these fees better be absolute or relative to the amount of a single transfer?&lt;/p&gt;&#xA;


### From Top 3 accepted answers:

849    &lt;p&gt;&lt;em&gt;I read that the market will find the equilibrium how much these transaction fees will be.&lt;/em&gt;&lt;/p&gt;&#xA;&#xA;&lt;p&gt;&lt;strong&gt;It will not.&lt;/strong&gt;  This is perhaps the biggest flaw in Bitcoin at the moment: once mining rewards end there is no direct linkage between the amount of hashpower needed to secure the network and the incentive to mine.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;True, there is a limit on the blocksize, so if the transaction volume in a block window (approximately 10 minutes) exceeds the block size you can expect a miniature &quot;auction&quot; where transactions fight for space in the block by bidding up the minimum transaction fee needed to get in.  However this isn't really a closed-loop adjustment: the maximum blocksize is an arbitrarily chosen number, and &lt;strong&gt;there's no reason to believe the maximum blocksize is small enough to ensure that transaction fees are high enough to incent enough miners to mine to keep the system secure&lt;/strong&gt;.  Unlike the difficulty and the USD/BTC exchange rate it does not respond to market activity.  It also has the negative side effect of capping the worldwide Bitcoin transaction throughput since other parts of the protocol rely on the assumption that blocks are created -- in the long run -- no more than once every ten minutes.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;Compare this to the current situation with mining rewards: the more valuable a bitcoin is the more incentive there is for somebody to try to overwhelm the &quot;good guys&quot; by gaining 50%+1 hashpower.  However, the more valuable a bitcoin is the more miners will mine!  It isn't perfect, but &lt;strong&gt;the important point is that the demand for security increases the incentive to mine&lt;/strong&gt;.  Note that although the difficulty will go up, that simply ensures that the reward granted every ten minutes is an approximately constant number of BTC -- the number of terahashes/sec fighting over that amount of BTC is free to respond to changes in their changing value (as measured in terms of all other goods in the world, including other currencies).&lt;/p&gt;&#xA;&#xA;&lt;p&gt;&lt;strong&gt;As the mining reward is reduced this &quot;direct coupling&quot; between the network's need for security and the incentive to mine becomes progressively more diluted.&lt;/strong&gt;&lt;/p&gt;&#xA;&#xA;&lt;p&gt;I worry a lot about what will happen to Bitcoin once we decouple those two forces.  I think the developers ought to at least come up with a story on how this will be solved so people can start testing it.&lt;/p&gt;&#xA;


### From Top 3 answers

389   &lt;blockquote&gt;&#xA;  &lt;p&gt;&lt;strong&gt;TL;DR&lt;/strong&gt;: No. The argument is basically that hoarding will make Bitcoins so valuable that nobody will be willing to offer people enough to part with them. Does that pass the giggle test? Another way of stating the argument is this, &quot;If gold is $2,000/oz today but people think it will be $5,000/oz next year, nobody will trade any gold today.&quot; Again, think about it. Does that pass the giggle test either?&lt;/p&gt;&#xA;&lt;/blockquote&gt;&#xA;&#xA;&lt;p&gt;Hoarding increases the value of Bitcoins, increasing the profits from mining. This encourages more people to mine, increasing the total hashing power and thus the security of the system. &lt;/p&gt;&#xA;&#xA;&lt;p&gt;It also makes holding Bitcoins more profitable. This helps to encourage people to accept them in trade because they are less worried about them decreasing in value while they are holding them. Using Bitcoins as a currency inevitably means people sometimes have to hold them and having them drop in value while you hold them is a risk. Hoarding reduces this risk. But it also makes it harder to price things in Bitcoins because the value will tend to change more. Merchants don't like to change their prices twice a day.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;Contrary to claims, it should not affect the trading volume or the willingness of people to use Bitcoins to pay for things.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;The argument that increasing value means people would prefer to hold Bitcoins rather than spend them is specious. While it will make people want to have Bitcoins more, it will also make people want to convince others to give them Bitcoins more so they can have them.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;Think about it, do people prefer to pay for goods in dollars or garbage? By the reasoning of this argument, they should prefer to pay for goods in garbage, since they'd rather hold their dollars and get rid of their garbage. But, of course, people don't like paying in garbage because nobody &lt;em&gt;wants&lt;/em&gt; garbage. If you can pay with the currency others want, you can get a better deal. So you actually prefer to spend the currencies sellers most &lt;em&gt;want&lt;/em&gt;.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;If Bitcoins are valuable because inflation doesn't deprive them of value, then a merchant would rather get my Bitcoins than my dollars, so he'll accept fewer of them. This will cancel out the effect of me preferring to pay in dollars rather than Bitcoins. So it should be a wash.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;Or, put another way, whatever the present and future prospects, there should always be some equivalence between dollars and Bitcoins that people roughly agree on. So whether I pay X dollars or Y bitcoins, where X and Y are in this ratio, will purely depend on whether I prefer the characteristics of dollars or Bitcoins for the transaction.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;A consequence of this is that hoarding won't negatively affect the trading volume either because that's only dependent on people's use of Bitcoins to buy and sell things. If hoarding makes Bitcoins worth twice as much, only half as many will be used to buy and sell things and the volume (the total value traded) will be the same.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;I don't believe it's lost opportunity either. It's not like people who want to trade Bitcoins can't get them because they're all being hoarded. (Nor will it ever be likely to be an issue, since that would just raise the price and thus fewer would be needed. Bitcoins have effectively unlimited divisibility.)&lt;/p&gt;&#xA;&#xA;&lt;p&gt;So why do so many people think currency hoarding is bad? Because it &lt;em&gt;usually&lt;/em&gt; is, and empiric studies even show that it is. But the logic of why currency hoarding is bad doesn't apply to Bitcoins, especially when it's a minority currency.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;Bitcoins are different enough from physical fiat currencies that empirical studies don't apply unless the suspected mechanisms for the observed effects are believed to apply to Bitcoins too. For example, if a penny were enough money to buy a car, how useful would dollars be?&lt;/p&gt;&#xA;  

**The corresponding question was**

[384    &lt;p&gt;&lt;a href=&quot;https://www.technologyreview.com/computing/38392/?p1=featured&quot;&gt;Some people believe that hoarding hurts the Bitcoin economy&lt;/a&gt;.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;But are they really right?&lt;/p&gt;&#xA;&#xA;&lt;p&gt;As long as corresponding goods vendors and services will be here to stay and reinforce people's faith in Bitcoin, hoarded bitcoins simply do not take part in daily business and do not hurt anyone.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;Quite the contrary, they will &lt;em&gt;decrease&lt;/em&gt; the supply of bitcoins in active circulation, thus &lt;em&gt;increase&lt;/em&gt; the demand for bitcoins, and thus &lt;em&gt;raise&lt;/em&gt; their over-all value, right?&lt;/p&gt;&#xA;&#xA;&lt;p&gt;Update: This question also comes with a premise or insight that Bitcoin &quot;power users&quot; have savings and spendings wallets or similar setups, and that those two forms of wallets will not tend to &quot;compete&quot; with each other so much. The bitcoins in the spendings wallets will rather compete with the fiat money that respective users will use to buy for goods and services. The bitcoins in the savings wallets will rather compete with more traditional forms of assets and investments.&lt;/p&gt;&#xA;

# Further analysis

The code "newanalysis" is ordering users accoriding to the reputation field. We are including another code called "newmetric" in which we consider the following parameters for each answer (from the posts file)

* Length in characters of the "Body" text, so longer answers are presumably more detailed

* We give a positive score if the "Body" includes the word http, so presumably this user is doing a bit more of research on the subject by giving references  

* If the answer was accepted it counts as positive

* We consider the score of the answer=Up-Down votes

Each one of this fields has a maximum value of 1/4=.25. For example is an answer was accepted then the score is .25, if the "Body" contains "http" then it counts .25 more. For the fields Score and Length, we consider that a bigger "value" must represent a better "score". Hence these fields will have a value of (1-(1/value))/4. Then, we add these scores per answer and find the user associated to that answer and update his/her score. Our results with this new metric coincide with those using the reputation of the user in the first 9 places (for the Bitcoin data set)

In other words, the Id of the top 10 users (ascending order) using the "reputation" field are

[78, 5757, 575, 48884, 2306, 153, 323, 5406, 208, 85]

On the other hand, the top 10 users (ascending order) using our own metric are

[51948, 575, 323, 5757, 48884, 153, 2306, 85, 208, 5406]

Below is also the analysis of the prefered hours to response questions of top 3 users in the Bitcoin dataset


![preferenceuser1](https://user-images.githubusercontent.com/13289981/39914128-ed8e9be6-54b8-11e8-8954-6a7e2c92a0b0.png)
![preferenceuser2](https://user-images.githubusercontent.com/13289981/39914129-ef2b1330-54b8-11e8-8103-dede7bbcbc84.png)





# Further ideas

There is a lot more ot do with this data base including

* Analize the time for questions to be responded

* Find geographic clusters of top responders, as well as the most common ocupations/jobs

* Meta analize  the data sets to find top responders in different topics

* In the particular case of Bitcoins and Ethereum, it is possible to compare this graphs with historical data of stock prices from yahoo finance

