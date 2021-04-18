import sqlite3 as dbase
from gen import StudentGen



class DataBase:
    def __init__(self, table):
        connect = dbase.connect("demo.db", check_same_thread=False)
        connect.row_factory = dbase.Row
        connect.isolation_level = None
        self.db = connect.cursor()
        self.table = table

    def create_table(self):
        sql = f"""CREATE TABLE IF NOT EXISTS `{self.table}`(
                        `id` INTEGER NOT NULL,
                        `fname` VARCHAR(22),
                        `sname` VARCHAR(22),
                        `points` INTEGER,
                        `faculty` VARCHAR(33),
                        `gender` VARCHAR(1),
                        `bdate` TEXT,
                        `group` VARCHAR(22),
                        `slug` VARCHAR(5),
                        PRIMARY KEY(`id`))"""
        self.db.execute(sql)
       

    def insert(self, dict_data):
        cols = "`, `".join(list(dict_data.keys()))
        values = "', '".join(list(dict_data.values()))
        sql = f"INSERT INTO `{self.table}` (`{cols}`) VALUES('{values}')"
        self.lastid = self.db.execute(sql).lastrowid


    def select_all(self):
        sql = f"SELECT * FROM { self.table } ORDER BY `fname` ASC"
        data = self.db.execute(sql).fetchall()
        return [dict(item) for item in data]

    def select_one(self, id):
        sql = f"SELECT * FROM { self.table } WHERE id = {id}"
        one = self.db.execute(sql).fetchone()
        return dict(one) if one else one

    
    def select_by_col(self, dict_cols):
        [(col, val)] = list(dict_cols.items())
        sql = f"SELECT * FROM `{self.table}` WHERE `{col}` = '{val}'"
        data = self.db.execute(sql).fetchall()
        return [dict(item) for item in data]

    def delete(self, id):
        sql = f"DELETE FROM { self.table } WHERE id = {id}"
        deleted = self.select_one(id)
        self.db.execute(sql)
        return deleted

    def update(self, dict_data, id):
        update_cols = ", ".join([f"'{key}' = '{value}'" for key, value in dict_data.items()])
        sql = f"UPDATE {self.table} SET {update_cols} WHERE id = {id}"
        self.db.execute(sql)
        return self.select_one(id)

    def show_records(self):
        records = self.select_all()
        result = []
        for data_dict in records:
            tmp=[]
            for key, val in data_dict.items():
                tmp.append(f"{key}:{val}")
            result.append("\n".join(tmp))
        print(f"{self.table.upper()}\n=======\n" + "\n=============\n".join(result))
    

#database = DataBase("demo")
#database.db.execute("DROP TABLE demo")
#id_inserted = []
#for stud in obj.students:
#    obj_1.insert(stud)
#    id_inserted.append(obj_1.lastid)


##print(id_inserted)
#print(obj_1.show_records())