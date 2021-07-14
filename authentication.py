import os
import stripe

# Set Stripe key globally
stripe.api_key = os.environ['STRIPE_SECRET_KEY']

# Get all customers
customer_list = stripe.Customer.list()

# Get first customer ID
customer_id = customer_list['data'][0]['id']

# # Get specific customer
print(stripe.Customer.retrieve(customer_id))

# # API key can be passed in per request
print(stripe.Customer.retrieve(customer_id,
                               api_key=os.environ['STRIPE_SECRET_KEY']))
