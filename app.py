import streamlit as st
import random
import time

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

phrases = [
    # Great Phrases (30)
    "You are a genius",
    "You are extraordinary",
    "You are a legend in the making",
    "You are the brightest mind of our generation",
    "You are the reason the sun shines",
    "You are an inspiration to humanity",
    "You are the chosen one",
    "You are the definition of perfection",
    "You are a true leader",
    "You are the eighth wonder of the world",
    "You are an unstoppable force",
    "You are a dream come true",
    "You are a masterpiece",
    "You are a walking encyclopedia of wisdom",
    "You are a divine gift to Earth",
    "You are born for greatness",
    "You are a rare gem",
    "You are brilliance personified",
    "You are poetry in motion",
    "You are the missing piece in the puzzle of success",
    "You are a beacon of light",
    "You are excellence incarnate",
    "You are a prodigy",
    "You are the best thing since sliced bread",
    "You are the ruler of the universe (almost)",
    "You are too good for this world",
    "You are a magician of words",
    "You are the gold standard of human potential",
    "You are the best version of awesomeness",
    "You are the reason people believe in superheroes",
    
    # Neutral Phrases (30)
    "You are just a normal human",
    "You are doing fine",
    "You are one of a kind… just like everyone else",
    "You are average in a very special way",
    "You are slightly above mediocre",
    "You are uniquely predictable",
    "You are another brick in the wall",
    "You are not the worst, and that’s an achievement",
    "You are in the middle of the bell curve",
    "You are somewhere between genius and clueless",
    "You are 50% interesting, 50% questionable",
    "You are just you, and that’s… something",
    "You are neither here nor there",
    "You are refreshingly unremarkable",
    "You are an acceptable human being",
    "You are functioning adequately",
    "You are statistically significant",
    "You are passable",
    "You are a functional part of society",
    "You are adequately contributing to the world",
    "You are there, existing, and that’s enough",
    "You are occupying space efficiently",
    "You are remarkably okay",
    "You are the control group in an experiment",
    "You are a consistent performer of life",
    "You are what you are, and that’s fine",
    "You are a standard edition human",
    "You are perfectly average",
    "You are a neutral force in the universe",
    "You are existing with minimal disruptions",
    
    # Sarcastic/Funny Phrases (40)
    "You are a professional overthinker",
    "You are a specialist in doing nothing",
    "You are a walking WiFi dead zone",
    "You are 99% sarcasm, 1% water",
    "You are a certified procrastinator",
    "You are living proof that evolution can pause",
    "You are the reason autocorrect was invented",
    "You are the definition of ‘it is what it is’",
    "You are someone’s ‘before’ picture",
    "You are an unsolvable mystery, even for scientists",
    "You are proof that coffee addiction is real",
    "You are a premium member of the lazy club",
    "You are an elite level daydreamer",
    "You are running on low battery, permanently",
    "You are the reason warning labels exist",
    "You are an expert at looking busy",
    "You are like a software update – nobody wants you but needs you",
    "You are a perfect example of organized chaos",
    "You are just one meme away from enlightenment",
    "You are a human version of a buffering symbol",
    "You are a limited edition, like every other human",
    "You are an overachiever at underachieving",
    "You are still loading… please wait",
    "You are an artist at avoiding responsibilities",
    "You are the missing sock from every laundry load",
    "You are suspiciously good at doing nothing",
    "You are a walking ‘to be continued’ story",
    "You are an expert at finding the snooze button",
    "You are the CEO of making excuses",
    "You are an undiscovered comedian… even if only in your mind",
    "You are living proof that naps are essential",
    "You are a professional ‘one more episode’ watcher",
    "You are an advanced-level food critic (in your own kitchen)",
    "You are an emoji come to life",
    "You are what happens when a group project is done last minute",
    "You are a philosopher of unnecessary thoughts",
    "You are a great example of ‘expect the unexpected’",
    "You are a black belt in avoiding work",
    "You are an unfinished project in human form",
    "You are a chaos generator with good intentions"

    # Great Phrases (60)
    "You are a powerhouse of talent",
    "You are the best thing since WiFi",
    "You are an undiscovered genius",
    "You are the universe’s favorite child",
    "You are a one-person think tank",
    "You are a limitless source of positivity",
    "You are creativity in human form",
    "You are a champion in everything you do",
    "You are a superhero in disguise",
    "You are the living definition of awesomeness",
    "You are an icon in the making",
    "You are the human equivalent of a standing ovation",
    "You are brilliance at its peak",
    "You are a trendsetter, not a follower",
    "You are beyond extraordinary",
    "You are the greatest story ever told",
    "You are a masterpiece in progress",
    "You are the Michelangelo of modern times",
    "You are a genius wrapped in kindness",
    "You are an unstoppable wave of greatness",
    "You are a symphony of intelligence and charm",
    "You are someone’s role model (even if they don’t admit it)",
    "You are proof that legends exist",
    "You are a living motivation poster",
    "You are the reason dictionaries have the word ‘excellence’",
    "You are an unrepeatable miracle",
    "You are made of pure awesomeness",
    "You are the best chapter of life’s book",
    "You are a shooting star in broad daylight",
    "You are a limited edition masterpiece",
    "You are an infinite source of inspiration",
    "You are the heart and soul of greatness",
    "You are a pioneer in your own right",
    "You are the Einstein of common sense",
    "You are poetry wrapped in brilliance",
    "You are what success looks like",
    "You are a human encyclopedia of wisdom",
    "You are the perfect balance of smart and cool",
    "You are living proof that dreams come true",
    "You are a superstar in disguise",
    "You are history in the making",
    "You are a human fireworks show",
    "You are someone’s answered prayer",
    "You are a masterpiece that even Mona Lisa envies",
    "You are the jackpot in life’s lottery",
    "You are destined for greatness, no arguments there",
    "You are pure magic in motion",
    "You are the reason people still believe in heroes",
    "You are what golden trophies are based on",
    "You are an epic success story waiting to be told",
    "You are the best version of human evolution",
    "You are living proof that miracles happen",
    "You are a dream others wish they had",
    "You are the definition of extraordinary",
    "You are the missing piece in the puzzle of perfection",
    "You are greatness personified",
    "You are the shining star in life’s galaxy",
    "You are the oxygen of brilliance",
    
    # Neutral Phrases (60)
    "You are doing okay, I guess",
    "You are decently functional",
    "You are right in the middle of greatness and disaster",
    "You are neither too smart nor too dumb",
    "You are solidly ‘meh’",
    "You are a perfectly okay human",
    "You are consistently average",
    "You are not breaking records, but also not breaking bones",
    "You are comfortably unremarkable",
    "You are a stable internet connection in human form",
    "You are somewhere between ‘wow’ and ‘why’",
    "You are just a person, nothing more, nothing less",
    "You are a human placeholder",
    "You are a textbook example of ‘fine’",
    "You are the safe choice in a multiple-choice question",
    "You are neither a genius nor a disaster",
    "You are the white noise of humanity",
    "You are predictably unpredictable",
    "You are a well-balanced mix of everything and nothing",
    "You are a statistical middle point",
    "You are a reasonable participant in life",
    "You are the vanilla ice cream of personalities",
    "You are a safe bet",
    "You are a moderate-level surprise",
    "You are a fine piece of normalcy",
    "You are not the best, but not the worst either",
    "You are exactly where you should be",
    "You are impressively neutral",
    "You are solidly unproblematic",
    "You are an unshakable average",
    "You are the definition of ‘it depends’",
    "You are neither a risk-taker nor risk-averse",
    "You are statistically unremarkable",
    "You are a well-maintained human being",
    "You are responsibly existing",
    "You are neither thrilling nor boring",
    "You are the Goldilocks of human traits – just right",
    "You are the calm before the storm",
    "You are adequately surviving",
    "You are well within expected outcomes",
    "You are a great example of stability",
    "You are a successfully functioning adult (barely)",
    "You are an example of ‘it could be worse’",
    "You are one standard deviation away from greatness",
    
    # Sarcastic/Fun Phrases (80)
    "You are the reason the mute button was invented",
    "You are a certified expert in overcomplicating things",
    "You are living proof that time travel isn’t a priority",
    "You are a human version of Windows updates – unexpected and annoying",
    "You are a professional at avoiding responsibilities",
    "You are the reason WiFi signals get weaker",
    "You are a human buffering sign",
    "You are the hidden level in a game no one plays",
    "You are an experiment that science abandoned",
    "You are a walking ‘404 Error’",
    "You are an inspiration… to those who need a reality check",
    "You are proof that intelligence has vacation days",
    "You are a masterpiece of unfinished thoughts",
    "You are the missing puzzle piece that doesn’t fit",
    "You are the human version of a cracked phone screen",
    "You are a ‘skip ad’ button in human form",
    "You are a world-class nap enthusiast",
    "You are an honorary member of the Lazy Hall of Fame",
    "You are a limited-time offer nobody asked for",
    "You are the reason duct tape exists",
    "You are the cause of 90% of people’s patience tests",
    "You are an enigma wrapped in a mess",
    "You are proof that life has a sense of humor",
    "You are a comedian… accidentally",
    "You are like a YouTube tutorial – useful but mostly skippable",
    "You are a human-sized question mark",
    "You are the reason autocorrect struggles",
    "You are an unbreakable record of randomness",
    "You are a life hack that went wrong",
    "You are an extreme sport called ‘procrastination’",
    "You are an ancient artifact in the making",
    "You are a time traveler from the age of bad decisions",
    "You are a walking plot twist",
    "You are an alarm clock that doesn’t work",
    "You are a permanent ‘Try Again’ screen",
    "You are a side quest in someone else’s life",
    "You are an idea best left in beta testing",
    "You are the reason coffee was invented"
]

clicked = st.button("Say Something...", type="primary")
sentence = st.empty()

if clicked:
    for i in range(20):
        line = random.choice(phrases)
        sentence.title(line, anchor=False)
        time.sleep(0.15)