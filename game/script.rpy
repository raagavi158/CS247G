
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
        "Stanford start-up guy":
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
    mc "It’s great to meet you, excited to hang out with you!"
    cs_guy "Me too! I saw that your Hinge profile mentions that you’re a CS major! Talking about machine learning models really gets me going."

    # Display the food choice
    menu:
        "I know I called you here for a date, but I’m here to investigate the murder of my roommate Jim, who you were seeing. Where were you on the night when Jim was murdered at Lake Lag?":
            cs_guy "Cool."
        "So what’s your next big thing?":
            cs_guy "Cool."
        "Wow, you look like you’d be really good at rock climbing. Want to go with me some time?":
            cs_guy "Cool."

    # Display the ending
    cs_guy "Thanks for a great date! Let's do it again sometime."
    jump end

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
                        startup_girl "Yes I know about the recent murder…but this is completely unrelated to that, I swear. I’m only working on this because my colleague <CS nerdy guy> suggested the idea to me and wanted my help on the business side of things."
                        "{i}You remember that 'CS nerdy guy' was also one of Jim's romantic interests that you thought of as a possible suspect.{/i}"
                        menu: 
                            "CS nerdy guy? Can you tell me more about him?":
                                startup_girl "I honestly don't really know anything about the guy. I swear. Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"
                                jump start
                            "CS nerdy guy? Are you aware that he was seeing Jim, the person who was murdered at Lake Lag recently?":
                                startup_girl "I honestly don't really know anything about the guy. I swear. Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"
                                jump start

                    "How would this even work?":
                        startup_girl "Simple. Users would input relevant details about their desired alibi—time, location, circumstances—and AlibiAI's advanced algorithms would generate a meticulously crafted narrative, backed by seemingly authentic evidence."
                        startup_girl "We'd offer different package tiers, from basic cover-ups to deluxe setups that include tailored social media posts and forged documents. Unsure how the technology works - I’m on the business side of things, but you can email my colleague <CS nerdy guy> who came to me with the idea and wanted my help on the business side of things while he codes it."
                        "{i}You remember that 'CS nerdy guy' was also one of Jim's romantic interests that you thought of as a possible suspect.{/i}"
                        menu: 
                            "CS nerdy guy? Can you tell me more about him?":
                                startup_girl "I honestly don't really know anything about the guy. I swear."
                                startup_girl "Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"                                
                                jump start
                            "CS nerdy guy? Are you aware that he was seeing Jim, the person who was murdered at Lake Lag recently?":
                                startup_girl "I honestly don't really know anything about the guy. I swear."
                                startup_girl "Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"                               
                                jump start
                            "This sounds like a really cool idea! It’s honestly so impressive how you’re spearheading the business side of things!":
                                show card:
                                    xalign 0.5 yalign 0.4
                                startup_girl "Thanks so much! It’s cool to see that it seems like an exciting project to you too! Here, I gotta get going, but let me give you my business card so we can chat more later. Would love to grab a meal sometime!"
                                jump start

                    "Is this your own original idea?":
                        startup_girl "I mean…depends on how you define “original”. It is my idea now too, since I’m working on the business side of things as the COO, but I will admit that my colleague <CS nerdy guy> did suggest the idea to me originally because he wanted my help."
                        "{i}You remember that 'CS nerdy guy' was also one of Jim's romantic interests that you thought of as a possible suspect.{/i}"
                        menu: 
                            "CS nerdy guy? Can you tell me more about him?":
                                startup_girl "I honestly don't really know anything about the guy. I swear."
                                startup_girl "Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"                                
                                jump start
                            "CS nerdy guy? Are you aware that he was seeing Jim, the person who was murdered at Lake Lag recently?":
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