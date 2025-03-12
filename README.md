# LittleLemon 

super user : admin
pw : 12345
email : admin@littlelemon.com

POST      /auth/users/             for user registration
GET       /auth/users/me/          to get the authenticated users profile
POST      /auth/token/login/       for user login(returns an authenticated token)
POST      /auth/token/logout/      user logout(deletes the token)

GET       /restaurant/menu/		        Retrieve all menu items.
POST      /restaurant/menu/		        Create a new menu item.
GET       /restaurant/menu/<int:pk>/	Retrieve a single menu item by ID.
PUT       /restaurant/menu/<int:pk>/	Update a menu item.
DELETE    /restaurant/menu/<int:pk>/	Delete a menu item.

GET	      /restaurant/bookings/	            Retrieve all bookings.
POST      /restaurant/bookings/		        Create a new booking.
GET       /restaurant//bookings/<int:pk>/	Retrieve a single booking by ID.
PUT       /restaurant/bookings/<int:pk>/	Update a booking.
DELETE    /restaurant/bookings/<int:pk>/	Delete a booking.


