import json 

class book_collection:

    def __init__(self):
        self.book_list=[]
        self.storage_file="books_data.json"
        self.read_from_file()

    def read_from_file(self):
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError,json.JSONDecodeError):
            self.book_list=[]

    def save_to_file(self):
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list , file, indent=4)

    def create_new_book(self):
        book_title=input("Enter book title: ")
        book_author=input("Enter Author: ")
        publication_year=input("Enter publication year: ")
        book_genre=input("Enter genre: ")
        is_book_read=(
            input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        )

        new_book = {
            "title":book_title,
            "author":book_author,
            "year":publication_year,
            "genre":book_genre,
            "read":is_book_read
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print("✅ BOOK ADDED SUCCESSFULLY!\n")

    def delete_book(self):
        book_title=input("Enter the title of book to remove: ")

        for book in self.book_list:
            if(book["title"].lower()==book_title.lower()):
                self.book_list.remove(book)
                self.save_to_file()
                print("✨BOOK REMOVED SUCCESSFULLY\n")
                return 
        print("Book Not Found!\n")

    def find_book(self):
        search_text=input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        search_text=input("Enter search term: ").lower()

        found_book=[
            book
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]
        if found_book:
            print("Matching Books:")
            for index, book in enumerate(found_book , 1):
                reading_status="Read" if book["read"] else "Unread"
                print(
                    f"{index}.{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
                )
        else:
            print("No Matching Book Found.\n")

    def update_books(self):
        book_title=input("Enter the title of book you want to edit: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():

                print("Leave blank to keep existing value.")
                book["title"]=input(f"New title ({book["title"]}): ") or book["title"]
                book["author"]=input(f"New Author ({book["author"]}): ") or book["author"]
                book["year"]=input(f"New Publication year ({book["year"]}): ") or book["year"]
                book["genre"]=input(f"New genre ({book["genre"]}): ") or book["genre"]
                book["read"]=(
                    input("Have you read this book?(yes/no): ").strip().lower() == "yes"
                )
                self.save_to_file()
                print("🎉Book updated Successfully!\n")
                return
            print("Book not found!\n")
        
    def show_all_books(self):
        if not self.book_list:
            print("Your collection is empty")
            return
        print("Your Book Collection: ")
        for index,book in enumerate(self.book_list , 1):
            reading_status="Read" if book["read"] else "Unread"
            print(
                f"{index}.{book['title']}  by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
            )
        print()

    def show_reading_progress(self):
        total_books=len(self.book_list)
        completed_book=sum(1 for book in self.book_list if book['read'])
        completion_rate=(
            (completed_book / total_books * 100) if total_books > 0 else 0
        )
        print(f"Total Books in Collection:{total_books}")
        print(f"Reading Progress: {completion_rate:.2f}%\n")


    def start_application(self):
        while True:
            print("🎉WELCOME TO YOUR BOOK COLLECTION MANAGER!")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice=input("Please choose an option from (1 - 7): ")

            if (user_choice == "1"):
                self.create_new_book()
            elif(user_choice == "2"):
                self.delete_book()
            elif(user_choice == "3"):
                self.find_book()
            elif(user_choice == "4"):
                self.update_books()
            elif(user_choice == "5"):
                self.show_all_books()
            elif(user_choice == "6"):
                self.show_reading_progress()
            elif(user_choice == "7"):
                self.save_to_file()
                print("❤THANK YOU FOR USING OUR BOOK COLLECTION MANGER. GOODBYE!")
                break
            else:
                print("Invalid Choice.Please Try Again! ")
            

if __name__=="__main__":
    book_manager=book_collection()
    book_manager.start_application()
    