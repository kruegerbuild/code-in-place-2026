from ai import call_gpt

'''
This is a simple generator for Haiku, a short Japanese poem
User will only be asked their name and desirable topic
Then GPT will create the haiku
'''

def main():
    user_name = input("Enter your name: ") #user input their name
    haiku_topic = input("Enter a topic: ") #user give generator a topic
    print("Creating your haiku...") #onboarding line
    response = call_gpt(f"Write a haiku based on the name: {user_name} and the topic: {haiku_topic}") #prompt
    print(response) #gpt's response will be printed because of the function


if __name__ == "__main__":
    main()