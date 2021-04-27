from semaphoreflask import app, mongo
import unittest

class TestFlaskAppConnections(unittest.TestCase):
    #Tests for a connection to the home page url
    def test_homepage(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    #Tests for a connection to the all posts url
    def test_all_posts_page(self):
        tester = app.test_client(self)
        response = tester.get('/task/all', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    #Tests for a conenction to new posts url
    def test_new_posts_page(self):
        tester = app.test_client(self)
        response = tester.get('/task/new', content_type='html/text')
        self.assertEqual(response.status_code, 200)

class TestMongoDB(unittest.TestCase):
    #Test for correct post title in db
    def test_correct_post_title_with_database(self):
        task_title = "test"
        task_description = "NULL"
        task_created_at = "NULL"
        mongo.db.tasks.insert_one({'task_title': task_title, 'task_description': task_description, 'task_created_at': task_created_at})
        tasks_data = []
        if mongo:
            tasks = mongo.db.tasks.find()
            if tasks:
                for task in tasks:
                    print(task)
                    tasks_data.append({'task_id': task['_id'], 'task_title': task['task_title'], 'task_description': task['task_description'],
                    'task_created_at': task['task_created_at']}) 
        
        self.assertEqual(tasks_data[0]['task_title'], "test")
    
    #Test for correct post contents in db
    def test_correct_post_contents_with_database(self):
        task_title = "NULL"
        task_description = "test-post"
        task_created_at = "NULL"
        mongo.db.tasks.insert_one({'task_title': task_title, 'task_description': task_description, 'task_created_at': task_created_at})
        tasks_data = []
        if mongo:
            tasks = mongo.db.tasks.find()
            if tasks:
                for task in tasks:
                    print(task)
                    tasks_data.append({'task_id': task['_id'], 'task_title': task['task_title'], 'task_description': task['task_description'],
                    'task_created_at': task['task_created_at']}) 
        
        self.assertEqual(tasks_data[0]['task_description'], "test-post")
    
    #Tets for correct post creation time in db
    def test_correct_post_creation_time_with_database(self):
        task_title = "NULL"
        task_description = "NULL"
        task_created_at = "NULL"
        mongo.db.tasks.insert_one({'task_title': task_title, 'task_description': task_description, 'task_created_at': task_created_at})
        tasks_data = []
        if mongo:
            tasks = mongo.db.tasks.find()
            if tasks:
                for task in tasks:
                    print(task)
                    tasks_data.append({'task_id': task['_id'], 'task_title': task['task_title'], 'task_description': task['task_description'],
                    'task_created_at': task['task_created_at']}) 
        
        self.assertEqual(tasks_data[0]['task_created_at'], "NULL")

    
if __name__ == '__main__':
    unittest.main()