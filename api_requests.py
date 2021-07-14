import os
import stripe

stripe.api_key = os.environ['STRIPE_SECRET_KEY']

# Create a customer with no params
# customer = stripe.Customer.create()
# print(customer)

# Retrieve a customer
# path = /v1/customers/cus_JpjTN9Ty5jCYxS
# customer = stripe.Customer.retrieve("cus_JpjTN9Ty5jCYxS")
# print(customer)

# Create a customer with name and email
# customer = stripe.Customer.create(email="test@testy.com",
#                                   name="Testy van tester")
# print(customer)

# Create a customer with nested dict
invoice_settings = {
    'default_payment_method': 'pm_card_visa',
}
customer = stripe.Customer.create(payment_method="pm_card_visa",
                                  invoice_settings=invoice_settings)
print(customer)
print(customer.invoice_settings)


