Feature: Add Product to Cart


Scenario: Add a Product to Cart
Given Open amazon main page
When Search for coffee
And Click on the first search result
And Click "Add to Cart" button
And Open cart page
Then Verify cart has 1 item
