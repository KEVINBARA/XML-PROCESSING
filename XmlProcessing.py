import xml.etree.ElementTree as ET

# Path to your XML file
xml_file = 'C:/Users/baran/Downloads/Exercise.xml'

# Parse the XML file
tree = ET.parse(xml_file)

# Get the root element of the XML tree
root = tree.getroot()

# Access attributes of the <Wire> element
file_id = root.get('fileId')
origin = root.get('origin')
file_date = root.get('fileDate')
print("Wire attributes:")
print("File ID:", file_id)
print("Origin:", origin)
print("File Date:", file_date)
print("---")

# Iterate over <Order> elements
for order in root.findall('Order'):
    # Access attributes of each <Order> element
    execution_date = order.get('executionDate')
    beneficiary = order.get('beneficiary')
    order_origin = order.get('origin')
    print("Order attributes:")
    print("Execution Date:", execution_date)
    print("Beneficiary:", beneficiary)
    print("Origin:", order_origin)

    # Access child elements of the <OrderDetails> element
    order_details = order.find('OrderDetails')
    amount = order_details.find('Amount').text
    exponent = order_details.find('Exponent').text
    currency = order_details.find('Currency').text
    print("Order Details:")
    print("Amount:", amount)
    print("Exponent:", exponent)
    print("Currency:", currency)
    print("---")