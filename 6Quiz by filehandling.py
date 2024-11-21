import time
import random
import os

user_data_file = "users.txt"
questions_file = "questions.txt"
results_file = "results.txt"

def create_account():
    print("\n--- Create Account ---")
    username = input("Choose a username: ")
    password = input("Create a password: ")

    with open(user_data_file, "a") as f:
        f.write(f"{username},{password}\n")
    print("Account created successfully!")

def log_in():
    print("\n--- Log In ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open(user_data_file, "r") as f:
        users = f.readlines()
        for user in users:
            user_data = user.strip().split(",")
            
            if len(user_data) == 2:
                stored_username, stored_password = user_data
                if stored_username == username and stored_password == password:
                    print("Login successful!")
                    return username
    print("Incorrect username or password!")
    return None

def load_quiz_questions():
    questions = []
    with open(questions_file, "r") as f:
        data = f.readlines()
        for line in data:
            question, *options, correct = line.strip().split(",")
            questions.append({
                "question": question,
                "options": options,
                "correct": correct
            })
    random.shuffle(questions) 
    return questions[:5]  

def take_quiz(username):
    print("\n--- Start Quiz ---")
    questions = load_quiz_questions()
    correct_answers = 0
    total_questions = len(questions)
    start_time = time.time()
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for j, option in enumerate(q['options'], start=1):
            print(f"{j}. {option}")
        
        answer = input("Select your answer (1-4): ")
        if q['options'][int(answer) - 1] == q['correct']:
            correct_answers += 1
    
    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    score = f"{correct_answers}/{total_questions}"

    with open(results_file, "a") as f:
        f.write(f"{username},{score},{time_taken} seconds\n")
    
    print(f"\nQuiz complete! Your score: {score}")
    print(f"Time taken: {time_taken} seconds")

def view_results(username):
    print("\n--- Your Results ---")
    with open(results_file, "r") as f:
        results = f.readlines()
        found = False
        for result in results:
            result_username, score, time_taken = result.strip().split(",")
            if result_username == username:
                print(f"Score: {score}, Time: {time_taken}")
                found = True
        if not found:
            print("No results available!")

def main():
    if not os.path.exists(user_data_file):
        open(user_data_file, 'w').close()  
    if not os.path.exists(questions_file):
        
        with open(questions_file, 'w') as f:
            
            # DBMS Questions
            f.write("What does DBMS stand for?,Data Base Management System,Database Management Source,Data Block Management System,Data Base Multiple Systems,Data Base Management System\n")
            f.write("Which of the following is a key feature of DBMS?,Data Redundancy Control,Data Storage Management,Data Integrity,All of the above,All of the above\n")
            f.write("Which command is used to retrieve data from a database?,GET,SELECT,FETCH,QUERY,SELECT\n")
            f.write("Which of the following is NOT a type of DBMS model?,Hierarchical Model,Relational Model,Object-Oriented Model,Linear Model,Linear Model\n")
            f.write("What is a primary key in a database?,A unique identifier for each record in a table,A key used to encrypt data,A key used for indexing,A key to group similar records,A unique identifier for each record in a table\n")

            # Cybersecurity Questions
            f.write("What does the term 'Phishing' refer to?,The act of hacking into a computer system,The use of fraudulent emails to steal sensitive information,A type of virus that destroys files,A technique for encrypting passwords,The use of fraudulent emails to steal sensitive information\n")
            f.write("Which of the following is a common method for protecting sensitive data?,Encryption,Password hashing,Two-factor authentication,All of the above,All of the above\n")
            f.write("What does the acronym 'DDoS' stand for?,Distributed Denial of Service,Digital Data Online System,Data Distribution Over Server,Direct Denial of Service,Distributed Denial of Service\n")
            f.write("Which of the following is a tool used for penetration testing?,Wireshark,Nmap,Metasploit,All of the above,All of the above\n")
            f.write("What is the purpose of a firewall in cybersecurity?,To detect malware,To monitor network traffic,To prevent unauthorized access to a network,To encrypt sensitive data,To prevent unauthorized access to a network\n")

            # Network Security Questions
            f.write("Which of the following is a network security protocol?,HTTP,HTTPS,FTP,SNMP,HTTPS\n")
            f.write("What does VPN stand for in network security?,Virtual Private Network,Virtual Protected Network,Virtual Public Network,Verified Protection Network,Virtual Private Network\n")
            f.write("Which of the following is a common attack method in network security?,Man-in-the-Middle (MITM) attack,Phishing,SQL Injection,All of the above,All of the above\n")
            f.write("What is the purpose of an Intrusion Detection System (IDS)?,To monitor and detect malicious network activity,To prevent unauthorized access to a network,To block all network traffic,To provide network access control,To monitor and detect malicious network activity\n")
            f.write("Which protocol is commonly used for securing email communication?,HTTP,POP3,SMTP,S/MIME,S/MIME\n")

    while True:
        print("\n--- Main Menu ---")
        print("1. Create Account")
        print("2. Log In")
        print("3. Take Quiz")
        print("4. View Results")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            username = log_in()
            if username:
                while True:
                    print("\n1. Take Quiz")
                    print("2. View Results")
                    print("3. Log Out")
                    sub_choice = input("Select an option: ")
                    if sub_choice == '1':
                        take_quiz(username)
                    elif sub_choice == '2':
                        view_results(username)
                    elif sub_choice == '3':
                        break
                    else:
                        print("Invalid option!")
        elif choice == '5':
            print("Exiting application...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
