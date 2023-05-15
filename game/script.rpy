
define mc = Character("Me")

# Define the love level variable
default love = 0

# Define the character to be dated

define startup_guy = Character("SBF", color="#c8ffc8", image="startup_guy")
define cs_guy = Character("Brian", color="#c8ffc8", image="cs_guy")
define frat_bro = Character("Chad", color="#c8ffc8", image="frat_bro")

image startup_guy = "startup_guy.png"
image cs_guy = "cs_guy.png"
image frat_bro = "frat_bro.png"


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
    show startup_guy:
        zoom 1.5

    # Display the date dialogue
    mc "Hey there! So, you're all about startups and entrepreneurship, huh? Changing the world one app at a time?"
    startup_guy "Absolutely! I'm like the Elon Musk of dorm room innovations. The next big thing is just a pitch deck away!"
    mc "You know I think my rommate went on a date with you. Jim? I wonder where you were the night of his murder."
    startup_guy " Ah, the night of that incident. I was sad to hear about that. Well, here's the deal, I was actually rocking the startup scene at an ultra-exclusive conference. Top secret stuff! "
    menu:
        "Is there any way you can prove you were there? Any witnesses or photos?":
            startup_guy "Oh, I wish! Unfortunately, this event was like a covert mission—invite-only, no social media allowed. It was so secretive, they had a password just to use the bathroom. What I can share though is what my new startup is currently working on, which is really exciting!"
        "What was the conference for?": 
            startup_guy "Oh, I wish I could tell you! Unfortunately, this event was like a covert mission—invite-only, no social media allowed. It was so secretive, they had a password just to use the bathroom. What I can share though is what my new startup is currently working on, which is really exciting!"         
        "What kind of startup are you working on that you brought to the table there?":
            jump next_big_thing

    label next_big_thing:
        mc "So what’s your next big thing?"
        menu :
            "Picture this – 'AlibiAI' – the ultimate solution for concealing unsavory activities. It's a revolutionary app that helps you create foolproof alibis, no questions asked. AlibiAI is all about empowering individuals to control their narratives. It's not just for criminals, but for anyone who wants to maintain privacy, protect their reputation, or maybe even hide a harmless secret or two."
            "This sounds very suspicious…":
                startup_guy "Yes I know about the recent murder…but this is completely unrelated to that, I swear."
            "How would this even work?":
                startup "Simple. Users would input relevant details about their desired alibi—time, location, circumstances—and AlibiAI's advanced algorithms would generate a meticulously crafted narrative, backed by seemingly authentic evidence."
        



    # Display the ending
    startup_guy "Thanks for a great date! Let's do it again sometime."
    jump end

# Define the ending label
label end:

    # Display the ending dialogue based on the love level
    if love >= 1:
        mc "I had a really great time. Maybe we can go on another date soon."
    else:
        mc "I'm not sure I'm interested in dating Stereotype again, but I'm glad I gave it a try."

return 