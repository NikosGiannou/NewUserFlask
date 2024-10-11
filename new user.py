from flask import Flask, render_template, request

app = Flask(__name__)

databasefile = "user_info.txt" #αρχειο με τα στοιχεια του χρήστη

@app.route('/', methods=["GET", "POST"]) #συνδεσμος στο local host

def signup():
    
    
    if request.method == "POST":
    
        firstname = request.form.get("firstname") #παιρνει πληροφοριες απο το αντιστοιχο κουτι του html
        
        lastname = request.form.get("lastname") 
        
        username = request.form.get("username")
        
        email = request.form.get("email")
        
        password = request.form.get("password")
        
        telephone = request.form.get("telephone")
        
        birthday = request.form.get("bdate")  
        
        with open(databasefile, 'a', encoding='utf=8') as file: # γραφονται οι πληροφοριες που παιρνει απο πανω
            file.write(f"Τα στοιχεία του χρήστη είναι:\n"
                       f"Ονοματεπώνυμο: {firstname} {lastname}\n"
                       f"Όνομα Χρήστη: {username}\n"
                       f"Κωδικός Πρόσβασης: {password}\n"
                       f"Ημερομηνία Γέννησης: {birthday}\n"
                       f"E-mail: {email}\n"
                       f"Αριθμός Τηλεφώνου: {telephone}\n\n")
            
        return render_template("succesful_signup.html") #χρηση του html μετα την επιτυχη εγγραφη του χρηστη

    return render_template("signup.html") # το html με την φορμα που πρεπει να συμπληρωσει ο χρηστης



if __name__ == '__main__':
    app.run(debug=True)