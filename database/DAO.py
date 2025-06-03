from database.DB_connect import DBConnect
from model.order import Order
from model.store import Store


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllStore():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = 'SELECT * FROM bike_store_full.stores s'

        cursor.execute(query)

        for row in cursor:
            result.append(Store(row["store_id"], row["store_name"], row["phone"], row["email"],
                                row["street"], row["city"], row["state"], row["zip_code"]))


        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getOrdersFromStore(store_id):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = 'select * from orders o  where o.store_id =%s'

        cursor.execute(query, (store_id,))

        for row in cursor:
            result.append(Order(row["order_id"], row["customer_id"], row["order_status"], row["order_date"],
                                row["required_date"], row["shipped_date"], row["store_id"], row["staff_id"]))


        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(store_id, Ngiorni):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = ('select o1.order_id as id_n1, o2.order_id as   id_n2  from orders o1, orders   o2     '
                 'where o1.order_id != o2.order_id and        o1.store_id = %s and o2.store_id = %s and    DATEDIFF('
                 'o1.order_date, o2.order_date) < %s    and o1.order_date > o2.order_date')

        cursor.execute(query, (store_id,store_id,Ngiorni, ))

        for row in cursor:
            result.append((row["id_n1"], row["id_n2"]))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getPeso(o1_id, o2_id):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = ('select sum(o1.quantity) + sum(o2.quantity) as som   from order_items o1, order_items    o2    where    o1.order_id = %s    and o2.order_id = %s')

        cursor.execute(query, (o1_id, o2_id, ))

        for row in cursor:
            result.append((row["som"]))

        cursor.close()
        conn.close()
        return result
