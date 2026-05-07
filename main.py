class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."

def main():
    # Initial list
    classmates = [
        Classmate("Kristine", "Amethyst", "Math"),
        Classmate("Jean", "Amethyst", "Science"),
        Classmate("Hariette", "Amethyst", "English"),
        Classmate("Jubilee", "Amethyst", "Math"),
        Classmate("Vivian", "Amethyst", "History")
    ]

    while True:
        print("\n--- Grade 10 Classmates System ---")
        print("1. Add Classmate")
        print("2. Show List")
        print("3. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter Name: ")
            section = input("Enter Section: ")
            subject = input("Enter Favorite Subject: ")
            classmates.append(Classmate(name, section, subject))
            print("Successfully added!")

        elif choice == '2':
            print("\n📋 Classmate List:")
            # Loop to display all introductions
            for student in classmates:
                print(student.introduce())
        
        elif choice == '3':
            break

if __name__ == "__main__":
    main()



import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from pyscript import document

# rthbis resets the data
absences_data = {
    'Monday': 0, 
    'Tuesday': 0, 
    'Wednesday': 0, 
    'Thursday': 0, 
    'Friday': 0
}

def handle_submit(event):
    # 
    day = document.querySelector("#daySelect").value
    raw_value = document.querySelector("#absenceInput").value
    
    # this coverts the number into intgere
    try:
        num_absences = int(raw_value) if raw_value else 0
    except ValueError:
        num_absences = 0

    # this updates the graph
    absences_data[day] = num_absences
    
    # this generates the graph
    days = list(absences_data.keys())
    counts = list(absences_data.values())
    
    #small help from ai -- i asked help where to put which
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(days, counts, marker='o', color='#198754', linewidth=2, markersize=8)
    ax.set_title('Weekly Absence Trend', fontsize=14, pad=15)
    ax.set_ylabel('Number of Students')
    ax.set_ylim(bottom=0) # Ensure Y axis starts at 0
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # small help aswell -- i just asked how to close this python code
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    
    # 5. Push the image back to the HTML container
    img_tag = f'<img src="data:image/png;base64,{img_base64}"/>'
    document.querySelector("#graph-output").innerHTML = img_tag

        #Additionally
        
        # -- Thank you maam evangelista for the 2 years we had as your students, 
        # your classes made me interested in information technology, and made me wanrt to learn more about it.

        # Starting grade 8, I learned the fundamentals of coding through scratch -- which initially,
        # I thought was stupid and childish but eventually, it helped me understand more complex and complicated programming languages.

        # Grade 10, starting phython, I was really struggling at first, but throughout your thorough comments and detailed help
        # I was able to overcome my struggles and learn how to do basic code in python.

        # Every detailed comment in every assesment made me learn something, and gave me enough criticism to know
        # what im lacking and what i need to improve on. These comments gave meinspiration to try harder in the next activity.

        #   Forever very very grateful for all the lesosns you have thought me and my classmates.
        #   Many thanks Ma'am Evangellista! Until the next the comment!    - Jairo 
 
