# Wordplease

Wordplease is a blogging app developed with Python/Django by Alejandro Capparelli

## Install

pip install -r requirements.txt

## APP Routes

- /signup

- /login

- /admin

all blogs: 
- /blogs

all posts from author`s blog: 
- /blogs/[username] 

sigle post from author`s blog:

- /blogs/[username]/[id]


## API Routes

GET     /api/1.0/users/<int: pk>

POST    /api/1.0/users/signup

GET     /api/1.0/blogs  | query parameters: "author=[username]", "order=[blog_title]"
