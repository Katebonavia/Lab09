from database.DB_connect import DBConnect
from model.airport import Airport
from model.arco import Arco


class DAO:
    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []
        query = """select *
                   from extflightdelays.airports a"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getAllArchi(idMap):  # passo un idMap che mi recupera gli oggetti dato l'id
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []
        query = """select f2.ORIGIN_AIRPORT_ID as p,f2.DESTINATION_AIRPORT_ID as d, avg(f2.DISTANCE) as avg
                   from extflightdelays.flights f2 
                    group by f2.ORIGIN_AIRPORT_ID, f2.DESTINATION_AIRPORT_ID
                    """

        cursor.execute(query)

        for row in cursor:
            result.append(Arco(idMap[row['p']], idMap[row['d']], row['avg']))  # qui mi arriva un id di due oggetti e un peso che devo capire come gestire

        cursor.close()
        conn.close()

        return result

