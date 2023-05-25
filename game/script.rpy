
define mc = Character("Me")

# Define the love level variable
default love = 0

# Define the character to be dated

define startup_girl = Character("SBF", color="#c8ffc8", image="startup_girl")
define cs_guy = Character("Brian", color="#c8ffc8", image="cs_guy")
define frat_bro = Character("Chad", color="#c8ffc8", image="frat_bro")

image startup_girl = "startup_girl.png"
image cs_guy = "cs_guy.png"
image frat_bro = "frat_bro.png"

image card = "card.jpeg"


# Define the starting label
label start:
    scene bg oval: 
        zoom 1.75

    # Display the introduction
    "It's a bright morning at Stanford University"

    # Display the date choice
    
    menu:
        "Who are you swiping on?"
        "Stanford start-up girl":
            jump start_up_date
        "Nerdy CS student":
            jump CS_guy_date
        "Frat bro":
            jump frat_bro_date


# Define the date label
label frat_bro_date:
    scene bg fountain: 
        zoom 3

    # Increment the love level
    $ love += 1
    show frat_bro:
        zoom 1.5

    # Display the date dialogue
    frat_bro "Hey, thanks for coming out with me! Let's go grab some food."

    # Display the food choice
    menu:
        "What would you like to eat?"
        "Pizza":
            frat_bro "Great choice! I love pizza too."
        "Sushi":
            frat_bro "I'm not a big fan of sushi, but I'll try it for you."
        "Burgers":
            frat_bro "Classic choice! I'll get the fries."

    # Display the ending
    frat_bro "Thanks for a great date! Let's do it again sometime."
    jump end

label CS_guy_date:
    scene bg coho: 
        zoom 0.75

    # Increment the love level
    $ love += 1
    show cs_guy:
        zoom 1.5

    # Display the date dialogue
    mc "Hey Brian! It’s great to meet you, excited to hang out with you!"
    cs_guy "Me too! I saw that your Hinge profile mentions that you’re a CS major! Talking about machine learning models really gets me going."

    # Display the food choice
    menu:
        "Look I know that we’re supposed to be on a date right now but I was hoping we could talk a bit more about my roommate Jim, who I know you went out on a date with.":
            cs_guy "Oh, I really liked Jim even though he wasn’t a CS major. Clearly, he wasn’t able to understand anything about my projects and any of my passions. Still, it was a shame to hear about the Lake Lag incident."
            menu: 
                "Where were you that night? Do you have any alibis or any evidence to back that up?":
                    cs_guy "I actually don’t but I was hanging out with my friend Brett before he said he had to go to Lake Lag for some Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa rush event."
                    cs_guy "After that, I was working by myself on one of my project’s – AlibiAI – code. That’s when the Jim murder happened, but I didn’t really take pictures of me coding or being in the room"
                    menu: 
                        "What rush event? Can you tell me more about Brett and Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa?":
                            cs_guy "Apparently the pledges were bringing potential dates to Lake Lag. That’s all I know. And Brett is a good friend of mine that I hang out with when I need to let loose after grinding on CS work and AlibiAI. But things have been weird lately, ever since he also started seeing Jim at the same time as me."
                            menu frat_guy_converge: 
                                "Oh that’s too bad. You’re probably a way better guy than Brett anyways, in my opinion, especially with what must be a cool project that you’re working on!":
                                    cs_guy "Oh, you’re too kind! But also you’re not wrong. Let me tell you more about AlibiAI. AlibiAI is an app that uses AI to help you create foolproof alibis using relevant details that you input."
                                    cs_guy "Brett was actually the one who really encouraged me to build it when I told him about it too. I can give you the access key to the beta demo if you want?"
                                    show card:
                                        xalign 0.5 yalign 0.4
                                    cs_guy "Oh shoot wrong card."
                                    cs_guy "Sorry I've got to head out really quick. Just remembered I have section. Bye!"
                                    jump start
                                "Can I get Brett’s number?":
                                    cs_guy "Really? After what I just said about things being weird because of a mutual love interest? No, I won’t give you his number. In fact, I’m gonna have to ask you to leave."
                                    "Sorry for the trouble!"
                                    jump start
                                "Can you tell me more about AlibiAI?":
                                    cs_guy "That’s a personal project that I’ve been working on ever since Andrew Ng told me that it would be a cool idea to look into. AlibiAI is an app that uses AI to help you create foolproof alibis using relevant details that you input."
                                    cs_guy "I personally thought it was a bit weird when he first told me about the idea, but I talked to my friend Brett about it, and he really strongly encouraged me to pursue it and implement it."
                                    menu more_alibi_ai: 
                                        "That sounds like a really cool project! It sounds like a very technically challenging engineering problem, so it’s so cool to see that you’re smart enough to tackle it.":
                                            cs_guy "Oh, you’re too kind! But also you’re not wrong. Let me tell you more about AlibiAI. AlibiAI is an app that uses AI to help you create foolproof alibis using relevant details that you input."
                                            cs_guy "Brett was actually the one who really encouraged me to build it when I told him about it too. I can give you the access key to the beta demo if you want?"
                                            show card:
                                                xalign 0.5 yalign 0.4
                                            cs_guy "Oh shoot wrong card."
                                            cs_guy "Sorry I've got to head out really quick. Just remembered I have section. Bye!"
                                            jump start
                                        "Why did Brett encourage you so much to build AlibiAI?":
                                            cs_guy "Honestly, I’m not really sure why. But it did seem like it might be because he really wanted to use it for himself. But that’s all I’ll say. Anyways, I gotta get going. Gotta keep working on my project. See you later! "
                                            jump start
                "What did you guys talk about? How did your date go with Jim?":
                    cs_guy "I tried explaining my projects to Jim, like for example my project AlibiAI, but he really didn’t understand what I was talking about. That’s when I knew that things between us weren’t going to work out."
                    cs_guy "Also, he was clearly more into my friend Brett and mentioned his name multiple times during our date. He even told me that they were supposed to meet up later somewhere. Since then, things between Brett and I have been a little weird, but I guess that’s not that important."
                    jump frat_guy_converge
        "Yes, I’d love to chat about your projects and what kind of research you’re doing! It’s so cool to connect with someone who is interested in the same things as me!":
            cs_guy "Oh yeah I would love to tell you all about the amazing things that I’ve been working on. It’s really setting me up for success for my Stanford CS PhD applications. I’m currently working in 2 labs! I’m working in Andrew Ng’s lab – which is super prestigious to get into – and I’m working on a personal project called AlibiAI."
            menu: 
                "Wow that's so cool! Can you tell me more about AlibiAI?":
                    cs_guy "That’s a personal project that I’ve been working on ever since Andrew Ng told me that it would be a cool idea to look into. AlibiAI is an app that uses AI to help you create foolproof alibis using relevant details that you input."
                    cs_guy "I personally thought it was a bit weird when he first told me about the idea, but I talked to my friend Brett about it, and he really strongly encouraged me to pursue it and implement it."
                    jump more_alibi_ai
                "I’d love to hear more about what you do outside of work though!":
                    cs_guy "Hmm let’s see…outside of work, sometimes I really need to let loose and I go hang out with some of my friends in Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa."
                    cs_guy " I’m really close to Brett actually who is in the frat, and he was the one who strongly encouraged me to pursue implementing the tech for AlibiAI, the project I mentioned earlier. But things got a bit weird between us when I heard he was also seeing Jim."
                    jump frat_guy_converge

label start_up_date:
    scene bg coupa: 
        zoom 3

    # Increment the love level
    $ love += 1
    show startup_girl:
        zoom 1.5

    # Display the date dialogue
    mc "Hey there! So, you're all about startups and entrepreneurship, huh? Changing the world one app at a time?"
    startup_girl "Absolutely! I'm like the Elon Musk of dorm room innovations. The next big thing is just a pitch deck away!"
    menu: 
        "Let’s get down to business. I know I called you here for a date, but I’m here to investigate the details of the murder of my roommate Jim, who I know you were seeing. Where were you on the night when Jim was murdered at Lake Lag?":
            label down_to_business:
                startup_girl " Ah, the night of that incident. I was sad to hear about that. Well, here's the deal, I was actually rocking the startup scene at an ultra-exclusive conference. Top secret stuff! "
                menu:
                    "Is there any way you can prove you were there? Any witnesses or photos?":
                        startup_girl "Oh, I wish! Unfortunately, this event was like a covert mission—invite-only, no social media allowed. It was so secretive, they had a password just to use the bathroom. What I can share though is what my new startup is currently working on, which is really exciting!"
                        menu: 
                            "Sigh…okay, what’s your startup idea?":
                                jump next_big_thing
                            "No, I don’t really care. What I really want to know is proof that you really were at this “conference” on that night.":
                                startup_girl " I swear, it’ll only take a second to pitch it to you! Okay, picture this —"
                                jump next_big_thing
                    "What was the conference for?": 
                        startup_girl "Oh, I wish I could tell you! Unfortunately, this event was like a covert mission—invite-only, no social media allowed. It was so secretive, they had a password just to use the bathroom. What I can share though is what my new startup is currently working on, which is really exciting!"         
                        menu: 
                            "Sigh…okay, what’s your startup idea?":
                                jump next_big_thing
                            "No, I don’t really care. What I really want to know is proof that you really were at this “conference” on that night.":
                                startup_girl " I swear, it’ll only take a second to pitch it to you! Okay, picture this —"
                                jump next_big_thing
                    "What kind of startup are you working on that you brought to the table there?":
                        jump next_big_thing

        "So what’s your next big thing?":
            label next_big_thing:
                startup_girl "'AlibiAI' – the ultimate solution for concealing unsavory activities. It's a revolutionary app that helps you create foolproof alibis, no questions asked."
                startup_girl "AlibiAI is all about empowering individuals to control their narratives. It's not just for criminals, but for anyone who wants to maintain privacy, protect their reputation, or maybe even hide a harmless secret or two."

                menu :
                    "This sounds very suspicious…":
                        startup_girl "Yes I know about the recent murder…but this is completely unrelated to that, I swear. I’m only working on this because my colleague Brian suggested the idea to me and wanted my help on the business side of things."
                        "{i}You remember that Brian was also one of Jim's romantic interests that you thought of as a possible suspect.{/i}"
                        menu: 
                            "Brian? Can you tell me more about him?":
                                startup_girl "I honestly don't really know anything about the guy. I swear. Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"
                                jump start
                            "Brian? Are you aware that he was seeing Jim, the person who was murdered at Lake Lag recently?":
                                startup_girl "I honestly don't really know anything about the guy. I swear. Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"
                                jump start

                    "How would this even work?":
                        startup_girl "Simple. Users would input relevant details about their desired alibi—time, location, circumstances—and AlibiAI's advanced algorithms would generate a meticulously crafted narrative, backed by seemingly authentic evidence."
                        startup_girl "We'd offer different package tiers, from basic cover-ups to deluxe setups that include tailored social media posts and forged documents. Unsure how the technology works - I’m on the business side of things, but you can email my colleague Brian who came to me with the idea and wanted my help on the business side of things while he codes it."
                        "{i}You remember that Brian was also one of Jim's romantic interests that you thought of as a possible suspect.{/i}"
                        menu: 
                            "Brian? Can you tell me more about him?":
                                startup_girl "I honestly don't really know anything about the guy. I swear."
                                startup_girl "Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"                                
                                jump start
                            "Brian? Are you aware that he was seeing Jim, the person who was murdered at Lake Lag recently?":
                                startup_girl "I honestly don't really know anything about the guy. I swear."
                                startup_girl "Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"                               
                                jump start
                            "This sounds like a really cool idea! It’s honestly so impressive how you’re spearheading the business side of things!":
                                show card:
                                    xalign 0.5 yalign 0.4
                                startup_girl "Thanks so much! It’s cool to see that it seems like an exciting project to you too! Here, I gotta get going, but let me give you my business card so we can chat more later. Would love to grab a meal sometime!"
                                jump start

                    "Is this your own original idea?":
                        startup_girl "I mean…depends on how you define “original”. It is my idea now too, since I’m working on the business side of things as the COO, but I will admit that my colleague Brian did suggest the idea to me originally because he wanted my help."
                        "{i}You remember that Brian was also one of Jim's romantic interests that you thought of as a possible suspect.{/i}"
                        menu: 
                            "Brian? Can you tell me more about him?":
                                startup_girl "I honestly don't really know anything about the guy. I swear."
                                startup_girl "Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"                                
                                jump start
                            "Brian? Are you aware that he was seeing Jim, the person who was murdered at Lake Lag recently?":
                                startup_girl "I honestly don't really know anything about the guy. I swear."
                                startup_girl "Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"
                                jump start
                            "This sounds like a really cool idea! It’s honestly so impressive how you’re spearheading the business side of things!":
                                show card:
                                    xalign 0.5 yalign 0.4
                                startup_girl "Thanks so much! It’s cool to see that it seems like an exciting project to you too! Here, I gotta get going, but let me give you my business card so we can chat more later. Would love to grab a meal sometime!"
                                jump start
        "Wow, you look like you’d be really good at rock climbing. Want to go with me some time?":
            startup_girl "Rock climbing! You know, I have a bit of a reputation in climbing circles. They call me the Spider. As much as I would love to though, I unfortunately won’t be able to. I’ve had my hands really full recently, so I really don’t have much free time these days. You know, other than for quick casual dates like this."
            menu:
                "What’s got you so busy?":
                    jump next_big_thing
                "I was making fun of you. I don’t even like rock climbing. What I really want to know is that you were doing on the night that my roommate Jim was murdered!":
                    jump down_to_business
        



    # Display the ending
    startup_girl "Thanks for a great date! Let's do it again sometime."
    jump end

# Define the ending label
label end:

    # Display the ending dialogue based on the love level
    if love >= 1:
        mc "I had a really great time. Maybe we can go on another date soon."
    else:
        mc "I'm not sure I'm interested in dating Stereotype again, but I'm glad I gave it a try."

return 