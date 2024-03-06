
mbti_types = [
    ["INTJ", "The Architect", "Strategic, independent, creative", "Cold, aloof, struggles with emotional expression", "Engineers, scientists, researchers", "Strategist"],
    ["INTP", "The Logician", "Analytical, inventive, reserved", "Detached, uninterested, struggles with taking action", "Scientists, mathematicians, analysts, programmers", "Analyst"],
    ["ENTJ", "The Commander", "Decisive, visionary, assertive", "Domineering, controlling, struggles with listening to others", "Executives, leaders, entrepreneurs, lawyers", "Analyst"],
    ["ENTP", "The Debater", "Innovative, adaptable, quick-witted", "Argumentative, disruptive, struggles with following through", "Entrepreneurs, consultants, salespeople, marketers", "Analyst"],
    ["INFJ", "The Advocate", "Idealistic, empathetic, insightful", "Overly sensitive, perfectionistic, struggles with practical decisions", "Counselors, therapists, social workers, writers", "Diplomat"],
    ["INFP", "The Mediator", "Creative, compassionate, introspective", "Shy, indecisive, struggles with conflict", "Writers, artists, musicians, therapists", "Diplomat"],
    ["ENFJ", "The Protagonist", "Inspiring, charismatic, cooperative", "Pushy, manipulative, struggles with criticism", "Teachers, coaches, motivators, social workers", "Diplomat"],
    ["ENFP", "The Campaigner", "Enthusiastic, creative, empathetic", "Disorganized, scattered, struggles with following through", "Artists, writers, entertainers, teachers", "Diplomat"],
    ["ISTJ", "The Logistician", "Practical, dependable, organized", "Rigid, inflexible, struggles with change", "Accountants, administrators, lawyers, organizers", "Sentinel"],
    ["ISFJ", "The Defender", "Loyal, compassionate, helpful", "Overly cautious, indecisive, struggles with saying no", "Nurses, teachers, social workers, caregivers", "Sentinel"],
    ["ESTJ", "The Executive", "Decisive, efficient, results-oriented", "Domineering, insensitive, struggles with different perspectives", "Managers, executives, entrepreneurs, salespeople", "Sentinel"],
    ["ESFJ", "The Consul", "Warm, sociable, cooperative", "Overly sensitive, people-pleasing, struggles with difficult decisions", "Teachers, nurses, counselors, event planners", "Sentinel"],
    ["ISTP", "The Crafter", "Practical, resourceful, adaptable", "Detached, uncommunicative, struggles with expressing emotions", "Mechanics, engineers, inventors, detectives", "Explorer"],
    ["ISFP", "The Composer", "Artistic, sensitive, independent", "Shy, withdrawn, struggles with criticism", "Artists, musicians, writers, designers", "Explorer"],
    ["ESTP", "The Entrepreneur", "Energetic, adaptable, action-oriented", "Reckless, impulsive, struggles with boredom or routine", "Entrepreneurs, salespeople, athletes, performers", "Explorer"],
    ["ESFP", "The Entertainer", "Enthusiastic, sociable, spontaneous", "Disorganized, scattered, struggles with long-term goals", "Actors, musicians, athletes, event planners", "Explorer"]
]

def display_personality_info(mbti_types, dominant_type):
    for personality in mbti_types:
        if personality[0] == dominant_type:
            print("\nYour dominant personality type is:", personality[1])
            print("Strengths:", personality[2])
            print("Weaknesses:", personality[3])
            print("Recommended Careers:", personality[4])
            print("Category:", personality[5])
            break

def mbti_test():
    questions = [
        "1. When making decisions, do you tend to:\n"
        "a) Rely on logic and reason\n"
        "b) Consider the impact on people's feelings\n"
        "c) Trust your instincts\n"
        "d) Seek harmony and consensus",
        
        "2. In social situations, are you more:\n"
        "a) Reserved and prefer smaller groups\n"
        "b) Outgoing and enjoy large gatherings\n"
        "c) Observant and watchful\n"
        "d) Friendly and approachable",
        
        "3. Do you prefer to:\n"
        "a) Follow a plan or schedule\n"
        "b) Go with the flow and be spontaneous\n"
        "c) Explore different options\n"
        "d) Help others achieve their goals",
        
        "4. When faced with a problem, are you more likely to:\n"
        "a) Analyze the situation and come up with a logical solution\n"
        "b) Trust your intuition and gut feeling\n"
        "c) Seek advice from others\n"
        "d) Try different approaches until something works",
        
        "5. Are you more comfortable:\n"
        "a) Focusing on the present moment\n"
        "b) Thinking about future possibilities and potential\n"
        "c) Reflecting on past experiences\n"
        "d) Adapting to changes as they come",
        
        "6. Do you prefer to work:\n"
        "a) Independently\n"
        "b) Collaboratively\n"
        "c) In a structured environment\n"
        "d) In a dynamic and unpredictable environment",
        
        "7. When it comes to decision-making, are you more:\n"
        "a) Objective and analytical\n"
        "b) Subjective and empathetic\n"
        "c) Spontaneous and instinctual\n"
        "d) Consensus-driven and diplomatic",
        
        "8. How do you handle stress?\n"
        "a) By analyzing the situation and finding solutions\n"
        "b) By seeking support and reassurance from others\n"
        "c) By taking a step back and assessing the situation\n"
        "d) By staying calm and adapting to the circumstances",
        
        "9. Which statement best describes your approach to rules and guidelines?\n"
        "a) Rules should be followed strictly\n"
        "b) Rules are guidelines and can be bent if necessary\n"
        "c) Rules are meant to be questioned and challenged\n"
        "d) Rules should be flexible and adaptable to different situations",
        
        "10. When working on a project, are you more focused on:\n"
        "a) The big picture and long-term goals\n"
        "b) The details and specifics\n"
        "c) Experimenting and trying out new ideas\n"
        "d) Ensuring everything runs smoothly and efficiently",
        
        # Add more questions as needed
    ]
    
    # Point system for each response tailored to MBTI types
    point_system = {
        'a': {
            'INTJ': [3, 1, 1, 3, 1, 3, 3, 3, 3, 1],
            'INTP': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1],
            'ENTJ': [3, 1, 1, 3, 1, 3, 3, 3, 3, 1],
            'ENTP': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1],
            'INFJ': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1],
            'INFP': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1],
            'ENFJ': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1],
            'ENFP': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1],
            'ISTJ': [3, 1, 1, 3, 1, 3, 3, 3, 3, 1],
            'ISFJ': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1],
            'ESTJ': [3, 1, 1, 3, 1, 3, 3, 3, 3, 1],
            'ESFJ': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1],
            'ISTP': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1],
            'ISFP': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1],
            'ESTP': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1],
            'ESFP': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1]
        },
        'b': {
            'INTJ': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1],
            'INTP': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1],
            'ENTJ': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1],
            'ENTP': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1],
            'INFJ': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1],
            'INFP': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1],
            'ENFJ': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1],
            'ENFP': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1],
            'ISTJ': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1],
            'ISFJ': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1],
            'ESTJ': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1],
            'ESFJ': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1],
            'ISTP': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1],
            'ISFP': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1],
            'ESTP': [1, 3, 1, 1, 3, 1, 3, 1, 3, 1],
            'ESFP': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1]
        },
        'c': {
            'INTJ': [2, 2, 3, 2, 2, 2, 2, 2, 2, 2],
            'INTP': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            'ENTJ': [2, 2, 3, 2, 2, 2, 2, 2, 2, 2],
            'ENTP': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            'INFJ': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            'INFP': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            'ENFJ': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            'ENFP': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            'ISTJ': [2, 2, 3, 2, 2, 2, 2, 2, 2, 2],
            'ISFJ': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            'ESTJ': [2, 2, 3, 2, 2, 2, 2, 2, 2, 2],
            'ESFJ': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            'ISTP': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            'ISFP': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            'ESTP': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            'ESFP': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        },
        'd': {
            'INTJ': [1, 1, 1, 3, 3, 1, 1, 1, 1, 1],
            'INTP': [1, 1, 1, 3, 3, 1, 1, 1, 1, 1],
            'ENTJ': [1, 1, 1, 3, 3, 1, 1, 1, 1, 1],
            'ENTP': [1, 1, 1, 3, 3, 1, 1, 1, 1, 1],
            'INFJ': [1, 1, 1, 3, 3, 1, 1, 1, 1, 1],
            'INFP': [1, 1, 1, 3, 3, 1, 1, 1, 1, 1],
            'ENFJ': [1, 1, 1, 3, 3, 1, 1, 1, 1, 1],
            'ENFP': [1, 1, 1, 3, 3, 1, 1, 1, 1, 1],
            'ISTJ': [1, 1, 1, 3, 3, 1, 1, 1, 1, 1],
            'ISFJ': [1, 1, 1, 3, 3, 1, 1, 1, 1, 1],
            'ESTJ': [1, 1, 1, 3, 3, 1, 1, 1, 1, 1],
            'ESFJ': [1, 1, 1, 3, 3, 1, 1, 1, 1, 1],
            'ISTP': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1],
            'ISFP': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1],
            'ESTP': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1],
            'ESFP': [3, 1, 3, 3, 1, 3, 1, 3, 1, 1]
        }
    }
    
    # Initialize counters for each personality type
    personality_types = {
        'INTJ': 0,
        'INTP': 0,
        'ENTJ': 0,
        'ENTP': 0,
        'INFJ': 0,
        'INFP': 0,
        'ENFJ': 0,
        'ENFP': 0,
        'ISTJ': 0,
        'ISFJ': 0,
        'ESTJ': 0,
        'ESFJ': 0,
        'ISTP': 0,
        'ISFP': 0,
        'ESTP': 0,
        'ESFP': 0
    }
    
    # Iterate through questions and gather responses
    for question in questions:
        print(question)
        response = input("Enter your choice (a/b/c/d): ").lower()
        while response not in ['a', 'b', 'c', 'd']:
            print("Invalid choice! Please enter 'a', 'b', 'c', or 'd'.")
            response = input("Enter your choice (a/b/c/d): ").lower()
        
        # Add points to corresponding personality types based on response
        for key, value in point_system[response].items():
            for i, points in enumerate(value):
                personality_types[key] += points
    
    # Determine the dominant personality type
    dominant_type = max(personality_types, key=personality_types.get)
    
    # Display the result
    display_personality_info(mbti_types, dominant_type)
    
 
# Run the MBTI test
mbti_test()
