"""
Skill to tell a story of the mentioed character

"""

from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome to Tell a Story"
    speech_output = "What story would like to hear? " \
                    "Please tell me your favorite princess name by saying, " \
                    "Tell me a story of Cinderella."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please tell me your favorite princess name by saying, " \
                    "my favorite Princess is Cinderella."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying Tell a Story app. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_favorite_character_attributes(favorite_character):
    return {"favoriteChracter": favorite_character}


def set_character_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'Princess' in intent['slots']:
        favorite_character = intent['slots']['Princess']['value']
        session_attributes = create_favorite_character_attributes(favorite_character)
        speech_output = "Story of " + \
                        favorite_character + \
                        get_Story(favorite_character)
                        
        reprompt_text = "You can ask a story of your favorite chracter saying, " \
                        "Tell me a Story of ?"+ favorite_character
    else:
        speech_output = "I'm not sure who is your favorite chratecter is. " \
                        "Please try again."
        reprompt_text = "I'm not sure who is your favorite chratecter is.  " \
                        "You can tell me your favorite color by saying, " \
                        "Please try again."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_Story(character):
    if character == "Cinderella":
        speech_out = "Once upon a time, there was a beautiful girl named Cinderella. She lived with her wicked stepmother and two stepsisters."\
                        "They treated Cinderella very badly. One day, they were invited for a grand ball in the kings palace."\
                        "But Cinderellas stepmother would not let her go. Cinderella was made to sew new party gowns for her stepmother and stepsisters," \
                        "and curl their hair. They then went to the ball, leaving Cinderella alone at home."\
                        "Cinderella felt very sad and began to cry. Suddenly, a fairy godmother appeared and said," \
                        "Dont cry, Cinderella I will send you to the ball But Cinderella was sad. She said," \
                        "I dont have a gown to wear for the ball. The fairy godmother waved her magic wand and changed Cinderellas old clothes into a beautiful new gown"\
                        "The fairy godmother then touched Cinderellas feet with the magic wand. And  She had beautiful glass slippers"\
                        "How will I go to the grand ball asked Cinderella. The fairy godmother found six mice playing near a pumpkin, in the kitchen."\
                        "She touched them with her magic wand and the mice became four shiny black horses and two coachmen and the pumpkin turned into a golden coach." \
                        "Cinderella was overjoyed and set off for the ball in the coach drawn by the six black horses." \
                        "Before leaving the fairy godmother said, Cinderella, this magic will only last until midnight."\
                        "You must reach home by then."\
                        "When Cinderella entered the palace, everybody was struck by her beauty. Nobody, not even Cinderellas stepmother or stepsisters," \
                        "knew who she really was in her pretty clothes and shoes. The handsome prince also saw her and fell in love with Cinderella. He went to her and asked," \
                        "Do you want to dance And Cinderella said, Yes The prince danced with her all night and nobody recognized the beautiful dancer." \
                        "Cinderella was so happy dancing with the prince that she almost forgot what the fairy godmother had said. At the last moment" \
                        "Cinderella remembered her fairy godmothers words and she rushed to go home." \
                        "Oh I must go, she cried and ran out of the palace. One of her glass slippers came off but Cinderella did not turn back for it." \
                        "She reached home just as the clock struck twelve. Her coach turned back into a pumpkin, the horses into mice and her fine ball gown into rags." \
                        "Her stepmother and stepsisters reached home shortly after that. They were talking about the beautiful lady who had been dancing with the prince."\
                        "The prince had fallen in love with Cinderella and wanted to find out who the beautiful girl was, but he did not even know her name."\
                        "He found the glass slipper that had come off Cinderellas foot as she ran home. The prince said, I will find her." \
                        "The lady whose foot fits this slipper will be the one I marry. The next day, the prince and his servants took the glass slipper and went to all the houses in the kingdom."\
                        "They wanted to find the lady whose feet would fit in the slipper." \
                        "All the women in the kingdom tried the slipper but it would not fit any of them. Cinderellas stepsisters also tried on the little glass slipper." \
                        "They tried to squeeze their feet and push hard into the slipper, but the servant was afraid the slipper would break." \
                        "Cinderellas stepmother would not let her try the slipper on, but the prince saw her and said, Let her also try on the slipper" \
                        "The slipper fit her perfectly. The prince recognized her from the ball. He married Cinderella and together they lived happily ever after."
                                            


    elif character == "Rapunzel":
        speech_out = "Once upon a time, there was a bad step mother and she had two daughters who are equally selfish and rude " \
                        "She had one beautiful step daughter, her name Cinderella"\
                        "One day, the Prince invited all the young ladies in the land to a royal ball,"\
                        "The two stepsisters gleefully planned their wardrobes for the ball, and taunted Cinderella by telling her that maids were not invited to the ball."    
    else:
        speech_out = "Once upon a time, there was a bad step mother and she had two daughters who are equally selfish and rude " \
                        "She had one beautiful step daughter, her name Cinderella"\
                        "One day, the Prince invited all the young ladies in the land to a royal ball,"\
                        "The two stepsisters gleefully planned their wardrobes for the ball, and taunted Cinderella by telling her that maids were not invited to the ball." 
    
    return speech_out
    
    
def get_color_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "You can say, my favorite color is red."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "TellStory":
        return set_character_in_session(intent, session)
    #elif intent_name == "WhatsMyColorIntent":
    #    return get_color_from_session(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
