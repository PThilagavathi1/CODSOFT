import re

def chatbot_response(user_input):
# Define chatbot rules using patterns and responses
    rules = [
        (r"hi|hello|hey", "Hello! How can I assist you?"),
        (r"bye|goodbye", "Goodbye! Take care!"),
        (r"your name", "I am RuleBot, your assistant."),
        (r"how are you", "I'm just a program, but I'm here to help!"),
        (r"what can you do", "I can answer simple questions based on my rules!"),
        (r"do you have a feeling?","No, I am just AI customer service."),
        (r"will chatgpt replace content creators?","No, ChatGPT won't replace content creators, but it can help them.It'his good at tasks like generating ideas, drafting, or improving SEO."),
        (r"how can i maintain a healthy diet?","To maintain a healthy diet, follow these simple tips:1. Eat a variety of foods: Include fruits, vegetables, whole grains, protein, and healthy fats in your meals."
         "2. Drink water :Stay hydrated and avoid sugary drinks."
         "3. Limit junk food :Cut down on processed snacks, sugary treats, and fried foods."
         "4. Watch portion sizes : Eat the right amount, not too much or too little!"
         "for further detailed visit google.com"),
         (r"what is meaning of life?","The one existence, thoughts,the surroundings. Philosophers, scientists,psychologists have different views on consciousness, but it  generally understood the subjective experience of the world, a mental state of awareness.On the other hand, What is the meaning of life? is a deeply philosophical question that has been explored for centuries by thinkers, religious leaders, and scientists. There is no universally agreed-upon answer, as the meaning of life can vary depending on cultural, spiritual, and personal beliefs. Some people find meaning in relationships, achievements, or helping others, while others seek purpose through spiritual or existential exploration. It is often viewed as a quest for personal fulfillment and understanding of one's role  the universe""Here are the books on the topics of the meaning of life:""How to create a Mind Throght Revealed"),
         (r"what is synonyms of breaking the ice?","Break the ice is an informal idiom that means to make people who have not met before feel more relaxed with each other. For example, someone might suggest playing a party game to break the ice."),
         (r"can you tell me roadmap for becoming the data analyst?","Here are some steps you can take to become a data analyst:Assess your interest and analytical ability: Make sure you're interested in the role and have the analytical skills to solve business problems with data. Learn the fundamentals: Familiarize yourself with the basics of data analysis. Take a structured course: Commit to a structured course to learn the skills you need. Develop soft skills: Work on improving your soft skills. Network: Start networking with other professionals in the field. Build a portfolio: Refine your portfolio and prepare for the job market. Learn programming languages: Data analysts use programming languages to automate tasks, perform advanced data manipulation, and solve complex problems. Gain experience with data visualization tools: Use tools like Tableau and Power BI to identify trends and patterns in large amounts of data. Practice technical skills: Prepare for interviews by practicing your technical skills and studying common interview questions. Demonstrate problem-solving abilities: Be able to show how you can solve problems during your interview. Data analysts use numerical and statistical data to create reports and visualizations to communicate their findings. They play a vital role in helping organizations improve their decision-making processe"),
         (r"how far technology go behind in 2050?","Technology in 2050 is expected to be integrated into everyday life, with artificial intelligence (AI), augmented reality (AR), and virtual reality (VR) becoming commonplace. Here are some predictions for how technology will be used in 2050: AI companions: AI systems will be indistinguishable from humans in terms of personality, emotion, and behavior. They will provide emotional support, companionship, and assistance in everyday tasks. Smart assistants: Smart assistants will be commonplace in the workplace.Immersive browsing: Browsing the web will be immersive with AR and VR, using voice commands, gestures, and brain-computer interfaces. Personalized content: Websites will offer personalized content. Brain implants: Brain implants might become common for accessing information. Volumetric displays: Holograms that could be used in advertising. Secure quantum internet: A quantum internet infrastructure that makes communications impossible to decrypt without disturbing the network. Wearable devices: Wearable devices like smartwatches, wristbands, and earbuds will be highly practical and fashionable. Microchipping: There will be a transition to more penetrative technology, such as microchipping, augmentations, and various other implants. Ocean thermal energy: Ocean thermal energy will play a crucial role in the future energy mix.")]
        
# Match user input with rules
    for pattern, response in rules:
        if re.search(pattern, user_input.lower()):
            return response
    
    return "Sorry, I didn't understand that."

# Chat loop
print("Chatbot: Hi!")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")

