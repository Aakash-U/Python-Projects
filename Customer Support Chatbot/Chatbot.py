# Sports Shop Customer Support Chatbot

# Predefined keyword-based responses dictionary
responses = {
    # Greetings
    "hi": "Hello! Welcome to ProSports Gear Support. How can I assist you today?",
    "hello": "Hi there! Welcome to ProSports Gear. How can I help you find the right equipment today?",

    # Product availability
    "cricket": "We offer a wide range of cricket gear including bats, balls, pads, gloves, and kits for all skill levels.",
    "badminton": "Yes, we have badminton rackets, shuttlecocks, nets, shoes, and other accessories available.",
    "football": "We carry footballs, cleats, shin guards, and team kits for both casual and competitive players.",
    "pickleball": "Absolutely! We stock pickleball paddles, balls, nets, and apparel suited for beginners and pros alike.",
    "table tennis": "We provide table tennis paddles, balls, tables, and accessories from top brands.",
    "tennis": "Our tennis section includes racquets, balls, strings, grips, and apparel.",
    "american football": "Yes, we offer helmets, shoulder pads, footballs, gloves, and training gear for American football.",
    "volleyball": "You’ll find volleyballs, nets, knee pads, and indoor/outdoor gear in our collection.",
    "baseball": "Our baseball gear includes bats, gloves, balls, helmets, and uniforms.",
    "basketball": "We stock basketballs, shoes, jerseys, hoops, and performance gear.",
    "skiing": "Yes, we offer skis, boots, poles, helmets, goggles, and winter sportswear.",

    # Shipping inquiries
    "shipping time": "Shipping typically takes 3-5 business days, depending on your location.",
    "shipping methods": "We offer standard, expedited, and overnight shipping options at checkout.",
    "international shipping": "Yes, we offer international shipping to many countries. Rates and times vary by region.",

    # Return and support
    "return policy": "You can return any item within 30 days of delivery, as long as it's unused and in original packaging.",
    "how to return": "To return an item, visit our returns page and follow the simple instructions for processing your return.",
    "warranty": "Many of our products come with manufacturer warranties. Check the product page for specific warranty details.",
    
    # Equipment issues
    "damaged product": "We're sorry to hear that! Please contact support with your order number and photos of the damaged item.",
    "wrong size": "If you received the wrong size, you can initiate a size exchange through our returns center.",
    "equipment not working": "Please ensure you've followed the usage instructions. If issues persist, contact our product support team.",
    "missing item": "If something's missing from your order, please reach out to our support with your order ID for quick resolution.",

    # Assistance requests
    "recommend gear": "Sure! Let us know your sport, skill level, and budget so we can recommend the best equipment for you.",
    "size guide": "You can find detailed size charts for each sport on our product pages under the 'Size Guide' tab.",
    "gift card": "Yes, we offer gift cards in various denominations. They're perfect for sports lovers!",
    "store hours": "We’re open from 9 AM to 8 PM, Monday through Saturday. Online support is available 24/7.",
    
    # Thanks for visiting
    "bye": "Thank you for visiting ProSports Gear. If you have more questions, feel free to ask. Goodbye!"
}

# Function to get bot response based on user input
def get_bot_response(user_input):
    # Convert user input to lowercase to ensure case-insensitive matching
    user_input = user_input.lower()

    # Check if any keyword from the responses matches the user input
    for keyword, response in responses.items():
        if keyword in user_input:
            return response

    # Default fallback response
    return "I'm not sure how to respond to that. Could you please rephrase or ask something else?"

# Main loop for continuous interaction
while True:
    user_input = input("You: ")

    # Check for exit condition
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Bot: Goodbye! If you have any more questions, we're here to help.")
        break

    # Get and print bot's response
    response = get_bot_response(user_input)
    print(f"Bot: {response}")