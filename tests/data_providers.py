import time
import random
from model.customer import Customer
from faker import Faker
from faker.providers import BaseProvider
faker = Faker('en_US')

first_name = faker.first_name()
last_name = faker.last_name()

# Our custom provider inherits from the BaseProvider
class simple_domain_names(BaseProvider):
    def fake_domain(self):
        domains = ['gmail.com', 'yahoo.ca', 'stargatecommand.co', 'altavista.com', 'hotmail.com', 'outlookmail.com', 'femail.net', 'globalpost.org', 'validhost.net']
        # We select a random destination from the list and return it
        return random.choice(domains)

faker.add_provider(simple_domain_names)
domain_name = faker.fake_domain()
email_address = '{}.{}@{}'.format(first_name, last_name, domain_name).lower()

# Our custom provider inherits from the BaseProvider
class US_States(BaseProvider):
    def fake_state(self):
        states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
        # We select a random state from the list and return it
        return random.choice(states)

faker.add_provider(US_States)
state = faker.fake_state()

valid_customers = [Customer(firstname=first_name,
                            lastname=last_name,
                            phone="360%d" % faker.random_number(7),
                            address=faker.street_address(),
                            postcode=faker.zipcode(),
                            city=faker.city(),
                            country="US",
                            zone=state,
                            email=email_address,
                            password="LiteCart1!"),
                   # ...
                   ]


