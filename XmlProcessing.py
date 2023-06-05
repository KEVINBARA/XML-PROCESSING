import xml.etree.ElementTree as ET
import psycopg2

from model.Wire import Wire


def process_file(file_path):
    
    # Parse the XML file
    tree = ET.parse(file_path)

    # Get the root element of the XML tree
    root = tree.getroot()

    # Access attributes of the <Wire> element
    file_id = root.get('fileId')
    origin = root.get('origin')
    file_date = root.get('fileDate')


    my_wire_list = []


    # Iterate over <Order> elements
    for order in root.findall('Order'):
        # Access attributes of each <Order> element
        execution_date = order.get('executionDate')
        beneficiary_account = order.get('beneficiary')
        origin_account = order.get('origin')
  

        # Access child elements of the <OrderDetails> element
        order_details = order.find('OrderDetails')
        wire_amount = order_details.find('Amount').text
        exponent = order_details.find('Exponent').text
        wire_amount_currency = order_details.find('Currency').text

        wire_item = Wire(file_id,origin,file_date,execution_date,beneficiary_account,origin_account,wire_amount,wire_amount_currency)

        my_wire_list.append(wire_item)

    save_wire(my_wire_list)    

def save_wire(wire_list):


    # Establish a connection to the postgres Database
    conn = psycopg2.connect(
    host = 'localhost',
    port = '5432',
    database ='postgres',
    user ='postgres',
    password ='toor')

    for wire in wire_list:
    
         order_query = """
                INSERT INTO bank.wires 
            (file_id, origin, file_date, execution_date, beneficiary_account,origin_account,wire_amount, wire_amount_currency)
           VALUES (%s, %s, %s, %s, %s, %s,%s,%s);
           """
         with conn.cursor() as cursor:
            cursor.execute(order_query,(wire.fileId,wire.origin,wire.fileDate,wire.executionDate,wire.beneficiaryAccount,wire.originAccount,
                                        wire.wireAmount,wire.wireAmountCurrency))
         
    conn.commit()
    conn.close()  

process_file('C:/Users/baran/Downloads/Exercise.xml')        

