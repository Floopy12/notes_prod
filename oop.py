from base import cur
from base import cur, con



class Save:
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def save_text(self):
        text_val = self.text.get('1.0' , 'end')
        name_val = self.name.get('1.0', 'end')
        
        cur.execute(f'''
        INSERT INTO note (name, content) VALUES ('{name_val}', '{text_val}')
        ''')
        

        
        con.commit()
 
           

class Delete:
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def delete_text(self):
        self.text.delete('1.0', 'end')
        # cur.execute('''
        # DELETE FROM note WHERE 
        # ''')
        con.commit()
        

