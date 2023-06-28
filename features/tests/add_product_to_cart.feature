Feature: Add Product to Cart


Scenario: Add a Product to Cart
Given Open amazon main page
When Search for coffee
And Click on the first search result
And Store product name
And Click on Add to cart button
And Open cart page
Then Verify cart has 1 item
And Verify cart has correct product
