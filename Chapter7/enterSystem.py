import time

db = {}
time_db = {}


def new_user():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        if name in db:
            prompt = 'name taken, try again! '
            continue
        else:
            break
    pwd = raw_input('password: ')
    second_time = time.time()
    db[name] = pwd
    time_db[name] = second_time


def old_user():
    name = raw_input('login: ')
    log_time = time.time()
    if (log_time - time_db[name]) <= 3600:
        print "You have already login."
    else:
        password = db.get(name)
        count = 0
        while count < 3:
            pwd = raw_input('password: ')
            if password == pwd:
                curr_time = time.time()
                time_db[name] = curr_time
                print "Welcome back, %s!" % name
                break
            else:
                print "Wrong password, please re-input!"
                count += 1
                continue
        if count == 3:
            print "You have entered three count with wrong password, you cannot enter system today," \
                  "please try again tomorrow!"

def show_menu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit

Enter choice: """
    
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print "\nYou picked: [ %s ] " % choice
            if choice not in 'neq':
                print "Invalid option, try again"
            else:
                chosen = True
    
        if choice == 'q':
            done = True
        if choice == 'n':
            new_user()
        if choice == 'e':
            old_user()

if __name__ == '__main__':
    show_menu()
