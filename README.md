# [LUSH](https://www.lush.co.kr/main/index.php) is a cosmetics retailer that produces and sells creams, soaps, shampoos, shower gels, lotions, moisturisers, scrubs, masks and other cosmetics for the face, hair, and body using only vegetarian recipes. This particular webistes not only cosmetic products but also spa and community events.

## This project was done by 3 backends and 3 frontends

## Demo
(https://www.youtube.com/watch?v=pjOPUkIn6mw)

## Applied Skills (Backend)

- Python
- Django
- Beautifulsoup
- Selenium
- Requests
- Pagination
- Bcrypt
- JWT
- Mysql
- CORS headers
- AWS : EC2, RDS, S3
- Git Rebase

## API's
### User App
- Sign Up & Sign In using Bcyrypt and JWT

### Review App
- Verified the user with the login decorator and let all verified users comment on the products.

### Order App
- View that manages all the shipping information of the users.
  - CRUD: User can create, edit, or delete the shipping information as they wish.
- View that lets customers place an order directly from the product page.
- Another View that lets customers place an order in their carts.
  - Generated a random order number using ```uuid```.
  - Saved the ordered products into out DB.

### Product App
- Displays the entire products and their necessary information.
- Uses pagination in order to limit the number of products displayed in one page (30 products per page).
