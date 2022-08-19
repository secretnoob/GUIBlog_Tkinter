import tkinter as tk
import sqlite3

#Main Window
window = tk.Tk()

#Blog Editor
def create_editor():
    editor = tk.Tk()
    label_for_headline = tk.Label(editor, text = "Write the Heading")
    headline = tk.Entry(editor)

    label_for_headline.pack()
    headline.pack()

    label_for_text = tk.Label(editor, text = "Enter the Post")
    blog_content = tk.Text(editor)
    label_for_text.pack()
    blog_content.pack()

    button_add_to_blog = tk.Button(editor, text = "Add to Blog" ,
                                   command = add_to_blog(headline, blog_content))
    button_add_to_blog.pack()

#This function takes the command from add_new_blog_post and starts the editor
def add_to_blog(headline, blog_content):
    con = sqlite3.connect("blog_posts.db")
    cur = con.cursor()

    cur.execute('''create table if not exists current_blog_posts
                    (HEADING text, CONTENT text)''')
    cur.execute('''insert into current_blog_posts (HEADING, CONTENT) values(?, ?)''', (headline, blog_content))
    cur.commit()
    con.close()

main_labelframe = tk.LabelFrame(window,
                                text = "Welcome to GUI Desktop Blog")
main_button = tk.Button(window, text = "main button", command = create_editor)
main_button.pack()
    
main_labelframe.pack()

window.mainloop()
