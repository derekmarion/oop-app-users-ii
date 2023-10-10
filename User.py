class User:
    
    def __init__(self, name, email, license) -> None:
        self._name = name
        self._email = email
        self._license = license
        self._posts = []

    @property
    def get_name(self):
        return self._name
    
    @property
    def get_email(self):
        return self._email
    
    @property
    def get_license(self):
        return self._license
    
    @property 
    def get_posts(self):
        return self._posts
    
    @get_posts.setter
    def set_post(self, post):
        self._posts.append(post)

    def __str__(self) -> str:
        return f"Username: {self.get_name}\nEmail: {self.get_email}\nLicense #: {self.get_license}"
    
user1 = User("Jimmy", "jimmy@gimmy.com", "as;lkdjfao92wi3")
user1.set_post = "This is a blog post"
user1.set_post = "Here's another"

print(user1.get_posts)
