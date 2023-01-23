# There are times we want to import modules from sibling packages
# intra packages reference there two ways to import a package.
# Relative and Absolute

# Supposing we were working on our "esales.py" and need to import a function from "contact.py"

# ABSOLUTE REFERENCE
from ecommerce.customer import contact # This is the absolute import

contact.contact_costumer()


# RELATIVE REFERENCE
# We use the "." operator to navigate to the parent folders.
# "." refers current package, ".." takes us one level up (at the ecommerce package level)
# Assume that this code is written in "ecommerce/shopping/sales.py"
from ..customer import contact

contact.contact_costumer()

# As a best practice prefer to use the absolute import. Thats what PEP 8 recommends.