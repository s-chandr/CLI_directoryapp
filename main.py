def helper():
    print('''Usage :-
    ./task add 2 hello world     # Add a new item with priority 2 and text "hello world" to the list
    ./task ls                    # Show incomplete priority list item sorted by priority in ascending order
    ./task del NUMBER   # Delete the incomplete item with the given priority number
    ./task done NUMBER  # Mark the incomplete item with the given priority_NUMBER as complete
    ./task help                  # Show usage 
    ./task report                # Statistics   
    ''')
def addtodb(Task,Priority,cursor):
    insert_script = 'INSERT INTO tasks (id, task_name, priority) VALUES (DEFAULT,%s,%s)'
    cursor.execute(insert_script,(Task,Priority))
    # cursor.execute('INSERT INTO tasks ( task_name, priority) VALUES ({0},{1})'.format(Task,Priority))
    connection.commit()    
# def mark_done(id,cursor):
    # pass
import psycopg2

#these all the details should be there in a seperate files
hostname = 'localhost'
database = 'pt'
username = 'postgres'
pwd = 'root'
port_id = 5432
connection = None
cursor = None
import sys 
from typing import List 
args: List[str] = sys.argv
# connection = None
try:
    # global connection
    connection = psycopg2.connect(
        host = hostname, dbname = database, user = username, password = pwd, port = port_id
    )
    cursor = connection.cursor()
    ddl_script = '''    
                        CREATE TABLE IF NOT EXISTS tasks(
                        id              SERIAL PRIMARY KEY,
                        task_name       varchar(35) not null,
                        priority        int not null,
                        status          BOOLEAN DEFAULT FALSE
                        )'''
    # status is true means done otherwise flase status meanse still pending 
    cursor.execute(ddl_script)
    # insert_script = 'INSERT INTO tasks (id, task_name, priority) VALUES (DEFAULT,%s,%s)'
    # inser_value = [(1,'John',200,3,'2021-01-07'),(2,'Johnnty',300,2,'2021-02-07'),(3,'Mohn',200,3,'2021-03-07'),(4,'Zoen',900,5,'2021-04-07')]
    # for item in inser_value:
    #     cursor.execute(insert_script,item)
    connection.commit()
    # cursor.execute('SELECT * FROM transactions ')
        
    if len(args) == 1 :
        helper()
    else:
        if args[1] == "help":
            helper()
        elif args[1] == "add" :
            addtodb(args[3],args[2],cursor)
            print("Added task {0} with priority {1}".format(args[3], args[2]))
        elif args[1] == "report":
            pending_script = cursor.execute('''SELECT COUNT(id) 
            FROM tasks
            WHERE status = 'FALSE'
            ''')
            pending_script = cursor.fetchone()
            
            print("Pending: {0}".format(pending_script[0]))
            # pending_script ,done_script  = 0,0 if pending_script == None or done_script == None
            pending_script_list = cursor.execute('''SELECT task_name,priority
            FROM tasks
            WHERE status = 'FALSE'
            ''')
            
            for Sno,record in enumerate(cursor.fetchall()):
                print(f'{Sno+1}. {record[0]} [{record[1]}]')
            
            done_script = cursor.execute('''SELECT COUNT(id) 
            FROM tasks
            WHERE status = 'TRUE'
            ''')
            done_script = cursor.fetchone()
            
            print("Completed: {0}".format(done_script[0]))
            done_script_list = cursor.execute('''SELECT task_name
            FROM tasks
            WHERE status = 'TRUE'
            ''')
            for Sno,record in enumerate(cursor.fetchall()):
                print(f'{Sno+1}. {record[0]} ')
            
        elif args[1] == "done":
            done_script = '''UPDATE tasks SET status = TRUE WHERE id IN(SELECT id
            from (select id , row_number() over (order by priority ) as rn 
            from tasks ) x 
            where x.rn = %s
            )
'''
            # id = int(id) - 1 
            
            cursor.execute(done_script,[int(args[2]) ])      
            connection.commit()     
            print("Marked item as done.")
        elif args[1] == "ls":
            # print("Already Stored:")
            script = 'select * from tasks WHERE status = FALSE order by priority'
            cursor.execute(script)
            for Sno,record in enumerate(cursor.fetchall()):
                print(f'{Sno+1}. {record[1]} has Priority {record[2]}')
            
except Exception as e:
    print(e)

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()



# print(args[1])
# print(args[2])
# pq.traverse()
# drop = '''DROP TABLE IF EXISTS tasks'''
# cursor.execute(drop)
	# Removing highest Priority item
	# for priority queue
# pq.pop()
# pq.traverse()
# print("Hello")



# Python3 code to implement Priority Queue
# using Singly Linked List

# Class to create new node which includes
# Node Data, and Node Priority

# class PriorityQueueNode:
	
#     def __init__(self, value, pr):
	
# 	    self.data = value
# 	    self.priority = pr
# 	    self.next = None
		
# # Implementation of Priority Queue

# class PriorityQueue:
#     def __init__(self):
#         self.front = None
#     def isEmpty(self):
#         return True if self.front == None else False
    	
# 	# Method to check Priority Queue is Empty
# 	# or not if Empty then it will return True
# 	# Otherwise False
    	
        
	
# 	# Method to add items in Priority Queue
# 	# According to their priority value
#     def add(self, value, priority):
#         if self.isEmpty() == True:
#             self.front = PriorityQueueNode(value,priority)
#             return 1
#         else:
#             if self.front.priority > priority:
#                 newNode = PriorityQueueNode(value,priority)
#                 newNode.next = self.front
#                 self.front = newNode
#                 return 1
#             else:
#                 temp = self.front
#                 while temp.next:
#                     if priority <= temp.next.priority:
#                         break
#                     temp = temp.next
#                 newNode = PriorityQueueNode(value,priority)
#                 newNode.next = temp.next
#                 temp.next = newNode
#                 return 1
# 	# Method to remove high priority item
# 	# from the Priority Queue
#     def pop(self):
#         if self.isEmpty() == True:
#             return
#         else:
#             self.front = self.front.next
#             return 1 

    		
# 	# Method to return high priority node
# 	# value Not removing it
    		
# 	# Method to Traverse through Priority
# 	# Queue    
    
#     def traverse(self):
#         counter = 1 
#         if self.isEmpty() == True:
#             return "Queue is empty!"
#         else:
#             temp = self.front
#             while temp:
#                 # print(temp.data , end = " ")
#                 print("{0}. {1} [{2}]".format(counter,temp.data,temp.priority))
#                 temp = temp.next
#                 counter = counter + 1

#     def delete_with_seq(self,number):
#         if self.isEmpty() == True:
#             return "Queue is empty!"
#         else:
#             temp = self.front
#             while number>0:
#                 temp = temp.next
#                 number = number - 1

# Driver code
# if __name__ == "__main__":
	
	# Creating an instance of Priority
	# Queue, and adding values
	# 7 -> 4 -> 5 -> 6

# pq.push(4, 1)
# pq.push(5, 2)
# pq.push(6, 3)
# pq.push(7, 0)
	
	# Traversing through Priority Queue
