class RequestSQL():

    def updateCourses(self, name, description, ide):
        script = f"UPDATE sistema_categorie_curses SET name = '{name}', description = '{description}' WHERE id = {ide};"
        return script 
    
    def requestCourses(self):
        script = "SELECT name, description, id FROM sistema_categorie_curses"
        return script
    
    def dellCourses(self, pk):
        script = f"DELETE FROM sistema_categorie_curses WHERE ID = {pk}"
        return script
    
    def filterCourses(self, id):
        script = f"SELECT name, description, id FROM sistema_categorie_curses WHERE ID = {id}"
        return script
    
    def insertCourses(self, name, description):
        script = f"INSERT INTO sistema_categorie_curses (name, description, delete) VALUES ('{name}', '{description}', 'True')"
        return script

    def requestUser(self):
        script = "SELECT * FROM auth_user"
        return script